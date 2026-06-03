# Project Critique: "The Roots of Japanese" Lexicon

> A thorough review of the project's content, structure, strengths, and issues as of 2026-06-03.

---

## Project Summary

**Goal:** Map Japanese characters as a system of combinable roots (analogous to Latin/Greek roots in English)
to make Japanese vocabulary learnable as building blocks, not isolated memorization.

**Files (5 core, 2,020 total lines):**

| File | Lines | Language | Role |
|------|-------|----------|------|
| `PROJECT_GOAL.md` | 120 | EN | Manifesto & overview |
| `Japanese_Kanji_Productive_Roots.md` | 547 | EN | Catalog of ~50 productive kanji by semantic family |
| `Kanji_Root_Families_Deep_Dive.md` | 399 | EN | Data-driven analysis from kanjidatabase.com |
| `Japanese_MultiFunctional_Verbs.md` | 385 | EN | Catalog of compound verb patterns (V1+V2) |
| `日本語の多機能動詞.md` | 386 | JA | Near-identical translation of the verb file |
| `JAPANESE-UNLOCKS.md` | 183 | EN | Grammar acquisition guide (orthogonal to roots) |

---

## Overall Assessment

**Rating: 6/10 — Strong concept, strong research instincts, undermined by critical data errors**

The core analogy (kanji : Latin/Greek roots) is genuinely insightful and pedagogically valuable. The project
surfaces real academic research (Tamaoka & Altmann) and connects it to practical learning. But the execution
has one fatal flaw: the left/right position analysis in the Deep Dive is likely **wholly inverted** for
several key kanji, which propagates confusion through the entire data layer.

---

## Strengths

### 1. Core Analogy Is Sound and Valuable
Framing kanji productivity through the Latin/Greek root lens is a powerful pedagogical bridge for English-speaking
learners. The metaphor is well-chosen: 不 = "un-", 者 = "-er", 的 = "-ic" — these mappings click instantly.

### 2. Academic Foundation
The project doesn't just rely on folklore. It cites:
- Tamaoka & Altmann (2004) — the foundational productivity study
- Tamaoka et al. (2017) — the kanjidatabase.com corpus (27,950 compounds, 2,136 Jōyō)
- NINJAL's Compound Verb Lexicon
- BCCWJ balanced corpus

This is the right research spine. The SQL queries included in the Deep Dive are a nice touch.

### 3. Good Organization Principles
- Semantic families (negation, people, location, systems, etc.) are the right grouping
- Position analysis (prefix-like vs suffix-like) is the right dimension to study
- Verb compounds split into V2 patterns and V1 bases is correct and clear
- NINJAL's VV/Vs/pV/V typology is properly explained

### 4. `JAPANESE-UNLOCKS.md` Is a Strong Standalone Resource
Taken on its own, this file is excellent — a concise, well-sourced synthesis of the most important
structural insights for Japanese learners (が-core, は/が distinction, head-final parsing, transitivity
pairs). It belongs in the *grammar* domain, not the *roots* domain, but it's well-made.

### 5. Bilingual Coverage
Including a Japanese version of the verb file shows awareness of different audiences (learners reading
Japanese, teachers, native speakers interested in the linguistic analysis).

### 6. Practical Orientation
Both the Roots Overview and UNLOCKS file include concrete learning strategies, not just theory.

---

## Critical Issues

### 🔴 FATAL: Left/Right Position Data Is Likely Inverted

This is the most serious problem. The Deep Dive file (`Kanji_Root_Families_Deep_Dive.md`) reports
kanjidatabase.com query results showing:

| Kanji | Reported Left | Reported Right | Reality |
|-------|-------------|----------------|---------|
| **不** | 0 | 161 | **Should be left-dominant** (不 + X compounds: 不安, 不便, 不可能...) |
| **者** | 87 | 1 | **Should be right-dominant** (X + 者: 医者, 科学者, 読者...) |
| **的** | 34 | 3 | **Should be right-dominant** (X + 的: 科学的, 経済的...) |
| **性** | 80 | 26 | **Should be right-dominant** (X + 性: 可能性, 安全性...) |
| **化** | 57 | 12 | **Should be right-dominant** (X + 化: 現代化, 自動化...) |

Every native speaker and every textbook knows that **不 is a prefix** (left-hand element) and **者/的/性/化
are suffixes** (right-hand elements). The database results showing the opposite patterns are almost certainly
a query error, a column swap, or a misinterpretation of the database schema.

#### The Confused Reasoning Cascade

The author notices the discrepancy but doesn't resolve it. Instead, the text tries to *rationalize*:

> "不 has zero left-hand compounds. It only appears in the second position... When you see 不 in a
> jukugo, 不 is always on the right — negating whatever comes before it: 不可能 = 可能 + 不 (not)...
> This is the opposite of how most textbooks explain it!"

No. Most textbooks are correct. 不 is the **first kanji** in 不可能. The characters are written 不→可→能.
The reasoning that "the database must be right, so let me reinterpret compounds to match" is a textbook
case of trusting the tool output over domain knowledge.

