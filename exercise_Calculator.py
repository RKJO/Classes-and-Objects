class Calculator:

    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append("added {} to {} got {}".format(num1, num2, result))
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append('multiplied {} with {} got {}'.format(num1, num2, result))
        return result

    def subtract(self, num1, num2):
        result = num2 - num1
        self.history.append('subtracted {} from {} got {}'.format(num1, num2, result))
        return result

    def divide(self, num1, num2):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print('Nie dzielimy przez )')
        self.history.append('divided {} by {} got {}'.format(num1, num2, result))
        return result

    def print_operation(self):
        print('Lista operacji')
        for operation in self.history:
            print(operation)
        if not self.history:
            print("Brak operacji")

    def clear_operatin(self):
        self.history.clear()

c = Calculator()
print(c.add(3, 5))
print(c.multiply(2, 2))
print(c.subtract(5, 3))
print(c.divide(4, 2))
print(c.divide(4, 0))
print(c.history)