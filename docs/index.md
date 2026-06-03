# The Roots of Japanese

> Learn Japanese vocabulary the way English speakers learn from Latin roots: by the building blocks, not one word at a time.

---

## The idea

In English, one Latin or Greek root unlocks a whole family of words:

| Root | Meaning | Words it unlocks |
|------|---------|------------------|
| **struct** | build | construct, structure, instruct, infrastructure, obstruction |
| **port** | carry | import, export, transport, support, portable |

Japanese works the same way. A single kanji is a root that combines with other kanji to generate families of compound words. Learn the root, and you can read (and eventually guess) compounds you have never seen before.

| Kanji root | Like | Unlocks |
|------------|------|---------|
| **不** (not) | un-, in-, dis- | 不安, 不便, 不可能, 不満, 不正 |
| **者** (person) | -er, -ist | 医者, 科学者, 記者, 読者, 労働者 |
| **生** (life) | bio-, -genesis | 生活, 生産, 生命, 学生, 先生 |

## Why this exists

The usual way to study is one kanji, then one compound, then another, like memorizing *construct*, *instruct*, and *structure* without ever noticing they share *struct*. Every word becomes a separate task.

This project reverse-engineers the system instead. It finds the **most productive kanji** (the ones that appear in the most compound words) and maps how they behave: which position they prefer, how many words they unlock, and which English root they mirror.

## The two systems

1. **Kanji roots** (nouns and concepts) - one kanji plus many partners makes many compound words. Like Latin and Greek roots.
2. **Verb roots** (actions and aspects) - one verb core plus many "particle" verbs makes many nuanced actions. Like English phrasal verbs (give up / give in / give out).

## Start here

1. **[Kanji Roots: Catalog](kanji-roots-catalog.md)** - browsable families of the most productive kanji, each mapped to its English-root analogy.
2. **[Kanji Roots: The Data](kanji-roots-data.md)** - the numbers behind the catalog: productivity counts and left/right position analysis from a 27,950-compound database.
3. **[Kanji Roots: Sound Roots](sound-roots.md)** - the phonetic part inside each character: learn one sound, predict many readings.
4. **[Verb Roots](verb-roots.md)** - how Japanese verbs combine, from the polymorphic 〜込む to bases like 取り〜.

New to the idea? Read in order. Want a reference? Jump straight to the Catalog.

## Sources

All productivity numbers on this site come from one dataset, for consistency:

- **Tamaoka et al. (2017)** - [kanjidatabase.com](https://www.kanjidatabase.com) (2,136 Jōyō kanji, 27,950 two-kanji compounds from an 11-year newspaper corpus). The source of every number here.
- **Tamaoka & Altmann (2004)** - the foundational study on kanji productivity, cited for historical context.
- **NINJAL Compound Verb Lexicon** - [vvlexicon.ninjal.ac.jp](https://vvlexicon.ninjal.ac.jp/en/) (2,700+ compound verbs).
- **NINJAL Basic Verb Handbook** - [www2.ninjal.ac.jp/verbhandbook](https://www2.ninjal.ac.jp/verbhandbook/) (190 polysemous verbs).
