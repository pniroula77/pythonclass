from abc import abstractmethod

class Shape:
    # define a abstract method
    @abstractmethod
    def calculate_area(self):
        pass 

class Circle(Shape):
    # create a constructor for circle

    def __init__(self,r):
        self.radius = r

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self,l,b):
        self.length = l 
        self.breadth = b

    def info(self):
        print("Inside Rectangle")

    def calculate_areas(self):
        return self.length * self.breadth

obj = Circle(1)
res = obj.calculate_area()
print(res)

recobj = Rectangle(2,3)
recobj.info()
resl = recobj.calculate_areas()
print(resl)

     