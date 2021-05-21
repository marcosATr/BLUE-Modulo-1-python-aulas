# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.​​

from datetime import datetime
anoAtual = datetime.now().year
dicio_principal = {}
cadastro= {}
print('Iniciar Cadastro: ')
while True:
   print('~ '* 15)
   nome = input('Digite o nome: ')
   nascimento = int(input('Digite o ano de nascimento no formato YYYY: '))
   ctps = input('''
   Entrada realizada com sucesso. 
   Deseja cadastrar emprego na CTPS?
   [ 1 ] SIM
   [ 0 ] NÃO

      ''')
   if  ctps == '0':
      cadastro = {nome: nascimento}
   else:
      salario = int(input('Digite o salário deste cadastro: '))
      anoContratacao = int(input('Digite o ano da contratação: '))
      idade = anoAtual - nascimento
      prev_aposentadoria = 35 + anoContratacao
      cadastro[nome] = {
         'Idade': idade,
         'Nascimento': nascimento,
         'Salário': salario,
         'Ano de Contratação': anoContratacao,
         'Previsão de Aposentadoria': prev_aposentadoria
      }
   dicio_principal.update(cadastro)
   continuar = input('Continuar? [S/N] ').upper().strip()[0]
   if continuar not in 'S':
      break
print(cadastro)
