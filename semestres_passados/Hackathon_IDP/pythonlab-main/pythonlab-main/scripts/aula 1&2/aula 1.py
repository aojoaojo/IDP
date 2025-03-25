#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:57:43 2023

@author: mac-prof
"""
print("Olá, Mundo!")

# Variáveis simples

nome = "Xerxes"
print(nome+nome)

idade = 5
peso = 3.9

print(idade+peso)
print(peso+idade)

vacinado = True
print(vacinado)

# Estruturas de dados
# Listas
compras = ['leite','ração','petisco']
print(compras)
print(compras[0])
print(compras[1])
print(compras[2])
compras.append('fruta')
print(compras)
compras.pop(3)
print(compras)

# Dicionário
carro = {"marca":"Fiat","modelo":"Uno",
         "ano":"2012"}
print(carro)
print(carro["marca"])
print(carro["modelo"])
print(carro["ano"])

carro_2 = {"marca":"Honda","modelo":"WRV",
         "ano":"2020"}
print(carro_2)
print(carro_2["marca"])
print(carro_2["modelo"])
print(carro_2["ano"])

# Lista de carros
carros = [carro, carro_2]
print(carros[0]["marca"])
print(carros[1]["marca"])
































