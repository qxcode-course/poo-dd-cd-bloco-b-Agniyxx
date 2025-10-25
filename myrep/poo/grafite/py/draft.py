class Lead:
    def __init__(self, thickness: int, hardness: str, size: int):
        self.__thickness =  thickness
        self.__hardness = hardness
        self.__size = size

    def usagePerSheet(self): int

    def getHardness(self):

    def getSize(self):

    def getThickness(self):

    def setSize(self, size: int):

    def __str__(self):
        print("calibre: {self.thickness}, grafite: {}")


class Pencil:
    def __init__(self, thickness: int,  tip: Lead | None): 


    def hasGrafite(self,): bool

    def insert(self, lead: Lead): bool

    def remove(self):

    def writePage(self):

    def __str__(self):
        print()