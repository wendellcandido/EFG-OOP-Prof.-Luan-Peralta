## Prog Otientada Objetos, tudo no python e classe, 
# classe; e de onde os obj vem, a forma (instancia), objt são gerados a partir das classes; objeto.
# objeto; tem atributos caracteristas e tem funções. um grupo de objetos cria aplicação/programa.
# metodo: o que ela faz ou comportamento. 
# atributo; as caracteristicas as variaveis.
# para efenir uma classe "class Nome" (a 1ª letra do nome sempre Maisc.

class Carro:
    cor = 'vermelho' # por ser string tem q usar aspas '
    marca = 'toyota'
    modelo = 'Yaris'

    def ligar_motor(self): #self diz sobre objeto, ele busca 
        print('Vrum, Vrum...')
    def cor_do_carro(self): #self. serve para ele buscar/executar a referencia 
        print(self.cor)
            
carrinho = Carro() 
print(carrinho.cor) 
carrinho.ligar_motor()  

print('\n'+'#'*10,  'Novo Objeto', '#'*10 + '\n')

novo_carro = Carro() # possivel criar nova classe dentro do msm classe
novo_carro.cor = 'Azul bebe'
novo_carro.marca = 'audi'
novo_carro.modelo = 'do papai' 
print(novo_carro.cor)
print(novo_carro.marca) 
print(novo_carro.modelo)
novo_carro.ligar_motor()