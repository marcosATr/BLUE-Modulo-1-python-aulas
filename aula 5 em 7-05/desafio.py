def funcData(_date):
#variaveis e fatiamento das strings
    day = _date[:2]
    month = _date[3:5]
    year = _date[-4:]
    
    #VERIFIQUE SE O ANO É BISSEXTO
    ano = int(year)
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        #print('Ano bissexto.')
        ano = 'bissexto'


    
    dayError = 'Dia inexistente nesse mês'

    if int(month) > 0 and int(month) <= 12:
      if month == '01':
          month = 'Janeiro'

          if int(day) > 31 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")

      elif month == '02':
          month = 'Fevereiro'

          if ano == 'bissexto':
            if int(day) > 29 or int(day) < 1:
                print(dayError)
                raise TypeError("Nesse ano Fev vai até 29")
          else:
            if int(day) > 28 or int(day) < 1:
                print(dayError)
                raise TypeError("Esse mês vai só até 28")

      elif month == '03':
          month = 'Março'
          if int(day) > 31 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")
      elif month == '04':
          month = 'Abril'
          if int(day) > 30 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")
      elif month == '05':
          month = 'Maio'
          if int(day) > 31 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")
      elif month == '06':
          month = 'Junho'
          if int(day) > 30 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")
      elif month == '07':
          month = 'Julho'
          if int(day) > 31 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")
      elif month == '08':
          month = 'Agosto'
          if int(day) > 31 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")
      elif month == '09':
          month = 'Setembro'
          if int(day) > 30 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")
      elif month == '10':
          month = 'Outubro'
          if int(day) > 31 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")
      elif month == '11':
          month = 'Novembro'
          if int(day) > 30 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")
      elif month == '12':
          month = 'Dezembro'
          if int(day) > 31 or int(day) < 1:
              print(dayError)
              raise TypeError("Dia inexistente nesse mês")

      print(f'{day} de {month} de {year}')
    else:
      month = None
      print('Erro! Mês não existente.')
      return None

    

a = input('digite a data: ')
funcData(a)