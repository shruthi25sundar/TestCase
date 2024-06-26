import joblib
import pandas as pd


def forecast(test):
    features = ['but_num_business_unit', 'dpt_num_department', 'year', 'month', 'week']
    X_test = test[features]
    
    # Load the saved model
    model = joblib.load('xgb_model.pkl')
    
    # Make predictions
    test_predictions = model.predict(X_test)
    test_predictions_series = pd.Series(test_predictions, name='predicted_turnover')
    test_with_predictions = pd.concat([test, test_predictions_series], axis=1)
    
    return test_with_predictions
