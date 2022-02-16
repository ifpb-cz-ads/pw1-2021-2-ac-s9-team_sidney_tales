class Televisão:
     def __init__(self, min, max):
         self.ligada = False
         self.canal = 2
         self.cmin = min
         self.cmax = max
     def muda_canal_para_baixo(self):
         print(self.cmax)
               
     def muda_canal_para_cima(self):
         print(self.cmin)

tv=Televisão(2,10)

tv.muda_canal_para_baixo()

tv.muda_canal_para_cima()