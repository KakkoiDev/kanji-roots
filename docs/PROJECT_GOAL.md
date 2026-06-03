# Project Goal: The "Roots of Japanese" Lexicon

> *Mapping Japanese characters as a system of combinable roots — like Latin and Greek in English*

---

## The Core Idea

English has Latin/Greek roots that unlock entire word families:

| Root | Meaning | Unlocked Words |
|------|---------|----------------|
| **struct** | build | construct, destruct, instruct, structure, infrastructure, obstruction, reconstruction |
| **port** | carry | report, import, export, transport, support, portable, deport, portfolio |
| **ject** | throw | project, reject, inject, subject, object, interject, trajectory |
| **dict** | say | predict, dictate, dictionary, contradict, verdict, edict, dictation |
| **spect** | look | inspect, respect, spectator, prospect, perspective, retrospect, spectacle |

Learning one root gives you **5–20+ words** for free.

**Japanese works the same way.** A single kanji is a root that combines with other kanji to generate families of compound words. Once you know the root, you can guess — and eventually generate — compounds you've never seen before.

---

## The Problem This Project Solves

### The Traditional Approach
Learners study kanji **one by one**, then encounter compounds **one by one**. This is like learning:
- construct
- destruct
- instruct
- structure
- infrastructure
- obstruction

...without ever realizing they all share **"struct"**. Each word is a separate memorization task.

### The Root-Based Approach
This project aims to **reverse-engineer** the Japanese compound system by identifying the most productive kanji — the ones that appear in the most compound words — and mapping their behavior in terms of:

1. **Which position they prefer** (left = prefix-like, right = suffix-like, or both)
2. **How many compounds they participate in** (productivity count)
3. **Which semantic family they belong to** (e.g., negation, people, location, action)
4. **Which English root they correspond to** (the analogy bridge)

---

## The Two Systems We're Mapping

### System 1: Kanji Roots (Nouns & Concepts)

Like Latin/Greek roots in English. One kanji + many partners = many compound nouns.

| Japanese Root | English Analogy | Compounds |
|--------------|----------------|-----------|
| **大** (big) | macro-, mega- | 大学, 最大, 拡大, 巨大, 大使, 大事 |
| **不** (not) | un-, in-, dis- | 不安, 不便, 不可能, 不満, 不正 |
| **人** (person) | -an, -ian | 日本人, 外国人, 詩人, 商人, 証人 |
| **生** (life) | bio-, -genesis | 生活, 生産, 生命, 学生, 先生, 誕生 |
| **出** (exit) | ex-, out- | 出口, 出発, 出現, 出版, 輸出 |
| **制** (control) | system-, regul- | 制度, 制限, 制御, 体制, 規制 |

**Count**: 27,950+ compound words, ~2,136 roots, ~30 of which are highly productive

### System 2: Verb Roots (Actions & Aspects)

Like English phrasal verbs. One verb core + many "particle" verbs = many nuanced actions.

| Japanese Verb Root | English Analogy | Compounds |
|-------------------|----------------|-----------|
| **取り〜** (take) | "take" base | 取り上げる, 取り入れる, 取り消す, 取り組む, 取り戻す |
| **〜込む** (into) | "in/into" particle | 飛び込む, 考え込む, 飲み込む, 書き込む, 詰め込む |
| **〜出す** (out) | "out" particle | 泣き出す, 走り出す, 飛び出す, 思い出す |
| **〜始める** (start) | "start" auxiliary | 食べ始める, 歩き始める, 降り始める |
| **〜合う** (each other) | "each other" | 話し合う, 助け合う, 愛し合う |

**Count**: ~30 productive V2 patterns × hundreds of possible V1s

---

## The End Goal

A **reference lexicon** organized by root rather than alphabetically, where each entry contains:

```
## 大 (big / だい)
English root analogy: macro-, mega-, magni-
Productivity: 285 unique compounds (57 left, 228 right) — #1 most productive kanji
Preferred position: Strongly right (suffix-like)

Meaning clusters:
  → Size:    最大 (maximum), 巨大 (huge), 強大 (powerful), 壮大 (grand)
  → Scale:   拡大 (expansion), 大規模 (large-scale), 大企業 (large corporation)
  → Status:  大学 (university), 大使 (ambassador), 大統領 (president)
  → Degree:  重大 (serious), 絶大 (enormous), 大変 (terrible/hard)
```

This makes Japanese learnable as a **system of combinable building blocks** — not an endless list of isolated pairs.

---

## Current Status

| System | Status | Files |
|--------|--------|-------|
| **Verb Compounds (V2 patterns)** | ✅ Complete | [`Japanese_MultiFunctional_Verbs.md`](Japanese_MultiFunctional_Verbs.md) |
| **Verb Compounds (V1 bases)** | ✅ Complete | [`Japanese_MultiFunctional_Verbs.md`](Japanese_MultiFunctional_Verbs.md) |
| **Kanji Roots (overview)** | ✅ Complete | [`Japanese_Kanji_Productive_Roots.md`](Japanese_Kanji_Productive_Roots.md) |
| **Kanji Roots (deep dive with data)** | ✅ Complete | [`Kanji_Root_Families_Deep_Dive.md`](Kanji_Root_Families_Deep_Dive.md) |
| **Grammar Unlocks** | ✅ Complete | [`JAPANESE-UNLOCKS.md`](JAPANESE-UNLOCKS.md) |
| **Verb Compounds (日本語)** | ✅ Complete | [`日本語の多機能動詞.md`](日本語の多機能動詞.md) |
| **This project doc** | ✅ Complete | [`PROJECT_GOAL.md`](PROJECT_GOAL.md) — also see [`index.md`](index.md) |

---

## How to Use These Files

1. **Start here** — understand the project goal
2. **Read [`Japanese_Kanji_Productive_Roots.md`](Japanese_Kanji_Productive_Roots.md)** — the overview of the top 20-30 kanji roots organized by semantic family, with English root analogies
3. **Read [`Kanji_Root_Families_Deep_Dive.md`](Kanji_Root_Families_Deep_Dive.md)** — the data-driven deep dive with actual productivity numbers from the 27,950-compound database, left/right positioning analysis
4. **Read [`Japanese_MultiFunctional_Verbs.md`](Japanese_MultiFunctional_Verbs.md)** — the verb system: ~30 V2 patterns (like English particles) and ~20 V1 bases (like "give" or "take") with detailed example lists
5. **Read [`JAPANESE-UNLOCKS.md`](JAPANESE-UNLOCKS.md)** — grammar foundations: が-core, は/が, transitivity, aspect — the structural unlocks that complement root-based vocabulary learning
6. **Query the database yourself** at [kanjidatabase.com/sql.php](https://www.kanjidatabase.com/sql.php) using the sample SQL queries in the deep dive
