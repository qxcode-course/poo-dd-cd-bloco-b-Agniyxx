class Roupa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, tamanho:str):
        self.__tamanho = tamanho
        tamanhos = ["PP", "P", "M", "G", "GG", "XG"]
        if tamanho in tamanhos:
            print(f"o tamanho escolhido foi {tamanho}")
            return True
        if not tamanho in tamanhos: 
            print(f"o tammanho deve ser {tamanhos}")
            return False

    def __str__(self) -> str:
        return f"roupa: {self.__tamanho}"
    
def main():
    roupa = Roupa()
    while roupa.getTamanho() == "":
        line: str = input()
        print(f"${line}")
        args = line.split(" ")
        if roupa.setTamanho(tamanho) == True:
            print("")
        elif args[0] =="end": 
            break
        elif args[0]== "show":
            print(roupa)
        elif args[0]== "size":
            print(tamanho)
        else:
            print("comando invalido")