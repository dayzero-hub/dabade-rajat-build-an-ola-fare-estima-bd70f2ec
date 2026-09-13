# Ola — fare estimate API (Python)

Welcome. This repository is **empty on purpose**. Everything in it is yours to create.

## Where the work is

Open the **Issues** tab. There are four, in order. Each one says exactly what done looks like,
and the fare rules are written out in full — there is nothing to invent.

One issue at a time:

```bash
git checkout main
git pull
git checkout -b issue-1
# ...make your changes...
git add .
git commit -m "Add the fare endpoint"
git push -u origin issue-1
```

Then open a **Pull Request** with `Closes #1` in the description. Raj reviews it.

## Setting up, once

You need Python 3. Check with `python3 --version`.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install flask
python app.py
```

**The bit that catches everyone:** `source .venv/bin/activate` has to be run again in every
new terminal window. If `flask` is suddenly "not found", that is almost always why — you are
in a shell where the venv was never activated.

No database. No Docker. One dependency.

## Why this repository is nearly empty

Deliberately, and it stays that way.

Some templates in the library hand you a scaffold — the boring setup done, so you can get
straight to the work. This one cannot, because **ticket 1 asks you to commit
`requirements.txt` and a `.gitignore` covering your virtual environment and `__pycache__`.**
Those files arriving ready-made would do two of that ticket's steps for you.

That is not busywork: keeping a virtual environment and `__pycache__` out of git is a habit
every Python repository needs, and the ticket makes you do it once, on purpose, before it can
become a bad habit.

(If you are an engineer auditing the templates: this repo being two files is a decision, not
the thin-template gap. Its ticket 1 creates exactly the files a scaffold would have added.)
