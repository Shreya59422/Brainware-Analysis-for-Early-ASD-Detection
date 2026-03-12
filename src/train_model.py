import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

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

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

X_train, X_test, y_train, y_test = train_test_split(
X_resampled, y_resampled, test_size=0.2, random_state=42)

model = XGBClassifier(
n_estimators=100,
max_depth=4,
learning_rate=0.1
)

model.fit(X_train, y_train)

joblib.dump(model, "asd_model.pkl")

print("Model trained and saved.")
