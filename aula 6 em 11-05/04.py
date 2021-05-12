# Exercício 4-Crie um programa que tenha uma função chamada voto ()que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.
def funcVoto(nasc):
    from datetime import datetime, timedelta
    anoAtual = datetime.now().year
    idade = anoAtual - int(nasc)
    print(f'idade: {idade}')
    if idade > 18 and idade < 65:
        print('voto obrigatório')
    elif idade > 16 or idade >= 65:
        print('voto opcional')
    else:
        print('voto negado')

funcVoto(2004)