from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from functions import *

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

data = load_data()

colors = {
    'background': 'rgb(149 179 233)',
    'text': '#FFFFFF',
    'container': '#636EFA'
}

top_marcas = get_top_marcas(data)

datas = [{'label': i, 'value': i} for i in data['mes_referencia'].unique()]
datas_ordenadas = sorted(datas, key=lambda x: converter_para_data(x['value']))

dados_com_variacao_percentual_de_preco, top_10_valorizacao, top_10_desvalorizacao = get_variacao('janeiro de 2024', 'fevereiro de 2024', data)
dados_com_variacao_percentual_de_preco_top_marcas = dados_com_variacao_percentual_de_preco[dados_com_variacao_percentual_de_preco['marca'].isin(top_marcas['fevereiro de 2024'].keys())]

quantidade_carros_gasolina, quantidade_carros_diesel = get_quantidade_carros_por_combustivel(data)

# Plot the graphs
fig_variacao = px.scatter(dados_com_variacao_percentual_de_preco_top_marcas, x='marca', y='variacao', title='Variação percentual do preço médio das marcas')
fig_quantidade_modelos = px.bar(top_marcas, x=top_marcas['fevereiro de 2024'].keys(), y=top_marcas['fevereiro de 2024'].values(), title='Quantidade de modelos por marca')


