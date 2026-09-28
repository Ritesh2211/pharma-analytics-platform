from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

def segment_doctors(doctors, n_clusters=4):
    features=['monthly_patient_volume','digital_engagement','adoption_propensity']
    x=doctors[features].copy()
    x['monthly_patient_volume']=x['monthly_patient_volume'].clip(upper=x['monthly_patient_volume'].quantile(.99))
    z=StandardScaler().fit_transform(x)
    model=KMeans(n_clusters=n_clusters,n_init=20,random_state=42)
    labels=model.fit_predict(z)
    out=doctors.copy(); out['cluster']=labels
    profile=out.groupby('cluster')[features].mean().sort_values('monthly_patient_volume',ascending=False)
    mapping={c:name for c,name in zip(profile.index,['High-value specialists','Engaged growth targets','Broad-reach physicians','Low-priority physicians'])}
    out['segment']=out.cluster.map(mapping)
    return out,profile
