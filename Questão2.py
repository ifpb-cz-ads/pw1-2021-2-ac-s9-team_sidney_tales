  
class Televisao:
     def __init__(self, canal):
           self.ligada = False
           self.canal = canal
     def muda_canal_para_baixo(self):
           self.canal -= 1
     def muda_canal_para_cima(self):
           self.canal += 1

canal = int(input("Informe o canal: "))
tv = Televisao(canal)
print("Canal", tv.canal)