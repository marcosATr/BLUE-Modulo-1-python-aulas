# # Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
# ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def func(a):
    if a > 0:
        a = str('P')
    elif a < 0:
        a = str('N')
    else:
        a = str('0')
    print(a)
    return a


func(0)
