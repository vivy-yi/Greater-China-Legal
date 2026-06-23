#!/usr/bin/env python3
"""
evolution-runner.py — Drive the evolution closed-loop for a legal scene.

Subcommands:
  run-case      Execute one test case against a (mocked) skill output, score it.
  regress       Re-run regression set after a patch; compare to pre-patch.
  reflect       Generate a reflection scaffold from EVAL results.
  propose       Generate a proposal scaffold from a reflection.
  merge-log     Append a merge-log entry after regression passes.

Design notes:
  - This runner is the *file-flow* layer. It does NOT invoke any LLM.
  - "Skill output" must be supplied via --skill-output (string) or --skill-output-file (path).
  - Future integration with real agent: replace --skill-output with an agent invocation.

Examples:
  # Run one case
  python3 scripts/evolution-runner.py run-case \\
      --scene contract-review \\
      --case plugins/scenes/contract-review/tests/cases/contract-review-001.md \\
      --skill-output "..."

  # Generate reflection from failed case
  python3 scripts/evolution-runner.py reflect \\
      --scene contract-review \\
      --case plugins/scenes/contract-review/tests/cases/contract-review-001.md \\
      --scores-json '{"law_citation_accuracy": 0.0, ...}'

  # Regression after patch
  python3 scripts/evolution-runner.py regress \\
      --scene contract-review \\
      --regression-set case-007,case-012 \\
      --pre-results plugins/scenes/contract-review/tests/_results.yaml \\
      --post-skill-output "..."
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip3 install pyyaml", file=sys.stderr)
    sys.exit(1)


# ============================================================
# Constants — paths and shared helpers
# ============================================================

REPO_ROOT = Path(__file__).resolve().parent.parent
SCENES_DIR = REPO_ROOT / "plugins" / "scenes"
SHARED_DIR = REPO_ROOT / "plugins" / "shared"
EVOLUTION_CONFIG_PATH = SHARED_DIR / "evolution" / "config.yaml"


def load_evolution_config() -> dict:
    """Load the evolution strategy config (single source of truth).
    Falls back to sane defaults if config file is missing — never crash the runner.
    """
    defaults = {
        "signoff_required": {
            "content-add": 0, "format-fix": 0, "restructure": 1,
            "legal-source-add": 1, "legal-source-replace": 2,
            "deletion": 1, "frame-mismatch": 3,
        },
        "triggers": {
            "failure_rate_threshold": 0.30,
            "consecutive_failures": 3,
            "self_audit_phase2_fail_threshold": 5,
        },
        "law_ref_normalize_pattern": "[《》\\s第条]",
        "smoke_test": {
            "default_sample_pct": 5,
            "required_adjacent_scenes": 2,
            "adjacent_scene_pool": [],
        },
        "archival": {
            "merge_log_archive_after_days": 90,
            "merge_log_active_max_entries": 500,
            "patterns_tier_threshold": {"promote_to_high": 5, "demote_to_low": 2},
        },
        "explore": {
            "read_skill_md": True,
            "read_git_log_commits": 20,
            "read_adjacent_scenes": 2,
            "require_human_approval": True,
        },
        "naming": {
            "reflection_id_pattern": "rfl-{date}-{seq}",
            "proposal_id_pattern": "prp-{date}-{seq}",
            "sequence_padding": 3,
        },
    }
    if not EVOLUTION_CONFIG_PATH.exists():
        return defaults
    try:
        loaded = yaml.safe_load(EVOLUTION_CONFIG_PATH.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return defaults
    # Shallow merge: loaded overrides defaults
    merged = {**defaults, **loaded}
    for k, v in defaults.items():
        if isinstance(v, dict) and isinstance(merged.get(k), dict):
            merged[k] = {**v, **merged[k]}
    return merged


EVOLUTION_CONFIG = load_evolution_config()
SIGNOFF_REQUIRED = EVOLUTION_CONFIG["signoff_required"]
LAW_REF_NORMALIZE_RE = re.compile(EVOLUTION_CONFIG["law_ref_normalize_pattern"])


def normalize_law_ref(text: str) -> str:
    """Normalize a law-reference string for comparison."""
    return LAW_REF_NORMALIZE_RE.sub("", text)


def parse_frontmatter(md_text: str) -> dict:
    """Extract YAML frontmatter from a markdown file."""
    match = re.match(r"^---\n(.*?)\n---\n", md_text, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML frontmatter: {e}")


def scene_paths(scene: str) -> dict:
    """Return the canonical paths for a scene's evolution/test directories."""
    scene_root = SCENES_DIR / scene
    return {
        "scene_root": scene_root,
        "tests_dir": scene_root / "tests",
        "cases_dir": scene_root / "tests" / "cases",
        "results_yaml": scene_root / "tests" / "_results.yaml",
        "evolution_dir": scene_root / "evolution",
        "reflections_dir": scene_root / "evolution" / "reflections",
        "proposals_dir": scene_root / "evolution" / "proposals",
        "merge_log": scene_root / "evolution" / "merge-log.yaml",
    }


