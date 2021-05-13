#02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

a = int(input('digite: '))
b = int(input('digite: '))
c = int(input('digite: '))
d = int(input('digite: '))
nove = 0
tup = (a, b, c, d)
for i in tup:
    if i == 9:
        nove += 1

print(nove)
tres = tup.index(3)
if 3 in tup:
    print(tres + 1)

