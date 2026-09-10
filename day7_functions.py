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