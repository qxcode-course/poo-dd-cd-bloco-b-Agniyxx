class chinela: 
    def __init__(self):
        self.__tamanho = 0
    
    def setTamanho(self, valor: int):
        if not (valor, int):
             print(f"fail:o tamanho deve ser um numero inteiro")
        if not (20 <= self.__tamanho <= 50):
            print(f"fail: o tamanho atibuido deve ser um numero entre 20 e 50")
            return
        if not valor % 2 != 0: 
             print(f"fail:o tamanho deve ser um numero par")
             return
        if self.__tamanho == valor:
            print(f"o tamanho foi definido como {self.__tamanho}")

    def __str__(self) -> str:
        print(f"")

def main():
    chinela = Chinela()
    line= input()
    args =