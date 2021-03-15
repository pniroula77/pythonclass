class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def Info(self):
        print("Inside circle class")

    def draw(self):
        print("Inside draw circle")

class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle")

obj = Circle()

obj.draw()

obj2 = Rectangle()

obj2.draw()

print("lines added")