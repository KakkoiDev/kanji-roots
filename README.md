# The Roots of Japanese

> Learn Japanese vocabulary by its building blocks, the way English speakers learn from Latin roots.

**Read it online: [KakkoiDev.github.io/kanji-roots](https://KakkoiDev.github.io/kanji-roots)**

A reference site that maps the most productive Japanese kanji and compound verbs as reusable "roots," each tied to its English-root analogy. Built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme.

## Contents

| Page | What it covers |
|------|----------------|
| Home | The idea, the two systems, where to start |
| Kanji Roots: Catalog | Productive kanji grouped by meaning, with English-root analogies |
| Kanji Roots: The Data | Productivity counts and left/right position analysis (2017 Kanji Database) |
| Verb Roots | The compound-verb system: V2 patterns and V1 bases |

All productivity numbers come from a single source (the 2017 Kanji Database) so figures stay consistent across the site.

## Build locally

```sh
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # quick preview (no furigana)
```

Furigana is generated at build time, not committed, so the source markdown stays clean. To preview with furigana exactly as CI builds it:

```sh
python scripts/patch-ruby-plugin.py    # restrict furigana matching to CJK
python scripts/add-furigana.py docs/   # edits docs/ in place - run `git checkout docs/` afterwards
mkdocs build
```

The `archive/` directory holds earlier material (a grammar guide and a Japanese-language verb file) kept out of the published site.

## License

Documentation (`docs/`) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); code is under MIT. See [LICENSE](LICENSE).
