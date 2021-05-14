#Faça um script em Python que exiba todos os possíveis palpites da Mega-Sena.
#Dados:
#Cada palpite possui 6 dezenas
#As dezenas variam de 1 até 60
# Não pode repetir dezena

import itertools
lista = []
for i in range(1,61):
    lista.append(i)

#print(lista)

for j in itertools.combinations(lista, 6):
    print(j)

