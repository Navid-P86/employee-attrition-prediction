import pandas as pd

def clean_hr_data(df):
    """
    Cleans the Salifort Motors HR dataset: renames columns, 
    removes duplicates, and handles specific column formatting.
    """
    # 1. Rename columns (fixing typos like 'montly')
    df = df.rename(columns={
        'average_montly_hours': 'average_monthly_hours',
        'time_spend_company': 'tenure',
        'Department': 'department'
    })

    # 2. Remove duplicates
    df = df.drop_duplicates(keep='first')

    # 3. Create 'overworked' feature (from your Construction phase)
    # Definition: average_monthly_hours > 175 AND satisfaction < 0.5
    df['overworked'] = 0
    df.loc[(df['average_monthly_hours'] > 175) & (df['satisfaction_level'] < 0.5), 'overworked'] = 1
    
    return df