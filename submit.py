"""Make the file you hand in on Canvas: the whole repository, with its history.

Run it from the repository folder, after every member has pushed:

    python submit.py

It writes a .bundle file in the folder above this one (your course folder).
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)


repo = Path(__file__).resolve().parent
if git("-C", str(repo), "rev-parse", "--is-inside-work-tree").returncode != 0:
    sys.exit("This folder is not a git repository. Run submit.py from your cloned project folder.")

if git("-C", str(repo), "remote").stdout.strip():
    print("Getting your teammates' latest commits...")
    pull = git("-C", str(repo), "pull", "--ff-only")
    if pull.returncode != 0:
        sys.exit("git pull failed:\n" + pull.stderr + "\nFix this (or ask a teammate), then run submit.py again.")

status = git("-C", str(repo), "status", "--porcelain").stdout.strip()
if status:
    sys.exit("These files have changes that are not committed:\n" + status
             + "\n\nCommit them (and push), then run submit.py again.")

if not (repo / "index.html").exists():
    print("Warning: index.html is missing. Render the page with `quarto render index.qmd` and commit it.")

out = repo.parent / f"{repo.name}-{datetime.now():%Y-%m-%d-%H%M}.bundle"
made = git("-C", str(repo), "bundle", "create", str(out), "--all")
if made.returncode != 0 or git("-C", str(repo), "bundle", "verify", str(out)).returncode != 0:
    sys.exit("Could not create the bundle:\n" + made.stderr)

commits = git("-C", str(repo), "rev-list", "--count", "HEAD").stdout.strip()
print(f"\nCreated {out}")
print(f"It contains {commits} commits. Upload this file to the Canvas assignment.")
