import pandas as pd

def launch_scenarios(market_summary, forecast, base_price=1000):
    total_forecast=forecast.groupby('region',as_index=False).forecast_units.sum()
    x=market_summary[['region','treated_patients','growth_pct','opportunity_score']].merge(total_forecast,on='region')
    x['base_revenue_inr']=x.forecast_units*base_price
    x['high_adoption_revenue_inr']=x.forecast_units*1.15*base_price
    x['low_adoption_revenue_inr']=x.forecast_units*.85*base_price
    x['revenue_range_inr']=x.high_adoption_revenue_inr-x.low_adoption_revenue_inr
    return x.sort_values('opportunity_score',ascending=False)
