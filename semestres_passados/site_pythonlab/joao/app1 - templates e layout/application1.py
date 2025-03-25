#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Projeto Aplicação Web

Professor: Álvaro Campos Ferreira
Contato: alvaro.ferreira@idp.edu.br
'''
import pandas as pd
from flask import Flask, render_template, request
from analise import get_data
from analise2 import get_data2
from analise3 import get_data3

data = get_data()
print(data)

data2=get_data2
print(data2)

data3=get_data3
print(data3)

netflix_data=pd.read_csv("static/archive/netflix_titles.csv")
netflix_data.head()

cientist_data=pd.read_csv("static/archive/ds_salaries.csv")
cientist_data.head()

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return render_template('index.html',name=name)

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/gosto")
def gosto():
    return render_template('gosto.html',data=data,cientist_data=cientist_data,netflix_data=netflix_data)

@app.route("/links")
def links():
    return render_template('links.html')

@app.route("/teste")
def teste():
    return render_template('teste.html')

@app.route("/recursos")
def recursos():
    return render_template('recursos.html')

@app.route("/pessoal")
def pessoal():
    return render_template('pessoal.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)