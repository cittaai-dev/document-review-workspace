"""Fill the database with sample documents (and a few tags).

    python -m app.seed

Safe to re-run: it rebuilds the tables from scratch each time.
"""
from app.db import DB_PATH, get_conn, init_db

DOCUMENTS = [
    dict(title="Master Services Agreement — Acme Corp", kind="contract", status="pending",
         body="This Master Services Agreement is entered into by Acme Corp and Northwind Ltd, "
              "effective 14 March 2025, for a total value of $48,000 over twelve months.",
         tags=[dict(type="party", value="Acme Corp"), dict(type="date", value="2025-03-14")]),
    dict(title="Invoice #10432", kind="invoice", status="reviewed",
         body="Invoice #10432 issued to Globex Inc on 02 April 2025. Amount due: $1,250.00. "
              "Net 30 terms.",
         tags=[dict(type="party", value="Globex Inc"), dict(type="amount", value="$1,250.00"),
               dict(type="date", value="2025-04-02")]),
    dict(title="NDA — Initech", kind="contract", status="untagged",
         body="Mutual Non-Disclosure Agreement between Initech and the Company, dated 21 May 2025.",
         tags=[]),
    dict(title="Expense Form — Q1 Travel", kind="form", status="untagged",
         body="Travel expense reimbursement form for Q1 2025. Total claimed: $860.40.",
         tags=[]),
    dict(title="Statement of Work — Umbrella", kind="contract", status="pending",
         body="Statement of Work for Umbrella Corp covering the analytics platform build. "
              "Estimated at $92,500, kickoff 09 June 2025.",
         tags=[dict(type="party", value="Umbrella Corp")]),
    dict(title="Invoice #10501", kind="invoice", status="untagged",
         body="Invoice #10501 to Stark Industries, 18 June 2025. Amount due: $7,900.00.",
         tags=[]),
    dict(title="Vendor Onboarding Form — Wayne Ent.", kind="form", status="reviewed",
         body="Vendor onboarding details for Wayne Enterprises. Primary contact: A. Pennyworth.",
         tags=[dict(type="party", value="Wayne Enterprises")]),
    dict(title="Lease Agreement — Suite 400", kind="contract", status="untagged",
         body="Commercial lease for Suite 400, term 36 months, monthly rent $3,200, "
              "commencing 01 July 2025.",
         tags=[]),
    dict(title="Invoice #10555", kind="invoice", status="pending",
         body="Invoice #10555 to Hooli, 30 June 2025. Amount due: $415.00.",
         tags=[dict(type="party", value="Hooli")]),
    dict(title="Consulting Agreement — Soylent", kind="contract", status="untagged",
         body="Consulting agreement with Soylent Corp, day rate $1,100, starting 12 August 2025.",
         tags=[]),
]


def seed() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()
    conn = get_conn()
    for doc in DOCUMENTS:
        cur = conn.execute(
            "INSERT INTO documents (title, kind, body, status) VALUES (?, ?, ?, ?)",
            (doc["title"], doc["kind"], doc["body"], doc["status"]),
        )
        doc_id = cur.lastrowid
        for tag in doc["tags"]:
            conn.execute(
                "INSERT INTO tags (document_id, type, value) VALUES (?, ?, ?)",
                (doc_id, tag["type"], tag["value"]),
            )
    conn.commit()
    conn.close()
    print(f"Seeded {len(DOCUMENTS)} documents into {DB_PATH.name}.")


if __name__ == "__main__":
    seed()
