#8) Crie classes para representar estados e cidades. Cada estado tem um nome, sigla e cidades. 
# Cada cidade tem nome e população. Escreva um programa de testes que crie três estados com 
# algumas cidades em cada um. Exiba a população de cada estado como a soma da população de suas cidades

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
        self.populacao = 0
    def Detalhes(self):
        print(f"Nome: {self.nome} ({self.sigla})\nPopulação Atual: {self.populacao}")
    def AddCidades(self, cidade):
        self.populacao += cidade[1]
        self.cidades.append(cidade)
    def Cidades(self):
        print("cidades:\n")
        for x in self.cidades:
            print(f"  Nome: {x[0]}\n  População Atual: {x[1]}")
        print('')

class Cidade:
    def __init__(self,nome,populacao):
        self.nome = nome
        self.populacao = populacao
    def Detalhes(self):
        print(f"   Nome: {self.nome}\n   População Atual: {self.populacao}")
    def AttPopulacao(self,valor):
        self.populacao += valor
        print(f"Novos {valor} habitantes adicionados a cidade\nPopulação Atual: {self.populacao}")

tst = Estado('Paraiba','PB')
ABC = []
x = -1
while(x != 0):
    a = input("Digite o nome da cidade: ")
    b = int(input("Digite a população atual da cidade: "))
    ABC.append([a,b])
    print("Cidade Adicionada com sucesso!")
    x = int(input("digite qualquer tecla para continuar ou digite 0 para sair: "))

for z in ABC:
    tst.AddCidades(z)
tst.Detalhes()
tst.Cidades()
