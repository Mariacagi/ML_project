from flask import Flask, request, render_template
import pandas as pd
import os
import sys
import numpy as np
import json

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

from data.listas_recorrer import lista_recorrer_Platform, lista_recorrer_Genre, lista_recorrer_Publisher
from src.utils.apis_tb import funcion_pred

with open(root_path + '/data/dicc_Genre.json') as f:
  data_genre = json.load(f)

# data_genre_dict = json.loads(data_genre)

with open(root_path + '/data/dicc_Platform.json') as z:
  data_platform = json.load(z)

# data_platform_dict = json.loads(data_platform)

with open(root_path + '/data/dicc_Publisher.json') as y:
  data_publisher = json.load(y)

# data_publisher_dict = json.loads(data_publisher)

# print("###########", data_genre_dict.get("Sports"))


app = Flask(__name__)

@app.route("/")
def home():
    Genre_list = lista_recorrer_Genre
    Platform_list = lista_recorrer_Platform
    Publisher_list = lista_recorrer_Publisher
    return render_template("upload.html", Genre_list = Genre_list, Platform_list=Platform_list, Publisher_list= Publisher_list)


@app.route("/upload_form", methods = ['POST', 'GET'])
def upload_form():
    if request.method == 'POST':
        genre_res = request.form['Genre']
        array_elegido_genre = np.array(data_genre[genre_res])

        platform_res= request.form['Platform']
        array_elegido_platform = np.array(data_platform[platform_res])
        
        publisher_res = request.form['Publisher']
        array_elegido_publisher = np.array(data_publisher[publisher_res])

        para_predecir = np.concatenate((array_elegido_genre, array_elegido_platform, array_elegido_publisher), axis=None)
        print("array:", para_predecir)
        X = para_predecir.reshape(1,-1)
        print(X.shape)
    return json.dumps(funcion_pred(X)) #modificar

if __name__ == '__main__':
    app.run(debug=True)