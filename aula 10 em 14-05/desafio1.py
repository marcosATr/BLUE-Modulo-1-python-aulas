# DESAFIO:

# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 

# Os códigos utilizados são:
# 1 , 2, 3  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;


# Candidato AAA - 1
# Candidato BBB - 2
# Candidato CCC - 3
# Candidato DDD - 4
# Voto nulo - 5
# Voto Branco - 6


#Iniciar Votação

voto = 0
computados =[]
while voto != 'encerrar':
    voto = input('digite seu voto: ')
    computados.append(voto)
    
aaa = computados.count('1')
bbb = computados.count('2')
ccc = computados.count('3')
ddd = computados.count('4')
brancos = computados.count('6')
nulos = len(computados) - aaa - bbb - ccc - ddd - brancos -1 #-1 é importante para não contar o encerrar!

print(f'O candidato AAA obteve {aaa} votos')
print(f'O candidato BBB obteve {bbb} votos')
print(f'O candidato CCC obteve {ccc} votos')
print(f'O candidato DDD obteve {ddd} votos')
print(f'Foram {nulos} votos nulos')
print(f'Foram {brancos} votos em branco')
    

