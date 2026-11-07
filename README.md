# Housing Offset Exchange

> For Orange County employers deciding where their community and ESG dollars go: a carbon-offset-style market where a company funds one working family's home near its job, sees every benefit it gets back, and gets the capital back when the home sells.

**Team:** TODO team name
**Members:** TODO names
**Lane:** 3 Fund it
**Built at:** Claude Impact Lab: UCI × SoCal Affordable Housing, November 7, 2026

## The real user

A made-up CFO at a mid-size Orange County nonprofit hospital. Nurses leave because they can't afford to live near work, and every bedside RN who leaves costs about $60,090 to replace (NSI 2026). Apple and Amazon have spent billions on housing, but a 3,000-person employer has no simple, measurable way to do the same.

**Before:** Housing shows up as a one-off donation request. The money is gone, the impact is vague, and nobody can say what the company gets back.
**After:** The CFO picks an amount and sees how many homes it funds today, a line-by-line benefit stack (retention, capital returned, tax, reporting, cost of capital, regulatory credit, new business, recognition), each benefit labeled by how strong its evidence is, and the real yearly cost. Then the CFO commits to specific homes in a shared market.

## What we built

One page, four parts:

1. **OC Housing Offset Index.** What it costs today to close one starter home for a moderate-income family of 4, after state programs. It's the median across 37 OC cities, built from HCD income limits, Freddie Mac weekly rates and Zillow starter-home values. It was **$159,484 on Nov 5, 2026**, down $10,457 since Oct 8 as rates fell.
2. **Benefit stack.** Pick a buyer type, an amount and a structure (recoverable stake or grant). Eight benefits, each with a value and an evidence label (Sourced, Framework exists, Needs counsel, Prove in pilot).
3. **Live market.** Nine Home Offset Units, priced at each city's real gap. Anyone signed in can commit, and the progress bars, leaderboard and trade ticker are shared live. Commitments are simulated; no money moves.
4. **AI benefit analyst.** Describe any company in plain text. Claude calls the page's own calculator, inventory and index as tools and returns that company's benefit stack, with what still needs proof.

A second page, `last-mile-map.html`, maps every OC city by the dollars left to close a starter home after state programs, with gift, rate, income and Dream For All controls.

**Demo video:** TODO (uploaded on the hub)
**Live demo:** https://claude.ai/artifact/JyUPJtdtUrQW7DiJCMVA7h
**Last-Mile Map:** https://claude.ai/artifact/1Efqbm2s6UcwYFXyAT6Mjo

## How Claude is used

- **Building it:** Claude Code cloned the event repo, pulled and joined the Lane 3 data sources, wrote the analysis script, and built and published both pages. The team chose the direction and checked the numbers.
- **Inside the tool:** the AI benefit analyst runs Claude with three tools the page provides (`benefit_inventory`, `run_stack`, `cheapest_units`). It is told to use only numbers those tools return and to say "unknown" otherwise. A person should check every claim it marks "Needs counsel" or "Prove in pilot".

## Try it

**Live (recommended):** open the live demo link above while signed in to claude.ai. The shared market and the AI analyst need that sign-in.

**Locally:**

```bash
git clone https://github.com/dbwdev/housing-offset-exchange.git
```

```bash
cd housing-offset-exchange
```

```bash
open index.html
```

Opened as a local file, the index, benefit stack and units work fully. The market and analyst show a note that they need claude.ai.

**Reproduce the analysis** (Python 3.9+, standard library only, no installs):

```bash
python3 analysis/oc_gap_by_city.py data/sample > out.csv
```

This reproduces `analysis/oc_gap_by_city.csv` from the small sample in `data/sample/`. To rebuild from the full source files:

```bash
./scripts/fetch_data.sh data/full && python3 analysis/oc_gap_by_city.py data/full > out.csv
```

No API keys or environment variables are needed.

## Sources and assumptions

