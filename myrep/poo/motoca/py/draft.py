class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade 
    
    def __str__ (self):
        return f"{self.__nome}:{self.__idade}"
  
class Moto:
    def __init__(self, potencia:int = 1):
        self.pessoa: Pessoa | None = None
        self.potencia = potencia
        self.tempo = 0

    def enter(self, pessoa: Pessoa) -> bool:
        if self.pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.pessoa = pessoa
        return True

    def remove(self) -> Pessoa| None:
        if self.pessoa is None:
            print("fail: empty motorcycle")
            return
        print(f"{self.pessoa}")
        self.pessoa = None
    
    def comprarTempo(self, time: int):
        if time < 0:
            print(f"fail: ")
        else:    
            self.tempo += time

    def drive(self, time: int):
        if self.pessoa is None:
            print("fail: buy time first")
            return
        if self.pessoa.get_idade() < 10:
            print("fail: too old to drive")
            return
        if time > self.tempo: 
            print(f"fail: time finished after {self.tempo} minutes")
        else:
            self.tempo -= time

    def honk(self):
        print("P" + "e" * self.potencia + "m")

    def show(self):
        print(self)
    
    def __str__(self) -> str:
        str_pessoa = str(self.pessoa) if self.pessoa else "empty"
        return f"power:{self.potencia}, time:{self.tempo}, person:({str_pessoa})"
    
def main():
    moto = Moto()
    while True:
        line:str = input()
        print(f"${line}")
        args: list[str] = line.split(" ")
        
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "init":
            moto = Moto(int(args[1]))
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            pessoa = Pessoa(nome, idade)
            moto.enter(pessoa)
        elif args[0] == "leave":
            moto.remove()
        elif args[0] == "buy":
            moto.comprarTempo(0)
        elif args[0] == "drive":
            moto.drive(0)
        elif args[0] == "honk":
            moto.honk()
        else:
            print("fail: comando invalido")

main()