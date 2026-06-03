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


def _is_hiragana(ch: str) -> bool:
    return bool(ch) and '\u3040' <= ch <= '\u309f'


# Forced readings for single kanji shown as roots. pykakasi reads an isolated
# kanji with a context-free reading that is often wrong for this project's
# "kanji as compound root" framing (e.g. \u751f alone -> \u306a\u307e "raw" not \u305b\u3044 "life").
OVERRIDES = {
    '\u751f': '\u305b\u3044',
    '\u884c': '\u3053\u3046',
    '\u5206': '\u3076\u3093',
    '\u8005': '\u3057\u3083',
    '\u4eba': '\u3072\u3068',
}


def _furiganize(text: str) -> str:
    """Add furigana to bare kanji in *text*, skipping already-annotated runs."""

    def _replace(m: re.Match) -> str:
        kanji = m.group(0)

        # ── Guard: already annotated? check if followed by (reading) ──────
        rest = text[m.end():m.end() + 15]
        if rest.startswith('(') and ')' in rest[:15]:
            return kanji

        # single kanji: the reading is context-dependent, so handle with care
        if len(kanji) == 1:
            nxt = text[m.end():m.end() + 1]
            # followed by okurigana (生きる, 行く): the kun reading varies,
            # so leave it bare rather than guess a wrong reading
            if _is_hiragana(nxt):
                return kanji
            if kanji in OVERRIDES:
                return f'{kanji}({OVERRIDES[kanji]})'

        # generate reading via pykakasi
        try:
            items = _kks.convert(kanji)
            reading = ''.join(it['hira'] for it in items)
        except Exception:
            return kanji

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

        # ── Skip table header separators & horizontal rules ─────────────────
        if stripped == '---' or stripped == '___' or re.match(r'^\|[\s\-:]+\|', stripped):
            out.append(line)
            continue

        # Skip headings: keep them clean and avoid shifting auto-generated anchors
        if stripped.startswith('#'):
            out.append(line)
            continue

        # ── Process: inline-code & markdown-link-aware line furiganization ──
        # Tokenize by backticks (inline code) and markdown links [text](url)
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
        rel = os.path.relpath(fp, root)
        # Skip landing/index pages
        if os.path.basename(fp) in ('index.md', 'sound-roots.md'):
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
