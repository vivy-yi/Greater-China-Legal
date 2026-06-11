#!/usr/bin/env python3
"""
sync-upstream.py — Sync from anthropic/claude-for-legal upstream

Usage:
    python3 scripts/sync-upstream.py [--check-only] [--force]

Options:
    --check-only  Just check if new upstream commits exist (no merge)
    --force Merge even if already synced
"""

import subprocess
import sys
import re
from pathlib import Path


UPSTREAM_REMOTE = "upstream"
UPSTREAM_REPO = "anthropics/claude-for-legal"
UPSTREAM_BRANCH = "main"
LAST_SYNC_FILE = ".last-sync-commit"


def run(cmd: list[str], capture=True) -> subprocess.CompletedProcess:
    result = subprocess.run(cmd, capture_output=capture, text=True)
    return result


def get_upstream_sha() -> str:
    run(["git", "remote", "add", UPSTREAM_REMOTE,
         f"https://github.com/{UPSTREAM_REPO}.git"], capture=False)
    run(["git", "fetch", UPSTREAM_REMOTE, UPSTREAM_BRANCH])
    result = run(["git", "rev-parse", f"{UPSTREAM_REMOTE}/{UPSTREAM_BRANCH}"])
    return result.stdout.strip()


def get_last_sync() -> str | None:
    f = Path(LAST_SYNC_FILE)
    if f.exists():
        return f.read_text().strip()
    return None


def write_last_sync(sha: str):
    Path(LAST_SYNC_FILE).write_text(sha + "\n")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    upstream_sha = get_upstream_sha()
    last_sync = get_last_sync()

    print(f"Upstream main: {upstream_sha}")
    print(f"Last sync:    {last_sync or '(never)'}")

    if not args.force and upstream_sha == last_sync:
        print("✅ Already synced — no new upstream commits")
        sys.exit(0)

    if args.check_only:
        print(f"⚠️  New upstream commits available ({upstream_sha})")
        sys.exit(1)

    # Merge upstream/main into current branch
    print("Merging upstream/main...")
    result = run(["git", "merge", f"{UPSTREAM_REMOTE}/{UPSTREAM_BRANCH}",
                  "--no-edit"])

    if result.returncode != 0:
        print("❌ Merge conflict detected")
        print(result.stderr)
        run(["git", "merge", "--abort"])
        sys.exit(1)

    write_last_sync(upstream_sha)
    run(["git", "add", LAST_SYNC_FILE])
    run(["git", "commit", "-m", f"chore: sync upstream ({upstream_sha[:8]})"])
    print(f"✅ Synced to {upstream_sha[:8]}")
    print("⚠️  Remember to push: git push origin main")


if __name__ == "__main__":
    main()