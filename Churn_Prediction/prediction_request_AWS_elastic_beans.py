import requests
host = 'churn-service-env.eba-xz2deep2.us-west-2.elasticbeanstalk.com'
url = f'http://{host}/predict'
customer = {
 "gender": "Female",
 "SeniorCitizen": 0,
 "Partner": "Yes",
 "Dependents": "No",
 "tenure": 3,
 "PhoneService": "Yes",
 "MultipleLines": "Yes",
 "InternetService": "Fiber optic",
 "OnlineSecurity": "No",
 "OnlineBackup": "No",
 "DeviceProtection": "Yes",
 "TechSupport": "No",
 "StreamingTV": "Yes",
 "StreamingMovies": "Yes",
 "Contract": "Month-to-month",
 "PaperlessBilling": "Yes",
 "PaymentMethod": "Electronic check",
 "MonthlyCharges": 10.5,
 "TotalCharges": 31.5
 }
print(requests.post(url, json = customer).json())

