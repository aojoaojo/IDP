import glob
import pandas as pd
from datetime import datetime

def load_data():
    # Read all .csv files in the ./data/ folder
    dados_juntos = pd.DataFrame()
    for file_name in glob.glob('./data/' + '*.csv'):
        x = pd.read_csv(file_name, low_memory=False)
        dados_juntos = pd.concat([dados_juntos, x], axis=0)
    
    if 'ano_modelo' in dados_juntos.columns:
        try:
            dados_juntos[['ano', 'combustivel']] = dados_juntos['ano_modelo'].str.split(' ', n=1, expand=True)
            dados_juntos = dados_juntos.drop(columns=['ano_modelo', 'data_consulta'])
        except Exception as e:
            print(f"Error splitting 'ano_modelo' column: {e}")
            dados_juntos[['ano', 'combustivel']] = pd.DataFrame([['', '']], columns=['ano', 'combustivel'])
    else:
        print("'ano_modelo' column not found in the DataFrame")
        dados_juntos[['ano', 'combustivel']] = pd.DataFrame([['', '']], columns=['ano', 'combustivel'])

    if 'preco_medio' in dados_juntos.columns:
        dados_juntos = dados_juntos.rename(columns={'preco_medio': 'preco'})

    return dados_juntos

def get_top_marcas(dados):

    meses = dados['mes_referencia'].unique().tolist()
    top_marcas = {}

    for mes in meses:
        marca_e_quantidade = {}
        dados_mes = dados[dados['mes_referencia'] == mes]
        contagem_modelos = dados_mes['marca'].value_counts()
        top_10_marcas = contagem_modelos.head(10).index.tolist()
        for marca in top_10_marcas:
            marca_e_quantidade[marca] = contagem_modelos[marca]
        top_marcas[mes] = marca_e_quantidade
    return top_marcas

def get_variacao(mes1, mes2, dados, faixa_preco = None):
    if faixa_preco:
        dados = dados[(dados['preco'] >= faixa_preco[0]) & (dados['preco'] <= faixa_preco[1])]

    dados_mes1 = dados[dados['mes_referencia'] == mes1]
    dados_mes2 = dados[dados['mes_referencia'] == mes2]
    dados_mes1 = dados_mes1.rename(columns={'preco': 'preco_mes1'})
    dados_mes2 = dados_mes2.rename(columns={'preco': 'preco_mes2'})
    merged_data = pd.merge(dados_mes1, dados_mes2, 
                           on=['marca', 'modelo', 'ano', 'combustivel'], 
                           how='inner')
    
    merged_data['variacao'] = ((merged_data['preco_mes2'] - merged_data['preco_mes1']) / merged_data['preco_mes1']) * 100
    
    novo_dataset = merged_data[['marca', 'modelo', 'ano', 'combustivel', 'preco_mes1', 'preco_mes2', 'variacao']]
    
    top_valorizados = novo_dataset.nlargest(10, 'variacao')
    
    top_desvalorizados = novo_dataset.nsmallest(10, 'variacao')
    
    return novo_dataset, top_valorizados, top_desvalorizados


def create_table(data):
    #create a dict with the data in the variable data. The key from the dict is the column mes_referencia, the value must be the rest of the dataset
    data_dict = {month: data[data['mes_referencia'] == month] for month in data['mes_referencia'].unique()}

    # calculate the percentage variation of the prices
    variacao['variacao'] = ((variacao['preco_janeiro_2024'] - variacao['preco_novembro_2023']) / variacao['preco_novembro_2023']) * 100

    # sort the values by the variation
    variacao = variacao.sort_values('variacao', ascending=False)

    # select the top 10 variations
    top_10_variacao = variacao.head(10)
    top_10_variacao = top_10_variacao[['marca', 'modelo', 'ano', 'combustivel', 'variacao']]

    # format the variation column to be .2f and add the % symbol
    top_10_variacao['variacao'] = top_10_variacao['variacao'].apply(lambda x: f'{x:.2f}%')

    return top_10_variacao

def get_quantidade_carros_por_combustivel(dados):
    quantidade_carros_gasolina = dados[dados['combustivel'] == 'Gasolina'].shape[0]
    quantidade_carros_diesel = dados[dados['combustivel'] == 'Diesel'].shape[0]

    return quantidade_carros_gasolina, quantidade_carros_diesel


meses = {
    'janeiro': 1,
    'fevereiro': 2,
    'março': 3,
    'abril': 4,
    'maio': 5,
    'junho': 6,
    'julho': 7,
    'agosto': 8,
    'setembro': 9,
    'outubro': 10,
    'novembro': 11,
    'dezembro': 12
}

def converter_para_data(data_str):
    mes_str, ano = data_str.split(' de ')
    mes = meses[mes_str.lower()]
    ano = int(ano)
    return datetime(ano, mes, 1)