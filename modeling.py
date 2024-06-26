from matplotlib import pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor
import joblib

def modeling(train):
    features = ['but_num_business_unit', 'dpt_num_department', 'year', 'month', 'week']
    X = train[features]
    y = train['turnover_capped']
    
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = XGBRegressor(
        objective='reg:squarederror',
        n_estimators=1000,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )
    
    eval_set = [(X_train, y_train), (X_val, y_val)]
    model.fit(X_train, y_train, 
              eval_set=eval_set,
              eval_metric=['rmse'],
              early_stopping_rounds=10,
              verbose=False)
    
    # Save the model to a file
    joblib.dump(model, 'xgb_model.pkl')

    # Get evaluation results
    evals_result = model.evals_result()

    # Extract training and validation RMSE from evals_result
    train_rmse = evals_result['validation_0']['rmse']
    val_rmse = evals_result['validation_1']['rmse']

    # Calculate R-squared for training and validation sets
    train_predictions = model.predict(X_train)
    val_predictions = model.predict(X_val)

    r2_train = r2_score(y_train, train_predictions)
    r2_val = r2_score(y_val, val_predictions)

    print(f'Training RMSE: {train_rmse[-1]:.4f}')
    print(f'Validation RMSE: {val_rmse[-1]:.4f}')
    print(f'Training R-squared: {r2_train:.4f}')
    print(f'Validation R-squared: {r2_val:.4f}')

    # Plotting training and validation RMSE
    epochs = range(len(train_rmse))
    plt.figure(figsize=(10, 6))
    plt.plot(epochs, train_rmse, 'b-', label='Training RMSE')
    plt.plot(epochs, val_rmse, 'r-', label='Validation RMSE')
    plt.xlabel('Number of Rounds')
    plt.ylabel('RMSE')
    plt.title('Training and Validation RMSE')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return model
