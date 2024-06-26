
# Training and Forecasting Pipeline

This repository contains scripts to preprocess training data, explore insights, handle outliers, model data, and forecast future values. The pipeline is designed to perform the following tasks:

## 1. Training Pipeline

### Files Included:
- `main.py`: Entry point script to execute the training and forecasting pipelines.
- `load_data.py`: Module for loading training and feature data.
- `preprocess_data.py`: Module for preprocessing data.
- `explore_data.py`: Module for exploring data insights.
- `handle_outliers.py`: Module for handling outliers in the data.
- `modeling.py`: Module for building and training models.
- `forecast.py`: Module for forecasting future values.

### Steps:
1. **Loading Data:**
   - Uses `load_data()` function from `load_data.py` to load training data (`train.csv`) and feature data (`bu_feat.csv`).

2. **Data Preprocessing:**
   - Utilizes `preprocess_data()` function to clean and preprocess the training data.

3. **Exploratory Data Analysis:**
   - Various functions from `explore_data.py` are employed to analyze the dataset:
     - `department_2016()`: Identifies the department with the highest turnover in 2016.
     - `department88_2015()`: Lists the top 5 week numbers for department 88 in 2015 based on turnover.
     - `performerstore_2014()`: Identifies the top performing store in 2014.
     - `sportdepartment73()`: Analyzes which sport department (department 73) might represent based on sales.
     - `sportdepartment117()`: Analyzes which sport department (department 117) might represent based on sales.
     - `geographical_analysis()`: Visualizes turnover by region using geographical features.
     - `seasonal_trends()`: Plots seasonal trends of sales turnover on a monthly and weekly basis.
     - `correlation_analysis()`: Performs correlation analysis between sales turnover and geographical features.

4. **Outlier Handling:**
   - Implements `handle_outliers()` to handle outliers in the training data.

5. **Modeling:**
   - Applies `modeling()` function from `modeling.py` to build and train models using the preprocessed data.

### Outputs:
- Insights from exploratory data analysis.
- Trained model ready for deployment.

## 2. Forecasting Pipeline

### Steps:
1. **Loading Test Data:**
   - Uses `load_test_data()` function from `load_data.py` to load test data (`test.csv`).

2. **Data Preprocessing:**
   - Applies `preprocess_data()` function to clean and preprocess the test data.

3. **Forecasting:**
   - Uses `forecast()` function from `forecast.py` to predict future values based on the trained model.

### Outputs:
- Forecasted values for test data (`test.csv`).

