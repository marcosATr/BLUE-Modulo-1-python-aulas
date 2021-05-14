# 3.Faça um programa que leia o estado civil de 15 pessoas (Solteiro/Casado) e mostre ao final a quantidade de pessoas de cada estadocivil.

lista = []
def func(n):
    for i in range(1, n+1):
        r = input('Digite estado civil: ').lower()
        lista.append(r)
    casado = lista.count("casado")
    solteiro = lista.count('solteiro')
    print(casado)
    print(solteiro)


func(15)