Similarly for 者:

> "Interesting: 者 (person suffix like -er) has only 1 right-hand compound... This is counterintuitive.
> 医者, 科学者... 者 is the second kanji."

The file flags the contradiction but ultimately reports the data as-is rather than debugging the query.
This is a research integrity problem — when data contradicts well-established knowledge, the data source
should be verified, not accepted uncritically.

#### Impact

This error propagates through:
- The "Practical Takeaways" section (recommendations based on wrong positions)
- The "Balanced vs Unbalanced" analysis
- Any learner who uses these files as a reference

### 🟡 Major: Internal Number Contradictions

| Data Point | Roots Overview | Deep Dive | Source |
|-----------|---------------|-----------|--------|
| 大 productivity | ~469 compounds | 285 total | Overview cites 2004 paper; Deep Dive cites 2017 DB |
| 不 productivity | ~350+ | 161 total | Same discrepancy |
| 人 productivity | ~260+ | 269 total | Slight mismatch |
| 生 productivity | ~250+ | 164 total | Large gap |

Both numbers are presented without reconciling the difference. The 2004 Tamaoka & Altmann study used a
smaller kanji set (1,945) but a different counting methodology. The 2017 database uses 2,136 Jōyō kanji
from newspaper data. The project should explain this rather than leaving the reader with contradictory
numbers.

### 🟡 Major: `JAPANESE-UNLOCKS.md` Is Orthogonal to the Project

This file is a **grammar acquisition guide**. It covers が-core, は/が, head-final parsing, transitivity,
て-form, aspect, giving/receiving verbs, and keigo. None of this is about kanji roots or compound analysis.
It belongs in a separate project (e.g., "Japanese Grammar Unlocks").

Its presence here muddies the project's identity. Is this a reference lexicon about kanji roots, or a
general Japanese learning resource? The scope is unclear.

### 🟡 Major: No Cross-References Between Files

- `PROJECT_GOAL.md` mentions the other files by name but has no markdown links
- No file links to `JAPANESE-UNLOCKS.md` at all
- The verb file and the kanji roots file never reference each other, despite covering related phenomena
  (e.g., 取る appears in both the verb compound analysis and the kanji compound analysis)

### 🟡 Major: `日本語の多機能動詞.md` Is Near-Duplicate Content

This file is a ~95% translation of `Japanese_MultiFunctional_Verbs.md`. It adds almost no new content.
Either:
- Delete it and note that the English version is the canonical one
- Or make it meaningfully different (target audience-specific adaptations, different examples, etc.)

As-is, it's maintenance burden: any edit to the English file must be mirrored in the Japanese file.

---

## Structural & Organizational Issues

### 1. No Entry Point or Index
The project has no `README.md`. `PROJECT_GOAL.md` partially fills this role but isn't named as a README.
A newcomer would have no idea which file to read first without opening `PROJECT_GOAL.md`.

### 2. Inconsistent File Naming
- `Japanese_Kanji_Productive_Roots.md` (Title Case)
- `Japanese_MultiFunctional_Verbs.md` (CamelCase: "MultiFunctional")
- `Kanji_Root_Families_Deep_Dive.md` (Snake_Case)
- `JAPANESE-UNLOCKS.md` (SCREAMING-KEBAB)
- `PROJECT_GOAL.md` (SCREAMING_SNAKE)
- `日本語の多機能動詞.md` (Japanese characters)

No naming convention. This is messy and hard to navigate.

### 3. The "How to Use These Files" Section Is Wrong

`PROJECT_GOAL.md` Section "How to Use These Files" says:

> 2. Read `Japanese_Kanji_Productive_Roots.md`
> 3. Read `Kanji_Root_Families_Deep_Dive.md`
> 4. Read `Japanese_MultiFunctional_Verbs.md`

But it doesn't mention `JAPANESE-UNLOCKS.md` or `日本語の多機能動詞.md` at all. The file inventory in the
"Current Status" table also omits `JAPANESE-UNLOCKS.md`. These are stale references.

### 4. Scope Creep: Three Projects in One

The files represent three distinct projects crammed into one directory:
1. **Kanji root/composition system** (PROJECT_GOAL, Roots Overview, Deep Dive)
2. **Compound verb system** (Verb file EN + JA)
3. **Grammar acquisition guide** (UNLOCKS file)

These could be three well-defined, interlinked projects. Jumbled together, they're less than the sum of
their parts.

---

## Content Gaps

### 1. Phonetic Components (形声) — The Missing "Root" Layer

The most glaring omission: the project never discusses **phonetic-semantic composition within individual
kanji**. This is arguably *more* fundamental than compound analysis:

- ~80% of Jōyō kanji are 形声 (phono-semantic compounds): one component hints at meaning, one at reading
- This *is* the "Latin/Greek root" parallel *within* the character system itself
- Examples: 青 (セイ) → 清・晴・静・精 all share the セイ reading
- `JAPANESE-UNLOCKS.md` mentions Outlier Linguistics and The Kanji Code but the main project files ignore this entirely

