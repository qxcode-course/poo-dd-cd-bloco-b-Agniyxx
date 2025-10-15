class roupa:
    def __init__(self):
        self.__tamanho: str = ""

    def setTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho:str):
        tamanhos = ["PP", "P", "M", "G", "GG", "XG"]
        if tamanho in tamanhos:
            self.tamanho = tamanho
            print(f"o tamanho escolhido foi {tamanho}")
            return
        if not tamanho in tamanhos: 
            print(f"o tammanho deve ser {tamanhos}")

def main()
roupa = Roupa()
while roupa.getTamanho() == "":
    print("Digite seu tamanho de roupa")
    tamanho = input()
    roupa.setTamanho(tamanho)

print("Parabens, você comprou uma rouppa tamanho", roupa.setTamanho())
