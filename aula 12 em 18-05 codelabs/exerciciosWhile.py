# NÃO PODE UTILIZAR LISTAS COMPOSTAS, NEM DICIONÁRIOS, APENAS WHILE:

#01 - Crie um programa que leia dois valores e mostre um menu na tela:
   # [ 1 ] somar
   # [ 2 ] multiplicar
   # [ 3 ] maior
   # [ 4 ] novos números
   # [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

# n1 = float(input('Digite o primeiro número: '))
# n2 = float(input('Digite o segundo número: '))
# menu = 0
# while menu != 5:
#    menu = int(input('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair\nDigite a opção desejada: '))
#    if menu == 1:
#       print(f'O valor da soma de {n1} e {n2} é: {n1+n2}')
#    if menu == 2:
#       print(f'O valor da multiplicação de {n1} e {n2} é: {n1*n2}')
#    if menu == 3:
#       if n1 > n2:
#          print(f'O maior número é: {n1}')
#       elif n1 < n2:
#          print(f'O maior número é: {n2}')
#       else:
#          print('Os números são iguais.')
#    if menu == 4:
#       n1 = float(input('Digite o primeiro número: '))
#       n2 = float(input('Digite o segundo número: '))

#02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
   #  A) quantas pessoas tem mais de 18 anos.
   #  B) quantos homens foram cadastrados.
   #  C) quantas mulheres tem menos de 20 anos.

#03 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
   # A) qual é o total gasto na compra.
   # B) quantos produtos custam mais de R$1000.
   # C) qual é o nome do produto mais barato.

nome = preco = continuar = 0
nomes = []
precos = []
while True:
   nome = input('Digite o nome do produto: ')
   preco = float(input('Digite o preço do produto: '))
   nomes.append(nome)
   precos.append(preco)
   continuar = input('Deseja continuar? [S/N]').upper()
   if continuar not in 'S':
      break

print(f'O total gasto na compra foi: {sum(precos):.2f}')

count = 0
for i in precos:
   if i > 1000:
      count += 1
print(f'O número de produtos com valor acima de R$1000 foi: {count}.')


barato = min(precos)
pos = precos.index(barato)
print(f'O mais barato foi: {nomes[pos]}')

while precos.count(barato) != 1:
   print('Há outro produto com esse mesmo preço!')
   precos.pop(pos)
   nomes.pop(pos)
   barato = min(precos)
   pos = precos.index(barato)
   print(f'O outro produto neste mesmo preço de R${barato:.2f} foi: {nomes[pos]}')