For a project named "The Roots of Japanese," skipping phonetic components is like writing about English
roots without mentioning "struct," "port," or "ject."

### 2. No Treatment of Okurigana

The relationship between kanji and trailing kana is essential for distinguishing on/kun readings in
compounds. When is a compound read on-on, kun-kun, or mixed? This is the practical question learners
actually face and the project never addresses it.

### 3. No Rendaku (連濁) Coverage

Sequential voicing (e.g., かみ + かみ → かみがみ in 神々) is a systematic phenomenon in jukugo that learners
need to understand. The project discusses compounds extensively without mentioning this key phonological
rule.

### 4. Missing Kanji-Kanji Distinction: Morpheme vs Word

The project treats kanji as "words" in compounds, but in modern Japanese, many kanji are bound morphemes
that cannot stand alone. This distinction matters for pedagogical sequencing — learners shouldn't try
to use 不 or 性 as standalone words.

### 5. No Code, No Automation

The Deep Dive includes SQL queries but there's no script that:
- Automatically queries the database
- Generates compound lists for a given kanji
- Validates the data
- Produces formatted output

For a "data-driven" project, the absence of any executable component is a missed opportunity.

### 6. No Frequency or Practicality Filtering

The project ranks kanji by raw productivity (compound count) but never cross-references with:
- Actual usage frequency (BCCWJ data is mentioned but not used)
- JLPT level practicality
- Which compounds learners actually encounter at each stage

A kanji with 150 compounds is impressive, but if 140 of them are rare newspaper terms, it's less useful for
learners than a kanji with 80 common compounds.

---

## Minor Issues

| # | Issue | Location |
|---|-------|----------|
| 1 | 者 appears twice in the Top 20 table (#3 and #12) with different counts | Roots Overview, Section 3 |
| 2 | "的性化" appears twice in the section 6.6 header (copy-paste error) | Roots Overview, TOC |
| 3 | 的 is listed under "Abstract Relations" twice with different meanings | Roots Overview, Section 6.6 |
| 4 | `JAPANESE-UNLOCKS.md` has file extension `.md` but is missing from the "Current Status" table | PROJECT_GOAL.md |
| 5 | "Practical Application" section mentions no tool to query kanjidatabase from the project itself | Roots Overview |
| 6 | The verb file says "~30 V2 patterns" but catalogues ~22; count is inconsistent | Verb file, Conclusion |
| 7 | `Kanji_Root_Families_Deep_Dive.md` TOC lists 道 with "?" for right count — placeholder never resolved | Deep Dive, Section 3 |

---

## Recommendations

### Immediate (Critical)

1. **Re-query kanjidatabase.com** with fresh, verified SQL. Double-check column definitions.
   The left/right assignments for 不, 者, 的, 性, 化 are almost certainly wrong. Fix before publishing.

2. **Reconcile the two data sources** (2004 paper vs 2017 database). Either pick one as canonical
   and explain the choice, or present both with caveats.

### Structural

3. **Split into separate projects** or at minimum separate directories:
   - `kanji-roots/` → PROJECT_GOAL, Roots Overview, Deep Dive
   - `verb-compounds/` → Verb file EN, Verb file JA
   - `grammar-unlocks/` → JAPANESE-UNLOCKS.md (or archive this as a separate project)

4. **Add a `README.md`** that serves as a proper index with links to all files.

5. **Standardize file naming** (suggestion: `kanji-productivity.md`, `kanji-deep-dive.md`,
   `verb-compounds.md`, `verb-compounds-ja.md`, `grammar-unlocks.md`).

### Content

6. **Add phonetic component (形声) coverage.** This is the missing piece that would make "Roots of
   Japanese" truly live up to its name.

7. **Add cross-references** between the kanji roots files and the verb compounds file — they overlap
   (e.g., 取る, 見る appear in both systems).

8. **Add a frequency/practicality layer** — tag each kanji with JLPT level and which compounds are
   most useful at each stage.

9. **Write a validation script** that queries the database and spot-checks the numbers in the files.

10. **Either differentiate the Japanese verb file or delete it.** If kept, make it target a different
    audience (e.g., Japanese teachers, native linguists) with adapted content.

11. **Add rendaku rules** and okurigana conventions to the compound analysis.

12. **Reconcile all TOC entries** — remove duplicates, fill in placeholder `?` values.

---

## Verdict

**The idea is excellent. The research effort is real. The writing is clear.** But the project is
currently undermined by a data-level error (inverted left/right positions for suffix kanji) that
renders much of the quantitative Deep Dive analysis unreliable. This needs to be fixed before the
project can serve as a trustworthy reference.

Once the data is corrected, the three sub-projects (kanji roots, verb compounds, grammar unlocks)
should be properly separated and cross-linked. With those fixes plus phonetic component coverage,
this could become a genuinely valuable open resource for Japanese learners.

In its current state, it's a promising draft with a critical bug.
