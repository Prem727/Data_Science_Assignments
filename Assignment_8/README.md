# Assignment 8 - Logistic Regression

## Diabetes Prediction

### Objective

The objective of this assignment is to build a Logistic Regression model to predict whether a patient has diabetes based on medical and demographic features.

## Dataset

The dataset contains the following features:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
- Outcome

The `Outcome` column is the target variable:

- `0` - No diabetes
- `1` - Diabetes

## Tasks Performed

### 1. Data Exploration

- Loaded the diabetes dataset using Pandas.
- Examined the dataset structure using `info()`.
- Calculated descriptive statistics using `describe()`.
- Checked data types.
- Checked missing values and duplicate records.

### 2. Exploratory Data Analysis

The following visualizations were created:

- Outcome distribution
- Histograms
- Box plots
- Correlation heatmap
- Pair plot
- Feature-wise comparisons

### 3. Data Preprocessing

- Identified invalid zero values in selected medical features.
- Replaced invalid zero values with missing values.
- Filled missing values using median imputation.
- Removed duplicate records where applicable.
- Separated the independent variables from the target variable.
- Split the dataset into training and testing data using an 80:20 ratio.
- Standardized the numerical features using `StandardScaler`.

### 4. Logistic Regression

A Logistic Regression classification model was trained using the training dataset.

The model was used to predict diabetes outcomes on the test dataset.

### 5. Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC score
- Confusion Matrix
- ROC Curve

### 6. Feature Interpretation

The Logistic Regression coefficients and odds ratios were calculated to understand how the features influence the probability of diabetes.

Positive coefficients indicate an increase in the log-odds of diabetes, while negative coefficients indicate a decrease when other variables are held constant.

## Streamlit Deployment

The trained Logistic Regression model was deployed using Streamlit.

The Streamlit application allows users to enter patient information and receive a diabetes prediction along with the predicted probability.

The application was tested successfully in a local environment.

## Screenshots

### Before Prediction

The Streamlit application with patient input values entered before generating the prediction.

![Before Prediction](before_prediction.png)

### After Prediction

The Streamlit application displaying the predicted diabetes outcome and probability after clicking the Predict button.

![After Prediction](after_prediction.png)
