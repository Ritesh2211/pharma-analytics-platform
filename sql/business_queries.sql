-- 1. Market opportunity by region
SELECT region, MAX(month) AS latest_month, MAX(treated_patients) AS treated_patients,
       ROUND(MAX(treated_patients)::numeric / SUM(MAX(treated_patients)) OVER () * 100,2) AS share_of_treated_market
FROM pharma_da.market GROUP BY region ORDER BY treated_patients DESC;

-- 2. Drug_A revenue trend
SELECT DATE_TRUNC('month',month) AS month, SUM(units_sold) units, SUM(revenue_inr) revenue
FROM pharma_da.sales WHERE drug='Drug_A' GROUP BY 1 ORDER BY 1;

-- 3. Physician prioritization
SELECT doctor_id, region, specialty, monthly_patient_volume, digital_engagement, adoption_propensity,
       (0.5*PERCENT_RANK() OVER (ORDER BY monthly_patient_volume)+0.3*digital_engagement+0.2*adoption_propensity) AS priority_score
FROM pharma_da.doctors ORDER BY priority_score DESC LIMIT 100;

-- 4. Regional growth
WITH x AS (SELECT region, MIN(month) first_month, MAX(month) last_month,
SUM(CASE WHEN month=(SELECT MIN(month) FROM pharma_da.sales) THEN revenue_inr ELSE 0 END) first_rev,
SUM(CASE WHEN month=(SELECT MAX(month) FROM pharma_da.sales) THEN revenue_inr ELSE 0 END) last_rev
FROM pharma_da.sales WHERE drug='Drug_A' GROUP BY region)
SELECT *, ROUND((last_rev/NULLIF(first_rev,0)-1)*100,2) growth_pct FROM x ORDER BY growth_pct DESC;
