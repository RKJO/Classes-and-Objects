from exercise_2_Shape import Shape
from math import pi


class Circle(Shape):

    def __init__(self, x, y, color, r):
        if isinstance(r, int) and r > 0.0:
            self.r = r
        else:
            self.r = 0
        super(Circle, self).__init__(x, y, color)
        self.shape_info()

    def shape_info(self):
            super(Circle, self).shape_info()
            print("Radius: {}".format(self.r))

    def area(self):
        return pi * (self.r ** 2)

    def perimeter(self):
        return 2 * pi * self.r


c = Circle(3, 4, 'red', 3)
print(c.area())
print(c.perimeter())

