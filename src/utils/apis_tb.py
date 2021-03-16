import os
import sys
import numpy as np
import pandas as pd
import json

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

from sklearn.decomposition import PCA
from pickle import load
from sklearn.linear_model import LinearRegression

model_load = open(root_path + "/data/Entrenamiento_pca.csv")
#model_load = open("ML_project\\data\\Entrenamiento_pca.csv")
numpy_array = np.loadtxt(model_load, delimiter=",")

# df = pd.read_csv("ML_project/src/to_submit.csv")

def funcion_pred(df):
    """ Leer el csv, aplicar get dummies y pca y hacer la predicción"""

    # df = encode_OneHot(df, "Platform")
    # df = encode_OneHot(df, "Genre")
    # df = encode_OneHot(df, "Publisher")
    to_pred = df
    to_pred = np.concatenate((numpy_array, df), axis=0)
    print("to_pred:", to_pred.shape)
    pca = PCA(n_components = 3)

    pca.fit(to_pred)
    to_pred = pca.fit_transform(to_pred)

    loaded_model = load(open(root_path + "/data/finalized_model.sav", "rb"))

    prediction = loaded_model.predict(to_pred)

    data = {}
    data['prediction_GLOBAL_SALES'] = prediction[-1][0]
    # print("############################", type(prediction))
    # prediction_json = json.dumps(data)

    return data
'''
arraymaria = np.zeros(621)
arraymaria[0] = 1
arraymaria[12] = 1
arraymaria[43] = 1

X = arraymaria.reshape(1,-1)

funcion_pred(X)
'''