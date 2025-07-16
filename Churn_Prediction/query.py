# ### Import packages and data
print("Importing Packages...")
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.feature_extraction import DictVectorizer
import warnings
from sklearn.exceptions import ConvergenceWarning
import pickle

model_file = 'Churn_Prediction_model_C=1.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

customer = {
 'gender': 'Female',
 'SeniorCitizen': 0,
 'Partner': 'Yes',
 'Dependents': 'No',
 'tenure': 3,
 'PhoneService': 'Yes',
 'MultipleLines': 'Yes',
 'InternetService': 'Fiber optic',
 'OnlineSecurity': 'No',
 'OnlineBackup': 'No',
 'DeviceProtection': 'Yes',
 'TechSupport': 'No',
 'StreamingTV': 'Yes',
 'StreamingMovies': 'Yes',
 'Contract': 'Month-to-month',
 'PaperlessBilling': 'Yes',
 'PaymentMethod': 'Electronic check',
 'MonthlyCharges': 10.5,
 'TotalCharges': '470.1',
 }
print("Cleaning Data...")
df = pd.DataFrame([customer])
df.columns = df.columns.str.lower().str.replace(' ','_')
df.totalcharges = pd.to_numeric(df.totalcharges,errors = 'coerce')
numericals = ['tenure', 'monthlycharges', 'totalcharges']
categorical = ['gender', 'partner', 'dependents',
       'phoneservice', 'multiplelines', 'internetservice',
       'onlinesecurity', 'onlinebackup', 'deviceprotection', 'techsupport',
       'streamingtv', 'streamingmovies', 'contract', 'paperlessbilling',
       'paymentmethod']
for c in categorical:
    df[c] = df[c].str.lower().str.replace(' ','_')
customer = df.to_dict(orient='records')[0]
x = dv.transform([customer])
y_pred = model.predict_proba(x)[:, 1]
print("input: ", customer)
print(f"Churn probability: {y_pred[0]:.3f}")