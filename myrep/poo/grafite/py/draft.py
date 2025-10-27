class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness =  thickness
        self.__hardness = hardness
        self.__size = size

    def usagePerSheet(self): 
        if self.__hardness == "HB":
            return 1
        elif self.__hardness == "2B":
            return 2
        elif self.__hardness == "4B":
            return 3
        elif self.__hardness == "6B":
            return 4
        else: 
            return 0
        
    def getHardness(self):
        return self.__hardness

    def getSize(self):
        return self.__size

    def getThickness(self):
        return self.__thickness

    def setSize(self, size: int):
        self.__size = size

    def __str__(self):
        return f"calibre: {self.__thickness}, grafite: [{self.__thickness}:{self.__hardness}:{self.__size}]"

class Pencil:
    def __init__(self, thickness: float): 
        self.__thickness = thickness
        self.__tip: Lead | None = None

    def hasGrafite(self,):
        return self.__tip is not None 

    def insert(self, lead: Lead):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return
        if lead.getHardness != self.__thickness:
            print("fail: calibre incompativel")
            return
            self.__tip = lead
        
    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return
        remove = self.__tip
        self.__tip = None
        return remove

    def writePage(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
        return
        lead = self.__tip
        if lead.getSize() <= 10:
            print("fail:tamanho insufuciente")

    def __str__(self):
        if self.__tip is not None:
            return f"calibre: {self.__thickness}, grafite: []"
        return f"calibre: {self.__thickness}, grafite: [{self.__tip.getThickness()}:{self.__tip.getHardness()}:{self.__tip.getSize()}]"

def main():
    pencil = Pencil(0.0)
    while True:
        line: str = input()
        print(f"${line}")
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pencil)
    
main()