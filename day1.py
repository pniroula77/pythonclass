class Toothpaste: #class ClassName

    def __init__(self,c,i):
        self.color = c
        self.ingred = i
    
    def getColor(self):
        return self.color

    def getIngred(self):
        return self.ingred

    def setColor(self,color):
        self.color = color


class GelToothpaste(Toothpaste):
    def __init__(self,color,ingred,gel):
        Toothpaste.__init__(self,color,ingred)
        self.gel = gel
    
    def show_type(self):
        print("Inside inherited class")
        print("color", self.color)
        print("ingred", self.ingred)
        print("Gel", self.gel)


obj = GelToothpaste("red","salt","cooling")
obj.show_type()






