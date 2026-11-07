#!/usr/bin/env bash
# Download the full source files once (be kind to public servers: run this once, then reuse the files).
set -euo pipefail
OUT="${1:-data/full}"; mkdir -p "$OUT"
curl -sSL -o "$OUT/pmms.csv" https://www.freddiemac.com/pmms/docs/PMMS_history.csv
curl -sSL -o "$OUT/city_zhvi_bottom.csv" https://files.zillowstatic.com/research/public_csvs/zhvi/City_zhvi_uc_sfrcondo_tier_0.0_0.33_sm_sa_month.csv
curl -sSL -o "$OUT/income-limits-2026.pdf" https://www.hcd.ca.gov/sites/default/files/docs/grants-and-funding/income-limits-2026.pdf
echo "Saved to $OUT"
