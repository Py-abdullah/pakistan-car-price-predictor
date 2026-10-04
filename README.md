# Pakistan Used Car Price Predictor

A machine learning application that predicts the estimated price of used cars in Pakistan based on key vehicle features such as year, mileage, engine size, location, and transmission.

## Overview

This project demonstrates an end-to-end machine learning workflow, from data preprocessing and exploratory analysis to model training, evaluation, and deployment through an interactive Streamlit application.

The project was developed using Python and Scikit-learn, with the trained model integrated into a user-friendly web interface.

## Key Features

- Used car price prediction in PKR
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Categorical feature encoding
- Machine learning model training
- Model evaluation using standard regression metrics
- Saved model using Joblib
- Interactive Streamlit web application

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and preprocessing |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data analysis |
| Joblib | Model serialization |
| Streamlit | Web application |

## Machine Learning

The project uses **Linear Regression** to estimate vehicle prices.

### Features

The model uses:

- **Year** — Manufacturing year of the vehicle
- **Mileage** — Distance driven in kilometers
- **Engine Size** — Engine capacity in cc
- **Location** — City where the vehicle is located
- **Transmission** — Automatic or Manual

Categorical variables are transformed using **One-Hot Encoding**, and preprocessing and prediction are handled through a Scikit-learn Pipeline.

## Model Performance

The current model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Results

| Metric | Score |
|---|---:|
| MAE | 245,545.59 PKR |
| RMSE | 296,182.64 PKR |
| R² | 0.9337 |

## Project Workflow

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Preprocessing
   ↓
Train / Test Split
   ↓
Linear Regression
   ↓
Model Evaluation
   ↓
Saved Model
   ↓
Streamlit Application
   ↓
Price Prediction