| Item | Source or assumption | Date checked |
|---|---|---|
| OC area median income, 4 persons: $138,600 | [HCD 2026 State Income Limits](https://www.hcd.ca.gov/sites/default/files/docs/grants-and-funding/income-limits-2026.pdf), revised Jun 23, 2026 | Nov 7, 2026 |
| Affordable housing cost: moderate 35% × 110% AMI, lower 30% × 70% AMI | [HSC 50052.5](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=50052.5), as HCD's PDF directs. **Percentages not yet checked against the statute text** (the page blocked automated fetches) | Nov 7, 2026 |
| 30-year rate 7.18% (Nov 5, 2026) and weekly history | [Freddie Mac PMMS history CSV](https://www.freddiemac.com/pmms/docs/PMMS_history.csv) | Nov 7, 2026 |
| Starter-home values by city | [Zillow Home Value Index](https://www.zillow.com/research/data/), bottom tier, all homes, smoothed, seasonally adjusted, Sep 30, 2026. Data provided by Zillow Group | Nov 7, 2026 |
| Dream For All: up to 20%, max $150,000 | [CalHFA](https://calhfa.ca.gov/dream/). Whether funds are open was **not confirmed** | Nov 6, 2026 (event repo) |
| Bedside RN turnover cost $60,090 | [NSI National Health Care Retention Report](https://www.nsinursingsolutions.com/Documents/Library/NSI_National_Health_Care_Retention_Report.pdf) | Nov 7, 2026 |
| Corporate charitable deduction limit, 21% federal rate | [IRS](https://www.irs.gov/charities-non-profits/charitable-organizations/charitable-contribution-deductions). A 1% floor from 2026 is our understanding; needs tax counsel | Nov 7, 2026 |
| Affordable housing eligible for social bonds | [ICMA Social Bond Principles](https://www.icmagroup.org/sustainable-finance/the-principles-guidelines-and-handbooks/social-bond-principles-sbp/) | Nov 7, 2026 |
| SB 253 Scope 3 reporting from 2027, categories pending | [Morgan Lewis, Aug 2026](https://www.morganlewis.com/pubs/2026/08/carb-extends-sb-253-deadline-and-previews-2027-reporting-rules) | Nov 7, 2026 |
| ~400 g CO₂ per mile, typical car | [EPA](https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle) | Nov 7, 2026 |
| CRA, Schedule H | [OCC](https://www.occ.treas.gov/topics/consumers-and-communities/cra/index-cra.html), [IRS Schedule H](https://www.irs.gov/forms-pubs/about-schedule-h-form-990) | Nov 7, 2026 |
| Corporate housing pledges (Apple $2.5B, Amazon ~$3.4B) | [Planetizen](https://planetizen.com/news/2021/01/111931-amazon-and-other-tech-giants-make-billion-dollar-commitments-affordable-housing), [ABC News](https://abcnews.go.com/Business/wireStory/amazon-invests-14-billion-affordable-housing-options-regions-111037994) | Nov 7, 2026 |
| 3% down, property tax 1.1%/yr, insurance 0.35%/yr, no HOA | **ASSUMPTION** | |
| 0.15 departures avoided per funded home per year | **ASSUMPTION**. A pilot would measure this | |
| Home price growth 4%/yr, pool keeps 25% of the gain, 5% opportunity cost | **ASSUMPTION** | |
| Turnover cost for school, hospitality, manufacturing and bank buyers | **ASSUMPTION**, no source checked | |
| 40 miles a day of commuting saved, 230 workdays | **ASSUMPTION** | |
| City dot positions on the Last-Mile Map | Approximate city centers, placed by hand | |

## What is real and what is mocked

| Part | Status |
|---|---|
| Housing Offset Index and its 9-week history | Working, real data |
| City gaps and unit prices | Working, real data (typical values, not specific listings) |
| Benefit stack calculator | Working; several inputs are labeled ASSUMPTION |
| Buyer types | Mocked: fictional examples, not real companies |
| Market commitments, leaderboard, ticker | Working shared database; the commitments themselves are simulated |
| AI benefit analyst | Working on claude.ai; output must be checked |
| Housing Offset Standard, registry, certificate | Concept only |

## Where it gets things wrong

- City values are Zillow index values for the bottom third of homes, not listings. A real deal needs a real price, HOA and tax bill.
- Seal Beach and Laguna Woods are excluded because their low-end homes are mostly in age-restricted communities. Other cities may have similar mixes we didn't catch.
- The retention benefit depends on an assumed departure rate. It is the biggest number in the stack and the least proven.
- Tax, accounting (loan versus wages, receivable versus expense) and CRA treatment are unknown until counsel and an examiner weigh in.
- If home prices fall, a shared-equity stake can lose value. The capital is not guaranteed to come back in full.
- The AI analyst can still be wrong. It is limited to tool numbers, but its "why" text is generated.

## Next steps

To be usable next month: one OC employer, one land trust or nonprofit, and three homes as a pilot, with income certified against the dated HCD table and the stake recorded on title. With one more week: confirm the HSC 50052.5 percentages, add HOA and real tax bills per listing, pull FHFA price history for the growth assumption, and get a tax opinion on the deduction and loan treatment.

## Data and privacy

This project uses only public or provided data. It contains no personal information about real tenants, buyers or residents. It does not file applications or contact any city or person. Market commitments are simulated and store only the company or team name a viewer types in.

## License

MIT, see [LICENSE](LICENSE).
