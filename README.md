#lista de palvras
palavras = ("goleiro,juiz,gol")

# calculando o total de letras da palavras
palavras_maior= [0]
palavra_menor=[0]


 #comparando o total de letras na palavras

if len(palavras_maior) > len(palavra_menor):
  print("a palavra_maior é maior")
    
elif len(palavra_menor) < len(palavras_maior):
    print("a palavra_menor e maior")
    
else:
    print("as duas palavras tem a mesma quantidade de letras")
        


                 
class Carro:
    def __init__ (self,marca,modelo,cor,ano,valor):
        self.marca=marca
        self.modelo=modelo
        self.cor=cor
        self.ano=ano 
        self.valor=valor 
class Estoque:
    def __init__(self):
        self.carros=[]
    def Adicionar_Carro(self,carro):
            self.carros.append(carro)
    def Mostra_Estoque(self):
        for carro in self.carros:
            print(F'{carro.modelo}, {carro.marca} ')
        
        
carro_1=Carro('mustang','shelby','preto', '2020', 50000 )
carro_2=Carro('koenigsegg', 'jesko', 'verde neon', '2024',30000000)
carro_3=Carro('bugatti','chiron', 'fosco', '2024', 55000000)
        
estoque=Estoque()
estoque.Adicionar_Carro(carro_1)
estoque.Adicionar_Carro(carro_2)
estoque.Adicionar_Carro(carro_3)
    
estoque.Mostra_Estoque()
                
