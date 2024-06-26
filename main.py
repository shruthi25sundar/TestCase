from load_data import load_data, load_test_data
from preprocess_data import preprocess_data
import explore_data 

from handle_outliers import handle_outliers
from modeling import modeling
from forecast import forecast

def main_train_pipeline(train_path, feat_path):
    # Load train data
    train, feat = load_data(train_path, feat_path)

    # Data preprocessing
    train = preprocess_data(train)


    #a. Which department made the highest turnover in 2016?
    explore_data.department_2016(train)

    #b.What are the top 5 week numbers (1 to 53) for department 88 in 2015 in terms of turnover over all stores?

    explore_data.department88_2015(train)

    #c. What was the top performer store in 2014?

    explore_data.performerstore_2014(train)

    #dBased on sales can you guess what kind of sport represents departement 73?
    explore_data.sportdepartment73(train)

    #e. Based on sales can you guess what kind of sport represents departement 117?
    explore_data.sportdepartment117(train)

    #f.f. What other insights can you draw from the data? Provide plots and figures ifneeded.


    explore_data.geographical_analysis(train, feat)
    explore_data.seasonal_trends(train)
    explore_data.correlation_analysis(train,feat)

    # Handle outliers
    train = handle_outliers(train)

    # Modeling
    model = modeling(train)

    return model

def main_forecast_pipeline(test_path):
    # Load test data
    test = load_test_data(test_path)

    # Data preprocessing
    test = preprocess_data(test)

    # Forecast future values
    forecasted_test = forecast(test)
    print(forecasted_test.head())

if __name__ == '__main__':
    train_path = r'train.csv'
    test_path = r'test.csv'
    feat_path = r'bu_feat.csv'

    main_train_pipeline(train_path, feat_path)
    main_forecast_pipeline(test_path)
