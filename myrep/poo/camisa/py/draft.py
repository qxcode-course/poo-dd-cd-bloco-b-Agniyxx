class Roupa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, tamanho:str):
        tamanhos = ["PP", "P", "M", "G", "GG", "XG"]
        if tamanho in tamanhos:
            self.__tamanho = tamanho
            print(f"o tamanho escolhido foi {tamanho}")
            return True
        else:
            print(f"fail: Valor invalido, tente PP, P, M, G, GG ou XG")
            return False

    def __str__(self) -> str:
        return f"size: ({self.__tamanho})"
    
def main():
    roupa = Roupa()
    while True:
        line: str = input()
        print(f"${line}")
        args = line.split(" ")

        if args[0] =="end": 
            break
        elif args[0] == "set":
            tamanho = args[1]
            roupa.setTamanho(tamanho)
        elif args[0]== "show":
            print(roupa)
        elif args[0]== "size":
            print(roupa.getTamanho())
        else:
            print("comando invalido")

main()