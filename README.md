# 🏦 Bank Customer Churn Prediction Platform

An end-to-end Machine Learning application designed to predict whether a bank customer is likely to churn.

The project combines **Data Science, Machine Learning, FastAPI, Streamlit, and database integration** to transform a trained churn prediction model into an interactive application.

---

## 📌 Project Overview

Customer churn is an important business problem for banks because losing customers can negatively affect revenue and long-term customer relationships.

The objective of this project is to develop a Machine Learning solution capable of predicting customer churn based on customer information such as:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Account Balance
- Number of Products
- Credit Card Status
- Active Membership
- Estimated Salary

The system produces:

- **Churn Prediction**
- **Churn Probability**
- **Risk Level**

---

## 🎯 Project Objectives

The main objectives of this project are to:

1. Explore and understand bank customer data.
2. Identify patterns associated with customer churn.
3. Prepare the dataset for Machine Learning.
4. Train and compare classification models.
5. Select an appropriate model for prediction.
6. Save the trained Machine Learning model.
7. Build an API for making predictions.
8. Develop an interactive web application.
9. Store prediction results for further analysis.

---

## 📊 Dataset

The project uses the **Churn Modelling** dataset.

The dataset contains information about bank customers and whether they exited the bank.

### Main features

| Feature | Description |
|---|---|
| CreditScore | Customer credit score |
| Geography | Customer's country |
| Gender | Customer gender |
| Age | Customer age |
| Tenure | Number of years with the bank |
| Balance | Customer account balance |
| NumOfProducts | Number of bank products |
| HasCrCard | Whether the customer has a credit card |
| IsActiveMember | Whether the customer is an active member |
| EstimatedSalary | Estimated customer salary |
| Exited | Target variable indicating customer churn |

---

## 🔍 Data Preprocessing

The following preprocessing steps were performed:

- Dataset inspection
- Missing-value checking
- Duplicate checking
- Removal of irrelevant identifiers
- Categorical variable encoding
- Train/test split
- Feature scaling
- Class-imbalance analysis using SMOTE

The following columns were removed because they are identifiers rather than predictive customer characteristics:

```text
RowNumber
CustomerId
Surname
