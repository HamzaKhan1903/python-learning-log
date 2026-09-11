print("--- Block 2: function with a parameter ---")
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Hamza")
greet_person("Sara")

print("--- Block 1: basic function ---")
def greet():
    print("Hello, welcome to the program!")

greet()
greet()

print("--- Block 3: one function per operation ---")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(add(5, 3))
print(subtract(5, 3))

print("--- Block 4: no return ---")
def add_no_return(a, b):
    print(a + b)

result = add_no_return(3, 4)
print(result)


print("--- Testing return is call-specific, not shared ---")
def add(a, b):
    return a + b

x = add(2, 3)
y = add(10, 20)
print(x)
print(y)

print("--- Block 6: default parameters ---")
def greet(name="friend"):
    print(f"Hello, {name}!")

greet()
greet("Hamza")

print("--- Block 7: mixing required and default parameters ---")
def describe_student(name, grade=100):
    print(f"{name} scored {grade}")

describe_student("Ravi")
describe_student("Meera", 78)

'''print("--- Block 8: broken parameter order ---")
def broken_function(name="friend", age):
    print(name, age)'''

print("====Practice problem====")
def calculate_total(price, tax=0.13):
    return price + (price*tax)

print(calculate_total(100))
print(calculate_total(100,0.05))


print("====Practice problem without return====")
def calculate_total(price, tax=0.13):
    print(price + (price*tax))
    return price + (price*tax)
default_tax = calculate_total(100)
print(default_tax)
optional_tax = calculate_total(100,0.05)
print(optional_tax)

print("--- Block 9: local scope ---")
def my_function():
    x = 10
    print(x)
print(x)
my_function()
print(x)

print("--- Block 11: local variable shadows global ---")
x = 999
def my_function():
    x = 10
    print(x)
print(x)
my_function()
print(x)

print("--- Block 12: does a for loop create its own scope? ---")
for n in range(1, 10):
    pass
print(n)

print("--- Block 14: *args ---")
def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add_all(1, 2))
print(add_all(1, 2, 3, 4, 5))
print(add_all())

print("--- Block 15: **kwargs ---")
def describe_person(**details):
    for key, value in details.items():
        print(key, ":", value)

describe_person(name="Hamza", age=30, city="Mississauga")

print("--- Block 16: kwargs really is a dictionary ---")
def show_type(**details):
    print(type(details))

show_type(name="Hamza", age=30)


print("--- Block 16: kwargs really is a dictionary ---")
def show_type(**details):
    for key, value in details.items():
        print(key, ":", value)
    print(type(details))
show_type(name="Hamza", age=30)
show_type(name="Hamza", age=30, city="Mississauga", province="Ontario")

print("--- Block 17: *args plus a regular default parameter ---")
def add_with_bonus(*numbers, bonus=0):
    total = 0
    for n in numbers:
        total += n
    return total + bonus

print(add_with_bonus(1, 2, 3))
print(add_with_bonus(1, 2, 3, 10))


print("--- Block 18: *args plus a regular default parameter ---")
def show_parts(*numbers, bonus=0):
    print("numbers:", numbers)
    print("bonus:", bonus)

show_parts(1, 2, 3, bonus=10)
print("---")
show_parts(1, 2, 3, 10)