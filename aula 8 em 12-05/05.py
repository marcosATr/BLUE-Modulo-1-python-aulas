#01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições. Dica: utilizar a biblioteca random do Python.

import random

x = (random.randint(1, 50))
y = (random.randint(1, 50))
z = (random.randint(1, 50))

tup = (x, y, z)
print(tup)
sorted = sorted(tup)
print(sorted)
menor = sorted[0]
maior = sorted[2]
print(f'o menor número é {menor} ')
print(f'o maior número é {maior} ')


