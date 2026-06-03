# Static Site for "Roots of Japanese" — Stack Proposition

## Goal

Publish the existing 6 markdown files as a navigable static site on GitHub Pages with **minimum effort and zero ongoing maintenance**.

---

## The Simplest Three Options

### Option 1: MkDocs + Material theme (★ Recommended)

| Dimension | Score |
|-----------|-------|
| Setup effort | ~10 lines of config |
| Build step | GitHub Actions (copy-paste) |
| Nav / TOC / search | Built-in, zero config |
| Looks | Professional immediately |
| Files needed | 2 new files (`mkdocs.yml`, `.github/workflows/deploy.yml`) |

**Why**: MkDocs is purpose-built for markdown documentation. The Material theme gives you a sidebar nav, auto-generated TOC for each page, and full-text search — all with zero customization. Your files are already in perfect MkDocs format (frontmatter, headings, tables).

**What you add**:
- `mkdocs.yml` — site name, nav structure, theme
- `.github/workflows/deploy.yml` — builds on push, deploys to `gh-pages` branch

```yaml
# mkdocs.yml (entire file)
site_name: The Roots of Japanese
site_description: Japanese as a system of combinable roots
repo_url: https://github.com/YOU/roots-of-japanese
theme:
  name: material
  features:
    - navigation.sections
    - toc.integrate
markdown_extensions:
  - toc:
      permalink: true
nav:
  - Home: README.md
  - Project Goal: PROJECT_GOAL.md
  - Kanji Roots:
      - Overview: Japanese_Kanji_Productive_Roots.md
      - Deep Dive: Kanji_Root_Families_Deep_Dive.md
  - Verb System:
      - Multi-Functional Verbs (EN): Japanese_MultiFunctional_Verbs.md
      - 日本語の多機能動詞 (JA): 日本語の多機能動詞.md
  - Grammar Unlocks: JAPANESE-UNLOCKS.md
```

```yaml
# .github/workflows/deploy.yml
name: deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```

**Result**: Push to `main` → site auto-deploys to `https://YOU.github.io/roots-of-japanese`. Every page has a sidebar nav, in-page TOC, search bar, and responsive design.

---

### Option 2: GitHub-native Jekyll (no build step)

| Dimension | Score |
|-----------|-------|
| Setup effort | ~5 lines of config |
| Build step | **None** — GitHub builds automatically |
| Nav / TOC / search | Manual or theme-dependent |
| Looks | Depends on theme |
| Files needed | 1 new file (`_config.yml`) |

**Why**: The absolute minimum. GitHub Pages natively builds Jekyll sites, so you don't even need GitHub Actions. Just add a config file and enable Pages in repo settings.

**The catch**: Jekyll themes are blog-oriented. Getting a sidebar nav with nested sections requires either finding the right theme or writing some Liquid. Your wide tables may need tweaking. It's simpler to *deploy* but more fiddly to *configure*.

**What you add**:
- `_config.yml`
- Possibly a `_layouts/default.html` or a theme that supports docs-style nav

Not recommended unless you already know Jekyll well.

---

### Option 3: Bare HTML index + raw MD links

| Dimension | Score |
|-----------|-------|
| Setup effort | 1 HTML file |
| Build step | None |
| Nav / TOC / search | None |
| Looks | Minimal |

Just an `index.html` that links to each `.md` file. GitHub renders markdown natively, so each file looks decent on its own. No navigation between pages, no search, no TOC.

Good for a quick share link, not a real site.

---

## Recommendation: **Option 1 — MkDocs + Material**

| What | Why |
|------|-----|
| **MkDocs** | Built for exactly this — turning a folder of markdown into a docs site |
| **Material theme** | Looks like real documentation. Sidebar, search, dark mode, responsive — all free |
| **GitHub Actions deploy** | One copy-paste workflow file, fully automated |
| **Your files need zero changes** | Frontmatter, tables, code blocks, headings — all render correctly |
| **Future-proof** | Adding a new page = one line in `mkdocs.yml` nav |

**Total new files to create**: 2  
**Total lines of config**: ~25  
**Time to live**: ~10 minutes (create 2 files, push, enable Pages in repo settings, wait for first deploy)

---

## Next Steps If You Choose MkDocs

1. Create `mkdocs.yml` with the nav structure above
2. Create `.github/workflows/deploy.yml`
3. Push to `main`
4. Go to repo Settings → Pages → Source: `gh-pages` branch (created automatically by the action)
5. Wait ~1 minute for first deploy
6. Visit `https://YOUR_USERNAME.github.io/roots-of-japanese/`

**Optional polish** (later, not required):
- Add a custom `docs/assets/extra.css` for table styling
- Enable `navigation.tracking` for scroll-spy in sidebar
- Add a logo / favicon

---

## Cost

$0. GitHub Pages is free for public repos. MkDocs Material is open-source (MIT). No domain needed (uses `github.io` subdomain).
