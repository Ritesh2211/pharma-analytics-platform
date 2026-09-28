import pandas as pd
from src.pricing import scenario_table
from src.segmentation import segment_doctors

def test_pricing_scenarios_have_positive_revenue():
    sales=pd.DataFrame({'drug':['Drug_A']*4,'avg_price_inr':[900,950,1000,1050],'units_sold':[110,105,100,95]})
    out=scenario_table(sales,base_price=1000,base_units=100,elasticity=-1)
    assert len(out)==9
    assert (out.expected_revenue_inr>0).all()

def test_segmentation_creates_four_segments():
    d=pd.DataFrame({'monthly_patient_volume':[100,200,300,400,500,600,700,800], 'digital_engagement':[.1,.2,.3,.4,.5,.6,.7,.8], 'adoption_propensity':[.1,.2,.3,.4,.5,.6,.7,.8]})
    out,_=segment_doctors(d,n_clusters=4)
    assert out.segment.notna().all()
    assert out.segment.nunique()==4
