# 01 - Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha:

senha = 123
password = int(input('digite sua senha: '))
while password != senha:
    print('Senha incorreta! Digite novamente.')
    password = input('digite sua senha novamente: ')
print("Seja bem-vindo(a)")