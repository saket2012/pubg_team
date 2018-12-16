import numpy as np
import pandas as pd


def import_data(file, is_train):
    if is_train:
        # Import training data set
        data_frame = pd.read_csv("training_data/train_V2.csv", low_memory = False)
        # data_frame = pd.read_csv(file)
    else:
        # Import testing data set
        data_frame = pd.read_csv(file)
    return data_frame


# feature_engineering function will process the training dataset. Processing includes
# creating new features form existing ones, finding missing values, dropping unnecessary
# columns from the dataset.
def feature_engineering(data_frame, match_type, is_train):

    # Select match type
    if match_type == 'duo-fpp':
        data_frame = data_frame.loc[data_frame['matchType'] == 'duo-fpp']
    else:
        data_frame = data_frame.loc[data_frame['matchType'] == 'squad-fpp']

    data_frame['totalDistance'] = data_frame['rideDistance'] + data_frame["walkDistance"] + \
                                  data_frame["swimDistance"]

    # Target feature
    target_feature = 'winPlacePerc'
    features = list(data_frame.columns)
    # Remove unnecessary feature form the dataset
    features.remove("Id")
    features.remove("matchId")
    features.remove("groupId")
    features.remove("matchType")
    features.remove("rideDistance")
    features.remove("walkDistance")
    features.remove("swimDistance")
    features.remove("vehicleDestroys")

    y = None

    if is_train:
        y = np.array(data_frame.groupby(['matchId', 'groupId'])[target_feature].
                     agg('mean'), dtype = np.float64)
        features.remove(target_feature)

    agg = data_frame.groupby(['matchId', 'groupId'])[features].agg('mean')
    if is_train:
        df = agg.reset_index()[['matchId', 'groupId']]
    else:
        df = data_frame[['matchId', 'groupId']]

    df = df.merge(agg.reset_index(), suffixes = ["", ""], how = 'left',
                          on = ['matchId', 'groupId'])

    agg = data_frame.groupby(['matchId', 'groupId']).size().reset_index(name = 'group_size')
    df = df.merge(agg, how = 'left', on = ['matchId', 'groupId'])

    df.drop(["matchId", "groupId"], axis = 1, inplace = True)

    feature_names = list(df.columns)
    X = np.array(df, dtype = np.float64)
    del data_frame, agg, df

    return X, y, feature_names
