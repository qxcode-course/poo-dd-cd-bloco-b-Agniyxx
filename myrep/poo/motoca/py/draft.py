class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_nome(self, valor:str):
        self.__nome = valor
    def __str__ (self):
        return self.__nome
    
class Moto:
    def __init__(self, potencia:int = 1):
        self.pessoa: Pessoa | None = None
        self.potencia = potencia
        self.tempo = 0

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.pessoa != None:
            print("moto ocupada")
            return False
        self.pessoa = pessoa
        return True

    def remover(self) -> Pessoa| None:
        if self.pessoa == None:
            print("moto vazia")
            return None
        aux: Pessoa = self.pessoa
        self.pessoa = None
        return aux
    
    def __str__(self) -> str:
        return f"power:{self.valor}, time:{self.tempo}, person:{self.pessoa}"
    
def main():
    moto = Moto()
    while True:
        line:str = input()
        print(f"${line}")
        args: list[str] = line.split(" ")
        break
    if args[0] == "end":
        break
    elif args[0]:
        print("")
    elif args[0] == "show":
        print(moto)
        potencia = int(args[1])
        
    elif args[0] == "init":

    else:
            print("fail: comando invalido")