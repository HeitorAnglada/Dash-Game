# game_logic.py
#'''
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
#'''
def calcular_pontuacao(c, c2, u, rd):

    entrada = []
        #u.sort()
        #entrada.append(u)
    for U in u:
        entrada.append(U)
    entrada.append(c)
    entrada.append(c2)  

    # Calcular a pontuação
    pontuacao = 5

    #return pontuacao  # Pontuação mínima é 0
    return optimal[1]
