## criar uma classe de pessoa, que tenha como atributos: nome, nascimento, CPF, rg, endereço completo, estado civil
# e que tenha como comportamento o calculo da idade, e outro que retorne todos os dados da pessoa formatados
# (da forma como achar melhor). detalhe: a idade não é fornecida, mas sim calculada com base na data de hoje...
from datetime import date
class Pessoa:   
    
    def __init__(self, nome, nascimento, cpf, rg, endereço, estado_civil):    
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.rg = rg
        self.endereço = rg
        self.estado_civil = estado_civil  

    def calcularIdade(self):  
        hoje = date.today()
        idade = hoje.year() - self.nascimento.year
        if hoje.month  < self.nascimento or (hoje.month == self.nascimento.month and hoje.day < self.nascimento.day):
            idade -= 1
        return idade
    
    def retornarDados(self):
        return {
        'nome': self.nome,
        'Data de Nascimento': self.nascimento.strftime('%d/%m/%Y'),
        'CPF': self.cpf,
        'RG': self.rg,
        'Endereço Completo': self.endereço,
        'Estado Civil': self.estado_civil,
        }
    
pessoa1 = Pessoa(
    nome = 'Wendell',
    nascimento = '19/11/1973',
    cpf = '001.002.003-45',
    rg = '123456',
    endereço = 'rua T-444, nº 48 setor Buenos Dias CEP 74150-210',
    estado_civil = 'estilo Fabio Jr.'
)  

pessoa1.nome
pessoa1.nascimento
pessoa1.cpf
pessoa1.rg
pessoa1.endereço
pessoa1.estado_civil

print(pessoa1.retornarDados({nome}, {nascimento}, ))
      
            