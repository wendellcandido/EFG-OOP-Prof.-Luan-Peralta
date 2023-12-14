
   ###### QUADRADO
#class FormaGeometrica:
#
#    def __init__(self, lado):
#       self.__lado = lado
#       
#    @property
#    def area(self):
#       pass
#    
#    @property
#    def perimetro(self):
#       pass
#    
#    @property
#    def lado(self):
#       return self.__lado
#    
#class Quadrado(FormaGeometrica): ## heranã manda os atributos formageometrica ele busca a classe que ele esta
#    
#    def __init__(self, lado):
#     super().__init__(lado)
#   
#    @property
#    def area(self):
#      return self.lado ** 2
#    
#    @property
#    def perimetro(self):
#       return (self.lado * 2) + (self.area *2)
#        
#        
#q = Quadrado(4)
#print(q.area)
#print(q.perimetro)

  ###### RETANGULO
#class FormaGeometrica:
#
#    def __init__(self, lado):
#       self.__lado = lado
#       
#    @property
#    def area(self):
#       pass
#    
#    @property
#    def perimetro(self):
#       pass
#    
#    @property
#    def lado(self):
#       return self.__lado
#    
#
#class Retangulo(FormaGeometrica):
#   def __init__(self, base, altura):
#       super().__init__(base)
#       self.__altura = altura
#
#   @property
#   def area(self):
#       return self.base * self.__altura
#     
#   @property
#   def altura(self):
#       return self.__altura 
#    
#   @property
#   def base(self):
#       return super().lado
#   
#   @property
#   def perimetro(self):
#       return(self.base * 2) + (self.altura * 2)
#   
#base = float(input('Digite a base: '))    
#altura = float(input('Digite altura: ')) 
#     
#r = Retangulo(base, altura)
#print(r.area)
#print(r.perimetro)


   ###### CIRCULO

from math import pi

class FormaGeometrica:

    def __init__(self, raio):
       self.__raio = raio
           
    @property
    def perimetro(self):
       pass
    
    @property
    def area(self):
       pass
    
class Circulo(FormaGeometrica):
   def __init__(self, base, altura):
       super().__init__(base)
       self.__altura = altura

   @property
   def area(self):
       return self.base * self.__altura
     
   @property
   def altura(self):
       return self.__altura 
    
   @property
   def base(self):
       return super().lado
   
   @property
   def perimetro(self):
       return(self.base * 2) + (self.altura * 2)
   
base = float(input('Digite a base: '))    
altura = float(input('Digite altura: ')) 
     
r = Retangulo(base, altura)
print(r.area)
print(r.perimetro)
#class Circulo:
#
#    def __init__(self, raio):
#       self.__raio = raio
#
#    @property
#    def perimetro(self):
#       return 2 * pi * self.__raio   
#    
#      
#    @property
#    def area(self):
#       return pi * raio ** 2
#    
#
#raio = float(input('Digite valor do raio para obter a circunferência: '))
#circulo = Circulo(raio)
#
#print(f"A área do círculo é: {circulo.area:.2f}")
#
##print(f'A cincunfêrencia do circulo é: {circulo.perimetro:.2f}')
#    
#from math import 
#
#class FormaGeometrica: ##herança de outras classes
#   pass
#
#class Triangulo:
#
#    def __init__(self, base, altura, lado_a, lado_b, lado_c, angulo_ab, angulo_ac, angulo_bc):
#       self.__base = base
#       self.__altura = altura
#       self.__lado_a = lado_a
#       self.__lado_b = lado_b
#       self.__lado_c = lado_c
#       self.__angulo_ab = angulo_ab
#       self.__angulo_ac = angulo_bc
#
#
#    @property
#    def perimetro(self):
#       return 2 * pi * self.__raio   
#    
#      
#    @property
#    def area(self):
#       return pi * raio ** 2
#    
#
#ase = float(input("digite o valor:"))
#altura = float(input("digite o valor:"))
#lado_1 = float(input("digite o valor:"))
#lado_2 = float(input("digite o valor:"))
#
#area_triangulo = (base*altura)/2
#
#perimetro_triangulo = base + lado_1 + lado_2
#
#print("área", area_triangulo)
#print("perimetro", perimetro_triangulo)    
#

    