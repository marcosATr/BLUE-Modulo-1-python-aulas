# 03 -Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. 
# O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

n = randint(0,10)
count = 1
r = int(input('Digite o número! '))
while r != n:
    r = int(input('Digite um novo número! '))
    count += 1
print(f'Vc fez {count} tentativas')