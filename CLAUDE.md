# Instructions for Claude in this project

Two students are writing a page of notes on a fintech topic for FIN 4506/5506 at WashU. The students are the authors and are graded on the page. Your job is to help them write it and to make it easy for them to check every claim. They must be able to explain every sentence and every line of code on the page.

## Sources

- **Never invent a source.** Cite only papers, reports, articles and datasets that the students have found and can open. If a claim needs a source and none is in `references.bib`, say so and suggest where to look; do not add a reference from memory.
- When you add a citation, tell the students exactly what to check in the source (page, table, section) so they can confirm it says what the sentence says.
- If you are not sure a fact is true, say so plainly. "I don't know" is a good answer.

## Data and code

- Figures use real data: downloaded by the code from a named public source (FRED, the SEC, Yahoo Finance, a blockchain explorer, a paper's replication files) or read from a file in `data/` whose origin is recorded in `data/README.md`. Never generate made-up data to stand in for real data.
- Run the code before describing its output. Report numbers as the code produced them, not from memory.
- Keep code short and readable. Explain any line a student new to Python would not follow.
- Add any package the code needs to `requirements.txt`.

## Writing

- Plain prose that explains the economics: what problem the technology solves, for whom, and what can go wrong. Define every technical term the first time it appears.
- Every figure has a caption, labeled axes with units, and alt text (`fig-alt`) that describes what it shows.
- Fill in the **What we checked** section as you go: each important claim, its source, and how the students checked it.

## Git

- Commit after each meaningful step, with a message that says what changed and what was checked.
- Keep the `Co-Authored-By: Claude` line in commit messages.
- Never rewrite history (no `git rebase`, `git commit --amend` on pushed commits, or force pushes). The history is part of the grade.
