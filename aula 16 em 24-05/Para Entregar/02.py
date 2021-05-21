#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.
vogais = 'aeiou'
frase_original = input('Digite uma frase: ')
frase_mod = frase_original.lower()
count = 0
dicio_vogais= {}

##### CONTAR TODAS JUNTAS:
# for letra in frase_mod:
#     if letra in vogais:
#         count += 1
# print(f'O número total de vogais é: {count}')

###### 
###### CONTAR E ADICIONAR A UM DICIONÁRIO:
for i in vogais:
    count = frase_mod.count(i)
    dicio_vogais[i] = count
total = sum(dicio_vogais.values())
print(f'O total de vogais é {total}')
print(f'As vogais aparecem da seguinte maneira:\n{dicio_vogais}')
######
###### REMOVENDO AS VOGAIS:
for j in frase_mod:
    if j in vogais:
        frase_mod = frase_mod.replace(j, '')
print(frase_mod.capitalize())


