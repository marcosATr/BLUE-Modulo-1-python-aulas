#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
if n1 > n2:
    maior = n1
elif n2 > n1:
    maior = n2
else:
    maior = 'nenhum! Os números são iguais.'
print(f'A soma de {n1} e {n2} é {n1 + n2}')
print(f'A multiplicação de {n1} e {n2} é {n1 * n2}')
print(f'A divisão inteira de {n1} e {n2} é {n1 // n2}')
print(f'O maior número é: {maior}')
if (n1 + n2) % 2 == 0:
    par_impar = 'A soma dos valores é par!'
else:
    par_impar = 'A soma dos valores é ímpar!'
print(f'{par_impar}')
if (n1 * n2) > 40:
    resultado = (n1 * n2)/(n1 // n2)
    print(f'O resultado do produto pela divisão inteira é: {resultado}')
else:
    print(f'A multiplicação de {n1} e {n2} não foi maior que 40!')