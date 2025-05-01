class Funcionarios:
    def _init_(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

       

    def get_nome(self):
         return self.__nome
     
    def set_nome(self,nome):
         self.__nome = nome

    def get_cpf(self):
        return self.__cpf
         
    
    def set_cpf(self,cpf):
         self.__cpf= cpf
        

    def get_salario(self):
        return self.__salario
     
    def set_salario(self,salario):
         self.__salario = salario
   
    def exibir_dados(self):
        print(f'nome: {self.__nome}')
        print(f'cpf: {self.__cpf}')
        print(f'salario: {self.__salario}')
        



class Gerente(Funcionarios):
    def _init_(self, nome, cpf, salario, bonus):
        super()._init_(nome, cpf, salario)
        self.__bonus = bonus

    def get_bonus(self):
         return self.__bonus
     
    def set_bonus(self,bonus):
         self.__bonus = bonus
    
    
       
    def exibir_dados(self):
        # print(f'nome: {self.__nome}')
        # print(f'cpf: {self.__cpf}')
        # print(f'salario: {self.__salario}')
        super().exibir_dados()
        print(f'bonus: {self.__bonus}')
        print(f'salario final: {self.get_salario() + self.__bonus}')


class Operacional(Funcionarios):
    def _init_(self, nome, cpf, salario, turno):
        super()._init_(nome, cpf, salario)
        self.__turno = turno

    def get_turno(self):
         return self.__turno
     
    def set_turno(self,turno):
         self.__turno = turno
    
    
       
    def exibir_dados(self):
        # print(f'nome: {self.__nome}')
        # print(f'cpf: {self.__cpf}')
        # print(f'salario: {self.__salario}')
        super().exibir_dados()
        print(f'turno: {self.__turno}')
       
        
       
        

gerente1 = Gerente('Zé Maria','444-232-564-90',6000.0,6000.0)

operacional1 = Operacional('Conrado','55-666-123-16',500,'integral')

gerente1.exibir_dados()
operacional1.exibir_dados()