

class Quadrado:

    def __init__(self, lado):
       self.__lado = lado
       
       
    @property
    def area(self):
       return self.__lado ** 2
    
    @property
    def perimetro(self):
       return self.__lado * 4
    
   
      
q = Quadrado(4)
print(q.area)
print(q.perimetro)

class Retangulo:

    def __init__(self, base, altura):
       self.__base = base
       self.__altura = altura

    @property
    def area(self):
       return self.__base * self.__altura
    
    @property
    def base(self):
       return self.__base * self.__altura
    
    @property
    def perimetro(self):
       return (self.__base * 2) + (self.__altura * 2)
    
base = float(input('Digite a base: '))    
altura = float(input('Digite altura: '))
    
   
      
r = Retangulo(base, altura)
print(r.base)
print(r.perimetro)

from math import pi

class Circulo:

    def __init__(self, raio):
       self.__raio = raio

    @property
    def area(self):
       return 2* pi * self.__raio   
    
    @property
    def base(self):
       return self.__base * self.__altura
    
    @property
    def perimetro(self):
       return (self.__base * 2) + (self.__altura * 2)
    
base = float(input('Digite a base: '))    
altura = float(input('Digite altura: '))
    
   
      
r = Retangulo(base, altura)
print(r.base)
print(r.perimetro)


    