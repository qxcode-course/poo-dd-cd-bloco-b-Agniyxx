class chinela: 
    def __init__(self):
        self.__tamanho = 0
    
    def setTamanho(self, valor: int):
        if not (valor, int):
            print(f"fail:o tamanho deve ser um numero inteiro")
            return False
        if not (20 <= self.__tamanho <= 50):
            print(f"fail: o tamanho atibuido deve ser um numero entre 20 e 50")
            return False
        if not valor % 2 != 0: 
            print(f"fail:o tamanho deve ser um numero par")
            return False
    
    def getTamanho(self):
        return self.__tamanho

    def __str__(self) -> str:
        return f"chinela: {self.__tamanho}"

def main():
    chinela = Chinela()
    while True:
        print("digite o tamanho da sua chinela")
        try:
            tamanho = int(input())
        except ValueError:
            print("fail: digite um número válido")
        if chinela.getTamanho(tamanho):
            break
