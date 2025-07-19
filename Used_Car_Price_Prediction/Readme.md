## 🚗 Used Car Price Prediction — Linear Regression with NumPy & Pandas

This project implements a **Linear Regression model from scratch** (no ML libraries like `scikit-learn` or `statsmodels`) 
to predict the **selling price of used cars** using structured data. The goal is to understand how machine learning works 
internally, focusing on:

- Manual implementation of linear regression  
- End-to-end data processing  
- Feature engineering  
- Evaluation using RMSE

---

## 🧠 Problem Overview

The dataset contains attributes such as:
- Manufacturing year
- Transmission type
- Mileage
- engine details

The goal is to estimate the **market value** of a used car based on these features using numerical and selected 
categorical variables.

---

## 📊 What Makes This Project Unique

✅ Built entirely **without ML libraries**  
✅ Includes **data cleaning**, **EDA** and **train/validation/test splitting**  

---

## ⚙️ Tech Stack

| Category        | Tools Used       |
|-----------------|------------------|
| Language        | Python           |
| Libraries       | NumPy, Pandas    |
| Modeling        | Manual Linear Regression |
| Format          | Jupyter Notebook |
| Data Source     | `data.csv`       |

---

## 📈 Project Flow

1. **Import and Clean Data**  
   Load CSV, handle missing values and convert data types.

2. **EDA**  
   Explore price distributions, correlations and feature relevance.

3. **Feature Engineering**  
   Encode selected categorical variables manually and normalize numerical ones.

4. **Train/Val/Test Split**  
   60-20-20 ratio split done manually for stability evaluation.

5. **Model Training (Manual)**  
   - Linear regression using matrix operations  
   - No `LinearRegression()`, everything built with `np.dot()` and algebra

6. **Evaluation**  
   - RMSE used as error metric  
   - Generalization quality measured across validation and test sets

---


