print("--- Block 1: string indexing ---")
name = "Hamza"
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])

print("--- Block 2: string slicing ---")
name = "Hamza"
print(name[1:4])
print(name[0:5])
print(name[:3])
print(name[2:])
print(name[:])

print("--- Block 3: string methods ---")
text = "  Hello World  "
print(id(text))
print(text.upper())
print(id(text))
print(text.lower())
print(text.strip())
print(text.replace("World", "Python"))
print(text.split())
print(text)

print("--- Block 4: f-strings ---")
name = "Hamza"
age = 5
print(f"My name is {name} and I am learning day {age}")
print(f"Next year, day count will be {age + 1}")

print("--- Block 4b: mixing types in f-strings ---")
name = "Hamza"
age = 5
print(f"Next age: {age + 1}")        # this works — int + int
print(f"Name plus number: {name + str(1)}")  # this will crash

print("--- Block 5: f-string without the f ---")
print("My name is {name}")

print("--- Block 6: f-string without the f --- older formatting method")
print("My name is {name}".format(name="Hamza"))

print("--- Block 6b: .format() positional style ---")
name = "Hamza" 
print("My name is {}".format(name))

print("--- Block 7: basic if/elif/else ---")
age = 13

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

print("--- Block 8: truthy vs falsy ---")
values = [0, 1, "", "hello", [], [1, 2], None, 0.0, -5]

for v in values:
    if v:
        print(f"{v!r} is truthy")
    else:
        print(f"{v!r} is falsy")


print("--- Block 9: bool() reveals the mechanism ---")
print(bool([]))
print(bool([1, 2, 3]))
print(bool(0))
print(bool(5))
print(bool(""))
print(bool("hello"))


print("--- Block 10: if statements with lists ---"  )
my_list = []
if my_list:
    print("has items")
else:
    print("empty")
# prints "empty" — because [] is falsy

my_list = [1, 2, 3]
if my_list:
    print("has items")
else:
    print("empty")
# prints "has items" — because [1, 2, 3] is truthy