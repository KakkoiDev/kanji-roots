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
      global_enable: true        # enable on all pages
      title_enable: true         # also annotate <title>
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
from sudachipy import tokenizer
from sudachipy import dictionary

tokenizer_obj = dictionary.Dictionary().create()
tokens = tokenizer_obj.tokenize("寿司を食べに行く")
for t in tokens:
    print(f"{t.surface()}: {t.reading_form()}")
# 寿司: スシ, を: ヲ, 食べ: タベ, に: ニ, 行く: イク
```

Rust-backed, fast, produces katakana readings (→ easy to convert to hiragana).

### Option C: MeCab (classic, needs native build)

[MikimotoH/furigana](https://github.com/MikimotoH/furigana) wraps MeCab to output HTML ruby
directly. Requires `libmecab-dev`. Most battle-tested but heaviest dependency.

---

## Architecture: How to wire it together

There are three integration strategies, ordered from simplest to most thorough:

### 1. Pre-process script (recommended to start)

A standalone Python script that:
1. Reads each `.md` file in `docs/`
2. Runs pykakasi or SudachiPy on it
3. Wraps kanji in `漢字(かんじ)` syntax
4. Saves back to `.md`

Run before `mkdocs build`. Can be a Makefile step or a pre-build hook in
`.github/workflows/deploy.yml`.

```yaml
# .github/workflows/deploy.yml (one extra step)
- run: pip install pykakasi
- run: python scripts/add-furigana.py docs/
- run: mkdocs build --strict
```

**Trade-off:** Modifies source files. But simple and transparent.

### 2. Custom MkDocs plugin (cleanest)

A small MkDocs plugin (one Python file) that:
- Hooks into `on_page_markdown` event
- Passes page content through pykakasi
- Outputs `漢字(かんじ)`-marked markdown

```python
# mkdocs_furigana/mkdocs_furigana_auto.py
from mkdocs.plugins import BasePlugin
import pykakasi

class FuriganaAutoPlugin(BasePlugin):
    def __init__(self):
        self.kks = pykakasi.kakasi()

    def on_page_markdown(self, markdown, page, config, files):
        # Parse markdown, wrap kanji with (reading)
        # Return modified markdown
        pass
```

Registered in `setup.py` and added to `mkdocs.yml` just like any plugin.

**Trade-off:** More code to write, but doesn't touch source files. Runs on every build.

### 3. CSS-only client-side (zero build change)

Skip markdown-level furigana entirely. Use a JavaScript library like
[kuroshiro.js](https://github.com/Dcard/kuroshiro.js) with a client-side analyzer to
annotate kanji in the browser after the page loads.

Add to `docs/extra.js`:

```javascript
// Uses kuroshiro + kuromoji to add <ruby> to all <p> kanji on page load
```

Referenced in `mkdocs.yml` as `extra_javascript`.

**Trade-off:** Adds JS dependency, works offline, no server-side build changes. But furigana
won't appear in search engine snippets, and there's a flash of un-annotated text.

---

## Recommendation for this project

| Phase | What to use | Why |
|-------|-------------|-----|
| **Rendering** | `mkdocs-ruby-plugin` (`pip install mkdocs-ruby-plugin`) | On PyPI, standard `<ruby>` output, supports multi-kanji segments |
| **Generation** | pykakasi pre-process script | Pure Python, same stack as MkDocs, no native deps |
| **Integration** | Custom MkDocs plugin (Phase 2) | Cleaner, doesn't touch source files |

**Immediate minimal setup (20 minutes):**

```bash
pip install mkdocs-ruby-plugin pykakasi
```

1. Add `mkdocs-ruby-plugin` config to `mkdocs.yml`
2. Write a 40-line Python script that reads markdown, passes through pykakasi,
   wraps kanji in `漢字(かんじ)` format, and writes back
3. Run it before `mkdocs build`

### Limitations to know

1. **Readings are ambiguous** — 生(なま) can be せい, しょう, う, い, き, なま. Morphological
   analyzers disambiguate from context but get it wrong sometimes (especially names).
2. **No pitch accent** — These tools give readings, not pitch patterns. Separate tool needed.
3. **Build-time cost** — Running a full NLP pipeline on every build adds ~seconds per page.

---

## Source comparison

| Tool | Language | Dependency | Accuracy | Ease |
|------|----------|-----------|----------|------|
| pykakasi | Python | None (pure) | Good | ✅ Easy |
| SudachiPy | Python | Rust binary | Excellent | ✅ pip + dict |
| MeCab | Python/C | Native lib | Excellent | ⚠️ Needs `libmecab` |
| kuroshiro.js | JS | Node/npm | Good | ⚠️ Client-side only |
| mkdocs-ruby-plugin | Python | MkDocs | N/A (rendering) | ✅ pip install |

For this project (Python stack, simple setup), **pykakasi** is the best balance.
