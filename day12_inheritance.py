print("--- Inheritance: Manager extends Employee ---")

class Employee:
    def __init__(self, name: str, hourly_rate: float, hours_worked: float) -> None:
        self.name = name
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    def calculate_pay(self) -> float:
        return self._hourly_rate * self._hours_worked
    def set_hourly_rate(self, new_rate: float):
            if new_rate < 0:
                print("Hourly rate cannot be negative.")
            else:
                self._hourly_rate = new_rate

class Manager(Employee):
    def __init__(self, name: str, hourly_rate: float, hours_worked: float, team_size: int) -> None:
        super().__init__(name, hourly_rate, hours_worked)
        self.team_size = team_size

    def calculate_pay(self) -> float:
        base_pay = super().calculate_pay()
        return base_pay + 200

    def team_info(self):
        print(f"{self.name} manages {self.team_size} people.")
    

mike = Manager("Mike", 40, 45, 5)
print(mike.name)
print(mike.calculate_pay())
mike.team_info()

print("--- The problem encapsulation addresses ---")
mike = Manager("Mike", 40, 45, 5)
mike.set_hourly_rate = -500
print(mike.calculate_pay())
print("========wiht proper underscores=======")
mike = Employee("Mike", 40, 45)
mike.set_hourly_rate(-500)
print(mike.calculate_pay())
#mike.set_hourly_rate(45)
#print(mike.calculate_pay())


print("--- Testing direct access WITH the correct underscore ---")
mike = Employee("Mike", 40, 45)
mike.set_hourly_rate = -500
print(mike.calculate_pay())