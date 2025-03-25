#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Hackathon IDP

Equipe: João Vitor Brandão, Rafael Nogueira, Lucas Rocha, João Victor Távora

'''

import flask
from flask import Flask, render_template, request, redirect, session

import requests

import pandas as pd


app = Flask(__name__)

   
@app.route("/")
def index():
    return render_template('index_inicial.html')

# @app.route("/carrinho/add", methods=['POST'])
# def adicionar_ao_carrinho():
#     produto_id = request.form.get('produto_id')
#     # Aqui você pode fazer o processamento adicional necessário, como consultar o banco de dados para obter os detalhes do produto com base no ID

#     # Adicione o item ao carrinho (isso pode ser armazenado em uma lista, banco de dados, etc.)
#     # Exemplo:
#     carrinho.append(produto_id)

#     return redirect(url_for('carrinho'))

# Defina uma classe para representar um item do carrinho
class CarrinhoItem:
    def __init__(self, produto_id, descricao, foto_url):
        self.produto_id = produto_id
        self.descricao = descricao
        self.foto_url = foto_url

carrinho_produtos = []

# Rota para adicionar um item ao carrinho
@app.route('/carrinho/add', methods=['POST'])
def adicionar_ao_carrinho():

    print(request.form)
    produto_id = request.form.get('produto_id')
    carrinho_produtos.append(produto_id)
    print(carrinho_produtos)
    # produto_id = request.form.get('produto_id')
    # descricao = request.form.get('descricao')
    # foto_url = request.form.get('foto_url')
    # url_for = request.form.get('url_for')
    # # Crie um objeto CarrinhoItem com as informações do produto
    # item = CarrinhoItem(produto_id, descricao, foto_url)

    # Adicione o item ao carrinho
    # carrinho.append(item)

    return redirect('/cardapio')

@app.route("/cardapio")
def cardapio():
    name = request.args.get("name")
    url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
    caminho = '/api/cliente/categorias'
    r = requests.get(url+caminho)
    
    resposta = r.json()
    # print(resposta)
    if request.method == 'POST':
         return render_template('cardapio.html',name=name,resposta=resposta,categoria_post=request.form['categoria'])
    return render_template('cardapio.html',name=name,resposta=resposta)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        passw = request.form['password']
        
        url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
        caminho = '/api/cliente/usuarios'
        r = requests.get(url + caminho)
        resposta = r.json()
        
        try:
            # Verifica se o usuário e a senha estão presentes na resposta da API
            if any(u['name'] == name and u['password'] == passw for u in resposta):
                session['logged_in'] = True
                return redirect('index_inicial.html')
            else:
                return 'Erro no login - usuário não encontrado'
        except:
            return 'Erro no login - falha na autenticação'
    
    elif request.method == 'GET':
        return render_template('login.html')


@app.route("/carrinho")
def carrinho():
    name = request.args.get("name")
    url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
    caminho = '/api/cliente/categorias/'
    r = requests.get(url + caminho)
    resposta_api = r.json()  # Converte a resposta da API para formato JSON

    # Crie uma estrutura para armazenar os produtos com informações da API
    produtos_api = {}

    for item_do_carrinho in carrinho_produtos:
        for categoria in resposta_api:
            produtos_da_categoria = categoria['produtos']
            for produto in produtos_da_categoria:
                if produto['id'] == int(item_do_carrinho):
                    produtos_api[produto['id']] = {
                        'nome': produto['nome'],
                        'imagem': produto['fotoUrl']
                    }

    return render_template('carrinho.html', produtos_api=produtos_api)


    
    # # Itera sobre as categorias da resposta da API
    # for categoria in resposta_api:
    #     for produto in categoria['produtos']:
    #         produto_id = produto['id']
    #         produto_nome = produto['nome']
    #         produto_imagem = produto['fotoUrl']

    #         # Armazene as informações do produto na estrutura
    #         produtos_api[produto_id] = {'nome': produto_nome, 'imagem': produto_imagem}



# Antes das rotas, declare uma lista vazia para o carrinho
carrinho = []

# @app.route('/carrinho/add/<int:produto_id>', methods=['GET'])
# def adicionar_carrinho(produto_id):

#     # Lógica para adicionar o produto ao carrinho
#     # Você precisa armazenar as informações do produto no carrinho, como foto e descrição
#     # ...

#     # Exemplo de armazenamento das informações do produto em um dicionário
#     produto = {
#         'id': produto_id,
#         'fotoUrl': 'caminho/para/foto.jpg',
#         'descricao': 'Descrição do produto'
#     }

#     # carrinho.append(produto)  # Adiciona o produto à lista do carrinho

#     return redirect('/carrinho')

def obter_preco_do_produto(produto_id):
    # Lógica para obter o preço do produto com base no ID
    # Substitua pela sua lógica de obtenção do preço do produto a partir da API, banco de dados ou outra fonte de dados

    # Exemplo: supondo que você tenha uma lista de produtos com os preços já conhecidos
    produtos = [
        {'id': 1, 'nome': 'Produto 1', 'preco': 10.99},
        {'id': 2, 'nome': 'Produto 2', 'preco': 19.99},
        {'id': 3, 'nome': 'Produto 3', 'preco': 5.99},
        # ...
    ]

    # Localiza o produto com base no ID e retorna o preço correspondente
    for produto in carrinho:
        if produto['id'] == produto_id:
            return produto['preco']

    # Retorna 0 caso o produto não seja encontrado (ou qualquer outra lógica adequada)
    return 0


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
        caminho = '/api/cliente/usuarios'
        payload = {
            'nome': nome,
            'email': email,
            'senha': senha
        }
        response = requests.post(url + caminho, json=payload)
        
        if response.status_code == 201:
            return 'Cadastro realizado com sucesso!'
        else:
            return 'Erro no cadastro - falha na API'
    
    elif request.method == 'GET':
        return render_template('cadastro.html')

def calcular_total_carrinho():
    total = 0

    # Itera sobre os produtos no carrinho
    for item_do_carrinho in carrinho_produtos:
        # Lógica para obter o preço do produto com base no ID
        # Substitua pela sua lógica para obter o preço do produto a partir da API ou outra fonte de dados
        preco = obter_preco_do_produto(item_do_carrinho)

        # Adiciona o preço do produto ao total
        total += preco

    return total

@app.route('/finalizar-compra')
def finalizar_compra():
    # Lógica para obter o valor total do carrinho
    total_carrinho = calcular_total_carrinho()  # Substitua pela sua lógica de cálculo do valor total

    # Chamada à API para obter as formas de pagamento
    url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
    caminho = '/api/formas-pagamento'
    response = requests.get(url + caminho)
    
    if response.status_code == 200:
        formas_pagamento = response.json()
    else:
        formas_pagamento = []

    return render_template('finalizar_compra.html', total_carrinho=total_carrinho, formas_pagamento=formas_pagamento)


if __name__ == '__main__':
    app.run(debug = True)