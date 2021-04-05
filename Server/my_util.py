import json
import pickle
import numpy as np

__location = None
__data_column = None
__model = None


def load_artifacts():
    global __data_column
    global __model
    global __location
    with open('Artifacts/columns.json', 'r') as f:
        __data_column = json.load(f)['data_columns']

    __location = __data_column[3:]

    with open("Artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading is done")


def predict_house_price(total_sqft, bath, bhk, location):
    load_artifacts()
    try:
        loc_index = __location.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_column))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >=0:
        x[loc_index]=1
    else:
        x[loc_index] = -1
    return np.round(__model.predict([x])[0],2)

def get_location():
    load_artifacts()
    return __location


if __name__ == '__main__':
    load_artifacts()
    #print(get_location())




