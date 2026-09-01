#!/usr/bin/env python3
"""
docx_to_md.py — convert a Word manuscript to canonical Markdown.

Usage:
    python tools/docx_to_md.py <input.docx> <output.md> "<Title>" "<status>"

The repo's source of truth is the generated .md. The .docx stays the authoring
copy (edited in Word); regenerate the .md after each rewrite pass:

    python tools/docx_to_md.py "path/Book.docx" corpus/x/book.md "Title" "rewrite-complete"

status is free text shown in the frontmatter, e.g.:
    rewrite-complete | first-draft | not-written
"""
import sys, os, docx

def run_md(run):
    t = run.text or ""
    if not t.strip():
        return t
    if run.bold and run.italic:
        return f"***{t}***"
    if run.bold:
        return f"**{t}**"
    if run.italic:
        return f"*{t}*"
    return t

def para_md(p):
    style = (p.style.name if p.style else "") or ""
    text = "".join(run_md(r) for r in p.runs).strip() or p.text.strip()
    if not text:
        return ""
    if style.startswith("Heading"):
        digits = "".join(c for c in style if c.isdigit())
        lvl = int(digits) if digits else 2
        lvl = max(1, min(lvl, 6))
        return "#" * lvl + " " + text
    if style == "Title":
        return "# " + text
    if "List" in style:
        return "- " + text
    return text

def convert(src, out, title, status):
    d = docx.Document(src)
    lines = []
    for p in d.paragraphs:
        m = para_md(p)
        if m:
            lines.append(m)
    body = "\n\n".join(lines)
    src_rel = os.path.basename(src)
    front = (
        "---\n"
        f"title: {title}\n"
        f"status: {status}\n"
        f"source: {src_rel}\n"
        "generated_by: tools/docx_to_md.py\n"
        "note: Canonical text is this .md. Edit the .docx, then regenerate.\n"
        "---\n\n"
    )
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(front + body + "\n")
    words = sum(len(l.split()) for l in lines)
    print(f"wrote {out}  ({words} words)")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(__doc__); sys.exit(1)
    convert(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
