# Brainwave Analysis for Early ASD Detection

## Overview
Autism Spectrum Disorder (ASD) is usually diagnosed through behavioral observations, which can be slow and subjective. Delayed diagnosis can result in missed opportunities for early intervention.

This project proposes an EEG-based machine learning approach for early ASD detection. EEG brainwave signals are analyzed using feature engineering and machine learning techniques to identify patterns associated with ASD.

The system uses an **XGBoost classifier** trained on EEG band power features and explains predictions using **SHAP (SHapley Additive Explanations)** to identify important neural biomarkers.

---

## Project Objectives

- Develop an EEG-based framework for early ASD detection  
- Train a machine learning model to classify ASD vs non-ASD  
- Handle class imbalance using SMOTE  
- Identify meaningful neural biomarkers from EEG data  
- Demonstrate explainable AI in neurological data analysis  

---

## Dataset

The dataset consists of EEG brainwave band power features collected from infant subjects.

Dataset source: **Zenodo.org (public EEG dataset)**

Number of samples: **383**

EEG frequency band features include:

- delta_F_sx  
- delta_F_dx  
- theta_F_sx  
- theta_F_dx  
- low_alpha_F_sx  
- low_alpha_F_dx  
- high_alpha_F_sx  
- high_alpha_F_dx  
- beta_F_sx  
- beta_F_dx  
- gamma_F_sx  
- gamma_F_dx  

Target variable:

Diagnosis_group  

- 0 → Non-ASD  
- 2 → ASD  

For machine learning training this was converted to:

- ASD = 1 → ASD detected  
- ASD = 0 → Non-ASD  

Dataset location:

```
data/Dataset.xlsx
```

---

## Methodology

The project follows a machine learning pipeline:

1. Data preprocessing  
2. Feature engineering  
3. Feature normalization using MinMaxScaler  
4. Class balancing using SMOTE  
5. Model training using XGBoost  
6. Hyperparameter tuning using GridSearchCV  
7. Model evaluation  
8. Biomarker identification using SHAP  
9. Model deployment for prediction  

---

## System Architecture

```
EEG Dataset
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Feature Scaling
      ↓
SMOTE Class Balancing
      ↓
XGBoost Model Training
      ↓
Model Evaluation
      ↓
SHAP Biomarker Identification
      ↓
ASD Prediction
```

Architecture diagram:

![Architecture](architecture.png)

---

## Repository Structure

```
Brainware-Analysis-for-Early-ASD-Detection
│
├── data/
│   └── Dataset.xlsx
│
├── src/
│   ├── train_model.py
│   ├── test_model.py
│   ├── biomarker_identification.py
│   └── predict.py
│
├── docs/
│   ├── project_description.md
│   ├── data_description.md
│   └── model_description.md
│
├── README.md
├── requirements.txt
├── architecture.png
├── demo_video_link.txt
└── setup_instructions.md
```

---

## Model Training

The model used for classification is **XGBoost**, a gradient boosting algorithm suitable for structured tabular data.

Training pipeline includes:

- EEG feature selection  
- MinMax feature scaling  
- SMOTE class balancing  
- XGBoost model training  

---

## Model Evaluation

The model performance is evaluated using the following metrics:

- Accuracy  
- Precision  
- Recall  
- F1 Score  
- ROC Curve  

---

## Biomarker Identification

SHAP explainable AI was used to analyze feature importance.

Key identified EEG biomarkers include:

- Elevated frontal **theta power**
- Differences in **delta band activity**
- **Frontal asymmetry** between left and right brain regions

These features strongly influence ASD prediction and may represent early neural indicators of ASD.

---

## Deployment

The trained model can be used to predict ASD risk using new EEG input values.

Run prediction using:

```
python src/predict.py
```

Input EEG features are provided through an Excel file.

---

## Requirements

Install required libraries using:

```
pip install -r requirements.txt
```

Main libraries used:

- pandas
- numpy
- scikit-learn
- xgboost
- imbalanced-learn
- shap
- matplotlib
- seaborn

---

## Demo Video

The demonstration video for this project is available in:

```
demo_video_link.txt
```

---

## Setup Instructions

Detailed setup instructions are provided in:

```
setup_instructions.md
```

---

## Team Members

- Nayana S P  
- Tejashwini S  
- Meghana M  
- Shreya Reddy S  

Mentor: **Miss. Lalli K**

---

## Conclusion

This project demonstrates how machine learning techniques can be used to analyze EEG brainwave data and support early ASD detection. The XGBoost model achieved strong classification performance, and SHAP analysis helped identify important EEG biomarkers contributing to the predictions.

Future improvements can include larger datasets and advanced deep learning models to further improve early ASD screening systems.