def today_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def next_seq_number(target_dir: Path, date_prefix: str) -> str:
    """Return next 3-digit sequence number for files matching date_prefix."""
    if not target_dir.exists():
        return "001"
    existing = sorted(target_dir.glob(f"{date_prefix}-*.md"))
    if not existing:
        return "001"
    last = existing[-1].stem.split("-")[-1]
    return f"{int(last) + 1:03d}"


# ============================================================
# Scoring (EVAL phase — used by run-case and regress)
# ============================================================

def score_law_citation(skill_output: str, expected_laws: list) -> float:
    if not expected_laws:
        return 1.0
    norm_output = normalize_law_ref(skill_output)
    hits = sum(1 for law in expected_laws if normalize_law_ref(law) in norm_output)
    return hits / len(expected_laws)


def score_coverage(skill_output: str, expected_items: list) -> float:
    if not expected_items:
        return 1.0
    hits = sum(1 for item in expected_items if item in skill_output)
    return hits / len(expected_items)


def score_advice_soundness(skill_output: str, expected_advice: list, must_not_contain: list) -> float:
    if not expected_advice:
        expected_advice_score = 1.0
    else:
        hits = sum(1 for a in expected_advice if a in skill_output)
        expected_advice_score = hits / len(expected_advice)
    bad_penalty = sum(1 for b in must_not_contain if b in skill_output) * 0.5
    return max(0.0, expected_advice_score - bad_penalty)


def evaluate(skill_output: str, case_fm: dict) -> dict:
    """Score a skill output against a parsed test-case frontmatter."""
    expected = case_fm.get("expected_output", {})
    dimensions = case_fm.get("evaluation_dimensions", [])
    scores = {}
    for dim in dimensions:
        if dim == "law_citation_accuracy":
            scores[dim] = score_law_citation(skill_output, expected.get("must_contain_laws", []))
        elif dim == "risk_coverage":
            scores[dim] = score_coverage(skill_output, expected.get("must_flag_risks", []))
        elif dim == "format_compliance":
            scores[dim] = score_coverage(skill_output, expected.get("must_have_sections", []))
        elif dim == "advice_soundness":
            scores[dim] = score_advice_soundness(
                skill_output,
                expected.get("must_contain_advice", []),
                expected.get("must_not_contain", []),
            )
        else:
            scores[dim] = 1.0  # unknown dimension: no penalty
    return scores


# ============================================================
# Subcommand: run-case
# ============================================================

