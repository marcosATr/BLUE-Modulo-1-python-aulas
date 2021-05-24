#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.
def retirar_vogais(frase):
    vogais = 'aeiou'
    frase.lower()
    count = 0
    dicio_vogais= {}
    for i in vogais:
        count = frase.count(i)
        dicio_vogais[i] = count
    total = sum(dicio_vogais.values())
    print(f'O total de vogais a serem retiradas da frase: {total}\n')
    print(f'As vogais aparecem da seguinte maneira:\n{dicio_vogais}\n')
    ###### REMOVENDO AS VOGAIS:
    for j in frase:
        if j in vogais:
            frase = frase.replace(j, '')
    print(f'A frase sem as vogais é:\n{frase.capitalize()}')


retirar_vogais('lorem ipsum dolor sit amet consectetur adipiscing elit.')