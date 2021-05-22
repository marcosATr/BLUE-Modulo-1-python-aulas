# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
import sys
lista = []
for i in range(5):        
    try:
        n = int(input('Digite um número natural: '))
    except (ValueError, TypeError):
        print('Números inválidos.')
        sys.exit(1)
    if i == 0:
        lista.append(n)
    else:
        if n > lista[-1]:
            lista.append(n)
        else:
            pos_anterior = len(lista) - 2 # -2 pq é na penúltima posição.
            lista.insert(pos_anterior, n) 
print(lista)

