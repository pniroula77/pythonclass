from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta): #absract class
    @abstractmethod
    def calculate_area(self): #function declaration, not definition
        pass 

class Circle(Shape):
    def __init__(self,r):
        self.radius = r
    def Info(self):
        print("Inside circle class")

    def calculate_area(self): #overriding, two class
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    def info(self):
        print("Inside Rectangle")

    def calculate_area(self): #overriding, two class
        return self.length * self.breadth

obj = Circle(4)

res = obj.calculate_area()
print(res)

obj2 = Rectangle(4,5)

obj2.info()
resl = obj2.calculate_area()
print(resl)