class ContaCorrente():
    def __init__(self, saldo, percentualImposto):
        self.__saldo = saldo
        self.__percentual = percentualImposto

    @property
    def saldo(self):
        pass
    @property
    def percentualImposto(self):
        pass
    @property
    def calcularImposto(self) -> int:
        return self.__saldo - (self.__saldo * self.__percentual)
 
class Poupança(ContaCorrente):
    def __init__(self, saldo, percentualImposto):
        super().__init__(saldo, percentualImposto)

    @property
    def calcularImposto(self):
        return super().calcularImposto
    
    
class ContaImposto(ContaCorrente):
    def __ini__(self, saldo, percentualImposto):
        super().__init__(saldo, percentualImposto)

    @property
    def calcularImposto(self):
        return super().calcularImposto

coCorrent = ContaCorrente(500, 0.2)
print(f'{coCorrent.calcularImposto:.2f}') 

poup = Poupança(600,0.1)
print(f'{poup.calcularImposto:.2f}')

conImposto = ContaImposto(400,0.01)
print(f'{conImposto.calcularImposto:.2f}')



       

