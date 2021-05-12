# Exercício 5 -Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def funcFicha():
    jogador = input('digite o nome do jogador: ')
    gols = input('digite o número de gols realizados: ')

    if jogador.isalpha() == False:
        jogador = "<DESCONHECIDO>"
    else:
        jogador = jogador.casefold().title()
    
    if gols.isdigit() == False:
        gols = "QUANTIDADE DESCONHECIDA DE"
    
    print(f'O jogador {jogador} fez {gols} GOLS na temporada.')


funcFicha()
