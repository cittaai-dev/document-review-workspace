// Document Review Workspace — frontend.
// The read flow (list + detail + tag display) is complete.
// The three tagging actions at the bottom are yours to wire up.

const listEl = document.getElementById("list");
const detailEl = document.getElementById("detail");

// ---------------------------------------------------------------------------
// Provided: load and render
// ---------------------------------------------------------------------------
async function loadDocuments() {
  const docs = await fetch("/api/documents").then((r) => r.json());
  listEl.innerHTML = "";
  for (const d of docs) {
    const item = document.createElement("button");
    item.className = "doc-item";
    item.innerHTML =
      `<span class="doc-title"></span><span class="doc-meta"></span>`;
    item.querySelector(".doc-title").textContent = d.title;
    item.querySelector(".doc-meta").textContent = `${d.kind} · ${d.status}`;
    item.onclick = () => loadDetail(d.id);
    listEl.appendChild(item);
  }
}

async function loadDetail(docId) {
  const doc = await fetch(`/api/documents/${docId}`).then((r) => r.json());
  detailEl.innerHTML = `
    <h2></h2>
    <p class="doc-meta"></p>
    <pre class="body"></pre>
    <h3>Tags</h3>
    <ul id="tags"></ul>
    <form id="add-tag">
      <select name="type">
        <option value="party">party</option>
        <option value="date">date</option>
        <option value="amount">amount</option>
        <option value="status">status</option>
      </select>
      <input name="value" placeholder="value" />
      <button type="submit">Add tag</button>
    </form>`;
  detailEl.querySelector("h2").textContent = doc.title;
  detailEl.querySelector(".doc-meta").textContent = `${doc.kind} · ${doc.status}`;
  detailEl.querySelector(".body").textContent = doc.body;
  renderTags(doc);
  document.getElementById("add-tag").onsubmit = (e) => onAddTag(e, doc.id);
}

function renderTags(doc) {
  const ul = document.getElementById("tags");
  ul.innerHTML = "";
  for (const tag of doc.tags) {
    const li = document.createElement("li");
    const label = document.createElement("span");
    label.className = "tag";
    label.textContent = `${tag.type}: ${tag.value}`;
    const edit = document.createElement("button");
    edit.textContent = "edit";
    edit.onclick = () => onEditTag(tag, doc.id);
    const remove = document.createElement("button");
    remove.textContent = "remove";
    remove.onclick = () => onRemoveTag(tag.id, doc.id);
    li.append(label, edit, remove);
    ul.appendChild(li);
  }
}

// ---------------------------------------------------------------------------
// YOUR TASK: wire these three to the API (endpoints live in app/main.py).
// Tip: after a successful change, call loadDetail(docId) to refresh the panel
// without a full page reload.
// ---------------------------------------------------------------------------
async function onAddTag(event, docId) {
  event.preventDefault();
  // TODO: read `type` and `value` from the form, POST to
  //       /api/documents/{docId}/tags, then refresh. Ignore an empty value.
  alert("TODO: implement add tag");
}

async function onEditTag(tag, docId) {
  // TODO: ask for a new value, PUT to /api/tags/{tag.id}, then refresh.
  alert("TODO: implement edit tag");
}

async function onRemoveTag(tagId, docId) {
  // TODO: DELETE /api/tags/{tagId}, then refresh.
  alert("TODO: implement remove tag");
}

loadDocuments();
