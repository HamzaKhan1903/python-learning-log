print("--- Block 1: your first class ---")
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

ravi = Student("Ravi", 85)
print(ravi.name)
print(ravi.grade)

print("--- Block 2: two independent objects ---")
meera = Student("Meera", 92)
print(ravi.name, ravi.grade)
print(meera.name, meera.grade)

print("--- Proving objects are dictionaries underneath ---")
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

ravi = Student("Ravi", 85)
print(ravi.__dict__)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def is_passing(self):
        return self.grade >= 40

ravi = Student("Ravi", 35)
print(ravi.is_passing())
print(ravi.__dict__)
ravi.grade = 50
print(ravi.is_passing())
print(ravi.__dict__)

print("--- Block 3: many objects, held in a list ---")
students = []
students.append(Student("Ravi", 85))
students.append(Student("Meera", 92))
students.append(Student("John", 35))

for student in students:
    print(student.name, student.grade)

print("=====Employee Payment Tracker====")
class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked
    def is_overtime(self):
        return self.hours_worked > 40

'''print("--- Testing missing attribute ---")
emp1 = Employee("Sara", 25, 45)
print(emp1.bonus)'''


print("--- Block: two employees ---")
emp1 = Employee("Sara", 25, 45)
emp2 = Employee("John", 30, 38)
print("===calling methids===")
print(emp1.calculate_pay())
print(emp2.calculate_pay())
print(emp1.is_overtime())
print(emp2.is_overtime())
print("===craeting a list of employees===")
emp = []
emp.append(Employee("Ravi", 25, 45))
emp.append(Employee("John", 30, 40))
emp.append(emp1)
emp.append(emp2)
#print(emp) - this shows the object memory address

while True:
    print("1- Add Employee details: ")
    print("2- View employees")
    print("3- Exit")

    choice = input(" Select an option.")
    if choice == "3":
        break
    elif choice == "1":
        name = input("Enter the name: ")
        try:
            hourly_rate =  float(input("Enter the no hourly rate: "))
            hours_worked = float(input("Enter teh no of hours worked: "))
            emp.append(Employee(name, hourly_rate, hours_worked))
        except ValueError:
            print("Enter valid details.")
    elif choice == "2":
        for employee in emp:
            print(employee.__dict__)
    else:
        print("Invalid choice. Select the correct option.")

print("--- Reading from the list ---")
print(emp[0].name)
print(emp[0].calculate_pay())
print("--- Verifying every employee's actual data ---")
for employee in emp:
    print(employee.name, employee.hourly_rate, employee.hours_worked, employee.calculate_pay())
print("--- Verifying via __dict__ ---")
for employee in emp:
    print(employee.__dict__)
