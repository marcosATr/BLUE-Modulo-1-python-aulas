# DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:​
# A) Quantas pessoas estão cadastradas.​
# B) A média da idade.​
# C) Uma lista com as mulheres.​
# D) Uma lista com as idades que estão acima da média.​
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.​

lista = []
while True:
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    while not idade.isdigit():
        idade = input('Idade INCORRETA, tentenovamente: ')
    idade = int(idade)
    sexo =  input('Digite o sexo: [M/F]: ').upper()[0]
    while sexo not in 'MF':
        sexo = input('Sexo incorreto, tente novamente [M/F]: ').upper()[0]
    continuar = input('Continuar? [S/N]: ').upper()[0]
    dicio = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }
    lista.append(dicio)
    if continuar not in 'S':
        break
print(lista)
#LISTA COM MULHERES:
lista_fem = []
print(f'A quantidade de pessoas cadastradas foi {len(lista)}')
for i in range(0, len(lista)):
    fem = lista[i]['sexo']
    if fem in 'F':
        lista_fem.append(lista[i]['nome'])
print('A lista feminina é:')
print(lista_fem)
#LISTA COM AS IDADES ACIMA DA MÉDIA:
lista_mais_velhos = []
soma = 0
for j in range(0, len(lista)):
    soma += lista[j]['idade']
media = soma / len(lista)
print(f'A média de idades é {media:.2f}') #MOSTRA A MÉDIA
for j in range(0, len(lista)):
    if lista[j]['idade'] > media:
        lista_mais_velhos.append(lista[j]['nome'])
print('A lista dos mais velhos é:')        
print(lista_mais_velhos)
