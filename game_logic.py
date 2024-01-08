# game_logic.py
def calcular_pontuacao(c, r, u, p, s, t):
    # Pesos arbitrários para os parâmetros
    peso_c = 2
    peso_r = 1
    peso_u = 1
    peso_p = 1
    peso_s = 2
    peso_t = 2

    # Valores base para cada parâmetro
    valor_base_c = 2
    valor_base_r = 2
    valor_base_u = 1
    valor_base_p = 1
    valor_base_s = 2
    valor_base_t = 2

    # Calcular a pontuação
    pontuacao = (c - valor_base_c) * peso_c + \
                (r - valor_base_r) * peso_r + \
                (u - valor_base_u) * peso_u + \
                (1 if p == 'night' else 0) * peso_p + \
                (1 if s == 'bad' else 0) * peso_s + \
                (1 if t == 'heavy' else 0) * peso_t

    return max(0, pontuacao)  # Pontuação mínima é 0
