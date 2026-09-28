import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px
ROOT=Path(__file__).resolve().parents[1]; P=ROOT/'data/processed'
st.set_page_config(page_title='Pharma Decision Analytics',layout='wide')
st.title('Pharma Commercial Decision Analytics')
st.caption('Synthetic portfolio case study | Drug_A | India | All numbers are simulated')
market=pd.read_csv(P/'market_opportunity.csv'); seg=pd.read_csv(P/'doctor_segments.csv'); fc=pd.read_csv(P/'demand_forecast.csv'); price=pd.read_csv(P/'pricing_scenarios.csv'); launch=pd.read_csv(P/'launch_scenarios.csv')

st.sidebar.header('Decision filters')
region=st.sidebar.selectbox('Region', ['All']+sorted(market.region.tolist()))
if region!='All': market_view=market[market.region==region]; fc_view=fc[fc.region==region]; launch_view=launch[launch.region==region]
else: market_view=market; fc_view=fc; launch_view=launch

c1,c2,c3,c4=st.columns(4)
c1.metric('Treated market',f"{market_view.treated_patients.sum()/1e6:.2f}M")
c2.metric('6M forecast units',f"{fc_view.forecast_units.sum()/1e3:.1f}K")
c3.metric('Base forecast revenue',f"₹{(launch_view.base_revenue_inr.sum()/1e6):.1f}M")
c4.metric('Top opportunity',str(market_view.sort_values('opportunity_score',ascending=False).iloc[0].region))

st.subheader('1. Market opportunity')
st.plotly_chart(px.bar(market_view.sort_values('opportunity_score',ascending=True),x='opportunity_score',y='region',orientation='h',text='opportunity_score',title='Opportunity score: market size + growth'),use_container_width=True)

st.subheader('2. Demand forecast')
plot_fc=fc_view.copy(); plot_fc['month']=pd.to_datetime(plot_fc.month)
st.plotly_chart(px.line(plot_fc,x='month',y='forecast_units',color='region',markers=True,title='Next 6 months — Drug_A demand forecast'),use_container_width=True)

st.subheader('3. Physician segmentation')
seg_counts=seg.groupby('segment').size().reset_index(name='physicians').sort_values('physicians',ascending=False)
st.plotly_chart(px.bar(seg_counts,x='segment',y='physicians',title='Physician segments'),use_container_width=True)

st.subheader('4. Pricing scenario')
st.plotly_chart(px.line(price,x='price_inr',y='expected_revenue_inr',markers=True,title='Price vs expected revenue'),use_container_width=True)
st.dataframe(price,use_container_width=True,hide_index=True)

st.subheader('5. Launch scenario range')
show=launch_view[['region','treated_patients','growth_pct','forecast_units','base_revenue_inr','low_adoption_revenue_inr','high_adoption_revenue_inr']].copy()
st.dataframe(show.sort_values('forecast_units',ascending=False),use_container_width=True,hide_index=True)

st.subheader('Executive interpretation')
top=market.sort_values('opportunity_score',ascending=False).head(3).region.tolist()
st.markdown(f'''**Decision frame:** prioritize commercial capacity where addressable patient volume and growth combine to create the largest opportunity. In this synthetic case, the highest composite opportunity regions are **{', '.join(top)}**.\n\n**Action:** use the physician segmentation to focus field activity on high-value specialists and engaged growth targets; use the forecast as a planning baseline; and treat pricing as a scenario rather than a single-point answer.\n\n**Caveat:** this is a portfolio demonstration using synthetic data, not a real market recommendation.''')
