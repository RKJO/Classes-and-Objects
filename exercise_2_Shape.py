class Shape:

    def __init__(self, x, y, color):
        if isinstance(x, int) and isinstance(y, int):
            self.__x = x
            self.__y = y
        else:
            __x = 0
            __y = 0

        if isinstance(color, str):
            self.__color = color
        else:
            self.__color = "transparet"

        self.shape_info()

    def shape_info(self):
        print('Shape position x: {}, y: {}, and color: {}'.format(
            self.__x,
            self.__y,
            self.__color
        ))

    def distance(self, other_shape):
        a = self.__y - other_shape.__y
        b = self.__x - other_shape.__x
        pow_a = a ** 2
        pow_b = b ** 2
        pow_c = pow_a + pow_b
        return pow_c ** (1/2) # math.sqrt(pow_c)


s = Shape(1, 2, "czarny")
#s.shape_info() # tego już nie trzeba ponieważ zostało dodane w konstruktorze line:16
a = Shape(3, 4, "czerwony")
#a.shape_info()
result = s.distance(a)
print(result)
b = Shape(10,12, "rudy")
print (a.distance(b))


