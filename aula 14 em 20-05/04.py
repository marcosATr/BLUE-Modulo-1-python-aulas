# Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. Dicas: procure sobre a função randint(), sleep() e itemgetter da bliblioteca operator.

from random import randint
resultados = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6),
}
print(resultados)
ordenado = dict()
ordenado = sorted(resultados.items(), key=lambda item: item[1], reverse=True)
for i in ordenado:
    print(f'{i[0].capitalize()} fez {i[1]} pontos.')