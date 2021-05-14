# 2.Elaborar um programa para imprimir os números de 1(inclusive) até 10 (inclusive) em ordem decrescente.
# 
lista = []
for i in range(1, 11):
    lista.append(i)
lista.sort(reverse=True)
for j in lista:
    print(j)
#ou print(lista)