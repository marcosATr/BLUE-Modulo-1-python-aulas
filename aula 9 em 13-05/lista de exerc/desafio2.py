# Desafio 2 - Faça um script que peça ao usuárioo
# número de matérias da escola , ou seja , um inteiro positivo.
# Emseguida, ele vai digitando o valor de cada nota , de cada matéria e isso será armazenado numa lista.
# Ao final, seu script deverá fornecer a média geral do aluno.

n = input('digite o n de matérias: ')
lista = []
if n.isalpha() == True:
    print('Número inválido')
elif n.isdigit() == False:
    print('Número inválido')
else:
    n = int(n)
    if n <= 0:
        print('Número inválido')
    else: 
        for i in range(1, n+1):
            i = float(input('digite a nota da matéria: '))
            lista.append(i)

        print(lista)
        media = sum(lista) / n
        print(f'média: {media:.2f}')