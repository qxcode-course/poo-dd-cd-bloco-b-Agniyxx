class chinela: 
    def __init__(self, tamanho: int):
        self.tamanho = 0
    
    
    def setTamanho(self, valor: int):
        if not (valor, int):
             print(f"fail:o tamanho deve ser um numero inteiro")
        if not (20 <= self.tamanho <= 50):
            print(f"fail: o tamanho atibuido deve ser um numero entre 20 e 50")
            return
        if not valor % 2 != 0: 
             print(f"fail:o tamanho deve ser um numero par")
             return
        if self.tamanho == valor:
            print(f"o tamanho foi definido como {self.tamanho}")

