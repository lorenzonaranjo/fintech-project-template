# FinTech notes project

FIN 4506/5506, Spring 2027, second half (Professor Naranjo).

You and your partner write one page of notes on a fintech topic, the way the course notes are written: prose that explains the economics, a figure built from real data, and code that anyone can rerun. You may use Claude (or any AI tool) for everything. What you are graded on is what the AI cannot do for you: checking that every claim is true and that the code does what the page says it does.

## What you hand in

One Quarto page, `index.qmd`, rendered to `index.html`, in this repository:

- About 1,500 words of prose, not counting code and references.
- At least one figure built from real data that the code downloads or reads from `data/`.
- Every factual claim backed by a source in `references.bib` that you have read yourselves.
- A filled-in **What we checked** section at the end of the page.
- The full commit history of the repository, which is part of the submission.

## Dates

| Date | What |
|---|---|
| March 25 | Pairs formed, repository created from this template |
| April 1, 11:59 pm CT | Proposal: the title, the question section, an outline of the other sections, and three sources in `references.bib`, committed and pushed |
| April 22, 11:59 pm CT | Final page committed and pushed, with `index.html` rendered from the final version |

The repository is read at the deadline. Commits after it are not graded.

## Rules for working together

- **Each partner commits from their own GitHub account.** The history shows who did what; a page committed entirely by one partner is graded as such.
- **Commit as you go**, not once at the end. A history that starts the night before the deadline costs points under Process.
- **Keep the `Co-Authored-By: Claude` line** that Claude Code adds to its commits. Using AI is allowed; hiding it is not.
- **Say in the commit message what you checked**, for example "Checked the 2024 stablecoin market cap against the BIS report, Table 1; corrected the number."

## How the page is graded

| Part | Weight | What earns the points |
|---|---|---|
| Verification | 40% | Every claim has a source; the sources exist and say what the page says they say; the What we checked section is specific |
| Economics | 25% | The mechanism is explained correctly and clearly, at the level of the course notes |
| Evidence | 20% | The figure uses real data, is labeled and explained, and the code runs from a fresh copy of the repository |
| Process | 15% | Proposal on time; both partners commit; the work is spread over time; commit messages say what was checked |

A citation to a paper that does not exist, or that does not say what the page claims, loses all the Verification points for that claim, whoever wrote the sentence. This is the mistake AI tools make most often, so checking for it is your job.

## Setup

Do this once, before March 25. You need four things: Git, Python, a Python environment with Quarto, and Claude Code.

1. **Claude Edu.** Complete the "AI Literacy for the WashU Scholar" module on Canvas. It gives you access to Claude Edu through your WashU account.
2. **Git and a GitHub account.** Install Git from <https://git-scm.com/downloads> (on a Mac, running `git --version` in the Terminal offers to install it). Create a GitHub account if you do not have one, then tell Git who you are, using the email of your GitHub account:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

3. **Python.** Install Python 3.13 from <https://www.python.org/downloads/>. On Windows, tick "Add python.exe to PATH" in the installer.
4. **Claude Code.** Follow the installation instructions at <https://code.claude.com/docs/en/setup>, then run `claude` in a terminal and log in with your WashU Claude account.
5. **This repository.** Accept the GitHub Classroom invitation posted on Canvas, then clone your repository and set up its Python environment:

   ```bash
   git clone <your repository URL>
   cd <repository folder>
   python -m venv .venv
   ```

   Activate the environment with `source .venv/bin/activate` (Mac) or `.venv\Scripts\activate` (Windows), then:

   ```bash
   pip install -r requirements.txt
   python check_setup.py
   ```

`check_setup.py` checks each piece and tells you what is missing. Come to the March 25 lab with every line passing, or with the output of the script if something fails.

## Working on the page

Activate the environment, start Claude Code in the repository folder, and work from there:

```bash
claude
```

Claude reads `CLAUDE.md` in this folder, which sets the rules it follows for this project. Read it too: it is a short description of how the course notes are produced.

To see the page, render it and open `index.html` in a browser:

```bash
quarto render index.qmd
```

While writing, `quarto preview index.qmd` re-renders the page every time you save.

## Files

| File | What it is |
|---|---|
| `index.qmd` | Your page |
| `references.bib` | Your sources, in BibTeX |
| `data/` | Data files the page reads, each listed in `data/README.md` with where it came from |
| `CLAUDE.md` | Instructions for Claude Code in this project |
| `_quarto.yml` | Rendering settings; leave it as it is |
| `requirements.txt` | Python packages; add any package your code needs |
| `check_setup.py` | Setup check |
