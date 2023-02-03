class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

class Rectangle(Shape):
    def __init__(self, color, length, breadth):
        Shape.__init__(self, color)
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, color, base, height):
        Shape.__init__(self, color)
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

rect = Rectangle("red", 10, 20)
print("Rectangle:")
print("Color:", rect.get_color())
print("Area:", rect.get_area())

tri = Triangle("blue", 10, 20)
print("\nTriangle:")
print("Color:", tri.get_color())
print("Area:", tri.get_area())
