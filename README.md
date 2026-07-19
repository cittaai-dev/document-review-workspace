# Document Review Workspace — Take-Home (Junior Full-Stack)

A small, **already-running** full-stack app. Your job is to finish one feature: **tagging documents**.

**Expected time: 2–3 hours.** Please don't spend more than that. A tidy, working solution to the checklist below is exactly what we want — no extra features needed.

---

## What this app is

A workspace where a team reviews documents (contracts, invoices, forms) and tags them with things like *party*, *date*, *amount*, and *status*. The document list, the document view, the database, and the sample data are already built and working. Three tagging actions — **add, edit, remove** — are left for you to implement, on both the backend and the frontend.

## What's already provided

- **Backend** (`app/`): a FastAPI server on a SQLite database, with sample data and the two read endpoints — list documents, and get one document with its tags.
- **Frontend** (`web/`): a plain HTML/JavaScript page that lists documents and shows a document with its tags. No build step, no frameworks.
- **Tests** (`tests/`): a few passing tests for the read endpoints.

## Your task

Implement the three tagging actions end to end. Each has a clearly marked `TODO`:

- **Backend** — `app/main.py`: `add_tag`, `update_tag`, `delete_tag`
- **Frontend** — `web/app.js`: `onAddTag`, `onEditTag`, `onRemoveTag`

### Acceptance criteria

Your solution is done when all of these are true:

1. A user can **add** a tag (type + value) to a document; it saves and shows up in the tag list **without a full page reload**.
2. A user can **edit** an existing tag's value.
3. A user can **remove** a tag.
4. Adding a tag with an **empty value is rejected** — no blank tags reach the database.
5. Acting on a **document or tag that doesn't exist returns 404**, not a crash.
6. Tags **persist** — they're still there after you restart the server.
7. The provided tests still pass, and you've **added one test** for adding a tag (un-skip and complete `test_add_tag` in `tests/test_tags.py`).

Keep it simple and readable. We're looking for these seven done cleanly, not for cleverness.

---

## Running it

Requires **Python 3.10+**.

```bash
pip install -r requirements.txt
python -m app.seed          # create and fill the database
uvicorn app.main:app --reload
```

Then open **http://localhost:8000**. (Or just run `./run.sh`.)

Run the tests:

```bash
pytest
```

## Project structure

```
app/
  main.py      FastAPI app — read endpoints done, tag endpoints are TODO
  db.py        tiny SQLite helper
  schema.sql   the two tables (documents, tags)
  seed.py      sample data
tests/
  test_tags.py read-endpoint tests + one TODO test
web/
  index.html   two-pane layout
  app.js       read flow done, tag actions are TODO
  style.css
```

## How we evaluate

We care most that it **works** and that your code is **clear and easy to read**. A working, tidy solution to the seven criteria is a strong submission. Trajectory matters more than polish — if you make a trade-off or run out of time, just tell us.

## Submitting

Push your solution to a repository and share the link (or send a zip). Add a short note — a few lines is plenty — covering anything you'd like us to know: what you'd improve with more time, and any assumptions you made.

Good luck — we're looking forward to seeing it.
