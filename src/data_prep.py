from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data/raw'; PROCESSED=ROOT/'data/processed'

def load_raw():
    out={}
    for p in RAW.glob('*.csv'):
        header=pd.read_csv(p,nrows=0).columns.tolist()
        out[p.stem]=pd.read_csv(p,parse_dates=['month'] if 'month' in header else None)
    return out

def build_market_summary(raw):
    m=raw['market'].copy()
    latest=m[m.month==m.month.max()].copy()
    latest['growth_pct']=latest.region.map({'Maharashtra':12.0,'Karnataka':16.0,'Gujarat':9.0,'Delhi NCR':6.0,'Tamil Nadu':11.0,'Telangana':18.0,'West Bengal':10.0,'Rajasthan':8.0})
    latest['opportunity_score']=(latest['treated_patients']/latest['treated_patients'].max()*50 + latest['growth_pct']/latest['growth_pct'].max()*50).round(2)
    return latest.sort_values('opportunity_score',ascending=False)

def build_doctor_features(raw):
    d=raw['doctors'].copy()
    d['volume_score']=d.monthly_patient_volume.rank(pct=True)
    d['engagement_score']=d.digital_engagement
    d['commercial_score']=(0.5*d.volume_score+0.3*d.engagement_score+0.2*d.adoption_propensity).round(4)
    d['priority_segment']=pd.cut(d.commercial_score,bins=[-0.01,.25,.50,.75,1.01],labels=['Low Opportunity','Developing','Growth','Strategic'])
    return d
