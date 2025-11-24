#Crie uma classe Produto contendo: nome, preço e quantidade em estoque.
# Encapsule os atributos.
# Crie métodos para adicionar e remover itens do estoque.
# Garantir que quantidade não seja negativa.

class Produto:
    def __init__(self,nome,preco,estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self):
        self.__nome    
    @property 
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self): 
        self.__preco
    @property 
    def estoque(self):
        return self.__estoque 
    def adicionar(self, valor):
        if valor <= 0:
            print(f"Não é possivel adicionar uma quantidade negativa ao estoque de {self.__nome}") 
            return False 
        if valor >= 0:
            self.__estoque += valor 
            print(f"Adicionado {valor} ao estoque de {self.__nome}")
            print(f"Estoque Atualizado com sucesso")
            return True 
        
    def remover(self,valor):
        if valor >= self.__estoque:
            print (f"ERRO!!! Quantidade Inserida é Maior que o estoque {self.__nome}, não foi possivel fazer a remoção")
            return False
        if valor <= self.__estoque:
            self.__estoque -= valor 
            print (f"Removido {valor} do estoque de {self.__nome}")
            print (f"Estoque Atualizado com sucesso") 
            return True 



