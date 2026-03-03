# HR Analytics: Predicting Employee Attrition for Salifort Motors

## Project Overview
This project applies predictive modeling to HR data to identify factors that lead to employee turnover at Salifort Motors. Using a dataset of ~15,000 employees, I conducted Exploratory Data Analysis (EDA) and built classification models to predict whether an employee is likely to quit.

The project follows the PACE (Plan, Analyze, Construct, Execute) framework.

## Repository Structure
```text
├── data/                       # HR_capstone_dataset.csv
├── notebooks/                  
│   └── 01_attrition_analysis_modeling.ipynb  
├── src/                        
│   ├── data_preprocessing.py    # Cleaning, renaming, and feature engineering
│   ├── visualizations.py       # Boxplots and attrition-by-department plots
│   ├── model_building.py       # Logistic Regression & Random Forest implementations
│   └── evaluation.py           # Confusion matrices and performance reports
├── README.md
├── requirements.txt            
└── .gitignore# 
```

## Key Findings & Business Impact
* Top Predictors: Satisfaction level, number of projects, and tenure were the strongest indicators of attrition.

* Model Performance: The Random Forest model (with balanced class weights) provided the highest F1-score and Recall, which is critical for HR to catch potential leavers before they quit.

* Recommendations: Identified a "critical tenure period" (4-6 years) where high-performing employees are most likely to leave, suggesting a need for career development intervention.

## How to Run
1. Clone the repository.

2. Install dependencies: pip install -r requirements.txt.

3. Run the notebook in the notebooks/ directory.