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
    def __init__(self, custo: int = 0):
        self.__custo = custo
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None

    def setDriver(self, motorista: Pessoa):
        if self.__motorista is not None:
            return True
        self.__motorista = motorista
        return True
        self.__motorista = Pessoa(nome, dinheiro)
        return True

    def setPass(self, passageiro: Pessoa):
        if self.__motorista is None:
            print("fail: dont have any driver")
            return
        if self.__passageiro is not None: 
            return True
        self.__passageiro = passageiro
        return True
        self.__passageiro = Pessoa(nome, dinheiro)
        self.__custo = 0
    
    def leavePass(self):
        if self.__motorista is None:
            print("fail: dont have any driver")
            return
        if self.__passageiro is None:
            print("fail: Passenger does not have enough money")
            return
        print(f"{self.__passageiro}")
        self.__passageiro = None


    def drive(self, km: int):
        if self.__motorista is None:
            print("fail: dont have any driver")
            return
        if self.__passageiro is None:
            print("fail: dont have any passenger")
            return
        if km > 0:
            self.__custo += km * 1

    def __str__(self) -> str:
        motorista_str = str(self.__motorista) if self.__motorista else None
        passageiro_str = str(self.__passageiro) if self.__passageiro else None
        return f"Cost: {self.__custo}, Driver: {motorista_str}, Passenger: {passageiro_str}"

def main():
    moto = Moto(0)
    while True:
        line: str = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            moto.setDriver(nome, dinheiro)
        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = int(args[2])
            moto.setPass(nome, dinheiro)
        elif args[0] == "drive":
            km = int(args[1])
            moto.drive(km)
        elif args[0] == "leavePass":
            moto.leavePass()
        else:
            print(f"fail: invalid comand")

main()