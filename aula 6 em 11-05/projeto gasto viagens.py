# PROJETO: bora começar
# Gastos com viagem - Escrever uma aplicação utilizando funções que calculem os 
# gastos com passagem, hospedagem, aluguel de carro e gastos extras
#  de uma viagem para uma determinada cidade.
# 
# Hospedagem1 -Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.
# 
# Passagem2 -Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que passagem para:
# 
# -São Paulo custa R$ 312,00;
# -Porto Alegre custa R$ 447,00;
# -Recife custa R$ 831,00;
# -Manaus custa R$ 986,00.
# 
# Aluguel de Carro3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
# -Calcule o custo do aluguel do carro sendo que:
# -A cada dia o carro custa R$ 40,00;
# -Alugando 7 dias ou +: R$ 50,00 de desconto;
# -Alugando 3 dias ou +: R$ 20,00 de desconto;
# -Você pode receber apenas um desconto;
# -Retorne o custo.Cálculo Total4 

# -Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.
# 
# -Reutilize as funções já criadas.
# -Exiba o total da viagem chamando apenas a nova função declarada!
# 
# Gastos Extras 5 
# -Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e some esse valor ao total da viagem.
# 
# Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais.

def custo_hotel(noites):
    valor = noites * 140 #ajustar o valor da diária aqui
    return valor


def custo_aviao(cidade):
    local = {
        'São Paulo': 312,
        'Porto Alegre': 447,
        'Recife': 831,
        'Manaus': 986,
    }
    preco = local[cidade]
    return preco


def custo_carro(noites):
    diaria_do_carro = 40
    aluguel = diaria_do_carro * noites
    if noites >= 7:
        aluguel -= 50
    elif noites >= 3:
        aluguel -= 20
    return aluguel


def funcTotal(noites, cidade, gastos_extras):
    custo_final = custo_hotel(noites) + custo_aviao(cidade) + custo_carro(noites) + gastos_extras
    print(f'O valor total da sua viagem foi: {custo_final}')


funcTotal(12, 'Manaus', 800)

