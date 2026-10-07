-- AtliQ Mart: example PostgreSQL analysis queries
-- These queries are provided as portfolio/reference SQL.
-- Run them only after loading the CSVs into PostgreSQL/Supabase.

-- 1. Order-level KPI scorecard
SELECT
    COUNT(*) AS total_orders,
    ROUND(AVG(on_time) * 100, 1) AS on_time_pct,
    ROUND(AVG(in_full) * 100, 1) AS in_full_pct,
    ROUND(AVG(otif) * 100, 1) AS otif_pct
FROM fact_aggregate;

-- 2. Customer OTIF performance
SELECT
    f.customer_id,
    c.customer_name,
    c.city,
    COUNT(*) AS orders,
    ROUND(AVG(f.on_time) * 100, 1) AS on_time_pct,
    ROUND(AVG(f.in_full) * 100, 1) AS in_full_pct,
    ROUND(AVG(f.otif) * 100, 1) AS otif_pct,
    t.otif_target_pct
FROM fact_aggregate f
JOIN dim_customers c
  ON f.customer_id = c.customer_id
JOIN dim_targets_orders t
  ON f.customer_id = t.customer_id
GROUP BY
    f.customer_id, c.customer_name, c.city, t.otif_target_pct
ORDER BY otif_pct ASC;

-- 3. Customer failure segmentation
WITH customer_kpis AS (
    SELECT
        customer_id,
        AVG(on_time) * 100 AS on_time_pct,
        AVG(in_full) * 100 AS in_full_pct,
        AVG(otif) * 100 AS otif_pct
    FROM fact_aggregate
    GROUP BY customer_id
)
SELECT *,
    CASE
        WHEN on_time_pct < 50 AND in_full_pct < 40 THEN 'Dual failure'
        WHEN on_time_pct < 50 THEN 'On-Time failure'
        WHEN in_full_pct < 40 THEN 'In-Full failure'
        ELSE 'Core'
    END AS segment
FROM customer_kpis
ORDER BY otif_pct ASC;
