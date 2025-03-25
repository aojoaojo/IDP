import requests

url = "https://veiculos.fipe.org.br/api/veiculos//ConsultarValorComTodosParametros"

headers = {
    "authority": "veiculos.fipe.org.br",
    "method": "POST",
    "path": "/api/veiculos//ConsultarValorComTodosParametros",
    "scheme": "https",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://veiculos.fipe.org.br",
    "referer": "https://veiculos.fipe.org.br/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "x-i-saax-ajax-request": "Ajax_Request",
    "x-requested-with": "XMLHttpRequest"
}

data = {
    "codigoTabelaReferencia": "310",
    "codigoMarca": "240",
    "codigoModelo": "10859",
    "codigoTipoVeiculo": "1",
    "anoModelo": "32000",
    "codigoTipoCombustivel": "1",
    "tipoVeiculo": "carro",
    "tipoConsulta": "tradicional"
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print("Requisição bem-sucedida!")
    print("Resposta da API:")
    print(response.json())  # ou response.text para texto puro
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)
