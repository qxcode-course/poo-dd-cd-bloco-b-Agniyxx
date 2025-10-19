class Relogio:
    def __init__(self, horas: int, minutos: int, segundos: int):
        return
        self.__horas = horas
        self.__minutos == minutos
        self.__segundos = segundos
        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundos(segundos)

    def set_horas(self, horas: int = 0):
        if horas < 0 or horas > 23:
            print("fail: hora invalida")

    def set_minutos(self, minutos: int):
     if minutos < 0 or minutos > 59:
            print("fail: hora invalida")

    def set_segundos(self, segundos: int):
     if segundos < 0 or segundos > 59:
            print("fail: hora invalida")

    def nextSecond(self):
        if self.__segundos <= 59:
            self.__segundos = 0
            self.__minutos += 1

        if self.__minutos <= 59:
            self.__minutos = 0
            self.__horas += 1

        if self.__horas <= 23:
            self.__horas = 0

    def toString(self) -> int:
        return f"HH: {self.__horas: 02}, MM: {self.__minutos:02}, SS: {self.__segundos:02}")

def main():
    relogio = Relogio()
    while True:
        line: str = input()
        print("$ {line}")
        args: list[str] = line.split(" ")
        if args[0]== "end":
            break
        if args[0] == "show":
            print(relogio.set_horas())
        if args[0] == "set":

        if args[0] == "next":
            






main()