class Relogio:
    def __init__(self, horas: int, minutos: int, segundos: int):
        self.__horas = 0
        self.__minutos = 0
        self.__segundos = 0
        self.set_horas(horas)
        self.set_minutos(minutos)
        self.set_segundos(segundos)

    def set_horas(self, horas: int):
        if horas <= 0 or horas <= 23:
            self.__horas = horas
        else:
            print("fail: hora invalida")

    def set_minutos(self, minutos: int):
        if minutos <= 0 or minutos <= 59:
            self.__minutos = minutos
        else:
            print("fail: minuto invalido")

    def set_segundos(self, segundos: int):
        if segundos <= 0 or segundos <= 59:
            self.__segundos = segundos
        else:
            print("fail: segundo invalido")

    def nextSecond(self):
        self.__segundos += 1
        if self.__segundos > 59:
            self.__segundos = 0
            self.__minutos += 1
        if self.__minutos > 59:
            self.__minutos = 0
            self.__horas += 1
        if self.__horas > 23:
            self.__horas = 0

    def __str__(self):
        return f"{self.__horas:02}:{self.__minutos:02}:{self.__segundos:02}"

def main():
    relogio = Relogio(0,0,0)
    while True:
        line: str = input()
        print(f"${line}")
        args: list[str] = line.split(" ")
        if args[0]== "end":
            break
        elif args[0] == "set":
            relogio.set_horas(int(args[1]))
            relogio.set_minutos(int(args[2]))
            relogio.set_segundos(int(args[3]))
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "next":
            relogio.nextSecond()
        elif args[0] == "init":
            relogio = Relogio(int(args[1]), int(args[2]), int(args[3]))
        else:
            print("fail: comando invalido")

main()