class Televisao:
     def __init__(self,marca, tamanho):
           self.ligada = False
           self.canal = 2
           self.marca = marca
           self.tamanho = tamanho
     def muda_canal_para_baixo(self):
           self.canal -= 1
     def muda_canal_para_cima(self):
           self.canal += 1

tv1 = Televisao("samsung", 42)
tv2 = Televisao("Phillips", 50)
print("TV1")
print("marca:", tv1.marca, tv1.tamanho, "polegadas")
print("TV2")
print("marca:", tv2.marca, tv2.tamanho, "polegadas")