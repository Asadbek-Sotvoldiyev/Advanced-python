import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi*self.radius**2

    def get_perimetr(self):
        return 2*math.pi*self.radius


circle1 = Circle(13)
print(circle1.get_area())
# Result: 530.929158456675
print(circle1.get_perimetr())
# Result: 81.68140899333463
