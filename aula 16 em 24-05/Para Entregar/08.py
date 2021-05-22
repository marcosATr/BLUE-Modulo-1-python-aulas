#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

#OPTEI POR AGRUPAR AS ENTRADAS DE DICIONÁRIOS EM UMA LISTA, PARA EVITAR CONFLITOS ENTRE KEYS

from datetime import datetime
lista = []
def cadastrar():
    dicio = {}
    nome = input('Digite o nome: ')
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = datetime.now().year - nascimento
    ctps = input('Digite a carteira de trabalho (Caso não tenha, digite 0): ')
    #ADICIONAR AO DICIONÁRIO TEMPORÁRIO:
    dicio['nome'] = nome
    dicio['nascimento'] = nascimento
    dicio['idade'] = idade
    dicio['carteira de trabalho'] = ctps
    if ctps not in '0':
        contratacao = int(input('Digite o ano de contratação: '))
        salario = input('Digite o salário: ')
        aposentadoria = contratacao + 35 #DADO QUE O USUÁRIO DEU ENTRADA NO SISTEMA E NÃO FICOU SEM TRABALHAR.
        #ACRESCENTAR AO DICIONÁRIO:
        dicio['ano de contratacao'] = contratacao
        dicio['salario'] =  salario
        dicio['ano aposentadoria'] = aposentadoria
    lista.append(dicio)
    continuar = input('Continuar? [S/N] ').upper().strip()[0]
    if continuar in 'S':
        cadastrar()


cadastrar()
print(lista)
