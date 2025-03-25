import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import random
from collections import deque
import dash_bootstrap_components as dbc

# Inicializar a aplicação Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Simular dados dos sensores
def simulate_sensor_data():
    """Simula dados de sensores de uma pessoa com fobia"""
    heart_rate = random.randint(60, 140)  # Frequência cardíaca
    skin_temp = random.uniform(35.0, 38.0)  # Temperatura da pele
    return {"heart_rate": heart_rate, "skin_temp": skin_temp}

# Inicializar dados
max_length = 50
time_series = deque(maxlen=max_length)
heart_rate_series = deque(maxlen=max_length)
skin_temp_series = deque(maxlen=max_length)

# Layout do dashboard
app.layout = dash.html.Div([
    dbc.Row([
        html.H1("Fabrica de Projetos"),
    ]),
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H2("Frequência Cardíaca", style={
                    'textAlign': 'center',
                    'color': '#FAF6F1',
                    'marginBottom': '0px'
                }),
                html.Div(id='heart-rate-box', style={
                    'fontSize': '48px',
                    'textAlign': 'center',
                    'padding': '20px',
                    'border': '2px solid #d9d9d9',
                    'borderRadius': '10px',
                    'width': '300px',
                    'margin': 'auto',
                    'backgroundColor': '#f9f9f9'
                })
            ]),
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.H2("Nome",
                                style={
                                    'textAlign': 'center',
                                    'color': '#FAF6F1',
                                    'marginTop': '20px',
                                    'marginBottom': '0px'
                                }),
                        html.Div("Bilbo Baggins", id='nome-box', style={
                            'fontSize': '30px',
                            'textAlign': 'center',
                            'padding': '20px',
                            'border': '2px solid #d9d9d9',
                            'borderRadius': '10px',
                            'width': '300px',
                            'margin': 'auto',
                            'margin-left': '20px',
                            'backgroundColor': '#f9f9f9'
                        }),
                    ]),
                    dbc.Col([
                        html.H2("Idade",
                                style={
                                    'textAlign': 'center',
                                    'color': '#FAF6F1',
                                    'marginTop': '20px',
                                    'marginBottom': '0px'
                                }),
                        html.Div("300 anos", id='idade-box', style={
                            'fontSize': '30px',
                            'textAlign': 'center',
                            'padding': '20px',
                            'border': '2px solid #d9d9d9',
                            'borderRadius': '10px',
                            'width': '250px',
                            'margin': 'auto',
                            'backgroundColor': '#f9f9f9'
                        }),
                    ]),
                    dbc.Col([
                        html.H2("Fobia",
                        style={
                            'textAlign': 'center',
                            'color': '#FAF6F1',
                            'marginTop': '20px',
                            'marginBottom': '0px'
                        }),
                        html.Div("Aranhas", id='fobia-box', style={
                            'fontSize': '30px',
                            'textAlign': 'center',
                            'padding': '20px',
                            'border': '2px solid #d9d9d9',
                            'borderRadius': '10px',
                            'width': '250px',
                            'margin': 'auto',
                            'backgroundColor': '#f9f9f9'
                        }),
                    ]),
                ]),
            ])
        ]),
        dbc.Col([
            dcc.Graph(id='skin-temp-graph',
                      style={'height': '500px',
                             'width': '90%',
                             'margin': 'auto'}),
        ])
    ]),

    # Intervalo para atualizar os dados em tempo real
    dcc.Interval(
        id='data-update',
        interval=1000,  # Atualizar a cada 1 segundo
        n_intervals=0
    )
])

# Função para atualizar os gráficos
@app.callback(
    [Output('heart-rate-box', 'children'),
     Output('skin-temp-graph', 'figure')],
    [Input('data-update', 'n_intervals')]
)
def update_graph(n):
    # Gerar novos dados dos sensores
    sensor_data = simulate_sensor_data()

    # Atualizar as séries de dados
    time_series.append(n)
    skin_temp_series.append(sensor_data["skin_temp"])

    # Caixa de frequência cardíaca
    heart_rate_value = f"{sensor_data['heart_rate']} BPM"

    # Gráfico de temperatura da pele
    skin_temp_fig = go.Figure()
    skin_temp_fig.add_trace(go.Scatter(x=list(time_series), y=list(skin_temp_series), mode='lines', name='Temperatura da Pele'))
    skin_temp_fig.update_layout(title='Temperatura da Pele (°C)', xaxis_title='Tempo', yaxis_title='°C')

    return heart_rate_value, skin_temp_fig

# Executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
