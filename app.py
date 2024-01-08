# app.py
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from game_logic import calcular_pontuacao
import random

optimal=[]
optimal.append([[[0, 0, 0], 'N'],[0, 2, 'H', 'L'], [0, 2, 'L', 'H'], [0, 2, 'L', 'L'], [1, 2, 'H', 'L'], [1, 2, 'L', 'H'], [1, 2, 'L', 'L']])
optimal.append([[[0, 0, 1], 'N'],[[0, 2, 'H', 'L'], [1, 2, 'H', 'L']]])
optimal.append([[[0, 1, 0], 'N'],[[1, 2, 'H', 'L'], [1, 2, 'L', 'H']]])
optimal.append([[[0, 1, 1], 'N'],[[1, 2, 'H', 'L']]])
optimal.append([[[1, 0, 0], 'N'],[[0, 2, 'H', 'L'], [0, 2, 'L', 'H']]])
optimal.append([[[1, 0, 1], 'N'],[[0, 2, 'H', 'L']]])
optimal.append([[[1, 1, 0], 'N'],[[0, 1, 'H', 'L'], [0, 1, 'L', 'H']]])
optimal.append([[[1, 1, 1], 'N'],[[0, 2, 'L', 'H'], [1, 2, 'L', 'H']]])
optimal.append([[[0, 0, 0], 'I'],[[0, 2, 'H', 'L'], [0, 2, 'L', 'H'], [1, 2, 'H', 'L'], [1, 2, 'L', 'H']]])
optimal.append([[[0, 0, 1], 'I'],[[0, 2, 'H', 'L'], [0, 2, 'L', 'H'], [1, 2, 'H', 'L'], [1, 2, 'L', 'H']]])
optimal.append([[[0, 1, 0], 'I'],[[1, 2, 'H', 'L'], [1, 2, 'L', 'H']]])
optimal.append([[[0, 1, 1], 'I'],[[1, 2, 'H', 'L'], [1, 2, 'L', 'H']]])
optimal.append([[[1, 0, 0], 'I'],[[0, 2, 'H', 'L'], [0, 2, 'L', 'H']]])
optimal.append([[[1, 0, 1], 'I'],[[0, 2, 'H', 'L'], [0, 2, 'L', 'H']]])
optimal.append([[[1, 1, 0], 'I'],[[0, 1, 'H', 'L'], [0, 1, 'L', 'H']]])
optimal.append([[[1, 1, 1], 'I'],[[0, 2, 'H', 'L'], [0, 2, 'L', 'H'], [1, 2, 'H', 'L'], [1, 2, 'L', 'H']]])


rd=random.randint(0,15)
x=optimal[rd][0]    

# Crie o aplicativo Dash
app = dash.Dash(__name__)

# Layout da interface gráfica
app.layout = html.Div([
    html.H1("Jogo de Operadora de Telecom"),
    html.H2(f"Scene = {x}"),

    # Adicione componentes para os parâmetros ajustáveis
    html.Label('Frequency User 1(Low/High):'),
    dcc.RadioItems(id='radio-c', options=[
        {'label': 'Low', 'value': "L"},
        {'label': 'High', 'value': "H"}
    ], value=1),

    html.Label('Frequency User 2(Low/High):'),
    dcc.RadioItems(id='radio-c2', options=[
        {'label': 'Low', 'value': "L"},
        {'label': 'High', 'value': "H"}
    ], value=1),
    
    html.Label('Usuários (0/1/2):'),
    dcc.Checklist(id='checklist-u', options=[
        {'label': '0', 'value': 0},
        {'label': '1', 'value': 1},
        {'label': '2', 'value': 2}
    ], value=[]),
    
    html.Button('Comparar Solução', id='button-compare'),
    html.Div(id='result-text')  # Mostrará o resultado da comparação
])

# Callback para atualizar o resultado quando o botão for pressionado
@app.callback(
    Output('result-text', 'children'),
    [Input('button-compare', 'n_clicks')],
    [Input('radio-c', 'value'),
     Input('radio-c2', 'value'),
     Input('checklist-u', 'value')
    ]
)

def comparar_solucao(n_clicks, c, c2, u, rd):
    if n_clicks is None:
        return ""
    else:
        pontuacao_jogador = calcular_pontuacao(c, c2, u, rd)
        # Aqui você pode comparar pontuacao_jogador com a solução ótima e gerar uma mensagem de feedback.  
        
        mensagem = f"{pontuacao_jogador}"

        return mensagem

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
