import pandas as pd

def load_data(train_path, feat_path):
    #Load the train data 
    train = pd.read_csv(train_path)
    #Load store and region information 
    feat = pd.read_csv(feat_path)
    return train, feat

def load_test_data(test_path):
    test = pd.read_csv(test_path)
    return test