class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.height * self.width
        return area

    def perimeter(self):
        perimeter = (self.height * 2) + (self.width * 2)
        return perimeter
        
rect = Rectangle(4, 5)
print(rect.area())
print(rect.perimeter())