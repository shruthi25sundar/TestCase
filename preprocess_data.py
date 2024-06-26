import pandas as pd

def preprocess_data(df):
    df['day_id'] = pd.to_datetime(df['day_id'])
    df['year'] = df['day_id'].dt.year
    df['month'] = df['day_id'].dt.month
    df['week'] = df['day_id'].dt.isocalendar().week
    return df