Emp_Name = []
hours = []
Gross_Pay = []
genders = []
Child_Number = []
Emp_Num = input('How many employees are there')
Emp_Num = int(Emp_Num)
for employee in range(0, Emp_Num):
    name = input('Please enter the name of the employee')
    Emp_Name.append(name)
    gender = input('What is your gender? M/F')
    genders.append(gender)
    hour = input('Enter the number of hours worked')
    hours.append(int(hour))
    children = input('How many children do you have?')
    children = int(children)
    Child_Number.append(children)
    
for value in range(0, Emp_Num):
    if genders[value] == 'M':
        if hours[value] <= 40:
            Gross_Pay.append(500*hours[value])
        if hours[value] > 40:
            Gross_Pay.append(1.5*500*hours[value])
    else:
        if hour[value] <= 40:
            Gross_Pay.append(550*hours[value])
        if hours[value] > 40:
            Gross_Pay.append(1.5*550*hours[value])

for value in Gross_Pay:
    value = (0.15 + 0.025 + 0.01) * value

for value in range(0, Emp_Num):
    if Child_Number[value] >= 3:
        if genders[value] == 'M':
            Gross_Pay[value] -= 10
        else:
            Gross_Pay[value] -= 20
    else:
        Gross_Pay[value] -= 0

print(('Employee Name\tNet Pay'))
for value in range(0, Emp_Num):
    print(Emp_Name[value] + '\t' + str(Gross_Pay[value]))

