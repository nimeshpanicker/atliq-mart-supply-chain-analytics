"""Validate the main AtliQ Mart supply-chain KPIs from the full-period CSV files."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "full_period"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

order_lines = pd.read_csv(DATA / "fact_order_line.csv")
orders = pd.read_csv(DATA / "fact_aggregate.csv")

# Parse source dates using the source DD-MM-YYYY convention.
for col in ["order_placement_date", "agreed_delivery_date", "actual_delivery_date"]:
    order_lines[col] = pd.to_datetime(order_lines[col], format="%d-%m-%Y")

orders["order_placement_date"] = pd.to_datetime(
    orders["order_placement_date"], format="%d-%m-%Y"
)

kpis = {
    "Total Orders": orders["order_id"].nunique(),
    "Total Order Lines": len(order_lines),
    "Line Fill Rate %": round(order_lines["In Full"].mean() * 100, 1),
    "Volume Fill Rate %": round(
        order_lines["delivery_qty"].sum()
        / order_lines["order_qty"].sum()
        * 100,
        1,
    ),
    "On-Time Delivery %": round(orders["on_time"].mean() * 100, 1),
    "In-Full Delivery %": round(orders["in_full"].mean() * 100, 1),
    "OTIF %": round(orders["otif"].mean() * 100, 1),
}

result = pd.DataFrame(
    [{"KPI": key, "Value": value} for key, value in kpis.items()]
)
result.to_csv(OUT / "kpi_validation.csv", index=False)

print("AtliQ Mart KPI validation")
print("-" * 28)
for key, value in kpis.items():
    print(f"{key}: {value}")

# Basic integrity checks.
assert order_lines["order_id"].notna().all()
assert orders["order_id"].is_unique
assert (order_lines["order_qty"] > 0).all()
assert (order_lines["delivery_qty"] >= 0).all()
assert (order_lines["delivery_qty"] <= order_lines["order_qty"]).all()

derived_if = (order_lines["delivery_qty"] >= order_lines["order_qty"]).astype(int)
derived_ot = (
    order_lines["actual_delivery_date"] <= order_lines["agreed_delivery_date"]
).astype(int)
derived_otif = derived_if * derived_ot

assert (derived_if == order_lines["In Full"]).all()
assert (derived_ot == order_lines["On Time"]).all()
assert (derived_otif == order_lines["On Time In Full"]).all()

print("\nValidation checks passed.")
