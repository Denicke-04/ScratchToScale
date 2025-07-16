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

print("Reading Data...")
df= pd.read_csv('data.csv')

# ### Set parameters
C = 1
n_splits = 10
output_file = f"Churn_Prediction_model_C= {C}.bin"

# ### Data Cleaning
print("Cleaning Data...")
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
df.totalcharges = df.totalcharges.fillna(0)
df.churn = (df.churn == 'Yes').astype(int)

# ### Split data into Train, Validation and Test sets
print("Splitting into train,valid and test sets")
df_train_full,df_test = train_test_split(df,test_size = 0.2, random_state = 120)
df_train,df_val = train_test_split(df_train_full,test_size = 0.25, random_state =120) # test_size is 0.25 to get 20% of the full data
y_train = df_train.churn
y_val = df_val.churn
y_test = df_test.churn
del df_train['churn']
del df_val['churn']
del df_test['churn']


# ### Regularization parameter tuning with KFold Cross validation
def train(df_train,y_train,C):
    x_train = df_train.to_dict(orient = 'records')
    dv = DictVectorizer(sparse = False)
    x_train = dv.fit_transform(x_train)
    model = LogisticRegression(random_state = 120,C=C)
    model.fit(x_train,y_train)
    return dv,model

def predict(dv,model,df_val):
    x_val = df_val.to_dict(orient = 'records')
    x_val = dv.transform(x_val)
    y_pred = model.predict_proba(x_val)[:,1]
    return y_pred

print(f"performing cross validation with C = {C} and k = {n_splits}")
warnings.filterwarnings("ignore", category=ConvergenceWarning)
scores = []
kfold = KFold(n_splits = n_splits,shuffle = True, random_state = 120)
df_full_train = df_train_full.copy()
fold = 0
for train_idx,val_idx in (kfold.split(df_full_train)):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]
    y_train = df_train.churn.values
    y_val = df_val.churn.values
    del df_train['churn']
    del df_val['churn']
    dv,model = train(df_train,y_train,C)
    y_pred = predict(dv,model,df_val)
    auc = roc_auc_score(y_val,y_pred)
    scores.append(auc)
    print(f"auc on fold {fold} is {auc}")
    fold+=1
print(f'Reg_param = {C}: auc = {np.mean(scores) +- np.std(scores)}')


# ### Training the Final model
print("Training the final model on the full train set")
y_full_train = df_train_full.churn.values
del df_train_full['churn']
dv,model = train(df_train_full,y_full_train,C=0.01)
y_pred = predict(dv,model,df_test)
auc = roc_auc_score(y_test,y_pred)
acc = accuracy_score(y_test, (y_pred > 0.5).astype(int))
print("auc = ",auc)
print("accuracy = ",acc)


# ### Saving the model
with open(output_file,'wb') as f_out:
    pickle.dump((dv,model),f_out)
print(f"Model Saved to the path {output_file}")

