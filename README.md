# A Book on Language Modelling

A compact, first-principles treatment of **language-model pretraining** — built
with [Quarto](https://quarto.org) (HTML-first, PDF secondary) and a runnable
Python companion package managed with [uv](https://docs.astral.sh/uv/).

## Render

```sh
quarto preview            # live HTML, auto-opens in your browser
quarto render             # all formats -> _book/
quarto render --to html   # website only
quarto render --to pdf    # PDF (run `quarto install tinytex` once)
```

## Companion code

```sh
uv sync --group render    # env + notebook/plot tooling
uv run pytest             # test src/thebook/
```

Book listings are static and quoted from `src/thebook/`; that package is the
runnable version.

## Layout

```
_quarto.yml     book config (parts, chapters, formats)
_macros.qmd     shared math macros (HTML + PDF)
index.qmd       preface
chapters/       one .qmd per chapter
appendices/     notation, math background, code tour
src/thebook/    runnable companion package
```

See [`CONVENTIONS.md`](CONVENTIONS.md) for markup house style.

## Deployment

Pushes to `main` render the HTML book and publish it to GitHub Pages via
[`.github/workflows/publish.yml`](.github/workflows/publish.yml). Enable it once:
**Settings → Pages → Source → GitHub Actions**.
