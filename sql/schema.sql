CREATE SCHEMA IF NOT EXISTS pharma_da;

CREATE TABLE pharma_da.market (month DATE, region TEXT, adult_population BIGINT, diagnosed_patients BIGINT, treated_patients BIGINT);
CREATE TABLE pharma_da.doctors (doctor_id TEXT PRIMARY KEY, region TEXT, city TEXT, specialty TEXT, monthly_patient_volume INT, digital_engagement NUMERIC, current_competitor TEXT, adoption_propensity NUMERIC);
CREATE TABLE pharma_da.sales (month DATE, region TEXT, drug TEXT, units_sold INT, avg_price_inr NUMERIC, revenue_inr NUMERIC);
CREATE TABLE pharma_da.products (drug TEXT PRIMARY KEY, company TEXT, price_inr NUMERIC, efficacy_score NUMERIC, access_score NUMERIC, monthly_growth NUMERIC);
CREATE TABLE pharma_da.doctor_engagement (doctor_id TEXT, month DATE, region TEXT, sales_calls INT, our_prescriptions INT, adoption_propensity NUMERIC);
