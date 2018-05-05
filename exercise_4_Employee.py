class Employee:
    id = None
    first_name = None
    last_name = None
    __salary = None

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def set_salary(self, salary):
        if isinstance(salary, int) and salary >= 0.0:
            self.__salary = salary
        else:
            print("Nie płacę za pracę")

    def _get_salary(self):
        return self.__salary


