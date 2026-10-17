# Preset: finance-eu

Use for: products that show money, holdings, returns or taxes to readers in
German-speaking Europe, with English or German page text.
Not for: products without money figures, or readers who expect `1,234.56`.

Copy these sections into `DESIGN.md` and adjust them there. The product's own
choices win.

## Formats

All formatting happens in one place on the server, never ad hoc in templates.

| What | Format |
|---|---|
| Money in EUR | `1.595,39 €`; never `-0,00 €` |
| Other currencies | `1.595,39 USD`, with the ISO code after |
| Signed amounts | `+1.595,39 €` / `-1.595,39 €` |
| Percentages | `2,66 %`, with a space |
| Dates | `17.10.2026` |
| Times | `14:05`, in the product's home time zone, named once on the page |

- Input accepts: `1.234,56` and `1234,56`. Money and number fields are
  `type="text" inputmode="decimal"`, never `type="number"`.
- Colour is never the only sign of gain or loss: show the `+` or `-` sign too.

## Glossary

Use one term per concept, everywhere: page text, labels, tables, help.

| Concept | Term | Never use |
|---|---|---|
| Something held in a portfolio | Holding | Position, security, asset |
| What holdings are worth now | Value | Market value, worth |
| Change in price since purchase | Gain | Price gain, profit, P&L |
| What was paid, for performance | Cost basis | Purchase price, cost adj. |
| Cash paid out by a holding | Dividends | Payouts, income |
| Payouts of a fund, on fund pages | Distributions | Dividends (on those pages) |
| A buy, sell, dividend, fee or transfer | Activity | Transaction, trade, booking |
| Return that weights by cash flows | Money-weighted return (IRR) | IRR alone, MWR |
| Return independent of cash flows | Time-weighted return | TWR alone |
| A reference index the user chose | Benchmark | Index, comparison |

Add the product's tax terms (for example a national capital gains tax) as
their own rows.
