# Preset: data-portal

Use for: server-rendered web portals with sidebar navigation, tables and
charts, read on phones as much as on desktops.
Not for: native apps, marketing sites, or apps built around a bottom tab bar.

Copy these sections into `DESIGN.md` and adjust them there. The product's own
choices win.

## Look

- Colours come only from the CSS custom properties of the product's main
  stylesheet, never from new hard-coded values.
- Every page works in light and in dark mode, following the system setting.
- New pages reuse existing components before adding new ones.

## Breakpoints

- Phone: 390x844. Desktop: 1440x900. Check every page at both sizes.
- One main phone breakpoint; add another only when a layout needs it.
- The page never scrolls sideways. Wide content gets a phone form:
  - **Tables:** each row becomes a card, and every column appears as a
    labelled value (`data-label`). A table may scroll sideways inside its own
    wrapper only when every column stays reachable that way.
  - **Charts:** inline SVG with `role="img"`, a title and a description. The
    figures a chart shows also appear as text. A wide time chart may scroll
    inside its own wrapper.
  - **Side panels** become a full-width panel opened by a labelled button.

## Navigation

- Desktop: a left sidebar. Phone: the sidebar becomes a compact band above
  the page.
- Both show the same items, in the same order, with the same names.
- The main create action is a floating button at both widths.

## Touch and input

- Tap targets are at least 44x44 px, links in the phone navigation band
  included.
- No information appears only on hover. A `title` tooltip may repeat
  visible text but never be its only source; values shown on hover can also
  be reached by a tap or as text.
- Every keyboard shortcut has a visible control.
- Keep a skip link, `aria-current` on the current page, `:focus-visible`
  rings, and `prefers-reduced-motion`.
