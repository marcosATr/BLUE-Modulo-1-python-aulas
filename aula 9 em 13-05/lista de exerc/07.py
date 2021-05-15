#02 - Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


a = input("Telefonou para a vítima? ").lower()
b = input("Esteve no local do crime? ").lower()
c = input("Mora perto da vítima? " ).lower()
d = input("Devia para a vítima? " ).lower()
e = input("Já trabalhou com a vítima? " ).lower()

respostas = [a, b, c, d, e]
sims = respostas.count("sim")

if sims < 2:
    print('suspeito')
elif sims == 2:
    print('suspeito')
elif sims == 3 or sims == 4:
    print('cúmplice')
elif sims == 5:
    print('assassino')