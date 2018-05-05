from exercise_1_calculator import Calculator


class AdvancedCalculator(Calculator):
    PI = 3.14159265

    @staticmethod
    def compute_circle_radius(r):
        ''''w metodzie statycznej nie mamy dostpu do historii,
        która jest w obiekcie klasy AdvanceCalculator
        '''

        return AdvancedCalculator.PI * (r ** 2)

    def pow(self, num1, num2):
        result = num1 ** num2
        self.history.append("{}^{} equals {}".format(num1, num2, result))

    def root(self, num1, num2):
        result = num1 ** (1/num2)
        self.history.append("root {} of {} equals {}".format(num2, num1, result))


ac = AdvancedCalculator()
print(ac.pow(2, 3))
print(ac.root(27, 3))
