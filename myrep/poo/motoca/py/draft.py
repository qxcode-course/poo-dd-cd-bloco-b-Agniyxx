class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade 
    
    def __str__ (self):
        return self.__nome: self.__idade
  
class Moto:
    def __init__(self, potencia:int = 1):
        self.pessoa: Pessoa | None = None
        self.potencia = potencia
        self.tempo = 0

    def enter(self, pessoa: Pessoa) -> bool:
        if self.pessoa != None:
            print("moto ocupada")
            return False
        self.pessoa = pessoa
        return True

    def remove(self) -> Pessoa| None:
        if self.pessoa == None:
            print("moto vazia")
            return None
        aux: Pessoa = self.pessoa
        self.pessoa = None
        return aux
    
    def comprarTempo(self, time: int):
        if time <= 0:
            print("fail: tempo invalido")
            return
        self.tempo += time

    def drive(self, time: int):
        if self.pessoa == None:
            print("fail: não ha ninguem na moto")
            return
        if self.pessoa.get_idade() < 10:
            print("fail: muito jovem pra pilotar")
            return
        if self.tempo == 0:
            print("fail: primeiro compre tempo")
            return
        if time > self.tempo: 
            print(f"fail: tempo acabou após andar {self.tempo} minutos")
        else:
            self.tempo -= time

    def honk(self):
        print("P" + "e" * self.potencia "m")

    def show(self):
        print(self)
    
    def __str__(self) -> str:
        return f"power:{self.potencia}, time:{self.tempo}, person:{self.pessoa}"
    
def main():
    moto = Moto()
    while True:
        line:str = input()
        print(f"${line}")
        args: list[str] = line.split(" ")
        break
    if args[0] == "end":
        break
    elif args[0] == "show":
        print(moto)
    elif args[0] == "init":
        
    elif args[0] == "enter":
       nome = args[1]
       idade =
    elif args[0] == "leave":

    elif args[0] == "buy":
           
    elif args[0] == "drive":

    elif args[0] == "honk":
       
    else:
            print("fail: comando invalido")