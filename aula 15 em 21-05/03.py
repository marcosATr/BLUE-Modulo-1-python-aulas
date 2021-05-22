# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Palíndromo, do grego palin (novo) e dromo (percurso), é toda palavra ou frase que pode ser lida de trás para a frente e que, independentemente da direção, mantém o seu sentido. Ex: arara, asa, ovo, oco.

frase = input('Digite uma frase: ').lower()
frase = frase.replace(' ', '') #desconsidere os espaços.
#INVERTER A FRASE:
comprimento = len(frase) -1
frase_rev = ''
for x in range(comprimento, -1, -1): #Eu podia ter colocado numa lista e usado reverse, mas achei que ia ser cheat! ;)
    frase_rev += frase[x]
if frase == frase_rev:
    print('A frase é palindrômica!')
else:
    print('A frase não é palindrômica!')
print(frase_rev)