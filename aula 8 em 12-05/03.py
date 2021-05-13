
#03 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores.

n = int(input('digite: '))

for i in range(1, n+1):
  if n % i == 0:
    print(i)

