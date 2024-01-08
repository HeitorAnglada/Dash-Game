# app.py
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from game_logic import calcular_pontuacao

# Crie o aplicativo Dash
app = dash.Dash(__name__)

# Layout da interface gráfica
app.layout = html.Div([
    html.H1("Jogo de Operadora de Telecom"),
    # Adicione componentes para os parâmetros ajustáveis
    html.Label('Frequency (Low/High):'),
    dcc.RadioItems(id='radio-c', options=[
        {'label': 'Low', 'value': 0},
        {'label': 'High', 'value': 1}
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
     Input('checklist-u', 'value'),

    ]
)
def comparar_solucao(n_clicks, c, u):
    if n_clicks is None:
        return ""
    else:
        pontuacao_jogador = calcular_pontuacao(c, u)
        # Aqui você pode comparar pontuacao_jogador com a solução ótima e gerar uma mensagem de feedback.
        
        mensagem = f"Sua pontuação: {pontuacao_jogador}. (Falta implementar a comparação com a solução ótima)"
        mensagem = f"c = {c}\n u={u}\n /nPontuação = {pontuacao_jogador}"

        return mensagem

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
