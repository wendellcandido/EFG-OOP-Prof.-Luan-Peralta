               #dunder (undrline duplo) 
class Carro:  ## __INIT__: serve para inicializar atributos
    #def __init__(self, marca, modelo, ligar, andar, parar):
     # pass; usado para um inicializador vazio, tem que ter se usar INIT 
    marca = 'Do Papai'
    modelo = 'Quase Meu...'
    ligado = False
    andando = False
    

    def ligar(self):
        self.ligado = True
        print('Estou ligando')
    
    def desligar(self):
        self.ligado = False
        print('Estou Desligando, carai.....')  

    def andar(self):
        self.andando = True
        print('Vms começar a andar') 

    def parar(self):
        self.andando = False
        print('Paraaaaa....') 

    

    def exebir_informações_do_carro(self):
        ligado = "Ligado" if self.ligado else "Desligado"
        movimento = "Andando" if self.andando else "Parado"

        print(self.marca, self.modelo, ligado, movimento)


carro1 = Carro()
carro1.ligar()
carro1.andar()
carro1.parar()
carro1.desligar()
carro1.exebir_informações_do_carro() 
carro1.andar()
carro1.parar()         
carro1.exebir_informações_do_carro() 
