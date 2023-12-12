import datetime

class Pessoa:
    def __init__(self, nome, nascimento, cpf, rg, endereco, estado_civil):
        self._nome = nome
        self._nascimento = nascimento
        self._cpf = cpf
        self._rg = rg
        self._endereco = endereco
        self._estado_civil = estado_civil
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property 
    def nascimento(self):
        return self._nascimento
    
    @nascimento.setter
    def nascimento(self, nascimento):
        self._nascimento = nascimento
    
    @property
    def cpf(self):
        return "***********" + self._cpf[-4:]
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
    
    @property
    def rg(self):
        return "********" + self._rg[-4:]
    @rg.setter
    def rg(self, rg):
        self._rg = rg
    
    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    
    @property
    def estado_civil(self):
        return self._estado_civil
    @estado_civil.setter
    def estado_civil(self, estado_civil):
        self._estado_civil = estado_civil
    
    def calcular_idade(self):
        data_atual = datetime.datetime.now()
        data_nascimento = datetime.datetime.strptime(self._nascimento, "%d/%m/%Y")
        idade = data_atual.year - data_nascimento.year
        if data_atual.month < data_nascimento.month or (data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
            idade -= 1
        return idade
    
    def retornar_dados_formatados(self):
        return f"Nome: {self._nome}\nNascimento: {self._nascimento}\nCPF: {self._cpf}\nRG: {self._rg}\nEndereço: {self._endereco}\nEstado Civil: {self._estado_civil}"


pessoa = Pessoa("Wendell Candido", "19/11/1973", "25485674504", "275652145", "Rua Y-51 Nº 52", "Etilo Fabio Jr")
print(pessoa.calcular_idade())
print(pessoa.retornar_dados_formatados())
print(pessoa.nome)
pessoa.nome = 'tadeu'
print(pessoa.nome)
print(pessoa.nascimento)
pessoa.nascimento = '18/12/1973'
print(pessoa.nascimento)
print(pessoa.cpf)
pessoa.cpf = '123456789123'
print(pessoa.cpf)
print(pessoa.rg)
pessoa.rg = '987654321'
print(pessoa.rg)
print(pessoa.endereco)
pessoa.endereco = 'Rua Z nº 53'
print(pessoa.endereco)
print(pessoa.estado_civil)
pessoa.estado_civil = 'Estilo Grethen'
print(pessoa.estado_civil)
