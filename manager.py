from dataset import import_data, feature_engineering
from prediction import rf_squad, rf_duo
from model import rf_model_duo, rf_model_squad

#Train model for 4 players team using random forest
def train_rf_squad():
    dataset = import_data(None, True)
    x_train, y, feature_names = feature_engineering(dataset, 'squad-fpp', True)
    model = rf_model_squad(x_train, y)
    print("Model training completed successfully")
    print(model)

#Train model for 2 players team using random forest
def train_rf_duo():
    dataset = import_data(None, True)
    x_train, y, feature_names = feature_engineering(dataset, 'duo-fpp', True)
    model = rf_model_duo(x_train, y)
    print("Model training completed successfully")
    print(model)


#Prediction of winning placement for 4 players team using random forest
def ramdon_forest_squad(file):
    dataset = import_data(file, False)
    df, y, feature_names = feature_engineering(dataset, 'squad-fpp', False)
    ans = rf_squad(df)
    return ans


#Prediction of winning placement for 2 players team using random forest
def ramdon_forest_duo(file):
    dataset = import_data(file, False)
    df, y, feature_names = feature_engineering(dataset, 'duo-fpp', False)
    ans = rf_duo(df)
    return ans
