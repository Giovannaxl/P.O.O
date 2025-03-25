class Carro:
    def __init__ (self,modelo,ano,cor,):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = 0
        self.velocidade = 0
        self.ligado = False
        self.limite_velocidade = 100
        
    
    def ligar(self):
       if self.combustivel >0:
        self.ligado = True
        print(f"O seu {self.modelo} Ligou!!")
       else:
          print(f"Seu {self.modelo} está sem combustivel,toma vergonha na cara e abastece teu carro")
       
    def desligar(self):
       if self.velocidade == 0:
        self.ligado = False
        print(f"O seu {self.modelo} está desligado")
       else:
        print(f"Seu {self.modelo} está em movimento,frea ai boy") 
    
    def acelerar(self):
        if self.ligado is True:
          if self.combustivel >= 5:
                if self.velocidade < self.limite_velocidade:
                    self.velocidade += 10
                    self.combustivel -=5
                    print(f"Seu {self.modelo} está a {self.velocidade} km/h")
                else: 
                 print(f"Seu {self.modelo} está no limite de velocidade,")
          else:
            print(f"Seu {self.modelo} está sem combustivel.")  
        else: 
         print(f"Seu {self.modelo} está desligado, quem é o idiota que acelera um carro desligado.")    
        
    
    def frear(self):
       if self.velocidade > 0:
          self.velocidade -= 10
          print(f"Seu {self.modelo} freou, agora está a {self.velocidade} km/h")
       else:
        print(f"Seu {self.modelo} já está parado,tabacudo")
    
    def abastecer(self,quantidade):
       if self.combustivel + quantidade < 100:
         self.combustivel += quantidade
         print(f"Seu {self.modelo} foi abastecido,combustível: {self.combustivel}")
       else:
          print(f"Abastecimento acima do limite de combustível")
       
    def buzinar(self):
       print(f"{self.modelo}: BEEP BEEP!!")
     
    def status(self):
       print(f"Modelo: {self.modelo}")
       print(f"Ano: {self.ano}:")
       print(f"cor: {self.cor}")
       print(f"combustível: {self.combustivel}")
       print(f"velocidade atual: {self.velocidade} km/h")
       print(f"ligado: {self.ligado}")
       print(f"Limite de velocidade: {self.limite_velocidade} km/h")


             

carro1= Carro("Fusca",1897,"Azul")
carro2= Carro("HB20",2000,"Branca")

carro1.ligar()
carro1.buzinar()
carro1.abastecer(50)
carro1.status()
carro1.ligar()
carro1.acelerar()
carro1.frear()

carro2.abastecer(80)
carro2.ligar()
carro2.buzinar()
carro2.status()
carro1.desligar()
carro1.acelerar()
carro1.ligar()
for i in range(4):
 carro1.acelerar()

carro1.desligar()
for i in range(10):
 carro1.frear()