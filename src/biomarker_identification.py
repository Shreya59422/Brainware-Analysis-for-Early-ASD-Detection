import pandas as pd
import shap
import joblib

model = joblib.load("asd_model.pkl")

data = pd.read_excel("data/Dataset.xlsx")

features = [
"delta_F_sx","delta_F_dx",
"theta_F_sx","theta_F_dx",
"low_alpha_F_sx","low_alpha_F_dx",
"high_alpha_F_sx","high_alpha_F_dx",
"beta_F_sx","beta_F_dx",
"gamma_F_sx","gamma_F_dx"
]

X = data[features]

explainer = shap.Explainer(model)

shap_values = explainer(X)

shap.summary_plot(shap_values, X)
