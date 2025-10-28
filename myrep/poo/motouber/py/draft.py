class Pessoa:
    def __init__(self, nome:str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def get_nome(self):
        return self.__nome
    
    def get_dinheiro(self):
        return self.__dinheiro
    
    def pay(self, valor: int):
        if self.__dinheiro >= valor:
            self.__dinheiro -= valor
            return valor
        else:
            pagamento = self.__dinheiro
            self.__dinheiro = 0
            return pagamento
    
    def receber(self, valor: int):
        self.__dinheiro += valor

    def __str__(self) -> str:
        return f"{self.__nome}:{self.__dinheiro}"

class Moto: 
    def __init__(self, custo: int = 0):
        self.__custo = custo
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None

    def setDriver(self, motorista: Pessoa):
        if self.__motorista is not None:
            return
        self.__motorista = motorista

    def setPass(self, passageiro: Pessoa):
        if self.__motorista is None:
            print("fail: dont have any driver")
            return
        if self.__passageiro is not None:
            print("fail: alredy have a passenger") 
            return
        self.__passageiro = passageiro
        return 
    
    def leavePass(self):
        if self.__motorista is None:
            print("fail: dont have any driver")
            return
        if self.__passageiro is None:
            print("fail: dont have any passenger")
            return
        print(f"{self.__passageiro}")
        self.__passageiro = None
        self.__custo = 0


    def drive(self, km: int):
        if self.__motorista is None:
            print("fail: dont have any driver")
            return
        if self.__passageiro is None:
            print("fail: dont have any passenger")
            return
        custo = km * 1
        if not self.__passageiro.pay(custo):
            print("fail: passenger does not have enough money")
            return
        self.__custo += custo

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
            moto.setDriver(Pessoa(nome, dinheiro))
        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = int(args[2])
            moto.setPass(Pessoa(nome, dinheiro))
        elif args[0] == "drive":
            km = int(args[1])
            moto.drive(km)
        elif args[0] == "leavePass":
            moto.leavePass()
        else:
            print(f"fail: invalid comand")

main()