# Pharma Commercial Decision Analytics

## Executive objective
Determine where and how a fictional pharmaceutical company should commercialize `Drug_A` for type-2 diabetes in India. The project combines market sizing, physician segmentation, demand forecasting, pricing elasticity, scenario analysis, and executive storytelling.

> **Important:** All data are synthetic and generated deterministically. No real patients, physicians, hospitals, or confidential company data are used.

## Why this project is relevant to Decision Analytics
The case is intentionally structured as **Business question → analytical framework → data synthesis → model → scenario → decision**.


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
