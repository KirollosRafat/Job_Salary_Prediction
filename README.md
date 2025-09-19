# 💼 Job Salary Prediction

This project provides a machine learning model to predict employee salaries based on demographic and job-related features. The app is served via Streamlit with a pre-trained model, input features, and a dataset for training/testing.

---

## 📁 Repository Structure
Job_Salary_Prediction/
├── APP.py # Streamlit app that loads the model and offers UI for predictions
├── salary_model.joblib # Trained model saved using joblib
├── Salaries.csv # Dataset containing salary + features
├── Models.ipynb # Notebook for training, exploring or building the model
├── preparation.ipynb # Data preprocessing and feature engineering notebook
├── requirements.txt # Project dependencies

---

## 🧾 Data & Features

- **Salaries.csv**  
  The dataset used for training includes features such as:
  - Age  
  - Years of Experience  
  - Gender  
  - Education Level  
  - Job Title  
  - Salary (target)

- **Preparation.ipynb**  
  This notebook shows how the data was cleaned, preprocessed, perhaps how missing values are handled, encoding of categorical variables, etc.

- **Models.ipynb**  
  Contains experiments, model selection, possibly hyperparameter tuning, metrics, etc.

---

## 📊 Model Evaluation
Several regression models were trained and evaluated using GridSearchCV with cross-validation:

1. Linear Regression (with Polynomial Features)

Best hyperparameters: poly_deg__degree = 1 (Multiple-linear Regression)

Test Set R² Score: 85%

2. XGBoost Regressor

Tuned parameters: max_depth, n_estimators

Best parameters: max_depth = 3, n_estimators = 300

Test Set R² Score: 93%

3. Random Forest Regressor

Tuned parameters: max_depth, n_estimators

Best parameters: max_depth = 6, n_estimators = 45

Test Set R² Score: 86%

## 📌 Notes

R² Score was the evaluation metric to measure how well the models explain salary variance.

GridSearchCV ensured systematic hyperparameter tuning and robust performance estimates via cross-validation.

Based on the reported scores, the best-performing model was exported as salary_model.joblib and deployed in the Streamlit app.













