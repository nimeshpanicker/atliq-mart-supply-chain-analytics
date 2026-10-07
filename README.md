# 🚚 AI-Powered Supply Chain Analytics & OTIF Performance Monitoring

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Excel](https://img.shields.io/badge/Excel-Analysis-217346?logo=microsoftexcel)
![Supply Chain](https://img.shields.io/badge/Domain-Supply%20Chain-orange)
![Analytics](https://img.shields.io/badge/Analytics-OTIF-green)

An end-to-end **Supply Chain Analytics project** focused on order fulfilment, delivery reliability, customer service performance, and OTIF (On-Time In-Full) monitoring for AtliQ Mart.

The project analyzes **24,195 order lines and 13,467 orders across 35 customers** in Ahmedabad, Vadodara, and New Jersey to identify service-level gaps, customer-specific failure patterns, and actionable supply-chain improvements.

---

## 📌 Project Overview

AtliQ Mart is a growing food manufacturer and distributor serving retail customers across India and the United States.

The primary business challenge is poor visibility into:

- On-Time Delivery
- In-Full Delivery
- OTIF performance
- Customer-level service failures
- Product availability
- Delivery reliability
- Customer-specific service targets

The objective of this project is to transform operational order data into validated supply-chain KPIs and identify the customers and operational patterns contributing to poor service performance.

---

## 🎯 Business Problem

Management needs to understand:

1. How reliably are customer orders delivered?
2. How many orders are delivered completely?
3. What is the actual OTIF performance?
4. Which customers are consistently underperforming?
5. Are failures caused by late delivery, short delivery, or both?
6. Are high-value customers receiving adequate service?
7. Are problems concentrated in specific cities or product categories?
8. What actions can improve supply-chain performance?

---

## 🎯 Project Objectives

- Calculate Line Fill Rate and Volume Fill Rate.
- Calculate On-Time, In-Full, and OTIF performance.
- Analyze performance at both line and order level.
- Compare actual performance against customer-specific targets.
- Identify underperforming customers.
- Segment customers according to their failure patterns.
- Analyze geographic and product-level performance.
- Validate the existing workbook KPIs.
- Identify data-quality problems.
- Generate actionable business recommendations.

---

# 🏗️ Project Architecture

```text
                 ┌─────────────────────┐
                 │   Source Data       │
                 │ CSV / Excel Files   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Data Preparation    │
                 │ & Validation        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ KPI Calculation     │
                 │ Python / Pandas     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Customer & Supply   │
                 │ Chain Analysis      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Business Insights   │
                 │ & Recommendations   │
                 └─────────────────────┘
