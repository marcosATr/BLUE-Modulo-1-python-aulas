#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.
vogais = 'aeiou'
frase = input('Digite uma frase: ').lower()
count = 0
dicio_vogais= {}

##### CONTAR TODAS JUNTAS:
# for letra in frase:
#     if letra in vogais:
#         count += 1
# print(f'O número total de vogais é: {count}')

###### 
###### CONTAR E ADICIONAR A UM DICIONÁRIO:
for i in vogais:
    count = frase.count(i)
    dicio_vogais[i] = count
total = sum(dicio_vogais.values())
print(f'O total de vogais é {total}')
print(f'As vogais aparecem da seguinte maneira:\n{dicio_vogais}')
###### REMOVENDO AS VOGAIS:
for j in frase:
    if j in vogais:
        frase = frase.replace(j, '')
print(frase.capitalize())


