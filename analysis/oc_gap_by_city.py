"""OC starter-home gap by city.

Joins three Lane 3 sources:
  - HCD 2026 State Income Limits (revised Jun 23, 2026): Orange County AMI, 4 persons = $138,600
  - Freddie Mac PMMS history CSV: latest 30-year fixed rate
  - Zillow ZHVI city file, bottom tier (0.0-0.33), all homes, smoothed, seasonally adjusted

Affordable housing cost uses HSC 50052.5 as summarized by HCD (benchmark household = bedrooms + 1):
  moderate = 35% x 110% of AMI, lower = 30% x 70% of AMI.  VERIFY against the statute text before citing.

ASSUMPTIONS (labelled): 3% down, 30-yr fixed, property tax 1.1%/yr, insurance 0.35%/yr, HOA $0.
Usage: python3 oc_gap_by_city.py <data_dir>   (data_dir holds pmms.csv and city_zhvi_bottom.csv)
"""
import csv, os, sys

AMI_4P = 138_600                      # HCD 2026, Orange County, 4 persons
TAX, INS, DOWN, HOA = 0.011, 0.0035, 0.03, 0   # ASSUMPTION
DFA_PCT, DFA_CAP = 0.20, 150_000      # CalHFA Dream For All page: up to 20%, max $150k (funds unconfirmed)
SENIOR_ONLY = {"Laguna Woods", "Seal Beach"}   # bottom tier dominated by age-restricted communities: exclude

def max_price(annual_cost, rate_pct):
    r = rate_pct / 100 / 12
    pf = r / (1 - (1 + r) ** -360) if r > 0 else 1 / 360
    return (annual_cost / 12 - HOA) / ((1 - DOWN) * pf + (TAX + INS) / 12)

def main(d):
    pm = [r for r in csv.DictReader(open(os.path.join(d, "pmms.csv"))) if r["pmms30"].strip()]
    rate_date, rate = pm[-1]["date"], float(pm[-1]["pmms30"])
    mod = max_price(0.35 * 1.10 * AMI_4P, rate)
    low = max_price(0.30 * 0.70 * AMI_4P, rate)
    rd = csv.reader(open(os.path.join(d, "city_zhvi_bottom.csv"))); h = next(rd)
    dates = [c for c in h if c[:2] in ("19", "20")]
    out = []
    for x in rd:
        row = dict(zip(h, x))
        if row["State"] != "CA" or row["CountyName"] != "Orange County": continue
        vals = [(c, float(row[c])) for c in dates if row[c]]
        if not vals or not vals[-1][0].startswith("2026"): continue
        asof, p = vals[-1]
        prev = dict(vals).get(dates[dates.index(asof) - 12])
        gap = p - mod
        out.append(dict(city=row["RegionName"], zhvi_asof=asof, starter_value=round(p),
                        afford_moderate=round(mod), gap_moderate=round(gap),
                        dream_for_all=round(min(DFA_PCT * p, DFA_CAP)),
                        gap_after_dfa=round(gap - min(DFA_PCT * p, DFA_CAP)),
                        gap_lower=round(p - low),
                        change_12mo=round(p - prev) if prev else "",
                        excluded="senior communities" if row["RegionName"] in SENIOR_ONLY else ""))
    out.sort(key=lambda r: r["gap_after_dfa"])
    w = csv.DictWriter(sys.stdout, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    print(f"# rate {rate}% on {rate_date}; moderate max price {mod:,.0f}; lower max price {low:,.0f}", file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv[1])
