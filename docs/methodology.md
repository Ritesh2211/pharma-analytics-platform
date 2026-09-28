# Methodology

## 1. Market opportunity
Composite score = 50% normalized treated-patient volume + 50% normalized annualized growth proxy. This is a portfolio simplification; a production model would use epidemiology, diagnosis rates, access, therapy eligibility, competitor share, and client assumptions.

## 2. Physician segmentation
K-Means clusters physicians using monthly patient volume, digital engagement, and adoption propensity. Clusters are renamed after profiling their centroids, not before modeling.

## 3. Forecasting
A gradient-boosted regression model uses lagged demand, rolling averages, time index, and monthly seasonality. Forecasts are recursive for six months. In a real client engagement, forecast validation would include rolling-origin backtesting and benchmark models such as naive, seasonal naive, ETS, and hierarchical forecasts.

## 4. Pricing
A log-log regression estimates price elasticity from synthetic observations. Revenue is then evaluated across price scenarios. Elasticity is directional and intentionally simple; a real pricing study would address endogeneity, promotional effects, payer/access effects, competitive response, and uncertainty.

## 5. Scenario analysis
Base, high-adoption (+15%), and low-adoption (-15%) revenue cases communicate uncertainty rather than pretending the model produces one certain answer.

## 6. Quality controls
- Deterministic data generation (`seed=42`)
- No real PII
- Automated tests
- Modular code
- Explicit assumptions and caveats
