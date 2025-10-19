class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    def get_nome(self):
        return self.__nome
    def set_nome(self, valor:str):
        self.__nome = valor
    def __str__ (self):
        return self.__nome
    
class Moto:
    def __init__(self):
        self.cliente: Pessoa | None = None

    def inserir(self, cliente: Pessoa) -> bool:
        if self.cliente != None:
            print("moto ocupada")
            return False
        self.cliente = cliente
        return True

    def remover(self) -> Pessoa| None:
        if self.cliente == None:
            print("moto vazia")
            return None
        aux: Pessoa = self.cliente
        self. cliente = None
        return aux
    
    def __str__(self) -> str:
        return f"moto: {self.cliente}"
    
def main():
    while True:
        moto = Moto()
        line:str = input()
        print(f"${line}")
        args: list

        if args[0] == "end":
            break
        elif args[0]:
            print("moto")
        elif args[0] == "show":
            print("")
        elif args[0] == "":

        else:
            print("fail: comando invalido")