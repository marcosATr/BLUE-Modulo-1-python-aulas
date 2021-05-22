#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

perguntas = [
    "Telefonou para a vítima? [S/N] ",
    "Esteve no local do crime? [S/N] ",
    "Mora perto da vítima? [S/N] ",
    "Devia para a vítima? [S/N] ",
    "Já trabalhou com a vítima? [S/N] "
]
sims = 0
# respostas = [] #Não quero perder as respostas.
for pergunta in perguntas:
   r = input(pergunta).upper()[0]
   if r in "S":
       sims +=1
print(f'O número de respostas SIM foram {sims}.')
if sims == 2:
    print(f'Classificação: Suspeito')
elif sims > 4:
    print(f'Classificação: Assassino')
elif sims > 2:
    print(f'Classificação: Cúmplice')
else:
    print(f'Classificação: Inocente')
