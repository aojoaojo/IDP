#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:14:54 2023

@author: mac-prof
"""
nome_cliente = "Xerxes"
cliente_ativo = True # False
numero_compras = "16"
numero_compras = int(numero_compras)
carrinho_compras = []
# print(carrinho_compras)
carrinho_compras.append("sapatênis")
# print(carrinho_compras)
carrinho_compras.append("camisa social")
# print(carrinho_compras)
carrinho_compras.append("meias")
# print(carrinho_compras)
carrinho_compras.pop(0)
# print(carrinho_compras[1])
cliente = [nome_cliente,numero_compras,
           cliente_ativo,carrinho_compras]
# print(cliente[0])
# print(cliente[1])

cliente= {"nome":nome_cliente,
          "ativo":cliente_ativo,
          "n de compras": numero_compras}
# print(cliente["nome"])
# print(cliente["n de compras"])
cliente["carrinho"] = carrinho_compras
# print(cliente)
# print(carrinho_compras[0])
# print(carrinho_compras[1])
# for compra in carrinho_compras:
    # print(compra)
# print("Boas compras!")
# print("Xerxes" == "Calvin")
# print("Xerxes" == "Xerxes")
# print(5 == 5)
# print(5 > 15)
# print(5 < 15)
numero = 5
while numero < 10:
    # print(numero)
    numero = numero + 1
# print(numero)
# numero = 15
# if numero == 5:
#     print("O numero é 5.")
# else:
#     print("O número não é 5.")
def somar_numeros(n1,n2):
    print(n1,n2)
    soma = n1+n2
    print(soma)
    return soma
soma = somar_numeros(10,2)
print(soma)

def multiplicar_numeros(n1,n2):
    print(n1,n2)
    produto = n1*n2
    print(produto)
    return produto
resultado = multiplicar_numeros(10,2)
print(resultado)















