# Escreva uma função que, dado um númeronotarepresentando a nota de um estudante, converte o valor denotapara um conceito (A, B, C, D, E e F).
# Nota Conceito
# >=9.0   A
# >=8.0   B
# >=7.0   C
# >=6.0   D
# <=4.0   F

def funcNota(nota):
    if nota > 0 and nota <= 10:
        if nota >= 9:
            nota = 'A'
        elif nota >= 8:
            nota = 'B'
        elif nota >= 7:
            nota = 'C'
        elif nota >= 6:
            nota = 'D'
        else:
            nota = 'F'
        print(nota)
        return nota
    else:
        print('Erro. A nota deve estar entre 0 e 10')


funcNota(1)
