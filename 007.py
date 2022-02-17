#7) Modifique o método resumo da classe Conta para exibir o nome e o telefone de cada cliente.
class Conta:
     def __init__(self, clientes, número, nome, telefone, saldo = 0):
         self.saldo = 0
         self.clientes = clientes
         self.nome = nome
         self.telefone = telefone
         self.número = número
         self.operações = []
         self.deposito(saldo)
     def resumo(self):
         print("CC N°: %s \nSaldo: %10.2f\nTelefone: %s" %
               (self.número, self.saldo, self.telefone))
     def saque(self, valor):
         if self.saldo >= valor:
               self.saldo -= valor
               self.operações.append(["SAQUE", valor])
     def deposito(self, valor):
         self.saldo += valor
         self.operações.append(["DEPÓSITO", valor])
     def extrato(self):
         print("Extrato CC N° %s\n" % self.número)
         print("Cliente %s\n" % self.nome)
         for o in self.operações:
               print("%10s %10.2f" % (o[0],o[1]))
         print("\n  Saldo: %10.2f\n" % self.saldo)


class ContaEspecial(Conta):
     def __init__(self, clientes, número, saldo = 0, limite=0):
         Conta.__init__(self, clientes, número, saldo)
         self.limite = limite
     def saque(self, valor):
         if self.saldo + self.limite >= valor:
               self.saldo -= valor
               self.operações.append(["SAQUE", valor])

print("testando a classe")
tst = Conta(0000,122112212,'xaxa','8699545-8512')
print(tst.resumo())
