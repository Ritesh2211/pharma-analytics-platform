from sklearn.ensemble import HistGradientBoostingRegressor
import pandas as pd
import numpy as np

def make_features(df):
    x=df.sort_values('month').copy()
    x['time_index']=np.arange(len(x))
    for lag in [1,2,3,6,12]: x[f'lag_{lag}']=x['units_sold'].shift(lag)
    x['rolling_3']=x['units_sold'].shift(1).rolling(3).mean()
    x['rolling_6']=x['units_sold'].shift(1).rolling(6).mean()
    x['month_num']=x.month.dt.month
    x['sin_month']=np.sin(2*np.pi*x.month_num/12)
    x['cos_month']=np.cos(2*np.pi*x.month_num/12)
    return x

def forecast_region(sales, region='Maharashtra', product='Drug_A', horizon=6):
    df=sales[(sales.region==region)&(sales.drug==product)][['month','units_sold']].sort_values('month').copy()
    feat=make_features(df).dropna().reset_index(drop=True)
    cols=[c for c in feat.columns if c not in ['month','units_sold']]
    model=HistGradientBoostingRegressor(max_iter=250,learning_rate=.06,max_leaf_nodes=12,l2_regularization=1.0,random_state=42)
    model.fit(feat[cols],feat.units_sold)
    history=df.copy()
    preds=[]
    for _ in range(horizon):
        next_month=history.month.max()+pd.offsets.MonthBegin(1)
        row={'month':next_month}
        temp=history[['month','units_sold']].copy()
        temp.loc[len(temp)]=[next_month,np.nan]
        f=make_features(temp).iloc[-1].copy()
        f['time_index']=len(history)
        f['month_num']=next_month.month
        f['sin_month']=np.sin(2*np.pi*next_month.month/12)
        f['cos_month']=np.cos(2*np.pi*next_month.month/12)
        val=float(model.predict(pd.DataFrame([f[cols].to_dict()]))[0])
        val=max(0,val)
        preds.append([next_month,round(val)])
        history.loc[len(history)]=[next_month,val]
    return pd.DataFrame(preds,columns=['month','forecast_units'])

def forecast_all(sales,horizon=6):
    rows=[]
    for r in sorted(sales.region.unique()):
        f=forecast_region(sales,r,'Drug_A',horizon)
        f['region']=r; rows.append(f)
    return pd.concat(rows,ignore_index=True)
