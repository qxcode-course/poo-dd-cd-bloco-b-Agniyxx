class Roupa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho:str):
        tamanhos = ["PP", "P", "M", "G", "GG", "XG"]
        if tamanho in tamanhos:
            self.tamanho = tamanho
            print(f"o tamanho escolhido foi {tamanho}")
            return
        if not tamanho in tamanhos: 
            print(f"o tammanho deve ser {tamanhos}")



    def __str__(self) -> str:
        return f"roupa: {self.tamanho}"
    
def main():
    roupa = Roupa()
    while roupa.getTamanho() == "":
        line: str = input()
        args = line.split()
        print(f"${line}")
        roupa = input("qual o tamanho de roupa você escolhe?").upper()

    if roupa.setTamanho(tamanho) == True:
    

    elif args[0] =="end": 
        break
    elif args[0]== "show":
        print(roupa)
    elif args[0]== "size":
        print(tamanho)

main()