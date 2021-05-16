# Exercício

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

mulheres = []
homens = []
p = 0
idade = 0
while True:
    p = input('Digite a letra correspondente sexo [F/M]: ').upper()
    idade = int(input('Digite a idade: '))
    continuar = input('Deseja continuar? [S/N]: ').upper()
    if p[0] in 'F':
        mulheres.append(idade)
    elif p[0] in 'M':
        homens.append(idade)
    else: 
        print('Sexo inválido, programa encerrado.')
        break    
    if continuar != 'S':
        break


### A) quantas pessoas tem mais de 18 anos. #Método tradicional
maiores_de_idade = 0
idade_total = mulheres + homens
for i in idade_total:
    if i >= 18:
        maiores_de_idade += 1
print(f'Maiores de idade: {maiores_de_idade}')

### B) quantos homens foram cadastrados.
print(f'Homens cadastrados: {len(homens)}')

# C) quantas mulheres tem menos de 20 anos. # Compressão de listas
mulheres_ate_20 = [m for m in mulheres if m < 20]
print(f'Mulheres até 20: {len(mulheres_ate_20)}')