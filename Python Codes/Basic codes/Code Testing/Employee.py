#Python Crash Course Page 11.3

class EmployeeSalary:
    def __int__(self, first_name, annual_salary):
        self.first_name = first_name
        self.annual_salary = annual_salary

    def give_raise(self):
        diff_raise_amount = int(input("Enter a specific raise amount. Enter N/A if it doesn't apply to you"))
        if diff_raise_amount:
            return self.annual_salary + diff_raise_amount
        else:
            return self.annual_salary + 5000

EmployeeSalary()