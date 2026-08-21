#!/usr/bin/env python3
"""
Phase 5 helper: Ghost/Casper auto-generates tag archive pages at
/tag/<tag-slug>/ (and author archive pages at /author/<author-slug>/).
Jasper/Jekyll doesn't build equivalent archive pages out of the box, so
without action those old URLs would 404 -- bad for anyone who bookmarked
or linked to a tag page, and bad for any search-index entries pointing there.

This script scans your converted _posts/ and _drafts/ front matter,
collects every unique tag, slugifies it the way Ghost does, and prints
a ready-to-paste `redirect_from:` block. Paste that block into the front
matter of whatever page should now catch those old URLs -- home page is
the simplest choice; a real tag-listing page is a nicer one if you build
one later.

Usage:
    python3 generate_redirect_list.py /path/to/your/jekyll/repo
"""
import re
import sys
from pathlib import Path

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
TAGS_LINE_RE = re.compile(r'^tags:\s*\[(.*?)\]\s*$', re.MULTILINE)


def ghost_slugify(tag: str) -> str:
    """Approximate Ghost's tag-slug algorithm: lowercase, spaces -> hyphens,
    strip anything that isn't a-z/0-9/hyphen."""
    s = tag.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9\-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def extract_tags(md_text: str) -> list[str]:
    fm_match = FRONT_MATTER_RE.match(md_text)
    if not fm_match:
        return []
    fm = fm_match.group(1)
    tags_match = TAGS_LINE_RE.search(fm)
    if not tags_match:
        return []
    raw = tags_match.group(1)
    # entries look like: "tag one", "tag-two"
    return [t.strip().strip('"') for t in raw.split(",") if t.strip()]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    repo = Path(sys.argv[1])
    dirs = [repo / "_posts", repo / "_drafts"]

    all_tags = set()
    files_scanned = 0
    for d in dirs:
        if not d.exists():
            continue
        for md_file in d.glob("*.md"):
            files_scanned += 1
            text = md_file.read_text(encoding="utf-8", errors="ignore")
            for tag in extract_tags(text):
                all_tags.add(tag)

    if files_scanned == 0:
        print(f"No .md files found under {dirs}. Point this at your Jekyll repo root.")
        sys.exit(1)

    tag_slugs = sorted({ghost_slugify(t) for t in all_tags if t})

    print(f"Scanned {files_scanned} files, found {len(all_tags)} unique tags.\n")
    print("Paste this into the front matter of the page that should now")
    print("catch old tag-archive URLs (home page is the simplest target):\n")
    print("redirect_from:")
    for slug in tag_slugs:
        print(f"  - /tag/{slug}/")
    print()
    print("# If Ghost author archive pages were ever linked or indexed,")
    print("# add lines like the ones below too (fill in your actual author slug(s)):")
    print("  # - /author/your-author-slug/")


if __name__ == "__main__":
    main()
