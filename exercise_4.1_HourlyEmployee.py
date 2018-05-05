from exercise_4_Employee import Employee


class HourlyEmpoyee(Employee):
    def compute_payment(self, hours):
        payment = self._get_salary() * hours
        return payment


z = HourlyEmpoyee(2, "Jan", "Kowalski")
z.set_salary(5)
print(z.compute_payment(150))
print(z._get_salary())


class SalariedEmployee(Employee):

    def compute_payment(self):
        return self._get_salary() * 190


zdzisiek = SalariedEmployee(4, "Zdzisiek", "Ortalionowy")
zdzisiek.set_salary(10)

print(zdzisiek.compute_payment())