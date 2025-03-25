#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:56:54 2023

@author: mac-prof
"""
import pandas as pd
dados = pd.read_excel("pokemon_data.xlsx")
print(dados['Name'][4:10])
print(dados.columns)
dados.info()
print(dados['Legendary'])
lendarios = dados[dados['Legendary']]
print(lendarios.count())
print(dados[dados["HP"] == 100])
print(dados[dados["HP"] > 150].mean())
print(dados.mean())
print(lendarios.mean())
print(dados.describe())
print(lendarios.describe())
print(dados.groupby("Type 1").count()["#"])
print(dados.groupby("Type 1").describe()["HP"])
print(dados.groupby("Legendary").describe()["Attack"])
print(dados.groupby("Legendary").describe()["Defense"])
# Raspagem de Dados

url = "https://en.wikipedia.org/wiki/Brazilian_diaspora"
diaspora = pd.read_html(url)
print(len(diaspora))
df1 = diaspora[1]
print(df1.describe())
























