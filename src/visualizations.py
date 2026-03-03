import seaborn as sns
import matplotlib.pyplot as plt

def plot_tenure_outliers(df):
    """Generates a boxplot to visualize outliers in tenure."""
    plt.figure(figsize=(6, 2))
    sns.boxplot(x=df['tenure'])
    plt.title('Tenure Boxplot (Checking for Outliers)')
    plt.show()

def plot_attrition_by_dept(df):
    """Plots employee attrition counts by department."""
    plt.figure(figsize=(11, 8))
    sns.countplot(data=df, x='department', hue='left')
    plt.title('Employee Attrition by Department')
    plt.xticks(rotation=45)
    plt.show()