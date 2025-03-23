class Cachorro:
    def __init__(self,nome,idade,raca,comida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.energia = 100
        self.acordado = False
        self.feliz = False
    
    def comer(self):
        if self.acordado is True:
         self.comida -=1
         print(f"{self.nome} comeu tudinho")
        else:
           print(f"{self.nome} está dormindo e não pode comer") 
    
    def dormir(self):
        self.acordado = False
        self.energia = 100
        print(f"{self.nome} recuperou as energias")
        print(f"{self.nome} está mimindo") 
    
    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado")
    
    def latir(self):
       if self.acordado:
        print(f"{self.nome} Latiu: AU AU!!!")
       else:
        print(f"{self.nome} Cão que dorme não late")
    
    def brincar(self):
       
       if self.acordado:
            if self.energia >= 20:
              self.energia -=20
              self.feliz = True
              print(f"{self.nome} está brincando feliz")
            else:
               print(f"{self.nome} Ta cansadinho")
          
       else:
          print(f"{self.nome} está dormindo e não pode brincar")
    
    def ignorar(self):
       if self.acordado is True:
          self.feliz = False
          print(f"{self.nome} foi ignorado e está triste")
       else:
           print(f"{self.nome} está dormindo")
    


             

cachorro1 = Cachorro("Luke", 8, "Poddle", 3)
cachorro2 = Cachorro("Pitoco", 100, "Golden rebaixado", 100)

cachorro1.acordar()
cachorro1.comer()
cachorro1.dormir()
cachorro1.latir()

cachorro2.acordar()
cachorro2.comer()
cachorro2.ignorar()
cachorro2.comer()
cachorro2.brincar()
