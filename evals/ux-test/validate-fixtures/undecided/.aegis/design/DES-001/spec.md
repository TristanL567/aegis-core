# DES-001 spec: dividend calendar

## Flows
- T1: open Dividend calendar for 2025; March is selected; tap another month (January to June) to see its payments.
- T2: each payment row shows the net amount in bold with the gross amount below it.

## Screens
### Dividend calendar
- Default: month buttons January to June 2025 (Jan to Jun), the selected month highlighted, its payments listed by date. Net = gross minus 27.5% KESt (Austrian securities only).
- Empty: "No payments expected in <Month>."
- Loading: month buttons stay visible; the list shows three grey placeholder rows.
- Error: "Couldn't load payments. Try again." with a Try again button; month buttons stay usable.
