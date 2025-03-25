
import requests

url = 'https://hackarestaurante-os-conquistadores-da-disrupcao.azurewebsites.net'
caminho = '/api/cliente/categorias'

r = requests.get(url+caminho)
resposta = r.json()