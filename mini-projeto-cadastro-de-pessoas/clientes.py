class clientes:
    def __init__(self, nome, idade, numero, cpf):
         self.nome = nome 
         self.idade = idade
         self.numero = numero
         self.cpf = cpf
    def __str__(self):
        return (f"cadastro feito com sucesso\n nome: {self.nome}, idade: {self.idade}, numero: {self.numero}, cpf: {self.cpf}")

nome = input("digite seu nome?")
idade = int(input("qual sua idade?"))
numero = int(input("qual seu numero?"))
cpf = int(input("digite seu cpf"))
  
cliente1 = clientes(nome, idade, numero, cpf)

print(cliente1)

