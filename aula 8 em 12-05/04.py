#04 - Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

frase = input('digite sua frase: ')
d = ['a', 'e', 'i', 'o', 'u']
for i in d:
    frase = frase.replace(i, "")
print(frase)