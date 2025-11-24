#Crie uma classe ContaBancaria com os atributos: número da conta, nome do titular e saldo.

class ContaBancaria:
    def __init__(self, number, nome, saldo):
        self.__number = number
        self.__nome = nome
        self.__saldo = saldo
    
    @property
    def number(self):
        return self.__number[0] + '******' + self.__number[-1]
    @number.setter
    def number(self):
        self.__number 
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self):
        self.__nome
        
    @property 
    def saldo(self):
        return self.__saldo
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor 
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("Erro: Valor de depósito deve ser positivo.")
            return False 

    def sacar(self, valor):
        """Saca um valor da conta, se houver saldo suficiente"""
        if valor <= 0:
            raise ValueError("ERRO: Valor de saque deve ser positivo.")
        
        if valor <= self.__saldo:
            self.__saldo -= valor 
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print ("ERRO: Valor da conta INSUFICIENTE para realizar o saque!")
            return False
        