def cmd_run_case(args) -> int:
    paths = scene_paths(args.scene)
    case_md = Path(args.case).read_text(encoding="utf-8")
    case_fm = parse_frontmatter(case_md)

    skill_output = _resolve_skill_output(args)
    scores = evaluate(skill_output, case_fm)
    passed = all(s >= 1.0 for s in scores.values())
    failed_dims = [d for d, s in scores.items() if s < 1.0]

    result = {
        "run_at": now_iso(),
        "run_id": f"auto-test-run-{today_iso()}",
        "scene": args.scene,
        "case_id": case_fm.get("case_id", "unknown"),
        "result": "PASS" if passed else "FAIL",
        "scores": scores,
        "failed_dimensions": failed_dims,
    }

    # Append to _results.yaml
    paths["results_yaml"].parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if paths["results_yaml"].exists():
        try:
            existing = yaml.safe_load(paths["results_yaml"].read_text()) or []
        except yaml.YAMLError:
            existing = []
    existing.append(result)
    paths["results_yaml"].write_text(
        yaml.dump(existing, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )

    # Console report
    print(f"[run-case] scene={args.scene} case={result['case_id']}")
    for dim, s in scores.items():
        marker = "PASS" if s >= 1.0 else f"FAIL ({s:.2f})"
        print(f"  {dim}: {marker}")
    print(f"  overall: {result['result']}")
    print(f"  appended to: {paths['results_yaml'].relative_to(REPO_ROOT)}")
    return 0 if passed else 1


def _resolve_skill_output(args) -> str:
    if args.skill_output_file:
        return Path(args.skill_output_file).read_text(encoding="utf-8")
    if args.skill_output:
        return args.skill_output
    print("ERROR: provide --skill-output or --skill-output-file", file=sys.stderr)
    sys.exit(2)


def resolve_scene_relative_path(path_arg: str, scene_root: Path) -> Path:
    """Resolve a user-supplied path: if absolute, use as-is; if relative, treat as
    repo-relative (NOT scene-relative) when it starts with 'plugins/'.
    """
    p = Path(path_arg)
    if p.is_absolute():
        return p
    # If user gave a full repo-relative path like 'plugins/scenes/.../foo.md',
    # use REPO_ROOT as the base. Otherwise fall back to scene-relative.
    if path_arg.startswith("plugins/") or path_arg.startswith("/"):
        return REPO_ROOT / path_arg
    return scene_root / path_arg


# ============================================================
# Subcommand: reflect
# ============================================================

REFLECTION_TEMPLATE = """---
reflection_id: {refl_id}
scene: {scene}
created_at: {date}
created_by: evolution-runner
trigger_ref: {trigger_ref}
trigger_type: {trigger_type}
failed_cases: [{failed_cases}]
eval_dimensions_failed: [{failed_dims}]
raw_evidence:
{raw_evidence_yaml}
root_cause_hypotheses:
{hyps_yaml}
selected_root_cause: {selected}
rationale: {rationale}
pattern_matched: null
next_stage: patch
next_stage_input:
  target_file: {suggested_target}
  suggested_patch_type: {suggested_patch_type}
---

# Reflection {refl_id}

Auto-generated by `evolution-runner.py reflect`.

## Failing dimensions
{failed_dims}

## Selected root cause
**{selected}**

{rationale}

## Action
Edit this file to refine hypotheses, then run:

```
python3 scripts/evolution-runner.py propose \\
    --scene {scene} \\
    --reflection evolution/reflections/{date}-{seq}.md
```
"""


def cmd_reflect(args) -> int:
    paths = scene_paths(args.scene)
    paths["reflections_dir"].mkdir(parents=True, exist_ok=True)

    date = today_iso()
    seq = next_seq_number(paths["reflections_dir"], date)
    refl_id = f"rfl-{date}-{seq}"

    scores = json.loads(args.scores_json) if args.scores_json else {}
    failed_dims = [d for d, s in scores.items() if s < 1.0]

    raw_evidence_yaml = "\n".join(
        f"  - case_id: {c}\n    expected: <TODO>\n    actual: <TODO>\n    diff_type: <TODO>"
        for c in (args.cases or [])
    )
    hyps_yaml = "\n".join(
        f"  - id: h{i+1}\n    hypothesis: <TODO>\n    evidence: <TODO>\n    confidence: medium"
        for i in range(2)  # at least 2 hypotheses required
    )

    content = REFLECTION_TEMPLATE.format(
        refl_id=refl_id,
        scene=args.scene,
        date=date,
        trigger_ref=args.trigger_ref or f"manual-{now_iso()}",
        trigger_type=args.trigger_type or "manual",
        failed_cases=", ".join(args.cases or []),
        failed_dims=", ".join(failed_dims),
        raw_evidence_yaml=raw_evidence_yaml or "  []",
        hyps_yaml=hyps_yaml,
        selected="h1",
        rationale='"TODO: explain why h1 was selected"',  # quoted to avoid YAML colon issues
        suggested_target=f"plugins/scenes/{args.scene}/skills/<skill-name>/SKILL.md",
        suggested_patch_type="content-add",
        seq=seq,
    )

    out_path = paths["reflections_dir"] / f"{date}-{seq}.md"
    out_path.write_text(content, encoding="utf-8")
    print(f"[reflect] created: {out_path.relative_to(REPO_ROOT)}")
    print(f"  reflection_id: {refl_id}")
    print(f"  next: edit {out_path.name} to fill in hypotheses, then run `propose`")
    return 0


# ============================================================
# Subcommand: propose
# ============================================================

PROPOSAL_TEMPLATE = """---
proposal_id: {prp_id}
scene: {scene}
created_at: {date}
created_by: evolution-runner
reflection_ref: {refl_ref}
patch_type: {patch_type}
target_file: {target_file}
target_section: {target_section}
diff_summary: |
  + <TODO: list additions>
  - <TODO: list deletions, if any>
rationale: |
  <TODO: reference reflection's selected_root_cause>
risk_assessment:
  legal_frame_impact: [{frame}]
  scene_impact: [{scene}]
  cross_scene_impact: []
  law_effective_date_verified: false
  law_effective_date: null
  breaking_change: false
expected_impact:
  metric: <TODO>
  current_value: <TODO>
  expected_value: <TODO>
  confidence: medium
regression_test_set:
  - <TODO: at least 1 case id>
smoke_test_set:
  - scene: <adjacent-scene>
    sample_pct: 5
signoff_required: {signoff_required}
signoff_status: pending
signoff_log: []
pattern_ref: null
---

# Proposal {prp_id}

Auto-generated by `evolution-runner.py propose`.

## Reflection reference
{refl_ref}

## Patch type
**{patch_type}** → signoff_required = {signoff_required}

## Action
Edit this file to fill in TODO fields, then either:
- Sign off yourself (if patch_type is content-add/format-fix and you trust the change), OR
- Forward to a lawyer for sign-off (patch_type=legal-source-*), OR
- Block and escalate (patch_type=frame-mismatch)

After sign-off, run:
```
python3 scripts/evolution-runner.py merge-log \\
    --scene {scene} \\
    --proposal evolution/proposals/{date}-{seq}.md
```
"""


def cmd_propose(args) -> int:
    paths = scene_paths(args.scene)
    paths["proposals_dir"].mkdir(parents=True, exist_ok=True)

    # Parse reflection to extract context
    refl_path = resolve_scene_relative_path(args.reflection, paths["scene_root"])
    if not refl_path.exists():
        print(f"ERROR: reflection not found at {refl_path}", file=sys.stderr)
        return 2
    refl_fm = parse_frontmatter(refl_path.read_text(encoding="utf-8"))

    patch_type = args.patch_type or "content-add"
    if patch_type not in SIGNOFF_REQUIRED:
        print(
            f"ERROR: invalid patch_type '{patch_type}'. "
            f"Valid: {', '.join(SIGNOFF_REQUIRED.keys())}",
            file=sys.stderr,
        )
        return 2

    signoff_required = args.signoff_required
    if signoff_required is None:
        signoff_required = SIGNOFF_REQUIRED[patch_type]
    elif signoff_required < SIGNOFF_REQUIRED[patch_type]:
        print(
            f"WARNING: signoff_required={signoff_required} is below matrix minimum "
            f"{SIGNOFF_REQUIRED[patch_type]} for patch_type={patch_type}",
            file=sys.stderr,
        )

    date = today_iso()
    seq = next_seq_number(paths["proposals_dir"], date)
    prp_id = f"prp-{date}-{seq}"

    target_file = args.target_file or refl_fm.get("next_stage_input", {}).get(
        "target_file", f"plugins/scenes/{args.scene}/skills/<skill-name>/SKILL.md"
    )
    target_section = args.target_section or "TODO"

    content = PROPOSAL_TEMPLATE.format(
        prp_id=prp_id,
        scene=args.scene,
        date=date,
        refl_ref=refl_fm.get("reflection_id", "unknown"),
        patch_type=patch_type,
        target_file=target_file,
        target_section=target_section,
        frame=args.frame or "cn-mainland",
        signoff_required=signoff_required,
        seq=seq,
    )

    out_path = paths["proposals_dir"] / f"{date}-{seq}.md"
    out_path.write_text(content, encoding="utf-8")
    print(f"[propose] created: {out_path.relative_to(REPO_ROOT)}")
    print(f"  proposal_id: {prp_id}")
    print(f"  patch_type: {patch_type} → signoff_required: {signoff_required}")
    print(f"  next: edit {out_path.name} to fill TODOs, then collect sign-offs")
    return 0


# ============================================================
# Subcommand: regress
# ============================================================

def cmd_regress(args) -> int:
    """Run regression set after a patch; compare to pre-patch results."""
    paths = scene_paths(args.scene)
    case_ids = [c.strip() for c in args.regression_set.split(",") if c.strip()]

    # Load pre-patch results
    pre_results = []
    if paths["results_yaml"].exists():
        try:
            pre_results = yaml.safe_load(paths["results_yaml"].read_text()) or []
        except yaml.YAMLError:
            pre_results = []
    pre_by_case = {r.get("case_id"): r for r in pre_results if r.get("case_id")}

    skill_output = _resolve_skill_output(args)

    # Find case files
    case_files = []
    for cid in case_ids:
        matches = list(paths["cases_dir"].glob(f"{cid}.md"))
        if not matches:
            print(f"WARN: case file not found for {cid}", file=sys.stderr)
            continue
        case_files.append(matches[0])

    if not case_files:
        print("ERROR: no case files found", file=sys.stderr)
        return 2

    # Score each
    print(f"[regress] scene={args.scene} cases={len(case_files)}")
    post_results = []
    for cf in case_files:
        cfm = parse_frontmatter(cf.read_text(encoding="utf-8"))
        scores = evaluate(skill_output, cfm)
        passed = all(s >= 1.0 for s in scores.values())
        post_results.append({
            "case_id": cfm.get("case_id"),
            "passed": passed,
            "scores": scores,
        })
        marker = "PASS" if passed else "FAIL"
        print(f"  {cfm.get('case_id')}: {marker}")

    # Compute regression verdict
    must_pass_all = all(r["passed"] for r in post_results)
    pre_pass_rates = []
    for cid in case_ids:
        pre = pre_by_case.get(cid)
        if pre:
            pre_pass_rates.append(1.0 if pre.get("result") == "PASS" else 0.0)
    pre_avg = sum(pre_pass_rates) / len(pre_pass_rates) if pre_pass_rates else 0.0
    post_avg = sum(1.0 if r["passed"] else 0.0 for r in post_results) / len(post_results)

    decision = "merged" if must_pass_all else "rejected"
    print(f"\n  pre-patch pass rate:  {pre_avg*100:.0f}%")
    print(f"  post-patch pass rate: {post_avg*100:.0f}%")
    print(f"  decision: {decision}")

    if args.write_merge_log:
        _append_merge_log(paths, args, post_results, pre_avg, post_avg, decision)
    return 0 if must_pass_all else 1


def _append_merge_log(paths, args, post_results, pre_avg, post_avg, decision):
    """Append a merge-log entry after regression."""
    paths["merge_log"].parent.mkdir(parents=True, exist_ok=True)
    log = []
    if paths["merge_log"].exists():
        try:
            log = yaml.safe_load(paths["merge_log"].read_text()) or []
        except yaml.YAMLError:
            log = []

    entry = {
        "proposal_id": args.proposal_id or f"unknown-{now_iso()}",
        "merged_at": now_iso(),
        "merged_by": args.merged_by or "evolution-runner",
        "regression_set": [r["case_id"] for r in post_results],
        "pre_patch": {"pass_rate": f"{pre_avg*100:.0f}%"},
        "post_patch": {
            "pass_rate": f"{post_avg*100:.0f}%",
            "scores": {r["case_id"]: r["scores"] for r in post_results},
            "still_failing": [r["case_id"] for r in post_results if not r["passed"]],
        },
        "decision": decision,
        "lessons_learned": args.lessons or "",
    }
    log.append(entry)
    paths["merge_log"].write_text(
        yaml.dump(log, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    print(f"  appended to: {paths['merge_log'].relative_to(REPO_ROOT)}")


# ============================================================
# Subcommand: compact (Pattern #5 — Progressive Compaction)
# ============================================================

def cmd_compact(args) -> int:
    """Archive old merge-log entries and rotate patterns across tiers.

    Archival policy (from config.yaml `archival:`):
      - merge_log_archive_after_days: archive entries older than N days
      - merge_log_active_max_entries: trigger if active log exceeds N
      - patterns_tier_threshold: promote/demote based on observed_count
    """
    from datetime import timedelta

    paths = scene_paths(args.scene)
    archival_cfg = EVOLUTION_CONFIG["archival"]
    archive_after = archival_cfg["merge_log_archive_after_days"]
    max_entries = archival_cfg["merge_log_active_max_entries"]
    tier_cfg = archival_cfg["patterns_tier_threshold"]

    report = {"merge_log": {}, "patterns": {}}
    archive_path = None  # local binding, set below only if any entry is archived

    # ---------- merge-log archival ----------
    if paths["merge_log"].exists():
        log = yaml.safe_load(paths["merge_log"].read_text(encoding="utf-8")) or []
    else:
        log = []

    cutoff = datetime.now() - timedelta(days=archive_after)
    active, archived = [], []
    for entry in log:
        merged_at_str = entry.get("merged_at", "")
        try:
            merged_at = datetime.fromisoformat(merged_at_str)
        except (ValueError, TypeError):
            merged_at = datetime.now()
        if merged_at < cutoff:
            archived.append(entry)
        else:
            active.append(entry)

    # Also archive if active log exceeds max_entries (size-based)
    size_triggered = False
    if len(active) > max_entries:
        size_triggered = True
        # Keep newest max_entries, archive the rest
        active.sort(key=lambda e: e.get("merged_at", ""), reverse=True)
        archived.extend(active[max_entries:])
        active = active[:max_entries]

    # Write archive file
    if archived:
        archive_dir = paths["merge_log"].parent / "archive"
        archive_dir.mkdir(parents=True, exist_ok=True)
        archive_path = archive_dir / f"merge-log-archived-{today_iso()}.yaml"
        # Append to existing archive file if same-day already exists
        if archive_path.exists():
            existing_archive = yaml.safe_load(archive_path.read_text(encoding="utf-8")) or []
        else:
            existing_archive = []
        existing_archive.extend(archived)
        archive_path.write_text(
            yaml.dump(existing_archive, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        paths["merge_log"].write_text(
            yaml.dump(active, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )

    report["merge_log"] = {
        "before": len(log),
        "active_after": len(active),
        "archived_count": len(archived),
        "size_triggered": size_triggered,
        "age_triggered": len(archived) > 0 and not size_triggered,
        "archive_path": str(archive_path.relative_to(REPO_ROOT)) if archive_path else None,
    }

    # ---------- pattern tier rotation ----------
    patterns_dir = paths["evolution_dir"] / "meta" / "patterns"
    if patterns_dir.exists():
        promotions = []
        demotions = []
        for tier_name in ["high", "medium", "low"]:
            tier_dir = patterns_dir / tier_name
            if not tier_dir.exists():
                continue
            for p_file in tier_dir.glob("p-*.md"):
                fm_text = p_file.read_text(encoding="utf-8")
                fm = parse_frontmatter(fm_text)
                count = fm.get("observed_count", 0)

                # Promote
                if tier_name in ("low", "medium") and count >= tier_cfg["promote_to_high"]:
                    target = patterns_dir / "high" / p_file.name
                    p_file.rename(target)
                    promotions.append(f"{p_file.name} → high/ (count={count})")
                # Demote
                elif tier_name in ("medium", "high") and count < tier_cfg["demote_to_low"]:
                    target = patterns_dir / "low" / p_file.name
                    p_file.rename(target)
                    demotions.append(f"{p_file.name} → low/ (count={count})")

        report["patterns"] = {
            "promotions": promotions,
            "demotions": demotions,
        }

    # ---------- output ----------
    print(f"[compact] scene={args.scene}")
    print(f"  merge-log: {report['merge_log']}")
    print(f"  patterns: {report['patterns']}")
    return 0


# ============================================================
# Subcommand: explore (Pattern #6 — Explore-Plan-Act)
# ============================================================

def cmd_explore(args) -> int:
    """Read-only exploration phase before REFL.

    Collects context (skill body, git log, adjacent scenes) WITHOUT generating
    any proposal. Output goes to evolution/explorations/<date>-<seq>.md for
    human review (per config.yaml `explore.require_human_approval: true`).
    """
    import subprocess  # local import to keep top-level clean
    paths = scene_paths(args.scene)
    explore_cfg = EVOLUTION_CONFIG["explore"]

    paths["evolution_dir"].mkdir(parents=True, exist_ok=True)
    explorations_dir = paths["evolution_dir"] / "explorations"
    explorations_dir.mkdir(parents=True, exist_ok=True)

    seq = next_seq_number(explorations_dir, today_iso())
    out_path = explorations_dir / f"{today_iso()}-{seq}.md"

    lines = [
        f"# Exploration Report — {args.scene}",
        f"",
        f"created_at: {now_iso()}",
        f"created_by: evolution-runner (explore phase)",
        f"purpose: read-only context collection BEFORE REFL/PATCH",
        f"",
        f"## 1. Target skill context",
        f"",
    ]

    # Read SKILL.md if target specified
    if args.target_skill:
        skill_path = resolve_scene_relative_path(args.target_skill, paths["scene_root"])
        if skill_path.exists():
            content = skill_path.read_text(encoding="utf-8")
            lines.append(f"**File**: `{skill_path.relative_to(REPO_ROOT)}`")
            lines.append(f"**Lines**: {len(content.splitlines())}")
            lines.append(f"**Bytes**: {len(content)}")
            fm = parse_frontmatter(content)
            lines.append(f"**Frontmatter keys**: {list(fm.keys())}")
            lines.append(f"")
            lines.append(f"### First 30 lines of body")
            lines.append(f"```")
            body = content.split("---", 2)[-1].strip() if "---" in content else content
            lines.extend(body.splitlines()[:30])
            lines.append(f"```")
        else:
            lines.append(f"⚠️ Target skill not found: {skill_path}")
    else:
        lines.append("(no --target-skill specified — exploration is shallow)")

    lines.append(f"")
    lines.append(f"## 2. Git log context")
    lines.append(f"")
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", f"-{explore_cfg['read_git_log_commits']}",
             "--", f"plugins/scenes/{args.scene}/"],
            capture_output=True, text=True, cwd=REPO_ROOT,
            timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            lines.append(f"```")
            lines.append(result.stdout.strip())
            lines.append(f"```")
        else:
            lines.append(f"(no git history or not a git repo)")
    except (subprocess.TimeoutExpired, FileNotFoundError):
        lines.append(f"(git unavailable)")

    lines.append(f"")
    lines.append(f"## 3. Adjacent scenes context")
    lines.append(f"")
    pool = EVOLUTION_CONFIG["smoke_test"].get("adjacent_scene_pool", [])
    adjacent_n = min(explore_cfg["read_adjacent_scenes"], len(pool))
    if adjacent_n > 0:
        lines.append(f"Reading {adjacent_n} adjacent scenes from config pool:")
        for adj in pool[:adjacent_n]:
            adj_root = SCENES_DIR / adj
            if adj_root.exists():
                skills = list((adj_root / "skills").glob("*/SKILL.md")) if (adj_root / "skills").exists() else []
                lines.append(f"- **{adj}**: {len(skills)} skills")
            else:
                lines.append(f"- **{adj}**: (does not exist)")
    else:
        lines.append(f"(no adjacent scene pool configured)")

    lines.append(f"")
    lines.append(f"## 4. Existing patterns in this scene")
    lines.append(f"")
    patterns_dir = paths["evolution_dir"] / "meta" / "patterns"
    if patterns_dir.exists():
        for tier in ["high", "medium", "low"]:
            tier_dir = patterns_dir / tier
            if tier_dir.exists():
                ps = list(tier_dir.glob("p-*.md"))
                lines.append(f"- **{tier}/**: {len(ps)} patterns")
                for p in ps:
                    fm = parse_frontmatter(p.read_text(encoding="utf-8"))
                    name = fm.get("name", p.stem)
                    lines.append(f"  - `{p.stem}` — {name}")
    else:
        lines.append(f"(no patterns yet — first exploration)")

    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## Next step")
    lines.append(f"")
    if explore_cfg["require_human_approval"]:
        lines.append(f"⚠️ **Human review required** before proceeding to REFL.")
        lines.append(f"")
        lines.append(f"After review:")
        lines.append(f"```")
        lines.append(f"python3 scripts/evolution-runner.py reflect \\")
        lines.append(f"    --scene {args.scene} \\")
        lines.append(f"    --exploration evolution/explorations/{today_iso()}-{seq}.md")
        lines.append(f"```")
    else:
        lines.append(f"Auto-proceed to REFL is enabled (require_human_approval=false).")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[explore] scene={args.scene}")
    print(f"  report: {out_path.relative_to(REPO_ROOT)}")
    print(f"  human_review_required: {explore_cfg['require_human_approval']}")
    return 0


# ============================================================
# Subcommand: merge-log (standalone append)
# ============================================================

def cmd_merge_log(args) -> int:
    paths = scene_paths(args.scene)
    paths["merge_log"].parent.mkdir(parents=True, exist_ok=True)
    log = []
    if paths["merge_log"].exists():
        try:
            log = yaml.safe_load(paths["merge_log"].read_text()) or []
        except yaml.YAMLError:
            log = []

    entry = {
        "proposal_id": args.proposal_id or f"unknown-{now_iso()}",
        "merged_at": now_iso(),
        "merged_by": args.merged_by or "manual",
        "decision": args.decision or "merged",
        "lessons_learned": args.lessons or "",
    }
    log.append(entry)
    paths["merge_log"].write_text(
        yaml.dump(log, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    print(f"[merge-log] appended: {paths['merge_log'].relative_to(REPO_ROOT)}")
    return 0


# ============================================================
# CLI entry point
# ============================================================

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Drive the evolution closed-loop for a legal scene.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # run-case
    p_run = sub.add_parser("run-case", help="Execute one test case and score it")
    p_run.add_argument("--scene", required=True)
    p_run.add_argument("--case", required=True, help="Path to test case .md")
    p_run.add_argument("--skill-output", help="Inline skill output string")
    p_run.add_argument("--skill-output-file", help="Path to skill output file")
    p_run.set_defaults(func=cmd_run_case)

    # reflect
    p_refl = sub.add_parser("reflect", help="Generate reflection scaffold")
    p_refl.add_argument("--scene", required=True)
    p_refl.add_argument("--cases", nargs="+", help="Failed case IDs")
    p_refl.add_argument("--scores-json", help='JSON dict of dimension scores, e.g. {"law_citation_accuracy": 0.0}')
    p_refl.add_argument("--trigger-ref", help="e.g. auto-test-run-2026-06-18")
    p_refl.add_argument("--trigger-type", default="manual")
    p_refl.set_defaults(func=cmd_reflect)

    # propose
    p_prp = sub.add_parser("propose", help="Generate proposal scaffold")
    p_prp.add_argument("--scene", required=True)
    p_prp.add_argument("--reflection", required=True, help="Path to reflection .md")
    p_prp.add_argument("--patch-type", help="Patch type (see evolution SKILL.md matrix)")
    p_prp.add_argument("--target-file", help="Override target SKILL.md path")
    p_prp.add_argument("--target-section", help="Override target section")
    p_prp.add_argument("--signoff-required", type=int, help="Override signoff count")
    p_prp.add_argument("--frame", default="cn-mainland", help="Legal frame")
    p_prp.set_defaults(func=cmd_propose)

    # regress
    p_reg = sub.add_parser("regress", help="Re-run regression set post-patch")
    p_reg.add_argument("--scene", required=True)
    p_reg.add_argument("--regression-set", required=True, help="Comma-separated case IDs")
    p_reg.add_argument("--pre-results", help="Path to _results.yaml (defaults to scene's)")
    p_reg.add_argument("--skill-output", help="Inline post-patch skill output")
    p_reg.add_argument("--skill-output-file", help="Path to post-patch skill output file")
    p_reg.add_argument("--proposal-id", help="Proposal being regressed")
    p_reg.add_argument("--merged-by", default="evolution-runner")
    p_reg.add_argument("--lessons", help="Lessons-learned text for merge-log")
    p_reg.add_argument("--write-merge-log", action="store_true", help="Append result to merge-log.yaml")
    p_reg.set_defaults(func=cmd_regress)

    # merge-log
    p_ml = sub.add_parser("merge-log", help="Append a merge-log entry directly")
    p_ml.add_argument("--scene", required=True)
    p_ml.add_argument("--proposal-id")
    p_ml.add_argument("--merged-by")
    p_ml.add_argument("--decision", choices=["merged", "rejected", "blocked"])
    p_ml.add_argument("--lessons")
    p_ml.set_defaults(func=cmd_merge_log)

    # compact (Pattern #5 Progressive Compaction)
    p_compact = sub.add_parser("compact", help="Archive old merge-log entries + rotate patterns across tiers")
    p_compact.add_argument("--scene", required=True)
    p_compact.set_defaults(func=cmd_compact)

    # explore (Pattern #6 Explore-Plan-Act)
    p_explore = sub.add_parser("explore", help="Read-only exploration phase before REFL")
    p_explore.add_argument("--scene", required=True)
    p_explore.add_argument("--target-skill", help="Path to target SKILL.md to inspect")
    p_explore.set_defaults(func=cmd_explore)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())