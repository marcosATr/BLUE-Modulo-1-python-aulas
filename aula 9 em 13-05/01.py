#01 - Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

lista = [5, 7, 2, 9, 4, 1, 3]


a = len(lista)
print(a)
print(max(lista))
print(min(lista))
print(sum(lista))
lista.sort()
print(lista)
lista.sort(reverse = True)
print(lista)

