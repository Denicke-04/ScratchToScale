# 👕 Cloth Classification — Vision Model with TFLite, Docker & AWS Deployments

This project classifies images of clothing items using a deep learning model based on **transfer learning**. 
It focuses on building a lightweight, production-ready image classifier and deploying it across **AWS Lambda**, 
**Kubernetes (EKS)** and **TensorFlow Serving via Docker Compose**.

---

## 🧠 Problem Overview

Given an input image of a clothing item (e.g., shirt, pants), the model predicts its class.  
It demonstrates the full ML lifecycle:
- Data preprocessing
- Transfer learning using `Xception`
- TFLite model export for edge deployment
- REST API serving with Flask
- Deployment across multiple production-grade environments

---

## ⚙️ Tech Stack

| Component        | Tools Used                          |
|------------------|-------------------------------------|
| Model Training   | TensorFlow, Keras, Xception         |
| Optimization     | TensorFlow Lite (TFLite)            |
| Serving API      | Flask                               |
| Deployment       | Docker, Docker Compose, AWS Lambda, EKS |
| Testing & Data   | Custom script, structured image folders |

---

## 🧪 Model Details

- **Base Model**: Pretrained `Xception` network
- **Fine-tuned on**: Custom clothing dataset (train/validation/test folders)
- **Exported to**: `.tflite` for lightweight inference
- Achieved **~88% accuracy** on test images

---

## 🚀 Deployment Options

### ☁️ 1. AWS Lambda (Serverless)

- Lambda function handler: lambda_function.py
- Packaged as a **Docker container image** for Lambda deployment
- Optimized for minimal cold start
- Lightweight and fast
- Ideal for on-demand classification (e.g., mobile uploads or API gateways)

### 📦 2. [TensorFlow Serving (Docker Compose + API Gateway)](./Tf_Serving_Docker_Compose)

- Production-grade setup using **two Docker containers**:
  - **Flask API Gateway** (custom): handles image download, preprocessing, gRPC request formatting, and class decoding
  - **TensorFlow Serving** (official image): loads and serves the exported `.tflite` model via gRPC
- Uses `docker-compose.yml` to orchestrate both services and ensure seamless communication
- gRPC-based high-performance inference, triggered via REST calls to the Flask API

> This setup simulates a real-world microservice architecture and is ideal for scalable, container-native ML inference.

### ☸️ 3. [Kubernetes (EKS)](./EKS_Model_Deployment)

- Deployed as **two containers** in the same cluster:
  - A Flask-based **API Gateway** container for user-facing REST requests
  - A **TensorFlow Serving** container for high-performance gRPC model inference
- Services defined in:
  - `gateway-deployment.yaml` + `gateway-service.yaml` → **Exposed to the public** for client interaction
  - `model-deployment.yaml` + `model-service.yaml` → **Internal-only**, accessible from the gateway via gRPC
- All components are orchestrated using `eks-config.yaml` and Helm-style resource management

> This architecture separates user interaction from model inference and follows modern microservice best practices using service discovery within the EKS cluster.

