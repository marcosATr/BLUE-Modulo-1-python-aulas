# DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:​
# A) Quantas pessoas estão cadastradas.​
# B) A média da idade.​
# C) Uma lista com as mulheres.​
# D) Uma lista com as idades que estão acima da média.​
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.​
lista = [] #foi
idades = [] #foi
mulheres = [] #foi
acimaDaMedia = []
while True:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('''
    [ M ] = MASCULINO
    [ F ] = FEMININO
    Digite a opção correspondente ao sexo: 
    ''').upper()[0]
    while sexo not in 'MF':
        sexo = input('Sexo incorreto, tente novamente [M/F]: ').upper()[0]
    dicio = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }
    lista.append(dicio)
    idades.append(idade)
    if sexo in 'F':
        mulheres.append(nome)
    continuar = input('Continuar? [S/N] ').upper()[0]
    if continuar not in 'S':
        break

media = sum(idades)/len(lista)
for i in idades:
    if i > media:
        acimaDaMedia.append(i)

print(f'O número de cadastrados é {len(lista)}')
print(f'A média de idades é {media}.')
print(f'A lista apenas com mulheres é:\n{mulheres}')
print(f'A lista com as idades acima da média é:\n{acimaDaMedia}')
