import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

def plot_confusion_matrix(model, X_test, y_test, model_name):
    """Generates and displays a confusion matrix."""
    preds = model.predict(X_test)
    cm = confusion_matrix(y_test, preds)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(values_format='')
    plt.title(f'Confusion Matrix: {model_name}')
    plt.show()

def get_feature_importances(model, feature_names):
    """Extracts and sorts feature importances for tree-based models."""
    importances = model.best_estimator_.feature_importances_
    data = pd.DataFrame({'feature': feature_names, 'importance': importances})
    return data.sort_values(by='importance', ascending=False)