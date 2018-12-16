from joblib import  load

def rf_squad(test_data):
    model = load('rf_squad.joblib')
    rank = model.predict(test_data)
    rank = rank[0]
    rank = float("{0:.4f}".format(rank))
    return rank


def rf_duo(test_data):
    model = load('rf_duo.joblib')
    rank = model.predict(test_data)
    rank = rank[0]
    rank = float("{0:.4f}".format(rank))
    return rank
