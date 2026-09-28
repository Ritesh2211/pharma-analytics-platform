from pathlib import Path
import pandas as pd
from .data_prep import load_raw, build_market_summary, build_doctor_features, PROCESSED
from .segmentation import segment_doctors
from .forecasting import forecast_all
from .pricing import estimate_elasticity, scenario_table
from .scenario import launch_scenarios

def main():
    PROCESSED.mkdir(exist_ok=True)
    raw=load_raw()
    market=build_market_summary(raw); market.to_csv(PROCESSED/'market_opportunity.csv',index=False)
    doctors=build_doctor_features(raw); doctors.to_csv(PROCESSED/'doctor_features.csv',index=False)
    seg,profile=segment_doctors(raw['doctors']); seg.to_csv(PROCESSED/'doctor_segments.csv',index=False); profile.to_csv(PROCESSED/'segment_profile.csv')
    forecast=forecast_all(raw['sales']); forecast.to_csv(PROCESSED/'demand_forecast.csv',index=False)
    elasticity,_=estimate_elasticity(raw['sales']); pd.DataFrame({'elasticity':[elasticity]}).to_csv(PROCESSED/'price_elasticity.csv',index=False)
    price=scenario_table(raw['sales'],elasticity=elasticity); price.to_csv(PROCESSED/'pricing_scenarios.csv',index=False)
    launch=launch_scenarios(market,forecast); launch.to_csv(PROCESSED/'launch_scenarios.csv',index=False)
    print('Pipeline complete.')
    print(f'Estimated Drug_A price elasticity: {elasticity:.3f}')
    print('Top regions:', ', '.join(market.head(3).region.tolist()))

if __name__=='__main__': main()
