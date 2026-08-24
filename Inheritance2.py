import math

class Triangle:
    def __init__(self, s1, s2, s3, a1, a2, a3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3


class EquilateralTriangle(Triangle):
    def cal_area(self):
        a = self.s1     
        area = math.sqrt(3) / 4 * a ** 2
        print(f"Area of equilateral triangle: {area}")


class Scalene(Triangle):
    def tangent(self):
        ang1_rad = math.radians(self.a1)
        ang2_rad = math.radians(self.a2)
        ang3_rad = math.radians(self.a3)

        tan_val1 = math.tan(ang1_rad)
        tan_val2 = math.tan(ang2_rad)
        tan_val3 = math.tan(ang3_rad)

        print(f"Tangents of angles: {tan_val1}, {tan_val2}, {tan_val3}")

    def cal_perimeter(self):
        perimeter = self.s1 + self.s2 + self.s3
        print(f"Perimeter: {perimeter}")

    def cal_area(self):
        s = (self.s1 + self.s2 + self.s3) / 2
        area = math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
        print(f"Area: {area}")


t1 = EquilateralTriangle(6, 6, 6, 60, 60, 60)
t1.cal_area()

t2 = Scalene(3, 4, 5, 60, 70, 50)
t2.tangent()
t2.cal_perimeter()
t2.cal_area()
