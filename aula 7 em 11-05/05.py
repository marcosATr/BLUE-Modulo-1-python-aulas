# Exercício 5 -Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def funcFicha(jogador=0, gols=0):
    nome = jogador
    gol = gols
    print(nome)
    print(gol)

funcFicha('dido')
