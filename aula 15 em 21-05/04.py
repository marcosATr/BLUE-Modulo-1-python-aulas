# Faça um programa que tenha uma função chamada func(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

# def func(i, f, p):
#     while i != f:
#         print(i, end = " ")
#         i = i + p
#     return i

# print(func(1, 10, 1))
# print(func(10, 0, -2))

def func(i, f, p):
    if i < f:
        while i <= f:
            print(i, end = " ")
            i = i + p

    else:
        while i >= f:
            print(i, end = " ")
            i = i + p

    print()
    return

func(1, 10, 1)
func(10, 0, -2)
func(1, 20, 2)