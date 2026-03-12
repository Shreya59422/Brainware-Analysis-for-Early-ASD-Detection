import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_excel("data/Dataset.xlsx")

data = data.dropna(subset=["Diagnosis_group"])

data["ASD"] = (data["Diagnosis_group"] == 2).astype(int)

features = [
"delta_F_sx","delta_F_dx",
"theta_F_sx","theta_F_dx",
"low_alpha_F_sx","low_alpha_F_dx",
"high_alpha_F_sx","high_alpha_F_dx",
"beta_F_sx","beta_F_dx",
"gamma_F_sx","gamma_F_dx"
]

X = data[features]
y = data["ASD"]

model = joblib.load("asd_model.pkl")

predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)

print("Accuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y, predictions))
