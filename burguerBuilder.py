# SEGUNDA VERSÃO DA ATIVIDADE CRIADA PELO PROFESSOR

from abc import ABC, abstractmethod


class portaria(ABC):
    @abstractmethod
    def entrar(self,pessoa):
        pass


class Aluno(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} tem relação com a instituição como Aluno"

class Professor(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} tem relação com a instiuição como Professor"

class Coordenador(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} tem relação com a instituição como Professor"

class Diretor(portaria):
    def entrar(self,pessoa):
        return f"O {pessoa} tem relação com a instituição como Diretor"

class Vestibulando(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} tem relação com a instituição como Vestibulando"

class Administrativo(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} tem relação com a instituição como Administrativo"
class naoPossui(portaria):
    def entrar(self, pessoa):
        return f"O {pessoa} não possui relação com a instituição, acompanhar até a secretaria" 

class FabricaPortaria:
    def criar_pessoa(self,cargo):
        if cargo=="Aluno":
            return Aluno()
        elif cargo=="Professor":
            return Professor()
        elif cargo=="Coordenador":
            return Coordenador()
        elif cargo=="Diretor":
            return Diretor()
        elif cargo=="Vestibulando":
            return Vestibulando()
        elif cargo=="Administrativo":
            return Administrativo()
        else:
            return naoPossui()
    
fabrica_pessoa = FabricaPortaria()
p= str(input("Digite S para cadastrar uma pessoa ou digite Q para sair: "))
if p == "Q":
    print("Não foi informado os dados necessários, finalizando atendimento...")
    exit()
while p!="Q":
    pessoa = fabrica_pessoa.criar_pessoa(str(input("Qual a sua relação com a FATEC: ")))
    print(pessoa.entrar(str(input("Entre com o seu nome: "))))
    print("---------------------------------------------------------------------")
    p= str(input("Digite S para cadastrar outra pessoa ou digite Q para sair: "))




class burguer:
    def __init__(self):
        self.meat = None
        self.bread = None
        self.cheese = None
        self.vegetable = None
        self.sauce = None

    def __str__(self):

        return f"\nSeu lanche foi montado, seu pedido é:\nCarne: {self.meat}\nPão: {self.bread}\nVegetais: {self.vegetable}\nQueijos: {self.cheese}\nMolho: {self.sauce}"
      
class burguerBuilder:
    def __init__(self) -> None:
        self.burguer = burguer()
  
    def build_meat(self):
        print("\n")
        print("//////////////////////////////////////////////////////////////")
        print("///////////////////      CARNES    ///////////////////////////")
        print("//            Digite 1 para colocar Frango Assado           //")
        print("//            Digite 2 para colocar Steak Cheddar Cremoso   //")
        print("//            Digite 3 para colocar Vegetariano             //")
        print("//////////////////////////////////////////////////////////////")
        print("\n")
        meat_statement = int(input("Digite qual opção deseja: "))
        if meat_statement ==  1:
            self.burguer.meat= "Frango assado"
        elif meat_statement == 2:
            self.burguer.meat = "Steak Cheddar Cremoso"
        elif meat_statement == 3:
            self.burguer.meat = "Vegetariano"
        else:
            print("Não possúimos essa carne no cardápio")
    
    def build_bread(self):
        print("\n")
        print("//////////////////////////////////////////////////////////////")
        print("///////////////////      PÃES      ///////////////////////////")
        print("//            Digite 1 para Parmesão                        //")
        print("//            Digite 2 para Italiano Branco                 //")
        print("//            Digite 3 para 9 Grãos                         //")
        print("//////////////////////////////////////////////////////////////")
        print("\n")

        bread_statement = int(input("Digite qual opção deseja: "))
        if bread_statement ==  1:
            self.burguer.bread= "Parmesão"
        elif bread_statement == 2:
            self.burguer.bread = "Italiano Branco"
        elif bread_statement == 3:
            self.burguer.bread = "9 Grãos"
        else:
            print("Não possúimos esse Pão no cardápio")

    def build_vegetable(self):
        print("\n")
        print("//////////////////////////////////////////////////////////////")
        print("///////////////////    Vegetais    ///////////////////////////")
        print("//            Digite 1 para Azeitona                        //")
        print("//            Digite 2 para Alface                          //")
        print("//            Digite 3 para Tomate                          //")
        print("//////////////////////////////////////////////////////////////")
        print("\n")

        bread_statement = int(input("Digite qual opção deseja: "))
        if bread_statement ==  1:
            self.burguer.vegetable= "Azeitona"
        elif bread_statement == 2:
            self.burguer.vegetable = "Alface"
        elif bread_statement == 3:
            self.burguer.vegetable = "Tomate"
        else:
            print("Não possúimos esse vegetal no cardápio")

    def build_cheese(self):
        print("\n")
        print("//////////////////////////////////////////////////////////////")
        print("///////////////////    Queijos     ///////////////////////////")
        print("//            Digite 1 para Cheddar                        //")
        print("//            Digite 2 para Suíço                          //")
        print("//            Digite 3 para Muçarela                          //")
        print("//////////////////////////////////////////////////////////////")
        print("\n")

        bread_statement = int(input("Digite qual opção deseja: "))
        if bread_statement ==  1:
            self.burguer.cheese= "Cheddar"
        elif bread_statement == 2:
            self.burguer.cheese = "Suíço"
        elif bread_statement == 3:
            self.burguer.cheese = "Muçarela"
        else:
            print("Não possúimos esse queijo no cardápio")

    def build_sauce(self):
        print("\n")
        print("//////////////////////////////////////////////////////////////")
        print("///////////////////    Molhos     ///////////////////////////")
        print("//            Digite 1 para Barbecue                       //")
        print("//            Digite 2 para Chipotle                       //")
        print("//            Digite 3 para Supreme                        //")
        print("//////////////////////////////////////////////////////////////")
        print("\n")

        bread_statement = int(input("Digite qual opção deseja: "))
        if bread_statement ==  1:
            self.burguer.sauce= "Barbecue"
        elif bread_statement == 2:
            self.burguer.sauce = "Chipotle"
        elif bread_statement == 3:
            self.burguer.sauce = "Supreme"
        else:
            print("Não possúimos esse molho no cardápio")


    def get_burguer(self):
        return self.burguer

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_burguer(self):
        self.builder.build_meat()
        self.builder.build_bread()
        self.builder.build_vegetable()
        self.builder.build_cheese()
        self.builder.build_sauce()

print("\n")
print("//////////////////////////////////////////////////////////////")
print("//            Digite 1 para ir para a sala de aula          //")
print("//            Digite 2 para ir para a FATEC Way             //")
print("//////////////////////////////////////////////////////////////")
print("\n")

a = int(input("Você deseja ir para sala de aula ou comer um lanche em nosso restaurant FATEC way?: "))

if a == 1:
    print("Você irá para a sala de aula Maker no segundo andar")
else:
    print("Iniciando atendimento...")
    hamburguer = burguerBuilder()
    diretor = Director(hamburguer)
    diretor.construct_burguer() 
    lanche = hamburguer.get_burguer()
    print(lanche)


