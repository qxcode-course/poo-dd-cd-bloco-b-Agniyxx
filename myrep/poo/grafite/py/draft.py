class Lead:
    def __init__(self, thickness: int, hardness: str, size: int):
        self.__thickness =  thickness
        self.__hardness = hardness
        self.__size = size

    def usagePerSheet(self): int

    def getHardness(self):
        return self.__hardness

    def getSize(self):


    def getThickness(self):
        return self.__thickness

    def setSize(self, size: int):
        return self.__size

    def __str__(self):
        return f"calibre: {self.__thickness}, grafite: [{self.__thickness}:{self.__hardness}:{self.__size}]"


class Pencil:
    def __init__(self, thickness: int,  tip: Lead | None): 
        self.__thickness = thickness
        self.__tip = tip

    def hasGrafite(self,): bool
        if self.thickness is None:
            return False

    def insert(self, lead: Lead): bool

    def remove(self):

    def writePage(self):

    def __str__(self):
        print()

def main():

main()