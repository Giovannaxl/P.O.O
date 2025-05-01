class Produto:
    def _init_(self,nome,preco,quantidade):
         self.__nome = nome
         self.__preco = preco
         self.quantidade = quantidade

    def get_nome(self):
         return self.__nome
     
    def set_nome(self,nome):
         self.__nome = nome

    def get_preco(self):
         return self.__preco
         
    
    def set_preco(self,preco):
         if preco >= 0:
          self.__preco = preco 
         else:
             print("Não é permitido valor negativo!")
    
             
produto1 = Produto("Prego", 1.5, 200)
novoPreco = float(input("Novo preço do produto: "))
produto1.set_preco(novoPreco)
print(f"Preço do {produto1.get_nome()}: {produto1.get_preco()}")