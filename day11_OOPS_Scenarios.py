print("--- Class attributes ---")
class Employee:
    company_name = "Acme Corp"      # CLASS attribute — one shared value, not per-object

    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name                    # INSTANCE attribute — unique per object
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

emp1 = Employee("Sara", 25, 45)
emp2 = Employee("John", 30, 40)

print(emp1.company_name)
print(emp2.company_name)
print(Employee.__dict__)

print("--- Testing reassignment through one instance ---")
emp1.company_name = "New Corp"
print(emp1.company_name)
print(emp2.company_name)
print(Employee.company_name)

print("--- The actual proof: emp1's own dictionary ---")
print(emp1.__dict__)
print(emp2.__dict__)



print("--- Type hints ---")
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 3))

print("--- Type hints don't actually enforce anything ---")
print(add("5", "3"))