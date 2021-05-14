# 3.Faça um programa que leia o estado civil de 15 pessoas (Solteiro/Casado) e mostre ao final a quantidade de pessoas de cada estadocivil.

p1 = input('digite o estado civil: ').lower()
p2 = input('digite o estado civil: ').lower()
p3 = input('digite o estado civil: ').lower()
p4 = input('digite o estado civil: ').lower()
p5 = input('digite o estado civil: ').lower()
p6 = input('digite o estado civil: ').lower()
p7 = input('digite o estado civil: ').lower()
p8 = input('digite o estado civil: ').lower()
p9 = input('digite o estado civil: ').lower()
p10 = input('digite o estado civil: ').lower()
p11 = input('digite o estado civil: ').lower()
p12 = input('digite o estado civil: ').lower()
p13 = input('digite o estado civil: ').lower()
p14 = input('digite o estado civil: ').lower()
p15 = input('digite o estado civil: ').lower()

lista = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]
casado = lista.count("casado")
solteiro = lista.count('solteiro')

print(casado)
print(solteiro)
