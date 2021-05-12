# Exercício Treino 1 - Escreva uma função que recebe dois parâmetros(números) e imprime o menor dos dois.Se eles forem iguais, imprima que são valores idênticos.

def funcMenor(a, b):
    if a < b:
        menor = a
    elif b < a:
        menor = b
    else:
        menor = ' valores idênticos'
    print(menor)


funcMenor(1, 1)