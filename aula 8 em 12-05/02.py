#02 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece as vogais a,e,i,o,u.

frase = input('digite uma frase: ').lower()

a=0
e=0
i=0
o=0
u=0

for letra in frase:
    if letra == 'a':
        a += 1
    if letra == 'e':
        e += 1
    if letra == 'i':
        i += 1
    if letra == 'o':
        o += 1
    if letra == 'u':
        u += 1

print(f'a letra a aparece {a} vezes')
print(f'e letra a aparece {e} vezes')
print(f'i letra a aparece {i} vezes')
print(f'o letra a aparece {o} vezes')
print(f'u letra a aparece {u} vezes')