# interface
app.layout = html.Div(
    
    style={
        'background': colors['background'],
        'height':'100vh',
        'paddingTop':'2rem',
    },

    children=[   
        html.H1(
            children='Análise da tabela FIPE',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(
            children='Trabalho da disciplina de Inteligência de Negócios.',
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'marginBottom': '2rem'
            }
        ),

        html.Div(
            style={
                'margin':'0 320px',
                'display':'flex',
                'flexDirection':'column',
                'gap':'0.5rem',
                'background':colors['container'],
                'padding':'1rem',
                'borderRadius':'10px',
                'border':'1px solid white'
                },
            children=[
            dcc.Dropdown(
                id='brand-dropdown',
                # get the unique values of the column 'marca' from the data
                options=[{'label': i, 'value': i} for i in data['marca'].unique()],
                placeholder='Selecione a marca'
            ),
            dcc.Dropdown(
                id='model-dropdown',
                placeholder='Selecione o modelo'
            ),
            dcc.Dropdown(
                id='year-dropdown',
                placeholder='Selecione o ano'
            ),
            dcc.Dropdown(
                id='month-dropdown',
                options=datas_ordenadas,
                placeholder='Selecione o mês de referência'
            ),

            html.H3(id='price-output', style={'textAlign': 'center', 'color': colors['text'], 'marginTop': '20px'})
        ]),
        
        html.Div(
            style={
                'margin':'2rem', 
                'display':'flex', 
                'justifyContent':'center', 
                'gap':'1rem',
                'marginBottom':'4rem',
                }, 
            children=[
                dcc.Graph(id='variacao-graph', figure=fig_variacao),
                dcc.Graph(id='quantidade-modelos-graph', figure=fig_quantidade_modelos)
            ]
        ),

        html.Div(
            style={
                'margin':'2rem',
                'display':'flex',
                'justifyContent':'center',
                'gap':'1rem',
                'flexDirection':'column'
                }, 
            children=[
                html.H3(
                    children='Selecione um intervalo de mês para ver o top 10 de valorização e desvalorização dos modelos.',
                    style={
                        'textAlign':'center',
                        'color':colors['container'],
                        'marginTop':'4rem'
                    }
                ),
                html.Span(
                    children='Insira primeiro o mês mais antigo e depois o mês mais recente.',
                    style={
                        'textAlign':'center',
                        'color':'black',
                    }
                ),
                html.Div(
                    style={
                        'margin':'0rem 20rem',
                        'display':'flex',
                        'flexDirection':'column',
                        'gap':'0.5rem',
                        'background':colors['container'],
                        'padding':'1rem',
                        'borderRadius':'10px',
                        'border':'1px solid white'
                    },
                    children=[
                        dcc.Dropdown(
                            id='month-dropdown-1',
                            options=datas_ordenadas,
                            placeholder='Selecione o primeiro mês de referência'
                        ),
                        dcc.Dropdown(
                            id='month-dropdown-2',
                            options=datas_ordenadas,
                            placeholder='Selecione o segundo mês de referência'
                        ),
                        dcc.Dropdown(
                            id='valorizacao-desvalorizacao-dropdown',
                            options=['valorizacao', 'desvalorizacao'],
                            placeholder='Valorização ou Desvalorização'
                        ),
                        dcc.Dropdown(
                            id='faixa-preco-dropdown',
                            options=['0 a 15 mil', '15 a 50mil', '50 a 100mil', '100 a 200mil', '200 a 500mil', '500 a 1 milhão', '1 milhão ou mais'],
                            placeholder='Faixa de preço'
                        ),
                    ]
                ),
                html.Div(id='table-output'),
                html.Div(
                    style={
                        'display':'flex',
                        'justifyContent':'center',
                        'gap':'1rem',
                    },
                    children=[
                        html.Div(
                            style={},
                            children=[
                                html.H3(
                                    children='Quantidade de carros a gasolina e diesel',
                                    style={
                                        'textAlign':'center',
                                        'color':colors['container'],
                                        'marginTop':'2rem'
                                    }
                                ),
                                dcc.Graph(
                                    figure=go.Figure(
                                        data=[
                                            go.Bar(
                                                x=['Gasolina', 'Diesel'],
                                                y=[quantidade_carros_gasolina, quantidade_carros_diesel]
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                    ]
                ),
            ]
        )
    ]
)

# callback to update the models based on the selected brand
@app.callback(
    Output('model-dropdown', 'options'),
    Input('brand-dropdown', 'value')
)
def set_models_options(selected_brand):
    if selected_brand is None:
        return []
    filtered_data = data[data['marca'] == selected_brand]
    models = filtered_data['modelo'].unique()
    return [{'label': model, 'value': model} for model in models]

# callback to update the years based on the selected model
@app.callback(
    Output('year-dropdown', 'options'),
    Input('model-dropdown', 'value'),
    Input('brand-dropdown', 'value')
)
def set_years_options(selected_model, selected_brand):
    if selected_brand is None or selected_model is None:
        return []
    filtered_data = data[(data['marca'] == selected_brand) & (data['modelo'] == selected_model)]
    years = filtered_data['ano'].unique()
    return [{'label': year, 'value': year} for year in years]

@app.callback(
    Output('price-output', 'children'),
    Input('brand-dropdown', 'value'),
    Input('model-dropdown', 'value'),
    Input('year-dropdown', 'value'),
    Input('month-dropdown', 'value')
)

def update_price(selected_brand, selected_model, selected_year, selected_month):
    if not all([selected_brand, selected_model, selected_year, selected_month]):
        return "Por favor, selecione todos os filtros."
    
    filtered_data = data[
        (data['marca'] == selected_brand) & 
        (data['modelo'] == selected_model) &
        (data['ano'] == selected_year) &
        (data['mes_referencia'] == selected_month)
    ]

    if filtered_data.empty:
        return "Nenhum dado encontrado para os filtros selecionados."
    
    price = filtered_data['preco'].values[0]
    return f"Preço: R${price:.2f}"

@app.callback(
    Output('table-output', 'children'),
    Input('month-dropdown-1', 'value'),
    Input('month-dropdown-2', 'value'),
    Input('valorizacao-desvalorizacao-dropdown', 'value'),
    Input('faixa-preco-dropdown', 'value'),
)
def update_table(mes1, mes2, valorizacao_desvalorizacao, faixa_preco):
    if not all([mes1, mes2, valorizacao_desvalorizacao, faixa_preco]):
        return "Por favor, selecione todos os filtros."
    
    if faixa_preco == '0 a 15 mil':
        faixa_preco = (0, 15000)
    elif faixa_preco == '15 a 50mil':
        faixa_preco = (15000, 50000)
    elif faixa_preco == '50 a 100mil':
        faixa_preco = (50000, 100000)
    elif faixa_preco == '100 a 200mil':
        faixa_preco = (100000, 200000)
    elif faixa_preco == '200 a 500mil':
        faixa_preco = (200000, 500000)
    elif faixa_preco == '500 a 1 milhão':
        faixa_preco = (500000, 1000000)
    else:
        faixa_preco = (1000000, 1000000000)

    if valorizacao_desvalorizacao == 'valorizacao':
        _, top_10_valorizacao, _ = get_variacao(mes1, mes2, data, faixa_preco)
        df = top_10_valorizacao
    else:
        _, _, top_10_desvalorizacao = get_variacao(mes1, mes2, data, faixa_preco)
        df = top_10_desvalorizacao

    return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

if __name__ == '__main__':
    app.run_server(debug=True)
