#!/usr/bin/env python3
"""Static checks on the production build, run by the `verify` CI job (added Nov 24, 2026).

Fails (exit 1) on: an internal link to a page or asset that is neither built nor redirected, a page without a
<title> or <h1>, JSON-LD that does not parse, "bookable now" before opening, or staging text.
Usage: python3 test/ci_static.py .
"""
import json
import os
import re
import sys
from urllib.parse import urlparse, unquote

root = sys.argv[1] if len(sys.argv) > 1 else "."
problems = []

redirects = set()
rp = os.path.join(root, "_redirects")
if os.path.exists(rp):
    for line in open(rp, encoding="utf-8"):
        parts = line.split()
        if parts and not parts[0].startswith("#"):
            redirects.add(parts[0].rstrip("/") or "/")


def exists(path):
    p = unquote(path.split("#")[0].split("?")[0])
    if p in ("", "/"):
        return True
    if (p.rstrip("/") or "/") in redirects:
        return True
    f = os.path.join(root, p.lstrip("/"))
    return any(os.path.isfile(c) for c in (f, f + ".html", os.path.join(f, "index.html")))


BUSINESS_TYPES = {"MedicalClinic", "LocalBusiness", "MedicalBusiness", "PhysicalTherapy"}


def schema_problems(rel, node):
    """Schema checks added Nov 26, 2026 after Semrush Site Audit markup errors:
    reviewedBy/lastReviewed are WebPage properties (not Article), and a LocalBusiness-type node needs an address."""
    if isinstance(node, list):
        for n in node:
            schema_problems(rel, n)
        return
    if not isinstance(node, dict):
        return
    types = node.get("@type")
    types = set(types) if isinstance(types, list) else {types}
    if "Article" in types and not (types & {"WebPage", "MedicalWebPage"}):
        for prop in ("reviewedBy", "lastReviewed"):
            if prop in node:
                problems.append(f"{rel}: {prop} on an Article node (belongs on the WebPage)")
    if types & BUSINESS_TYPES and "address" not in node:
        problems.append(f"{rel}: {sorted(types & BUSINESS_TYPES)[0]} node without address")
    for v in node.values():
        schema_problems(rel, v)


pages = 0
for dirpath, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in ("node_modules", "test", ".git", ".github")]
    for name in files:
        if not name.endswith(".html"):
            continue
        pages += 1
        rel = os.path.relpath(os.path.join(dirpath, name), root)
        html = open(os.path.join(dirpath, name), encoding="utf-8", errors="replace").read()
        noindex = re.search(r'<meta name="robots" content="[^"]*noindex', html) is not None
        if not noindex:
            if not re.search(r"<title>[^<]+</title>", html):
                problems.append(f"{rel}: missing <title>")
            if "<h1" not in html:
                problems.append(f"{rel}: missing <h1>")
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                json.loads(block)
            except ValueError as e:
                problems.append(f"{rel}: invalid JSON-LD ({e})")
                continue
            schema_problems(rel, json.loads(block))
        if re.search(r"bookable now", html, re.I):
            problems.append(f"{rel}: claims bookable now (Proof opens Feb 2027)")
        if re.search(r"DEMO-|Staging build", html):
            problems.append(f"{rel}: staging text")
        for href in re.findall(r'(?:href|src)="([^"]+)"', html):
            u = urlparse(href)
            if u.scheme or href.startswith(("//", "#", "mailto:", "tel:", "data:", "javascript:")):
                continue
            if not href.startswith("/"):
                href = "/" + os.path.normpath(os.path.join(os.path.dirname(rel), href)).lstrip("./")
            if not exists(href):
                problems.append(f"{rel}: broken internal link {href}")

print(f"pages checked: {pages}; problems: {len(problems)}")
for p in sorted(set(problems))[:200]:
    print("  " + p)
sys.exit(1 if problems or pages == 0 else 0)
