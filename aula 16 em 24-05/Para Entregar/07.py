#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

par = []
impar = []
lista= [par] + [impar] #MANTENHA AS LISTAS SEPARADAS
for i in range(7):
    n = int(input('Digite um número natural: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
print(lista)