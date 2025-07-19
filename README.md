# 🧠 Machine Learning & AI Projects Portfolio

Welcome to my portfolio of end-to-end Machine Learning and AI projects. This repository is designed to showcase not just model-building but the full ML lifecycle from problem definition and training to deployment on scalable infrastructure using modern DevOps and MLOps tools.

Each project is independently packaged, containerized and deployed using production-grade technologies such as Docker, AWS Lambda, Elastic Beanstalk, Tensorflow Serving and EKS.

---

## 🚀 Featured Projects

### 📉 [Churn Prediction](./Churn_Prediction)
A classification project predicting customers who churn from a telecommunication system based on user activity and engagement.

**Key Features:**
- Trained using Logistic Regression with `scikit-learn`
- Dockerized for local deployment
- Deployed to **AWS Elastic Beanstalk**
- Includes:
  - Test scripts for local/remote inference
  - `Pipfile` for dependency management
  - Clean training and inference code (`.ipynb` + `.py`)

---

### 👕 [Cloth Classification](./Cloth_Classification)
A deep learning project for image classification using transfer learning and multi-platform deployment.

**Key Features:**
- Built with a pretrained **Xception** model
- Converted to **TensorFlow Lite** for lightweight serving
- Deployed in 3 ways:
  - **AWS Lambda** (serverless)
  - **TF Serving with Docker Compose**
  - **AWS EKS** (Kubernetes)
- Includes training notebooks and custom request scripts

---

### 🚗 [Used Car Price Prediction](./Used_Car_Price_Prediction_no_functions)
A regression project estimating the price of used cars from tabular data — built entirely from scratch.

**Key Features:**
- **Linear Regression implemented manually** using NumPy and Pandas
- No external ML libraries (`no scikit-learn`, `no TensorFlow`)
- Focused on mathematical correctness and algorithm design
- Notebook-based pipeline: EDA → preprocessing → training → evaluation

---

## 🛠 Tools & Technologies

| Category           | Tools / Libraries                            |
|--------------------|-----------------------------------------------|
| **Languages**       | Python, Bash                                 |
| **ML Libraries**    | Scikit-learn, TensorFlow, TFLite, Keras       |
| **Data Handling**   | Pandas, NumPy                                |
| **Model Serving**   | Flask, TensorFlow Serving, AWS Lambda        |
| **DevOps**          | Docker, Docker Compose, Kubernetes (EKS)     |
| **Cloud**           | AWS Elastic Beanstalk, Lambda, EKS           |
| **Infra Mgmt**      | Pipenv, Pipfile, requirements.txt            |

---

## 🧩 Repository Structure

```plaintext
From-Scratch-to-Scale/
├── Churn_Prediction/               # Classification + AWS Elastic Beanstalk + Docker
├── Cloth_Classification/           # Vision + Lambda + EKS + TensorFlow Serving
├── Used_Car_Price_Prediction_/     # Tabular regression with EDA + modeling
├── README.md                       # Main portfolio overview (this file)
