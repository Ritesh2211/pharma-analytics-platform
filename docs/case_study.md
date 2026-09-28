
1. **Why this problem?**
Because Decision Analytics starts with a business decision, not a model.

2. **Why K-Means?**
The goal is to discover physician groups with similar commercial behavior. I standardized features because their scales differ.

3. **How did you choose four clusters?**
I profiled several cluster counts and selected a small, interpretable segmentation; in a production engagement I would support this with silhouette score plus business interpretability.

4. **Why gradient boosting for forecasting?**
It captures nonlinear relationships among lagged demand, trend and seasonality. I would benchmark it against naive/seasonal-naive and classical time-series models.

5. **How would you validate the forecast?**
Rolling-origin time-series backtesting using MAE, RMSE and MAPE/sMAPE, plus business error thresholds.

6. **What does price elasticity mean?**
It approximates the percentage change in demand associated with a 1% change in price, holding the modeled relationship constant.

7. **What are the biggest limitations?**
Synthetic data, simplified market assumptions, no causal identification, no payer/access constraints, and no external epidemiology or competitor events.

8. **What would you do with real data?**
Establish data definitions, reconcile sources, assess missingness/bias, create a forecasting hierarchy, validate assumptions with SMEs, and quantify uncertainty.

9. **How did you communicate the analysis?**
I separated model outputs from the decision narrative and built an executive dashboard plus a concise recommendation deck.

10. **What is the most important lesson?**
The model is not the deliverable. The deliverable is a defensible decision with transparent assumptions and measurable next actions.
