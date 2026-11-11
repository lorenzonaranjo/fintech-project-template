# FinTech notes project

FIN 4506/5506, Spring 2027, second half (Professor Naranjo).

The three of you write one page of notes on a fintech topic, the way the course notes are written: prose that explains the economics, a figure built from real data, and code that anyone can rerun. You may use Claude (or any AI tool) for everything. What you are graded on is what the AI cannot do for you: checking that every claim is true and that the code does what the page says it does.

## What you hand in

One Quarto page, `index.qmd`, rendered to `index.html`, in this repository:

- About 1,500 words of prose, not counting code and references.
- At least one figure built from real data that the code downloads or reads from `data/`.
- Every factual claim backed by a source in `references.bib` that you have read yourselves.
- A filled-in **What we checked** section at the end of the page.
- The full commit history of the repository, which is part of the submission. You hand it in as a single file made by `submit.py` (see Handing in below).

## Dates

| Date | What |
|---|---|
| March 25 | Groups of three formed; one member creates the repository and every member clones it |
| April 1, 11:59 pm CT | Proposal handed in on Canvas: the title, the question section, an outline of the other sections, and three sources in `references.bib` |
| April 22, 11:59 pm CT | Final page handed in on Canvas, with `index.html` rendered from the final version |

Canvas records when the file arrives. One member hands in for the group.

## Rules for working together

- **Each member commits from their own GitHub account.** The history shows who did what; a member with no commits is graded as such.
- **Each member owns sections.** The page is split into section files (see Files below) so that you can work at the same time without overwriting each other. Agree who owns which file; anyone may fix anything, but say so in the commit message.
- **Commit as you go**, not once at the end. A history that starts the night before the deadline costs points under Process.
- **Keep the `Co-Authored-By: Claude` line** that Claude Code adds to its commits. Using AI is allowed; hiding it is not.
- **Say in the commit message what you checked**, for example "Checked the 2024 stablecoin market cap against the BIS report, Table 1; corrected the number."

## How the page is graded

| Part | Weight | What earns the points |
|---|---|---|
| Verification | 40% | Every claim has a source; the sources exist and say what the page says they say; the What we checked section is specific |
| Economics | 25% | The mechanism is explained correctly and clearly, at the level of the course notes |
| Evidence | 20% | The figure uses real data, is labeled and explained, and the code runs from a fresh copy of the repository |
| Process | 15% | Proposal on time; every member commits; the work is spread over time; commit messages say what was checked |

A citation to a paper that does not exist, or that does not say what the page claims, loses all the Verification points for that claim, whoever wrote the sentence. This is the mistake AI tools make most often, so checking for it is your job.

## Setup

You already set up Git, Python, Claude Code and the course environment for your class log (see its README).

One member creates the group's repository:

1. Open <https://github.com/lorenzonaranjo/fintech-project-template>, click **Use this template**, then **Create a new repository**.
2. Choose your own account as the owner, give it a name, and select **Private**.
3. In the new repository, go to **Settings > Collaborators** and add the other two members by their GitHub usernames. They accept the invitation from their email or from GitHub's notifications.

Then each member clones the repository into the course folder, next to the class log:

```bash
cd fin4506
git clone <your project repository URL> project
```

Activate the environment with `source .venv/bin/activate` (Mac) or `.venv\Scripts\activate` (Windows), then:

```bash
cd project
pip install -r requirements.txt
python check_setup.py
```

`check_setup.py` checks each piece and renders the page.

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

Before you start working, run `git pull` to get your teammates' latest commits; when you finish, commit and `git push`.

## Handing in

GitHub's "Download ZIP" button leaves out the history, so do not use it. Instead, once everyone has pushed, one member runs, with the environment active:

```bash
python submit.py
```

It pulls the latest commits, stops if anything is not committed, and writes one file in the course folder, for example `fin4506/project-2027-04-22-2315.bundle`, that holds the whole repository with its history. Upload that file to the Canvas assignment.

## Files

| File | What it is |
|---|---|
| `TOPICS.md` | The project topics, with sources and data to start from |
| `index.qmd` | The page: title, authors, and the list of section files it includes |
| `_question.qmd`, `_how-it-works.qmd`, `_evidence.qmd`, `_what-we-learned.qmd` | The sections of the page, one file each |
| `_checks.qmd` | The What we checked table; each member adds rows for the claims they checked |
| `references.bib` | Your sources, in BibTeX |
| `data/` | Data files the page reads, each listed in `data/README.md` with where it came from |
| `CLAUDE.md` | Instructions for Claude Code in this project |
| `_quarto.yml` | Rendering settings; leave it as it is |
| `requirements.txt` | Python packages; add any package your code needs |
| `check_setup.py` | Setup check |
| `submit.py` | Makes the file you hand in on Canvas |
