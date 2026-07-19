"""Document Review Workspace — API + static frontend.

Read endpoints (list, get-one) are complete. The three tagging actions
below are yours to implement — look for the `TODO` blocks.
"""
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.db import get_conn

app = FastAPI(title="Document Review Workspace")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


class TagIn(BaseModel):
    type: str
    value: str


# ---------------------------------------------------------------------------
# Provided: read endpoints
# ---------------------------------------------------------------------------
@app.get("/api/documents")
def list_documents():
    conn = get_conn()
    rows = conn.execute(
        "SELECT id, title, kind, status FROM documents ORDER BY id"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.get("/api/documents/{doc_id}")
def get_document(doc_id: int):
    conn = get_conn()
    doc = conn.execute("SELECT * FROM documents WHERE id = ?", (doc_id,)).fetchone()
    if doc is None:
        conn.close()
        raise HTTPException(404, "document not found")
    tags = conn.execute(
        "SELECT id, type, value FROM tags WHERE document_id = ? ORDER BY id", (doc_id,)
    ).fetchall()
    conn.close()
    return {**dict(doc), "tags": [dict(t) for t in tags]}


# ---------------------------------------------------------------------------
# YOUR TASK: implement these three. See the README acceptance criteria.
# ---------------------------------------------------------------------------
@app.post("/api/documents/{doc_id}/tags", status_code=201)
def add_tag(doc_id: int, tag: TagIn):
    # TODO: insert a new tag for this document and return the created tag.
    #   - reject empty type/value
    #   - 404 if the document does not exist
    raise HTTPException(501, "not implemented — see README acceptance criteria")


@app.put("/api/tags/{tag_id}")
def update_tag(tag_id: int, tag: TagIn):
    # TODO: update this tag's type/value and return it. 404 if it does not exist.
    raise HTTPException(501, "not implemented — see README acceptance criteria")


@app.delete("/api/tags/{tag_id}", status_code=204)
def delete_tag(tag_id: int):
    # TODO: delete this tag. 404 if it does not exist.
    raise HTTPException(501, "not implemented — see README acceptance criteria")


# ---------------------------------------------------------------------------
# Serve the frontend (keep this mount last so /api/* routes win)
# ---------------------------------------------------------------------------
app.mount(
    "/", StaticFiles(directory=Path(__file__).parent.parent / "web", html=True), name="web"
)
