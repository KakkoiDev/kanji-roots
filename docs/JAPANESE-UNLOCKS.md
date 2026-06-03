# Japanese Structural Unlocks

The high-leverage models that make Japanese *cohere* - so sentences parse the way a native intuits them,
instead of as decoded English. Adopt-existing-tools edition. Each unlock has native examples and the
resource that teaches it best.

> **Note:** This file covers **grammar and syntax**. For kanji root families and compound analysis, see the main [Roots of Japanese](https://github.com/KakkoiDev/kanji-roots) project: [Kanji Roots](Japanese_Kanji_Productive_Roots.md) | [Verb Compounds](Japanese_MultiFunctional_Verbs.md)

> Read the three caveats first. They decide whether any of this sticks.

---

## Before the list - three things that decide if this works

1. **Two different "click" layers. Don't expect one tool for both.**
   - *Kanji-root click* (your original `作る/造る`, `様` question) = vocabulary + reading leverage. Lives in
     the written character: meaning-roots, phonetic series 形声, 異字同訓 (one word, many kanji = nuance).
     Covered in the last section.
   - *Grammar/structure click* (what you actually want) = syntax + semantics. は/が, head-final order,
     transitivity, て-form. That is the bulk of this doc.
   - The bridge between them is unlock **#5** (on/kun = the Latinate layer).

2. **"Click like a native" has a ceiling.** Natives don't see structure consciously - they run on
   intuition compiled from years of input. The clean models below (が-core, topic-comment) are
   *pedagogical scaffolding*, not how a native brain represents it. Cure Dolly's "every sentence has an
   invisible が" is a useful model that some linguists dispute. Use it as training wheels, then let real
   exposure overwrite it.

3. **Insight decays without exposure.** This is Alec's own embryology story: understood it cold, forgot it
   in two weeks. A satisfying click is necessary, not sufficient. Each unlock must be *re-met in real
   input* or it evaporates. That is why the routine at the bottom matters more than this list.

Don't binge all ten at once. They only click when you have enough input to attach them to. Tier 1 first.

---

## Tier 1 - the syntactic spine (front-loaded, pays off forever)

### 1. The が-core: every sentence is `A が B` (carriage + engine)
が marks the doer/be-er; the whole sentence is built around it, even when が is dropped or hidden under は.
`B` (the verb/adjective/copula) is the engine; `A が` is what it acts on or through.
- `雨が降る` - *rain falls.* (が = 雨 is the faller; 降る is the engine)
- `(私が) 寿司を食べる` - *(I) eat sushi.* The が-doer is there even when omitted.

Once you stop hunting for an English-style "subject" and instead find the が-core, the so-called
"subjectless sentence" stops being mysterious.
-> Cure Dolly [Lesson 1](https://www.youtube.com/watch?v=pSvH9vH60Ig) and
[Lesson 2](https://www.youtube.com/watch?v=P3n8n0u3LHA); book *Unlocking Japanese*
([Goodreads](https://www.goodreads.com/book/show/32614930)); text mirror
[cure-script](https://kellenok.github.io/cure-script/1-the-basic-types-of-sentences.html).

### 2. は = topic ("as for X"), NOT subject. は vs が.
は floats *above* the が-core and sets the frame; it is not a subject marker.
- `象は鼻が長い` - *As for elephants, the nose is long.* (は = topic 象; が = subject 鼻 of 長い)
- うなぎ文: at a restaurant, `僕はうなぎだ` = *"I'll have the eel"*, literally "as-for-me, it's eel." Proof
  that は ≠ "I = eel."
- Minimal pair: `私が行きます` = "*I* (and not the others) will go" (が identifies/selects);
  `私は行きます` = "as for me, I'll go" (は = neutral topic).
-> Jay Rubin, *Making Sense of Japanese* (20 pages on は/が, "the myth of the subjectless sentence")
([Amazon](https://www.amazon.com/Making-Sense-Japanese-What-Textbooks/dp/156836492X)); Tae Kim
[Complete Guide](https://guidetojapanese.org/learn/).

### 3. Head-final / left-branching: the core comes LAST, everything before it modifies it
Verb last. Relative clauses precede the noun with **no relative pronoun**. Particles are *post*positions.
- `私が買った本` - *the book that I bought.* (the clause `私が買った` sits in front of `本`, no "that")
- `私は寿司を食べる` - literally *I / sushi / eat.*

Train yourself to hold the front material as "modifiers" and wait for the head. That waiting *is* the
native parse.
-> [IMABI](https://imabi.org/) (see [Table of Contents](https://imabi.org/table-of-contents-%E7%9B%AE%E6%AC%A1/));
Tae Kim [Grammar Guide](https://guidetojapanese.org/learn/grammar).

### 4. Particles tag the role -> phrase order is flexible
を/が/に/で/へ/と mark grammatical role, so order before the verb is free without changing meaning.
- `私は寿司を食べる` ≈ `寿司を私は食べる` - same meaning; を keeps 寿司 the object either way.

This is *why* head-final works: roles are glued on by particles, not by position. Contrast English's rigid
subject-verb-object order.
-> Tae Kim [Complete Guide](https://guidetojapanese.org/learn/); IMABI.

---

## Tier 2 - regular patterns that unlock hundreds of items

### 5. on-yomi vs kun-yomi = the Latinate layer (bridge to your kanji question)
on-yomi (borrowed Chinese readings) ≈ the Latin/Greek register in English (formal, compounds).
kun-yomi (native readings) ≈ Anglo-Saxon everyday words.
- `火` *ひ (hi)* = "fire" (native, everyday) vs `火災` *かさい (kasai)* = "conflagration" (Sino, formal).
  Exactly English fire vs conflagration.
- `水` *みず (mizu)* "water" vs `水族館` *すいぞくかん* "aquarium" (sui-). water vs aquatic.

Rule of thumb: standalone word + okurigana -> usually kun; multi-kanji compound -> usually on. This single
insight explains *why* kanji have two reading systems and roughly when each fires.
-> [Tofugu](https://www.tofugu.com/japanese/kanji-radicals-mnemonic-method/); Outlier Linguistics.

### 6. Transitivity pairs (自動詞 / 他動詞): self-moves vs someone-moves-it
Semi-regular morphology links the pair, so learning one teaches its partner.
- `ドアが開く` (*あく*, intransitive: the door opens) vs `ドアを開ける` (*あける*, transitive: open the door).
- `始まる / 始める`, `出る / 出す`, `入る / 入れる`, `落ちる / 落とす`.
- Hints: `-aru` tends intransitive; `-eru` / `-su` tend transitive. ~300 common pairs share this skeleton.
-> Tofugu [Transitivity](https://www.tofugu.com/japanese-grammar/transitivity/); Cure Dolly.

### 7. て-form = the universal connector + aspect engine
Master one form, open a whole productive system:
- `食べている` (ongoing / resulting state), `置いておく` (do in advance), `食べてしまう` (complete / regret),
  `持ってくる` (bring = come holding) / `持っていく` (take), `〜てください` (request), and clause-chaining.
-> Tae Kim [Complete Guide](https://guidetojapanese.org/learn/); Cure Dolly.

### 8. Aspect over tense: `-る` (nonpast) vs `-た` (past). No future.
Japanese cares more about complete vs incomplete than past/present/future.
- `食べる` = "eat / will eat" (`明日食べる` = will eat tomorrow - same form). `食べた` = past/complete.
- `ている` adds aspect (ongoing or resultant state), which is a *different axis* from tense.
-> Rubin, *Making Sense of Japanese*; IMABI.

---

## Tier 3 - the social/perspective clicks natives feel, learners miss

### 9. うち / そと (in-group vs out-group) + viewpoint drives giving verbs, keigo, direction
- `あげる` = I give *outward* (toward the out-group). `くれる` = someone gives *toward me / my side*.
  `もらう` = I receive.
- Same event, viewpoint differs: `友達に本をあげた` (I gave my friend a book) vs `友達が本をくれた`
  (my friend gave me a book - `くれる` only because the benefit comes toward my side).
-> Cure Dolly (giving/receiving series); Makino & Tsutsui, *Dictionary of Basic Japanese Grammar* (DBJG).

### 10. Viewpoint stays anchored: なる-orientation, the suffering passive, 〜てくれる
Japanese prefers describing situations as naturally-occurring over agent-forced.
- `日本語が上手になりましたね` - "your Japanese *has become* good" (preferred over "you made it good").
- 迷惑の受身 (suffering passive): `雨に降られた` = "I got rained on" - passive marks being adversely affected.
- `〜てくれる` frames another's action as a benefit *received by* the speaker's side.
-> Rubin, *Making Sense of Japanese*; Makino & Tsutsui, DIJG / DAJG (intermediate / advanced).

---

## Resource spine (beginner -> advanced)

| Resource | Best for | Link |
|----------|----------|------|
| Cure Dolly - *Organic Japanese* (YouTube) + *Unlocking Japanese* | structure-first click engine, が-core | [channel start](https://www.youtube.com/watch?v=pSvH9vH60Ig) / [book](https://www.goodreads.com/book/show/32614930) |
| Jay Rubin - *Making Sense of Japanese* | は/が, subjectless myth, "Japanese isn't vague" | [book](https://www.amazon.com/Making-Sense-Japanese-What-Textbooks/dp/156836492X) |
| Tae Kim - *Guide to Japanese Grammar* (free) | grammar from the Japanese POV, Tier 1 entry | [site](https://guidetojapanese.org/learn/) |
| IMABI (free) | exhaustive structural reference, all levels | [site](https://imabi.org/) |
| Makino & Tsutsui - DBJG / DIJG / DAJG | nuance bible; advanced end of your range | (print) |
| Tofugu | per-unlock deep dives (transitivity, on/kun) | [transitivity](https://www.tofugu.com/japanese-grammar/transitivity/) |

**Kanji layer (your original question):**
[Outlier Linguistics Kanji Dictionary](https://www.outlier-linguistics.com/),
[*The Kanji Code* phonetic components](https://thekanjicode.com/2018/12/16/japanese-phonetic-components/),
文化庁 [「異字同訓」の漢字の使い分け例 (2014)](https://www.bunka.go.jp/seisaku/bunkashingikai/kokugo/hokoku/pdf/ijidokun_140221.pdf),
and the [Keisei 形声 WaniKani userscript](https://community.wanikani.com/t/userscript-keisei-%E5%BD%A2%E5%A3%B0-semantic-phonetic-composition/21479) if you use WaniKani.

---

## The cement (Alec's lesson, applied)

A click you never re-meet is a click you lose. Pair every unlock with real input:
- **Input habit:** [Tadoku free graded readers](https://tadoku.org/japanese/en/free-books-en/) ->
  [NHK News Easy](https://www3.nhk.or.jp/news/easy/) -> native content. Meet each unlock in the wild until
  it stops needing conscious decoding.
- **If you use SRS:** card the **structure / whole sentence**, not isolated vocab. This is Alec's
  "principle, not fact" point applied to grammar - sentence cards beat word cards for *this* goal.

---

## 4-week front-loaded sequence (~20-30 min/day: half explainer, half input)

| Week | Unlocks | Study | Daily input |
|------|---------|-------|-------------|
| 1 | #1-2 が-core, は/が | Cure Dolly L1-3; Tae Kim particles + は/が | 10 min Tadoku L0 |
| 2 | #3-4 head-final, particle roles | Tae Kim modifiers/relative clauses; IMABI | parse 3 relative-clause sentences/day |
| 3 | #5-8 on/kun, transitivity, て-form, aspect | Tofugu transitivity + on/kun; Cure Dolly て-form | collect 10 transitivity pairs from reading |
| 4 | #9-10 giving/receiving, viewpoint | Cure Dolly giving/receiving; Rubin chapters | NHK Easy daily; spot くれる/もらう + 迷惑の受身 |

Input never stops after week 4. Re-run the checklist below at the end, then again two weeks later.

---

## Verification (how you know it clicked, not just "read it")

- Parse a head-final sentence with an embedded relative clause out loud - naming the が-core, the は-topic,
  and each particle's role - *without* reordering into English first.
- Explain は vs が in `象は鼻が長い`, and produce a minimal pair where swapping them changes the meaning.
- Given an unfamiliar verb, predict its transitive/intransitive partner from the morphology.
- Read 3 NHK Easy paragraphs and spot at least 2 Tier-1/2 unlocks operating in real text.
- Re-test on fresh sentences after 2 weeks (the Alec interval). Still works -> it stuck.
