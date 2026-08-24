import math

class Shape:
    def __init__(self, radius):
        self.radius = radius

class Circle(Shape):
    def cal_area(self):
        area = math.pi * self.radius ** 2
        print(f"Area of Circle is {area}")

class Sphere(Shape):
    def cal_volume(self):
        volume = (4/3) * math.pi * self.radius ** 3
        print(f"Volume is: {volume}")
              
c1 = Circle(2)
s1 = Sphere(3)

c1.cal_area()
s1.cal_volume()
