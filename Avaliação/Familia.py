class Pessoa:

    def __init__(self, nome, idade, cpf, endereço, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__endereço = endereço
        self.__sexo = sexo

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def cpf(self):
        return self.__cpf
    @property
    def endereço(self):
        return self.__endereço
    @property
    def sexo(self):
        return self.__sexo
     
class Pai(Pessoa):
    
    def __init__(self, nome, idade, cpf, endereço, sexo):
        super().__init__(nome, idade, cpf, endereço, sexo)

p = Pai('Wendell', 50, '123456789321', 'Rua t-44 Nº 52 Setor Bueno', 'Masculino')
print(p.nome)
print(p.idade)
print(p.cpf)
print(p.endereço)
print(p.sexo)

class Mae(Pessoa):
    
    def __init__(self, nome, idade, cpf, endereço, sexo):
        super().__init__(nome, idade, cpf, endereço, sexo)

m = Mae('Josefina Maria', 21, '987654321987', 'Rua t-44 Nº 52 Setor Bueno', 'Feminino')
print(m.nome)
print(m.idade)
print(m.cpf)
print(m.endereço)
print(m.sexo)

class Filho(Pessoa):
    
    def __init__(self, nome, idade, cpf, endereço, sexo):
        super().__init__(nome, idade, cpf, endereço, sexo)

f = Filho('Yan Candido', 4, '741852963123', 'Rua t-44 Nº 52 Setor Bueno', 'Masculino')
print(f.nome)
print(f.idade)
print(f.cpf)
print(f.endereço)
print(f.sexo)