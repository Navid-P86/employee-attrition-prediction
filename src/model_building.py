import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def train_logistic_regression(X_train, y_train):
    """Fits a Logistic Regression model with the parameters from your notebook."""
    clf = LogisticRegression(random_state=42, max_iter=500)
    clf.fit(X_train, y_train)
    return clf

def train_random_forest(X_train, y_train):
    """Fits a Random Forest model using the 'balanced' class weight you specified."""
    rf = RandomForestClassifier(random_state=42, class_weight='balanced')
    rf.fit(X_train, y_train)
    return rf