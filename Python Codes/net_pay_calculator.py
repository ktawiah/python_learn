"""
Net Pay calculator for JB and Sons Company
Question
--------
Employees of JB and Sons Consultants Ltd are paid on an hourly basis at the end of every week.
If an employee works for not more than 40 hours a week, it is considered regular and Overtime
for hours worked in excess of 40. Regular hours are paid at 500 cedis and 550 cedis per hour for
males and females respectively while the overtime rate is one and half times the regular rate per
hour for the different sexes. All employees are to pay 15% of their gross pay as Income Tax,
2.5% as National Health Contribution Levy, 1% as District Tax. Employees who have more than
three children are to pay 10 and 20 cedis per child in excess of three towards Educational Fund
For All for males and females respectively. Devise a computer solution that can be used to
calculate the Net Pay of employees.
"""


def calculate_employee_netpay():
    """Calculates the netpay and returns a dictionary with details of employee"""
    employee_name = input("Enter employee name's name: ")
    hours = int(input("Enter hours worked: "))
    number_of_children = int(input("How many children does this employee have?: "))
    gender = input("What is this employee's gender? M/F: ")

    if gender == "M":
        if hours <= 40:
            if number_of_children >= 3:
                net_pay = 500 * hours * (0.815) - 10
            else:
                net_pay = 500 * hours * (0.815)
        else:
            if number_of_children >= 3:
                net_pay = 1.5 * 500 * hours * (0.815) - 10
            else:
                net_pay = 1.5 * 500 * hours * (0.815)
    else:
        if hours <= 40:
            if number_of_children >= 3:
                net_pay = 550 * hours * (0.815) - 20
            else:
                net_pay = 550 * hours * (0.815)
        else:
            if number_of_children >= 3:
                net_pay = 1.5 * 550 * hours * (0.815) - 20
            else:
                net_pay = 1.5 * 550 * hours * (0.815)

    employee_data = {
        "Employee's Name": employee_name,
        "Hours worked": hours,
        "Number of children": number_of_children,
        "net_pay": f"{net_pay:.2}",
    }
    return employee_data


if __name__ == "__main__":
    print(calculate_employee_netpay())
