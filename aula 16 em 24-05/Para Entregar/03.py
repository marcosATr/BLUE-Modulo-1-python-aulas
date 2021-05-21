#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.
from random import randint
senha = ('blue')
def funcSenha():
    senha_usuario = input('Digite a senha para entrar: ')
    if senha_usuario != senha:
        print('\nSenha incorreta, tente novamente: ')
        #senha_usuario = input('Digite a senha para entrar: ')
        funcSenha()
    else:
        print('\nUsuário entrou com sucesso')


funcSenha()
print('-='*18+'\nBem-vindo(a) ao jogo de adivinhação\n'+'-='*18)
n = randint(1, 10)
print('Você consegue adivinhar em qual número de 1 a 10 eu estou pensando?')
guess = 0
c = 0
while guess != n:
    guess = int(input('Tente um número: '))
    c += 1
    if n > guess:
        print('Mais! Mais! Meu número é maior!')
    else:
        print('Meu número é menor!')
else:
    print(f'Você acertou! Foram usados {c} palpites!')
