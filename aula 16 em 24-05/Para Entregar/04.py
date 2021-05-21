#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.
def func_data(_date):
    import sys
    lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    lista_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    try:
        #variaveis e fatiamento das strings
        day = int(_date[:2])
        month = int(_date[3:5])
        year = int(_date[-4:])
    except (ValueError, TypeError):
        print('A data selecionada é inválida!')
        sys.exit(1)
    #VERIFIQUE SE O ANO É BISSEXTO
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Ano bissexto!') #ATUALIZANDO LISTA DE DIAS!
        ano_bissexto = True
        lista_dias.pop(1)
        lista_dias.insert(1, 29)
    #SUBSTITUINDO POR MÊS POR EXTENSO:
    posicao = month -1 #porque a lista começa com index 0
    #VALIDAÇÃO extra DA DATA:
    if not 0 < day <= lista_dias[posicao]:
        print('Dia inválido.')
    elif not 0 < month < 13:
        print('Mês inválido.')
    elif not 0 < year:
        print('Ano Inválido')
    else:
        month = lista_meses[posicao] #A ALTERAÇÃO DO MÊS SÓ PODE SER REALIZADA APÓS A VALIDAÇÃO.
        print(f'Data: {day} de {month} de {year}')


func_data('26/02/0008')
