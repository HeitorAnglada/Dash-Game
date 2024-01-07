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
    dcc.Slider(id='slider-c', min=1, max=3, value=1, marks={1: 'Low', 2: 'Mid', 3: 'High'}),
    dcc.Slider(id='slider-r', min=1, max=3, value=1, marks={1: '1', 2: '2', 3: '3'}),
    dcc.Slider(id='slider-u', min=0, max=3, value=0, marks={0: '0', 1: '1', 2: '2', 3: '3'}),
    dcc.Dropdown(id='dropdown-p', options=[
        {'label': 'Day', 'value': 'day'},
        {'label': 'Night', 'value': 'night'}
    ], value='day'),
    dcc.RadioItems(id='radio-s', options=[
        {'label': 'Good', 'value': 'good'},
        {'label': 'Bad', 'value': 'bad'}
    ], value='good'),
    dcc.RadioItems(id='radio-t', options=[
        {'label': 'Light', 'value': 'light'},
        {'label': 'Heavy', 'value': 'heavy'}
    ], value='light'),
    html.Button('Comparar Solução', id='button-compare'),
    html.Div(id='result-text')  # Mostrará o resultado da comparação
])

# Callback para atualizar o resultado quando o botão for pressionado
@app.callback(
    Output('result-text', 'children'),
    [Input('button-compare', 'n_clicks')],
    [Input('slider-c', 'value'),
     Input('slider-r', 'value'),
     Input('slider-u', 'value'),
     Input('dropdown-p', 'value'),
     Input('radio-s', 'value'),
     Input('radio-t', 'value')]
)
def comparar_solucao(n_clicks, c, r, u, p, s, t):
    if n_clicks is None:
        return ""
    else:
        pontuacao_jogador = calcular_pontuacao(c, r, u, p, s, t)
        # Aqui você pode comparar pontuacao_jogador com a solução ótima e gerar uma mensagem de feedback.
        mensagem = f"Sua pontuação: {pontuacao_jogador}. (Falta implementar a comparação com a solução ótima)"
        return mensagem

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
