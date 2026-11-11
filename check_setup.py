"""Check that everything the project needs is installed.

Run it from the repository folder with the environment active:

    python check_setup.py
"""

import importlib
import shutil
import subprocess
import sys
from pathlib import Path

results = []


def check(name, ok, fix=""):
    results.append(ok)
    print(f"[{'ok' if ok else 'MISSING'}] {name}")
    if not ok and fix:
        print(f"         {fix}")


def run(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return out.returncode == 0, (out.stdout + out.stderr).strip()
    except (OSError, subprocess.TimeoutExpired) as err:
        return False, str(err)


# Python
check(
    f"Python {sys.version.split()[0]}",
    sys.version_info >= (3, 11),
    "Install Python 3.13 from https://www.python.org/downloads/",
)
in_venv = sys.prefix != sys.base_prefix
check(
    "Course environment (.venv) active",
    in_venv,
    "From your fin4506 folder: source .venv/bin/activate (Mac) or .venv\\Scripts\\activate (Windows)",
)

# Git
has_git = shutil.which("git") is not None
check("Git installed", has_git, "Install Git from https://git-scm.com/downloads")
if has_git:
    name_ok, name = run(["git", "config", "user.name"])
    email_ok, email = run(["git", "config", "user.email"])
    check(
        f"Git user: {name} <{email}>" if name_ok and email_ok else "Git user name and email",
        name_ok and email_ok,
        'Run: git config --global user.name "Your Name"  and  git config --global user.email "you@example.com"',
    )
    repo_ok, _ = run(["git", "rev-parse", "--is-inside-work-tree"])
    check(
        "Running inside your cloned repository",
        repo_ok,
        "Run this script from the folder you cloned from GitHub",
    )

# Python packages
for pkg in ["numpy", "pandas", "matplotlib", "requests", "jupyter_core",
            "statsmodels", "yfinance", "pyarrow", "psycopg"]:
    try:
        importlib.import_module(pkg)
        check(f"Package {pkg}", True)
    except ImportError:
        check(f"Package {pkg}", False, "Run: pip install -r requirements.txt")

# Quarto
quarto = shutil.which("quarto")
if quarto:
    ok, out = run([quarto, "--version"])
    check(f"Quarto {out}" if ok else "Quarto", ok, "Run: pip install -r requirements.txt")
else:
    check("Quarto", False, "Run: pip install -r requirements.txt")

# Claude Code
claude = shutil.which("claude")
check(
    "Claude Code installed",
    claude is not None,
    "Install it: https://code.claude.com/docs/en/setup",
)

# Render a page: the project page in the project repository, the test page in the class log
page = next((p for p in [Path("index.qmd"), Path("setup-test.qmd")] if p.exists()), None)
if quarto and page:
    html = page.with_suffix(".html")
    print(f"Rendering {page} (this can take half a minute the first time)...")
    ok, out = run([quarto, "render", str(page)])
    check(f"{page} renders to {html}", ok and html.exists(), out[-500:])

print()
if all(results):
    print("Everything is set up.")
else:
    print(f"{results.count(False)} item(s) missing. Fix them and run this script again.")
    sys.exit(1)
