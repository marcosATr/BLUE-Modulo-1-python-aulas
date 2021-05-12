# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg

# imc = peso/ alt²

def calImc(peso, alt):
    imc = float((peso) / (alt ** 2))
    print(f'Seu IMC é {imc:.2f}')
    return imc

calImc(87, 1.83)
