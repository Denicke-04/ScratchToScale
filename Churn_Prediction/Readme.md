## 📉 Churn Prediction — Logistic Regression with Flask & AWS

This project predicts customer churn based on behavioral and demographic features. It demonstrates an end-to-end 
machine learning workflow from training and packaging a model to deploying it as a REST API using **Flask**, **Docker**
and **AWS Elastic Beanstalk**.

---

## 🧠 Problem Overview

Customer churn — when users cancel or stop using a service is a major issue for subscription-based businesses.  
The goal of this project is to predict whether a customer is likely to churn based on inputs like:

- Contract type
- Monthly charges
- Tenure
- Service usage

---

## ⚙️ Tech Stack

| Area            | Tools Used                       |
|-----------------|----------------------------------|
| Model Training  | `scikit-learn`, `pandas`, `numpy` |
| API Framework   | `Flask`                          |
| Packaging       | `Docker`, `Pipenv`               |
| Deployment      | **AWS Elastic Beanstalk**        |
| Testing         | Python scripts |

---

## 🧪 Model Details

- **Algorithm**: Logistic Regression (`C=1.0`)
- **Library**: `scikit-learn`
- **Model File**: `Churn_Prediction_model_C=1.bin`
- Achieved ~**82% accuracy** on test data
- Clean, interpretable features and preprocessing

---

## 🚀 Deployment

### ✅ 1. Local Deployment (Flask + Docker)

Build and run the container locally:

```bash
docker build -t churn-prediction .
docker run -p 9696:9696 churn-prediction
```
Test with:

```bash
python prediction_request_localhost.py
```
---

### ☁️ 2. Cloud Deployment (AWS Elastic Beanstalk)

Deployed using:
- Dockerfile
- Pipfile and requirements.txt for clean dependency control
- AWS EB CLI or Web Console

Test with:

```bash
python prediction_request_AWS_elastic_beans.py
```
Update `url = ...` in the script to match your AWS endpoint.

---
