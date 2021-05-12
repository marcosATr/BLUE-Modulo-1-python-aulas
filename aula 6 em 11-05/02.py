# Exercício Treino 2-Escreva uma função que recebe dois números (a e b) como parâmetroe retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

def funcLimite(a, b, c):
    if (a + b) > c:
        print('True')
    else:
        print('False')
    
funcLimite(1, 2, 5)