# Pharma Commercial Decision Analytics — ZS Portfolio Case Study

## Executive objective
Determine where and how a fictional pharmaceutical company should commercialize `Drug_A` for type-2 diabetes in India. The project combines market sizing, physician segmentation, demand forecasting, pricing elasticity, scenario analysis, and executive storytelling.

> **Important:** All data are synthetic and generated deterministically. No real patients, physicians, hospitals, or confidential company data are used.

## Why this project is relevant to Decision Analytics
The case is intentionally structured as **Business question → analytical framework → data synthesis → model → scenario → decision**. It mirrors the skills described in current ZS Decision Analytics postings: advanced statistical/forecasting work, synthesizing diverse sources, actionable business insights, scenario modeling, and communicating results.

## Project questions
1. Where is the addressable market and where should launch investment be concentrated?
2. Which physician segments should the commercial team prioritize?
3. What is the expected 6-month demand for Drug_A?
4. How does price affect expected units and revenue?
5. How sensitive is the recommendation to competitor price and adoption assumptions?
6. What should an executive team do next?

## Stack
- Python: pandas, NumPy, scikit-learn, statsmodels
- SQL: PostgreSQL-compatible analytical queries
- Visualization: Plotly + Streamlit
- Deliverables: executive PDF + PowerPoint
- Testing: pytest

## Quick start
### Windows PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m src.pipeline
streamlit run dashboard/app.py
```
Open the Streamlit URL shown in the terminal.

### Run tests
```powershell
pytest -q
```

## Repository
```text
data/raw/              synthetic source data
data/processed/        generated analytical tables and model outputs
src/                    reusable analysis modules
sql/                    PostgreSQL schema + business queries
dashboard/              interactive Streamlit decision dashboard
tests/                  automated tests
docs/                   methodology and interview guide
presentation/           executive presentation source
outputs/                generated charts/tables/reports
```

## Recommended interview story
**Situation:** A pharma client is considering how to scale Drug_A in a competitive diabetes market.

**Task:** Quantify market opportunity, identify priority physicians, forecast demand, and evaluate pricing scenarios.

**Action:** Integrated market, sales, physician, engagement, and product data; engineered commercial features; built segmentation and forecast models; tested pricing scenarios; translated model outputs into an executive decision framework.

**Result:** The final dashboard provides a transparent decision trail from assumptions to forecast, scenario outputs, and recommended commercial actions.

## What not to claim
Do not present the synthetic numbers as real ZS/client results. Say: **“I built a synthetic pharma commercial decision-analytics case to demonstrate the workflow.”**
