# DES-001 spec: dividend calendar

Scope: declared dividends from Austrian stocks. Foreign securities and coupon or interest payments are out of scope (see the ticket's non_goals).

## Flows
- T1: open Dividend calendar; it shows the current year with the current month selected and that month's dividends. Tap a month button (January to December) to switch month; use the previous/next year controls to change year.
- T2: each dividend row shows the net amount in bold, net = gross minus 27.5% KESt, with the gross amount below it.

## Screens
### Dividend calendar
- Default: year with previous/next controls; month buttons January to December, the selected month highlighted; its dividends listed by date (DD.MM.YYYY), each with net and gross in EUR.
- Empty: "No dividends expected in <Month> <Year>."
- Loading: year and month controls stay visible; the list shows three grey placeholder rows.
- Error: "Couldn't load dividends. Try again." with a Try again button; year and month controls stay usable.
