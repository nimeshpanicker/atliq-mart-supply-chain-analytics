# AtliQ Mart Supply Chain Analytics Report

## Executive Summary

This report presents an AI-assisted supply chain analysis of AtliQ Mart's order fulfillment and delivery performance. The analysis uses **Excel and Quadratic AI** for spreadsheet-based exploration and business analysis, supported by **Python/Pandas for independent KPI validation**.

The dataset contains **24,195 order lines and 13,467 orders across 35 customers** in Ahmedabad, Vadodara, and New Jersey, covering orders placed from 1 March to 16 May 2025.

Key observations from the analysis include:

* The validated order-level OTIF performance is **28.7%**, meaning only 3,866 of 13,467 orders were delivered both on time and in full.
* The original Excel workbook reported **45.9% OTIF**, but this figure was calculated at line level using a 1,000-line sample rather than the complete dataset at order level.
* Overall On-Time Delivery is **59.2%**, while In-Full Delivery is **52.6%**.
* Line Fill Rate is **65.9%**, while Volume Fill Rate is **96.6%**, indicating that many short deliveries are relatively shallow in quantity.
* None of the 35 customers meets its On-Time, In-Full, or OTIF target.
* Twelve customers form a major service-failure cluster, representing approximately 40% of orders while achieving only **13.8% OTIF**.
* Performance is relatively consistent across cities and product categories, indicating that customer-specific operational factors are more important than broad geographic or product-level differences.
* The analysis identified important data-quality issues in the original Excel workbook that should be corrected before automated reporting or dashboarding.

---

## Overall Supply Chain KPI Statistics

| Metric | Value |
|---|---:|
| Total orders | 13,467 |
| Total order lines | 24,195 |
| Total units ordered | 5,676,448 |
| Line Fill Rate | 65.9% |
| Volume Fill Rate | 96.6% |
| On-Time Delivery | 59.2% |
| In-Full Delivery | 52.6% |
| OTIF | 28.7% |
| Customers | 35 |
| Products | 18 |
| Product categories | 3 |

---

## Dataset Overview

The analysis uses the following Excel and CSV source files:

| Dataset | Description |
|---|---|
| `fact_order_line.csv` | Order-line level quantities, dates and fulfillment flags |
| `fact_aggregate.csv` | Order-level On-Time, In-Full and OTIF flags |
| `dim_customers.csv` | Customer master data |
| `dim_products.csv` | Product master data |
| `dim_targets_orders.csv` | Customer-specific service targets |
| `Output.xlsx` | Original Excel analysis workbook |

### Customer Coverage

The dataset contains 35 customer accounts across:

* Ahmedabad
* Vadodara
* New Jersey, USA

### Product Coverage

The dataset contains 18 products across:

* Dairy
* Food
* Beverages

---

## KPI Analysis

### On-Time Delivery

The validated order-level On-Time Delivery rate is:

**59.2%**

This means 7,975 of 13,467 orders were delivered on or before their agreed delivery date.

The remaining orders experienced at least one late order line.

---

### In-Full Delivery

The validated order-level In-Full Delivery rate is:

**52.6%**

This means 7,078 of 13,467 orders were delivered with every order line fulfilled at the requested quantity.

Because an order fails the In-Full KPI when even one line is short, the order-level result is lower than the line-level Fill Rate.

---

### OTIF Performance

The validated order-level OTIF is:

# 28.7%

This represents:

**3,866 OTIF orders / 13,467 total orders**

OTIF combines both delivery dimensions:

* Delivered On Time
* Delivered In Full

An order must satisfy both conditions to be classified as OTIF.

---

## Excel Workbook vs Validated Results

One of the most important findings was the difference between the original Excel workbook and the independently validated results.

| KPI | Excel Workbook | Validated Full Dataset |
|---|---:|---:|
| On-Time | 71.8% | 59.2% |
| In-Full | 62.3% | 52.6% |
| OTIF | 45.9% | 28.7% |

The Excel workbook's KPI sheet was based on the first 1,000 order lines and calculated performance at line level.

The validated analysis uses the complete dataset and calculates the primary service KPIs at **order level**.

This difference demonstrates the importance of clearly defining the **grain and denominator** of supply-chain KPIs.

---

## Customer Target Analysis

Customer-specific service targets were provided in:

`dim_targets_orders.csv`

### Actual vs Target

| KPI | Actual | Target | Gap |
|---|---:|---:|---:|
| On-Time | 59.2% | 85.3% | -26.0 pts |
| In-Full | 52.6% | 76.3% | -23.8 pts |
| OTIF | 28.7% | 65.1% | -36.4 pts |

### Key Observation

**None of the 35 customers meets its On-Time, In-Full, or OTIF target.**

This indicates that the supply-chain service problem is broader than a small number of isolated customer accounts.

---

## Customer-Level Analysis

The analysis identified **12 customers with significantly weaker service performance**.

These customers represent approximately:

* 34% of customers
* 40% of orders
* 34% of order value

Their combined OTIF performance is approximately:

**13.8%**

compared with:

**38.7%**

for the remaining 23 customers.

---

## Customer Failure Segmentation

Customers were classified according to their On-Time and In-Full performance.

