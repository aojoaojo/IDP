# API
## Explicando a estrutura:

A pasta "Routers" contém modulos que definem as rotas (endpoints) para algum aspecto especifico da aplicação.
Por exemplo, "users.py" tratam-se dos endpoints que são voltados para usuarios

"dependencies.py" serve para definir e armazenar dependecias utilizadas em varias partes da aplicação.
Por exemplo a conexão com banco de dados e funções que serão comuns entre os códigos.

Já a pasta "internal" serve para armazenar módulos internos da aplicação, que não são expostos como rotas, mas são 
usados internamente 

Essa estrutura foi tirada da documentação oficial da FastAPI para grandes aplicações

https://devdocs.io/fastapi/tutorial/bigger-applications/index#an-example-file-structure

## Para rodar corretamente:
Ao clonar o repositório usso o commando:
```bash
pip install -r requirements.txt
```
você deve estar dentro do dir api para que o comando funcione.
Esse comando instalara todas as bibliotecas necessárias para funcionamento da api

### Rodando:
Para iniciar a api utilize:
```bash
uvicorn main:app --reload
```
Esse comando inicia a aplicação e a reinicia toda vez que uma sofre alteração em um arquivo

