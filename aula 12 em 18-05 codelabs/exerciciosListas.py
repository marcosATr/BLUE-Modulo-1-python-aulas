#01 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


# par = []
# impar = []
# for i in range(7):
#    n = int(input('Digite um número: '))
#    if n % 2 == 0:
#       par.append(n)
#    else:
#       impar.append(n)
# print(sorted(par))
# print(sorted(impar))


#02 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:
""" 
[  1  ][  2  ][  3  ]
[  4  ][  5  ][  6  ]
[  7  ][  8  ][  9  ] 

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[coluna][linha]) 
"""
# # ### COMEÇO DA 2
lista = []
for i in range(9):
   i = int(input('Digite um número: '))
   lista.append(i)
print(lista)
pares = 0
for c in lista:
   if c % 2 == 0:
      pares += c

for k in range(3):
   temp = []
   for j in range(3):
      x = lista.pop(0)
      temp.append(x)
   lista.append(temp)
print(lista)

for y in range(3):
   for z in range(3):
      print(f'[  {lista[y][z]}  ]', end="" )
   print('\n')

# ###FIM DA 2
### RESPOSTAS DA 3
print(f'A soma dos valores pares é {pares}')
soma3 = 0
for l in range(3):
   soma3 += lista[l][2]
print(f'O valor da soma da terceira coluna é {soma3}')

print(f'O maior valor da segunda linha é {max(lista[1])}')

#03 - Aprimore o desafio anterior, mostrando no final:
   # A) A soma de todos os valores pares digitados.
   # B) A soma dos valores da terceira coluna. 
   # C) O maior valor da segunda linha.

#04 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# from random import randint
# n = int(input('Digite o número de jogos: '))
# listaFinal = []
# for j in range(0, n):
#    palpite = []
#    for i in range(0, 6):
#       dez = randint(1, 60)
#       while dez in palpite:
#          dez = randint(1, 60)
#          if dez not in palpite:
#             break
#       palpite.append(dez)
#    listaFinal.append(palpite)
# print(listaFinal)