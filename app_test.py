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
    html.Label('Custo (Low/Mid/High):'),
    dcc.RadioItems(id='radio-c', options=[
        {'label': 'Low', 'value': 1},
        {'label': 'Mid', 'value': 2},
        {'label': 'High', 'value': 3}
    ], value=1),
    
    html.Label('Reclamações (1/2/3):'),
    dcc.RadioItems(id='radio-r', options=[
        {'label': '1', 'value': 1},
        {'label': '2', 'value': 2},
        {'label': '3', 'value': 3}
    ], value=1),
    
    html.Label('Usuários (0/1/2/3):'),
    dcc.RadioItems(id='radio-u', options=[
        {'label': '0', 'value': 0},
        {'label': '1', 'value': 1},
        {'label': '2', 'value': 2},
        {'label': '3', 'value': 3}
    ], value=0),
    
    html.Label('Período (Day/Night):'),
    dcc.RadioItems(id='radio-p', options=[
        {'label': 'Day', 'value': 'day'},
        {'label': 'Night', 'value': 'night'}
    ], value='day'),
    
    html.Label('Satisfação (Good/Bad):'),
    dcc.RadioItems(id='radio-s', options=[
        {'label': 'Good', 'value': 'good'},
        {'label': 'Bad', 'value': 'bad'}
    ], value='good'),
    
    html.Label('Tráfego (Light/Heavy):'),
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
    [Input('radio-c', 'value'),
     Input('radio-r', 'value'),
     Input('radio-u', 'value'),
     Input('radio-p', 'value'),
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
        mensagem = f"c = {c}\n r={r}\n u={u}\n p={p}\n s={s}\n t={t}"

        return mensagem

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
