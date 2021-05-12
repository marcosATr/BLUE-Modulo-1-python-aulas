def funcData(_date):
#variaveis e fatiamento das strings
    day = _date[:2]
    month = _date[3:5]
    year = _date[-4:]
    
    #VERIFIQUE SE O ANO É BISSEXTO
    ano = int(year)
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print('Ano bissexto.')
    else:
        print('Não é um ano bissexto.')

    
    dayError = 'Dia inexistente nesse mês'

    if int(month) > 0 and int(month) <= 12:
      if month == '01':
          month = 'Janeiro'

          if int(day) > 31 or int(day) < 1:
              print(dayError)
              raise TypeError("Only integers are allowed")

      elif month == '02':
          month = 'Fevereiro'

          if int(day) > 282 or int(day) < 1:
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

    

a = input('digite a data: ')
funcData(a)
