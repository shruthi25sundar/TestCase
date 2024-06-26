# Function to handle outliers
def handle_outliers(train):
    Q1 = train['turnover'].quantile(0.25)
    Q3 = train['turnover'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers_before = train[(train['turnover'] < lower_bound) | (train['turnover'] > upper_bound)].shape[0]
    train['turnover_capped'] = train['turnover'].clip(lower=lower_bound, upper=upper_bound)
    outliers_after = train[(train['turnover'] != train['turnover_capped'])].shape[0]

    print(f'Number of outliers before capping: {outliers_before}')
    print(f'Number of outliers after capping: {outliers_after}')

    return train