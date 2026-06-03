"""
add-furigana.py — Pre-process markdown files to add furigana readings to kanji.

Uses pykakasi (dictionary-based Japanese morphological analyzer, no LLM).
Outputs in mkdocs-ruby-plugin syntax:
  - Single kanji:  漢字(かんじ)
  - Multi-kanji:   {文章(ぶんしょう)}

Run:  python scripts/add-furigana.py docs/
"""

import re
import sys
import os

import pykakasi


# ── Initialise pykakasi once ────────────────────────────────────────────────
_kks = pykakasi.kakasi()

# Regex: CJK Unified Ideographs (kanji)
RE_KANJI = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf]+')

# Regex: detect existing mkdocs-ruby-plugin annotation
# Matches: 漢字(かんじ)  or  {文章(ぶんしょう)}
RE_EXISTING = re.compile(
    r'\{[\u4e00-\u9fff\u3400-\u4dbf]+\([^)]+\)\}'   # {複数漢字(よみ)}
    r'|[\u4e00-\u9fff\u3400-\u4dbf]+\([^)]+\)'       # 単漢字(よみ)
)


def _furiganize(text: str) -> str:
    """Add furigana to bare kanji in *text*, skipping already-annotated runs."""

    def _replace(m: re.Match) -> str:
        kanji = m.group(0)

        # ── Guard: already annotated? ──────────────────────────────────────
        start, end = m.start(), m.end()
        # Check if this kanji is inside an existing {compound(reading)}
        if text[max(0, start - 1):end] in (
            # single-char annotation: 漢字(かんじ) — kanji is already before (
            # multi-char: {漢字(かんじ)} — kanji is inside braces
        ):
            pass  # fall through to pykakasi
        # Quick lookahead for (reading) or )} right after
        rest = text[end:end + 40]
        if rest.startswith('(') and ')' in rest[:15]:
            # Likely already annotated — return unchanged
            return kanji
        if kanji.startswith('{') and '}' in rest[:40]:
            return kanji

        # ── Generate reading via pykakasi ───────────────────────────────────
        try:
            items = _kks.convert(kanji)
            reading = ''.join(it['hira'] for it in items)
        except Exception:
            return kanji  # fallback: return bare kanji

        if not reading or reading == kanji:
            return kanji

        if len(kanji) > 1:
            return f'{{{kanji}({reading})}}'
        return f'{kanji}({reading})'

    return RE_KANJI.sub(_replace, text)


# ── Line-based markdown parser ──────────────────────────────────────────────
def process_file(path: str) -> bool:
    """Read, furiganize, and write back *path*. Return True if changed."""
    with open(path, encoding='utf-8') as f:
        raw = f.read()

    lines = raw.splitlines(keepends=True)
    out = []
    changed = False

    in_frontmatter = False
    in_code_block = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # ── Track frontmatter ────────────────────────────────────────────────
        if i == 0 and stripped == '---':
            in_frontmatter = True
            out.append(line)
            continue
        if in_frontmatter and stripped == '---':
            in_frontmatter = False
            out.append(line)
            continue
        if in_frontmatter:
            out.append(line)
            continue

        # ── Track fenced code blocks ────────────────────────────────────────
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            out.append(line)
            continue
        if in_code_block:
            out.append(line)
            continue

        # ── Skip headings & horizontal rules ────────────────────────────────
        if stripped.startswith('#'):
            out.append(line)
            continue
        if stripped == '---' or stripped == '___':
            out.append(line)
            continue

        # ── Skip table rows ─────────────────────────────────────────────────
        if '|' in line and ('---' in stripped or '|' == stripped[0]):
            out.append(line)
            continue

        # ── Process: inline-code & markdown-link-aware line furiganization ──
        # Tokenize by backticks (inline code) and markdown links [text](url)
        # so we don't annotate code or URLs
        pattern = r'(`[^`]*`|\[[^]]+\]\([^)]+\))'
        tokens = re.split(pattern, line, flags=re.DOTALL)
        processed = []
        for tok in tokens:
            if tok.startswith('`') or tok.startswith('['):
                processed.append(tok)  # keep code & links untouched
            else:
                new = _furiganize(tok)
                processed.append(new)
                if new != tok:
                    changed = True

        out.append(''.join(processed))

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(out)
    return changed


# ── CLI ─────────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/add-furigana.py <directory>")
        sys.exit(1)

    root = sys.argv[1]
    md_files = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.endswith('.md'):
                md_files.append(os.path.join(dirpath, fn))

    total = changed_count = 0
    for fp in sorted(md_files):
        # Skip files that shouldn't be annotated (index, landing pages)
        rel = os.path.relpath(fp, root)
        if os.path.basename(fp) in ('index.md', 'PROJECT_GOAL.md'):
            print(f"  SKIP  {rel}")
            continue
        total += 1
        ok = process_file(fp)
        if ok:
            changed_count += 1
            print(f"  ✓     {rel}")
        else:
            print(f"  —     {rel}")

    print(f"\n{changed_count}/{total} files annotated.")


if __name__ == '__main__':
    main()
