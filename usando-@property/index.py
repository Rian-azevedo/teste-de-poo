class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade
    
    @property
    def idade(self,):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade
        else:
            print("idade nao pode ser negativa")