class Pessoa:
    def __init__(self, nome:str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def get_nome(self):
        return self.__nome
    
    def get_dinheiro(self):
        return self.__dinheiro 

    def __str__(self) -> str:
        return f"{self.__nome}:{self.__dinheiro}"

class Moto: 
    def __init__(self, custo: int, motorista: Pessoa | None, passageiro: Pessoa | None):
        self.__custo = 0
        self.__motorista = motorista
        self.__passageiro = passageiro

    def __str__(self) -> str:
        return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"

def main():
    moto = Moto(0, None, None)
    while True:
        line: str = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)

main()