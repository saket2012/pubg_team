import warnings
from sklearn.ensemble import RandomForestRegressor
from joblib import dump


warnings.filterwarnings("ignore", category = DeprecationWarning)

# Training Random Forest model for 4 players team
def rf_model_squad(training_data, y):
    model = RandomForestRegressor(n_estimators = 100, min_samples_leaf = 2, min_samples_split = 3, max_features = 0.5,
                                  n_jobs = -1)
    model.fit(training_data, y)
    dump(model, 'rf_squad.joblib')
    return model

# Training Random Forest model for 2 players team
def rf_model_duo(training_data, y):
    print("training the model")
    model = RandomForestRegressor(n_estimators = 100, min_samples_leaf = 2, min_samples_split = 3, max_features = 0.5,
                                  n_jobs = -1)
    model.fit(training_data, y)
    dump(model, 'rf_duo.joblib')
    return model
