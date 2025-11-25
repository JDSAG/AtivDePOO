# Crie uma classe Aluno com nome, matrícula e média final.
# Encapsule os atributos.
# Crie um método que retorne se o aluno está aprovado (média ≥ 7).

class Aluno:
    def __init__(self, nome, matricula):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = []
        self.__media = 0.0 

    @property
    def matricula(self):
        return self.__matricula[0] + '******' + self.__matricula[-1]
    @matricula.setter
    def matricula(self):
        self.__matricula 
    
    @property
    def nome(self):
        return self.__nome 
    @nome.setter
    def nome(self):
        self.__nome

    @property 
    def media(self):
        return self.__media 
    def calcular_media(self): 
        """Calcular a media atraves da função (adicionar_notas), complicado viu"""
        if self.__notas:
            self.__media = sum(self.__notas) / len(self.__notas)

    @property
    def notas(self):
        return self.__notas
    
    def adicionar_nota(self,valor):
        """Requer no minimo 2 notas, não pode ser negativo, e se possivel atraves de input, só coloca saporra"""
        if valor < 0:
            print(f'Nota Invalida, Não é possivel colocar nota negativa ao aluno')
            return False
        elif valor > 10:
            print ("Nota invalida, Não é possivel colocar nota acima de 10 para o aluno ")
        if valor >= 0 and valor <= 10:
            self.__notas.append(valor)
            self.calcular_media() 
            print ("Nota Adicionada com sucesso")
            return True 
    def situacao(self): #Nao ta dando certo de nenhuma forma, vo ver essa 
        self.calcular_media() #Tentando chamar a media 
        if self.__media >= 7:
            return "Aluno Aprovado!"
        elif self.__media < 7:
            return "Aluno Reprovado!"
