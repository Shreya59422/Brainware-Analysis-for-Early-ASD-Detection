# Setup Instructions

Follow the steps below to run the Brainwave Analysis for Early ASD Detection project.

## 1. Clone the Repository

Clone the GitHub repository to your local system.

```
git clone https://github.com/yourusername/Brainware-Analysis-for-Early-ASD-Detection.git
```

Move into the project folder:

```
cd Brainware-Analysis-for-Early-ASD-Detection
```

---

## 2. Install Required Libraries

Install all required Python dependencies using:

```
pip install -r requirements.txt
```

---

## 3. Dataset Setup

Ensure the dataset file is placed in the following location:

```
data/Dataset.xlsx
```

---

## 4. Train the Model

Run the training script to train the XGBoost model:

```
python src/train_model.py
```

This will train the model and save it as:

```
asd_model.pkl
```

---

## 5. Test the Model

Evaluate the model performance using:

```
python src/test_model.py
```

This will display evaluation metrics such as accuracy, precision, recall and F1-score.

---

## 6. Biomarker Identification

Run SHAP analysis to identify important EEG biomarkers:

```
python src/biomarker_identification.py
```

This will generate feature importance visualizations showing which EEG signals influence ASD prediction.

---

## 7. Run Prediction (Deployment)

To predict ASD risk for new EEG inputs:

```
python src/predict.py
```

Input EEG values should be provided in the Excel file used for prediction.

---

## Software Requirements

- Python 3.8 or higher
- Libraries listed in `requirements.txt`
- Operating System: Windows / Linux / MacOS

---

## Development Environment

The project was developed using:

- Python
- Google Colab
- Scikit-learn
- XGBoost
- SHAP
- Pandas
- NumPy
```
