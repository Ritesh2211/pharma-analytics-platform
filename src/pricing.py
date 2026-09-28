import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def estimate_elasticity(sales):
    # Use observed monthly Drug_A price and units by region; log-log elasticity.
    d=sales[sales.drug=='Drug_A'].copy()
    d=d[(d.avg_price_inr>0)&(d.units_sold>0)].copy()
    d['ln_price']=np.log(d.avg_price_inr); d['ln_units']=np.log(d.units_sold)
    model=LinearRegression().fit(d[['ln_price']],d['ln_units'])
    return float(model.coef_[0]), model

def scenario_table(sales, base_price=1000, base_units=None, elasticity=-1.05, competitor_change=0.0):
    if base_units is None:
        base_units=float(sales[sales.drug=='Drug_A'].tail(8).units_sold.mean())
    prices=np.arange(base_price*.80,base_price*1.21,base_price*.05)
    rows=[]
    for p in prices:
        relative=p/base_price
        units=base_units*(relative**elasticity)*(1-0.20*competitor_change)
        revenue=units*p
        rows.append([round(p),round(units),round(revenue,0)])
    return pd.DataFrame(rows,columns=['price_inr','expected_units','expected_revenue_inr'])
