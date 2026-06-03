# Furigana in MkDocs — Tooling Report

## Q: Can MkDocs render furigana?

Yes. The standard web approach — `<ruby>` tags — works directly in MkDocs because it
passes through raw HTML in markdown. But that means hand-writing every ruby annotation,
which is impractical at scale.

Two dedicated MkDocs plugins exist that add a shorthand syntax:

| Plugin | Syntax | Status | pip |
|--------|--------|--------|-----|
| [mkdocs-ruby-plugin](https://github.com/LeslieZhu/mkdocs-ruby-plugin) | `漢字(かんじ)` or `{複数漢字(ふくすうかんじ)}` | PyPI 0.0.3, 2024 | ✅ Works |
| [mkdocs-furigana-plugin](https://github.com/ijaureguialzo/mkdocs-furigana-plugin) | `漢字【かんじ】` or `§今日【きょう】` | GitHub only, 2023 | Needs manual install |

Both convert inline syntax into `<ruby>漢字<rt>かんじ</rt></ruby>` during the MkDocs build.
**mkdocs-ruby-plugin** is the better choice — it's on PyPI, uses the standard HTML `<ruby>` tag,
and supports multi-kanji segments with `{...}`.

```yaml
# mkdocs.yml
plugins:
  - ruby:
      global_enable: true
      title_enable: true
      outer_begin: '{'
      outer_end: '}'
      inter_begin: '('
      inter_end: ')'
```

Then in markdown: `漢字(かんじ)` → produces `<ruby>漢字<rt>かんじ</rt></ruby>`.

---

## Q: How to generate the furigana automatically?

The plugin handles rendering, but you still need to write `漢字(かんじ)` next to every kanji
in your markdown. That's where a **third-party morphological analyzer** comes in.

These tools parse Japanese text and output each kanji's reading. They are deterministic NLP
tools — not LLMs — so readings are consistent, predictable, and based on dictionary data.

### Option A: pykakasi (Python, best for this project)

[pykakasi](https://github.com/miurahr/pykakasi) — 455 stars, actively maintained, pure Python.

```python
import pykakasi
kks = pykakasi.kakasi()
text = "かな漢字交じり文"
result = kks.convert(text)
for item in result:
    print(f"{item['orig']}[{item['hepburn']}] ", end='')
# かな[Kana] 漢字[Kanji] 交じり[Majiri] 文[Bun]
```

**Why it fits:**
- Pure Python — no C dependencies, no JVM, no native binaries
- Same ecosystem as MkDocs — can be a build step or custom MkDocs plugin
- Outputs per-character kana readings, which maps directly to `漢字(かんじ)` format
- On PyPI: `pip install pykakasi`

### Option B: SudachiPy (highest accuracy)

[SudachiPy](https://github.com/WorksApplications/SudachiPy) — used by the modern
[furigana-generator](https://github.com/igorkulman/furigana-generator) which also supports
JLPT-level filtering (only add furigana for N3+ kanji, skip N5).

```bash
pip install sudachipy sudachidict_core
```

```python
from sudachipy import tokenizer, dictionary
tokenizer_obj = dictionary.Dictionary().create()
tokens = tokenizer_obj.tokenize("寿司を食べに行く")
for t in tokens:
    print(f"{t.surface()}: {t.reading_form()}")
# 寿司: スシ, を: ヲ, 食べ: タベ, に: ニ, 行く: イク
```

Rust-backed, fast, produces katakana readings.

### Option C: MeCab (classic, needs native build)

[MikimotoH/furigana](https://github.com/MikimotoH/furigana) wraps MeCab to output HTML ruby
directly. Requires `libmecab-dev`. Most battle-tested but heaviest dependency.

---

## Implementation in this project

This project uses:

| Layer | Tool | File |
|-------|------|------|
| **Rendering** | `mkdocs-ruby-plugin` (patched) | `mkdocs.yml` → `plugins.ruby` |
| **Generation** | pykakasi pre-process script | `scripts/add-furigana.py` |
| **Plugin patch** | regex fix for CJK-only matching | `scripts/patch-ruby-plugin.py` |
| **Toggle button** | JS + CSS, client-side | `docs/assets/.../furigana-toggle.*` |

**Patching needed:** The `mkdocs-ruby-plugin` uses `(.)\((.+?)\)` for single-kanji matching,
which matches any character (including spaces) before `(...)`. This causes false positives on
English text like `click (your original...)`. The patch restricts to CJK kanji only:
`([\u4e00-\u9fff])\((.+?)\)` — applied in CI via `patch-ruby-plugin.py`.

**Limitations:**
- Readings are ambiguous — `生` can be せい/しょう/う/い/き/なま. Context-dependent.
- Isolated kanji in tables often get kun-yomi readings; in compounds they'd take on-yomi.
- The script skips markdown links, inline code, code blocks, and already-annotated text.
- Annotations are generated at build time and never committed to the repo.

---

## Source comparison

| Tool | Language | Dependency | Accuracy | Ease |
|------|----------|-----------|----------|------|
| pykakasi | Python | None (pure) | Good | ✅ Easy |
| SudachiPy | Python | Rust binary | Excellent | ✅ pip + dict |
| MeCab | Python/C | Native lib | Excellent | ⚠️ Needs `libmecab` |
| kuroshiro.js | JS | Node/npm | Good | ⚠️ Client-side only |
| mkdocs-ruby-plugin | Python | MkDocs | N/A (rendering) | ✅ pip install |
