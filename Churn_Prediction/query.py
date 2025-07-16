# ### Import packages and data
from flask import Flask, request, jsonify
import pandas as pd
import pickle

model_file = 'Churn_Prediction_model_C=1.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)
    
app = Flask('Churn_Prediction')
@app.route('/predict',methods=['POST'])
def predict():
    customer = request.get_json()
    print("Received customer data:", customer)
    df = pd.DataFrame([customer])
    df.columns = df.columns.str.lower().str.replace(' ','_')
    df.totalcharges = pd.to_numeric(df.totalcharges,errors = 'coerce')
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
    result = {
        "Churn Probability": float(y_pred),
        "Churn Decision": bool(y_pred >= 0.5)       
    }
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0',port = 9601)
