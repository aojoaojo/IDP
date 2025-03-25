import os
import csv
import sys
import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def extract_columns_from_text(text):
    columns = text.split('\n')
    return columns[1]

def trata_string_preco(text):
    return text.replace('R$ ', '').replace('.', '').replace(',', '.')

def add_row_to_df(df, mes_referencia, codigo_fipe, marca, modelo, ano_modelo, autenticacao, data_consulta, preco_medio):
    dicionario = {'mes_referencia': mes_referencia, 'codigo_fipe': codigo_fipe, 'marca': marca, 'modelo': modelo, 'ano_modelo': ano_modelo, 'autenticacao': autenticacao, 'data_consulta': data_consulta, 'preco_medio': preco_medio}
    new_row_df = pd.DataFrame([dicionario])
    df = pd.concat([df, new_row_df], ignore_index=True)
    return df

def abre_aba_carro(driver):
    aba_utilitario = driver.find_elements(By.CLASS_NAME, value = "ilustra")[0]
    aba_utilitario.click()

def salvar_indices(indices, mes_referencia):
    caminho_arquivo=f'./data/indices/indices_atuais_{mes_referencia}.json'
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(indices, arquivo)

def carregar_indices(mes_referencia):
    try:
        caminho_arquivo=f'./data/indices/indices_atuais_{mes_referencia}.json'
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        return {'index_marca': 1, 'index_modelo': 1, 'index_ano': 1}

def main(arg):
    WEBSITE = 'https://veiculos.fipe.org.br/#carro-comum'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    driver.get(WEBSITE)

    time.sleep(0.5)

    #select element by id
    select_mes = Select(driver.find_element(By.ID, 'selectTabelaReferenciacarro'))
    select_marca_carro = Select(driver.find_element(By.ID, 'selectMarcacarro'))
    select_modelo_carro = Select(driver.find_element(By.ID, 'selectAnoModelocarro'))
    select_ano_carro = Select(driver.find_element(By.ID, 'selectAnocarro'))
    aba_utilitario = driver.find_element(By.XPATH, value = "//a[@data-slug='carro']")
    pesquisar_button = driver.find_element(By.XPATH, value = "//a[@id='buttonPesquisarcarro']")

    abre_aba_carro(driver)
    select_mes.select_by_index(int(arg))
    with open('./month_index.json', 'r') as file:
        month_index = json.load(file)

    mes_referencia = month_index[arg]
    mes_referencia = mes_referencia.replace('/', '-')

    indices_atuais = carregar_indices(mes_referencia)
    csv_name = f'./data/dados_fipe_{mes_referencia}.csv'
    columns=['mes_referencia', 'codigo_fipe', 'marca', 'modelo', 'ano_modelo', 'autenticacao', 'data_consulta', 'preco_medio']
    
    if not os.path.exists(csv_name):
        with open(csv_name, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(columns)



    flag = True
    index_marca = 1
    index_modelo = 1
    index_ano = 1

    columns=['mes_referencia', 'codigo_fipe', 'marca', 'modelo', 'ano_modelo', 'autenticacao', 'data_consulta', 'preco_medio']
    with open(csv_name, mode='a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        while(index_marca < len(select_marca_carro.options)):
            if flag:
                index_marca = indices_atuais['index_marca']
            select_marca_carro.select_by_index(index_marca)
            time.sleep(0.01)
            while(index_modelo < len(select_modelo_carro.options)):
                if flag:
                    index_modelo = indices_atuais['index_modelo']
                select_modelo_carro.select_by_index(index_modelo)
                time.sleep(0.01)
                while (index_ano < len(select_ano_carro.options)):
                    if flag:
                        index_ano = indices_atuais['index_ano']
                        flag = False
                    select_ano_carro.select_by_index(index_ano)
                    pesquisar_button.click()
                    matches = driver.find_elements(By.TAG_NAME, 'tr')
                    count = 0
                    for match in matches:
                        if(match.text == ''):
                            break
                        aux = extract_columns_from_text(match.text)
                        if count == 0:
                            mes_referencia_atual = aux
                        elif count == 1:
                            codigo_fipe = aux
                        elif count == 2:
                            marca = aux
                        elif count == 3:
                            modelo = aux
                        elif count == 4:
                            ano_modelo = aux
                        elif count == 5:
                            autenticacao = aux
                        elif count == 6:
                            data_consulta = aux
                        elif count == 7:
                            preco_medio = trata_string_preco(aux)
                        count += 1
                    #save data in csv
                    linha = [mes_referencia_atual, codigo_fipe, marca, modelo, ano_modelo, autenticacao, data_consulta, preco_medio]
                    print(linha)
                    escritor_csv.writerow(linha)
                    time.sleep(0.01)
                    if index_ano == len(select_ano_carro.options) - 1:
                        break
                    index_ano += 1
                #clean search to not miss the next model options
                salvar_indices({'index_marca': index_marca, 'index_modelo': index_modelo, 'index_ano': index_ano}, mes_referencia)
                limpa_pesquisa = driver.find_element(By.XPATH, value = "//*[@id='buttonLimparPesquisarcarro']/a")
                limpa_pesquisa.click()        
                time.sleep(0.05)
                select_marca_carro = Select(driver.find_element(By.ID, 'selectMarcacarro'))
                select_modelo_carro = Select(driver.find_element(By.ID, 'selectAnoModelocarro'))
                select_ano_carro = Select(driver.find_element(By.ID, 'selectAnocarro'))
                pesquisar_button = driver.find_element(By.XPATH, value = "//a[@id='buttonPesquisarcarro']")
                select_marca_carro.select_by_index(index_marca)
                time.sleep(0.05)
                select_modelo_carro.select_by_index(index_modelo)
                index_modelo += 1
                index_ano = 1
            index_marca += 1
            index_modelo = 1
            index_ano = 1
    print("Extração finalizada ;)")
    return True

error_count = 0
while True:
    try:
        if main(sys.argv[1]):
            break
    except Exception as e:
        error_count += 1
        print(error_count)
        print(e)
        print("Erro ao extrair dados da FIPE. Tentando novamente em 1 segundo.")
        time.sleep(1)