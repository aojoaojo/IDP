#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:54:51 2023

@author: mac-prof
"""
import pandas as pd
def cadastrar():
    continuar = True
    dados = {}
    dados_df = pd.read_excel("censo.xlsx")
    while continuar:
        nome = input("nome: ")
        idade = int(input("idade: "))
        moradores = int(input("n de moradores: "))
        animais = int(input("n de animais: "))
        dados["nome"] = nome
        dados["idade"] = idade
        dados["moradores"] = moradores
        dados["animais"] = animais
        continuar = bool(input("continuar? "))
        dados_df = dados_df.append(pd.Series(dados), ignore_index=True)
    #dados_df = pd.DataFrame(dados)
    dados_df.insert(0, 'index', dados_df.index)
    dados_df.to_excel("censo.xlsx", columns=["nome","idade","moradores","animais"],index=False)
    return dados_df

dados = cadastrar()














