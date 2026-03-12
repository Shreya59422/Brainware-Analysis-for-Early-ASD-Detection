# Model Description

## Machine Learning Model

This project uses the XGBoost classifier to detect Autism Spectrum Disorder from EEG features.

XGBoost is a gradient boosting algorithm that builds multiple decision trees sequentially to improve prediction accuracy.

## Model Training Steps

1. EEG features were selected from the dataset
2. Missing values in the target variable were removed
3. The ASD label was created from the diagnosis group
4. Feature scaling was applied using MinMaxScaler
5. SMOTE was used to balance the dataset
6. The dataset was split into training and testing sets
7. XGBoost model was trained on the training dataset

## Model Evaluation

The trained model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## Biomarker Identification

SHAP (SHapley Additive exPlanations) was used to identify important EEG features contributing to ASD prediction.

These important features can be considered potential EEG biomarkers.
