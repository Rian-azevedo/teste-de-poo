class personagem:
    
    def __init__(self, nome, idade, classe):
        self.nome = nome
        self.idade = idade
        self.classe = classe
        self.comida = 10
    
    def poder_de_fogo(self):
        print(f"o {self.nome} atirou uma bola de fogo")
    
    def comer(self):
        if self.comida <= 0:
            print(f"voce tem {self.comida} de comida, precisa comprar mais")
        else:
            self.comida -= 1
            print(f"o {self.nome} esta se alimentando, agora voce tem {self.comida} de comida")
    
    def comprar_comida(self):
        self.comida += 1
        print(f"{self.nome} comprou comida agora seu estoque esta em {self.comida}")
    