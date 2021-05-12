# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.


def func(a, b):
    if a > b:
        menor = b
    elif a < b:
        menor = a
    else:
        menor = 'São iguais'
    print(menor)
    return menor


func(32, 32)
