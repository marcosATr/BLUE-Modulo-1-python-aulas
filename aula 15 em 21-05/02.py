# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
print('Digite uma letra para interromper.')
while True:
    n = input('Digite um número natural: ')
    if n.isdigit():
        n = int(n) #TRANSFORMA EM INTEIRO APÓS A VERIFICAÇÃO.
        lista.append(n)
    else:
        print('Número inválido. Interrompendo!')
        break
if len(lista) > 0: #SÓ IMPRIMIR SE AS LISTAS TIVEREM PELO UMA ENTRADA VÁLIDA.
    print(len(lista))
    print(sorted(lista))
    if 5 in lista:
        print('5 está na lista.')
    else:
        print('5 NÃO está na lista.')