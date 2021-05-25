class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self. saldo = saldo


    def __str__(self) -> str:
        return f'Olá, {self.titular}. Seu saldo é R${self.saldo}.'


    def sacar(self, valor):
        if self.saldo >= valor:
            print(f'{self.titular}, aguarde a contagem das cédulas.')
            self.saldo -= valor
            print(f'Retire as cédulas.\nSeu novo saldo é R${self.saldo}.')
        else:
            print(f'Saldo insuficiente para sacar R${valor}.\nSeu saldo atual é R${self.saldo}.')

    def depositar(self, deposito):
        self.saldo += deposito
        print(f'Depósito de R${deposito} recebido.\nSeu novo saldo é R${self.saldo}.')





