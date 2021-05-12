# Exercício 6 Um  professor,  muito  legal,  fez  3  provas  durante  um semestre,mas  só  vai  levar  em  conta  as duas notas mais altas para calcular a média.Faça  uma  aplicação  que  peça  o  valor  das  3  notas,  mostre  como  seria  a  média  com  essas  3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

def funcMedia():
    a = float(input('digite a nota 1: '))
    b = float(input('digite a nota 2: '))
    c = float(input('digite a nota 3: '))
    notas = []
    notas.append(a)
    notas.append(b)
    notas.append(c)
    notas.sort()

    mediaGeral = (a + b + c) / 3
    maiorNota = notas[2]
    menorNota = notas[0]
    mediaMaior = (int(notas[1]) + int(notas[2])) / 2

    print(f'sua média geral seria: {mediaGeral}')
    print(f'sua maior nota foi: {maiorNota}')
    print(f'sua menor nota foi: {menorNota}')
    print(f'sua média com as notas mais alta é: {mediaMaior}')

funcMedia()