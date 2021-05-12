# # DESAFIO-Data com mês por extenso.
# # Construa uma função que receba uma data no
# # formato DD/MM/AAAA
# #  e devolva uma string no formato D de mesPorExtenso de AAAA.
# #
# #  Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
# #  Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.

def funcData(_date):
    #variaveis e fatiamento das strings
    _date = input('digite a data: ')
    day = _date[:2]
    month = _date[3:5]
    year = _date[-4:]

    #VERIFIQUE SE O ANO É BISSEXTO

    ano = int(year)
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print('Ano bissexto.')
    else:
        print('Não é um ano bissexto.')

    #global day, month, year

    dayError = 'Dia inexistente nesse mês'
    monthCheckpoint = int(month)
    dayCheckpoint = int(day)

    if monthCheckpoint > 0 and monthCheckpoint <= 12:
      if month == '01':
          month = 'Janeiro'

          if dayCheckpoint > 31 or dayCheckpoint < 1:
              print(dayError)
              raise TypeError("Only integers are allowed")

      elif month == '02':
          month = 'Fevereiro'

          if dayCheckpoint > 282 or dayCheckpoint < 1:
              print(dayError)
              raise TypeError("Only integers are allowed")

      elif month == '03':
          month = 'Março'
      elif month == '04':
          month = 'Abril'
      elif month == '05':
          month = 'Maio'
      elif month == '06':
          month = 'Junho'
      elif month == '07':
          month = 'Julho'
      elif month == '08':
          month = 'Agosto'
      elif month == '09':
          month = 'Setembro'
      elif month == '10':
          month = 'Outubro'
      elif month == '11':
          month = 'Novembro'
      elif month == '12':
          month = 'Dezembro'

      print(f'{day} de {month} de {year}')
    else:
      month = None
      print('Erro! Mês não existente.')
      return None





funcData(_date)
