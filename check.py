#!/usr/bin/env python3
"""Check the documentation pages: python3 check.py [repo dir]. Exit 1 on a problem."""

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent).resolve()
PAGES = ROOT / "pages"
MAX_WORDS = 25  # STE: 20 in an instruction, 25 in a description
problems = []


def problem(where, text):
    problems.append(f"{where}: {text}")


def prose(text):
    """The page without code blocks, inline code, HTML comments, tables, headings and images."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines = [l for l in text.splitlines() if not l.lstrip().startswith(("|", "#", "!["))]
    text = "\n".join(lines)
    text = re.sub(r"`[^`]*`", "code", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text


def anchors(text):
    """GitHub-style heading anchors, as Forgejo and the website make them."""
    out = set()
    for h in re.findall(r"^#{1,6}\s+(.*)$", text, re.M):
        a = re.sub(r"[^\w\- ]", "", h.lower()).strip().replace(" ", "-")
        out.add(a)
    return out


order = [p["slug"] for p in tomllib.loads((ROOT / "pages.toml").read_text())["page"]]
for p in tomllib.loads((ROOT / "pages.toml").read_text())["page"]:
    if not p.get("summary"):
        problem("pages.toml", f"{p['slug']}: no summary")
files = {f.stem for f in PAGES.glob("*.md")}
for slug in sorted(set(order) - files):
    problem("pages.toml", f"{slug}: no pages/{slug}.md")
for slug in sorted(files - set(order)):
    problem(f"pages/{slug}.md", "not in pages.toml")
readme = (ROOT / "README.md").read_text()
for slug in order:
    if f"(pages/{slug}.md)" not in readme:
        problem("README.md", f"no link to pages/{slug}.md")

texts = {slug: (PAGES / f"{slug}.md").read_text() for slug in order if slug in files}
for slug, text in texts.items():
    where = f"pages/{slug}.md"
    lines = [l for l in text.splitlines() if l.strip()]
    if not lines or not re.match(r"# \S", lines[0]):
        problem(where, "must start with a '# Title' line")
    if len(lines) < 2 or not re.match(r"<!-- description: .+ -->$", lines[1]):
        problem(where, "the second line must be '<!-- description: ... -->'")
    if len(re.findall(r"^# ", text, re.M)) > 1:
        problem(where, "more than one '# ' title")
    if "misc-docs" in text:
        problem(where, "links to the private misc docs")
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"[a-z]+:", target):
            continue
        path, _, frag = target.partition("#")
        if path.startswith("../images/"):
            if not (ROOT / path[3:]).is_file():
                problem(where, f"no image {path}")
            continue
        page = path[:-3] if path.endswith(".md") else (slug if path == "" else None)
        if page not in texts:
            problem(where, f"link to a page that does not exist: {target}")
        elif frag and frag not in anchors(texts[page]):
            problem(where, f"link to a heading that does not exist: {target}")
    # A paragraph or a list item is one block; its lines join into sentences.
    for para in re.split(r"\n\s*\n|\n(?=\s*(?:[-*]|\d+\.)\s)", prose(text)):
        para = " ".join(re.sub(r"^\s*(?:>\s*)*(?:[-*]|\d+\.)?\s*", "", l) for l in para.splitlines())
        for sentence in re.split(r"(?<=[.!?:])\s+", para):
            n = len(sentence.split())
            if n > MAX_WORDS:
                problem(where, f"sentence has {n} words (max {MAX_WORDS}): {sentence[:70]}...")

for p in problems:
    print(p)
print(f"{len(texts)} pages, {len(problems)} problems")
sys.exit(1 if problems else 0)