| Segment | Customers | Main Issue |
|---|---:|---|
| Core | 23 | Relatively stronger service |
| On-Time Failure | 5 | Late deliveries |
| In-Full Failure | 4 | Short deliveries |
| Dual Failure | 3 | Late and short deliveries |

### Interpretation

The customer segmentation shows that the service problem has **different failure modes**.

Late-delivery customers require logistics and dispatch investigation, while short-delivery customers require inventory, allocation, and order-fulfillment investigation.

---

## High-Value Customer Risk

Several commercially important customers also have weak service performance.

Examples include:

| Customer | Order Value | OTIF |
|---|---:|---:|
| Acclaimed Stores – Ahmedabad | ₹18.12M | 20.1% |
| Vijay Stores – Vadodara | ₹17.97M | 9.1% |
| Lidl – New Jersey | ₹17.77M | 21.7% |
| Price Rite – New Jersey | ₹17.60M | 8.8% |

These customers have relatively high order value but significantly weaker OTIF performance.

This creates potential customer-service and commercial risk.

---

## Geographic Analysis

| Geography | On-Time | In-Full | OTIF |
|---|---:|---:|---:|
| India | 58.4% | 52.9% | 28.5% |
| USA | 61.2% | 51.8% | 29.1% |
| Ahmedabad | 58.5% | 54.1% | 29.3% |
| Vadodara | 58.2% | 51.7% | 27.7% |
| New Jersey | 61.2% | 51.8% | 29.1% |

### Interpretation

Performance is relatively consistent across the analyzed geographies.

Vadodara records the lowest OTIF at **27.7%**, but the analysis indicates that customer mix is likely more important than geography itself.

---

## Product & Category Analysis

| Category | Lines | Line Fill Rate | Volume Fill Rate | OTIF — Line |
|---|---:|---:|---:|---:|
| Dairy | 16,086 | 65.8% | 96.6% | 47.6% |
| Food | 4,095 | 66.2% | 96.6% | 48.6% |
| Beverages | 4,014 | 66.2% | 96.6% | 48.1% |

### Interpretation

The three product categories have very similar performance.

Line Fill Rate ranges only from **65.8% to 66.2%**, suggesting that the observed service problem is not primarily concentrated in one product category.

---

## Fill Rate Analysis

A significant difference exists between Line Fill Rate and Volume Fill Rate.

| Metric | Result |
|---|---:|
| Line Fill Rate | 65.9% |
| Volume Fill Rate | 96.6% |

### Interpretation

The company delivers approximately **96.6% of the total quantity ordered**, but only **65.9% of order lines are completely fulfilled**.

This means that many short deliveries are relatively small quantity differences.

The analysis found recurring shortfall levels of approximately:

* 5%
* 10%
* 20%

This pattern should be investigated to determine whether allocation rules, packaging constraints, or other operational processes contribute to the shortfalls.

---

## Root-Cause Analysis

The dataset contains delivery outcomes but does not contain all operational variables required to prove the underlying causes.

### Observed Patterns

* Customer-level failures are highly concentrated.
* Product categories have similar fulfillment performance.
* Geographic performance is relatively consistent.
* Weekly performance is relatively flat.
* Late deliveries are concentrated in specific customer accounts.
* Short deliveries follow recurring shortfall levels.
* Core customers also remain significantly below their targets.

### Potential Areas for Investigation

* Customer-specific delivery windows
* Dispatch cut-off times
* Delivery scheduling
* Order consolidation
* Inventory allocation rules
* Customer-specific ordering processes
* Fixed pack or batch-size constraints

These are **potential hypotheses and should not be interpreted as confirmed root causes** without additional operational data.

---

## Data Quality

The full CSV datasets passed several validation checks.

| Data Quality Check | Result |
|---|---|
| Missing values in fact tables | Passed |
| Duplicate order lines | None found |
| Duplicate order-product combinations | None found |
| Duplicate order IDs | None found |
| Customer ID validation | Passed |
| Product ID validation | Passed |
| Customer target coverage | Passed |
| OT/IF/OTIF flag consistency | Passed |
| Order vs line reconciliation | Passed |

### Issues Identified in the Original Excel Workbook

Several issues were identified in the original `Output.xlsx`:

* Sheet3 contains a 1,000-line sample rather than the complete dataset.
* Sheet3 calculates OT, IF and OTIF at line level.
* Sheet2 contains 999 lines instead of 1,000.
* Placement dates have a day/month interpretation issue.
* Customer lookup data is incomplete for one customer.
* Product lookup data is incomplete for one product.
* 252 of 999 Sheet2 lines have missing `total_amount`.
* Sheet4 and Sheet5 use different grains and scopes.
* Several KPI values are hard-coded rather than formula-driven.

These issues demonstrate why independent validation is required before using the workbook for automated reporting.

---

## AI-Assisted Analysis Using Quadratic AI

### Quadratic AI + Excel Workflow

Quadratic AI was used as the primary **AI-assisted spreadsheet analysis environment** for exploring and analyzing the Excel-based supply-chain data.

The workflow included:

```text
Excel / CSV Data
       ↓
Quadratic AI
       ↓
Data Exploration
       ↓
KPI Analysis
       ↓
Customer Analysis
       ↓
Business Insights
       ↓
Python / Pandas Validation
       ↓
Validated Results
       ↓
Final Report
