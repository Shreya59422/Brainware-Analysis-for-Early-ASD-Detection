import pandas as pd
import joblib

model = joblib.load("asd_model.pkl")

input_data = pd.read_excel("asd_eeg_input_template.xlsx")

prediction = model.predict(input_data.values)

print("ASD Prediction:", prediction)
