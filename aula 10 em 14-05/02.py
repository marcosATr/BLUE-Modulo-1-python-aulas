#02 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Sexo M ou F? Digite a letra correspondente:').upper()
while sexo != 'M' and sexo != 'F':
    print("Sexo incorreto, digite novamente.")
    sexo = input('Sexo M ou F? Digite a letra correspondente:').upper()