# Conventions

House style for the book so chapters stay consistent as they fill in.

## File anatomy

Every chapter starts with the macro include, then a single `#` title carrying a
stable cross-reference id:

```markdown
{{< include /_macros.qmd >}}

# Tokenization {#sec-tokenization}
```

## Math macros

Defined once in `_macros.qmd` (mirrored HTML/LaTeX blocks). Use them instead of
raw commands so notation stays uniform — e.g. `\vx`, `\mW`, `\softmax`,
`\loss`, `\dmodel`, `\vocab`. Add a macro only if it earns its keep across
chapters; keep the two blocks in sync.

## Theorem-like environments

Cross-referenceable, via labelled divs (HTML) backed by `amsthm` (PDF):

```markdown
::: {#def-lm}
A **language model** is a distribution $p_\params$ over token sequences.
:::
```

Prefixes: `def-` definition, `thm-` theorem, `lem-` lemma, `cor-` corollary,
`exm-` example. Reference with `@def-lm`, `@sec-tokenization`, `@fig-attn`,
`@eq-softmax`.

## Code

Book code is **static and for reading** — plain fenced ```python blocks, kept
short. The runnable version lives in `src/thebook/`; reference it by path so
readers can find it:

> The full implementation is in `src/thebook/attention.py`.

Only use executable ```{python}``` cells for figures/plots generated at render
time, and keep them cheap (they run on every build unless cached).

## Margin notes & citations

HTML puts references, citations, and figure captions in the margin. Use
footnotes (`^[like this]`) for asides — they render as margin notes — and
`[@key]` for citations from `references.bib`.

## Voice

Terse, precise, motivated. Define before use. Prefer one worked example over
three hand-wavy ones.
