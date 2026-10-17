# DESIGN.md: <product>

Presets: <names from the design-track skill's `presets/`, or none>

This is the product's design contract. Every UI ticket follows it, and the
validator checks against it. The first design ticket fills it in and the human
approves it. Later design freezes add new patterns and terms.

## Parity rule

One product, two layouts. Every task, piece of information, action and label
on desktop exists on the phone. Layout may differ; capability and names may
not. A gap at one width is a defect, never a simplification.

## Look

- Colours, fonts and components: <where they are defined; reuse before adding>
- Light and dark mode: <for example, both, following the system setting>

## Breakpoints

- Phone: 390x844. Desktop: 1440x900. <add tablet if needed>
- Wide content gets a phone form, never clipping:
  - tables: <for example, cards with labelled values>
  - charts: <for example, a simplified chart and the key figures as text>
  - side panels: <for example, a sheet opened by a labelled button>

## Navigation

- Phone: <for example, a bottom bar with N items and safe-area padding;
  content never sits under it>
- Desktop: <for example, a top bar>
- Both use the same items, in the same order, with the same names.

## Touch and input

- Tap targets are at least 44x44 px.
- No information appears only on hover.
- Number fields open a numeric keyboard (`inputmode="decimal"` or
  `"numeric"`).
- Every action has a visible label or an accessible name.
- <product-specific rules>

## Formats

- Dates: <for example, DD.MM.YYYY>
- Numbers and money: <for example, 1.234,56 €>
- Input accepts: <which formats the fields accept>

## Glossary

Use one term per concept, everywhere.

| Concept | Term | Never use |
|---|---|---|
| <concept> | <term> | <synonyms to avoid> |

## Content priority per screen

For each screen, list what a phone user must see first. Everything else
stays reachable, never removed.

| Screen | First on phone | Reachable via |
|---|---|---|
| <screen> | <key figures and actions> | <for example, a scroll or a labelled section> |
