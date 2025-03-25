#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:21:58 2023

@author: mac-prof
"""
nome_do_morador = "Xerxes"
apartamento = 106
aluguel = 1775.50
condomino = True 

pessoas = ["Álvaro", 
           "Guilherme", 
           "Pedro"]
print(pessoas[0])
print(pessoas[1])
print(pessoas[2])

pessoa = {"nome" : "Álvaro"}
print(pessoa["nome"])
def cadastrar():
    """
    Cadastro de condominos
    
    RETURN: lista de condominos cadastrados
    """
    condominos = []
    continuar = True
    while continuar:
        nome = input("nome: ")
        apartamento = int(input("apartamento: "))
        aluguel = float(input("aluguel: "))
        condominio = bool(input("condominio: "))
        continuar = input("continuar? ")
        if continuar == "Não":
            continuar = False
        else:
            continuar = True
        condomino = {"nome" : nome,
                     "apartamento" : apartamento,
                     "aluguel" : aluguel,
                     "condominio" : condominio}
        condominos.append(condomino)
    for pessoa in condominos:
        print(pessoa["nome"])
        if pessoa["condominio"]:
            print("é condômino")
        else:
            print("não é condômino")
    return condominos

#pessoas = cadastrar()

def somar_numeros(a,b):
    soma = a + b
    print(soma)
    return soma

resultado = somar_numeros(10239,123497)
imagem = "po-para-sorvete-acai-du-porto-200g-2928f0fa4c3d0032c855441bec5635fc.png"
from skimage import io
import matplotlib
img = io.imread(imagem)
matplotlib.pyplot.imshow(img[100:400,250:400,:])





















