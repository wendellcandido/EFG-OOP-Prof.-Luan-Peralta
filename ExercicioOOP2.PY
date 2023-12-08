class Carro:
    cor = 'Cada parte uma cor' # por ser string tem q usar aspas '
    marca = 'Do papai...'
    modelo = 'É o que tem'

    def ligar_motor(self): #self diz sobre objeto, ele busca 
        print('ligar Motor/Vrum, Vrummm...')
    def Partida(self):
        print('Andar, vai, vai...')
    def Parar(self):    
        print('Para, paraaaaaa Porraaaa...')
    def cor_do_carro(self): #self. serve para ele buscar/executar a referencia 
        print(self.cor)
    
            
carrinho = Carro() 
print(carrinho.cor) 
carrinho.ligar_motor()
print('Desligar')  


print('\n'+'#'*10,  'Novo Objeto', '#'*10 + '\n')

novo_carro = Carro() # possivel criar nova classe dentro do msm classe
novo_carro.cor = 'Azul bebe'
novo_carro.marca = 'Audi'
novo_carro.modelo = 'do papai' 
novo_carro.ligar = 'Ligar Motor'
novo_carro.andar = 'celera Garoto...'
novo_carro.parar = 'Paraaaa... paraaaaaaa jisuissss...'
novo_carro.desligarmotor = 'Desligar Motor'


print(novo_carro.cor)
print(novo_carro.marca) 
print(novo_carro.modelo)
print(novo_carro.ligar)
print(novo_carro.andar)
print(novo_carro.parar)
print(novo_carro.desligarmotor)
