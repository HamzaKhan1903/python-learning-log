print("--- Block 1: for loop over a list ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("--- Block 2: range with start, stop, step ---")
for i in range(2, 10, 2):
    print(i)


print("--- Block 4: enumerate ---")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("--- Block 5: nested loops ---")
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)

print("--- Block 7: accumulator pattern - sum ---")
numbers = [10, 20, 30, 40]
#total = 0
for num in numbers:
    total = 0
    total = total + num
print(total)

print("-----Block 8: ages older than 18 - for loop-----")
ages = [15,22,8,34,17,45]
for age in ages:
    if age >= 18:
        print(age)

print("-----Block 9: ages younger than 18 - for loop accumulator-----")
ages = [15,22,8,34,17,45]
count = 0
for age in ages:
    if age <= 18:
        count = count +1
print (count)

print("--- Testing letter comparison ---")
print("R" > "J")
print("J" > "J")
print("A" > "J")

print("-----Block 10: student with enumerator and condition-----")
students = ["Ravi", "Meera", "John", "Sana"]
for index, name in enumerate(students):
    if name[0]  > "J":
        print(index, name)

print("--- Block 11: basic while loop ---")
count = 1
while count <= 5:
    print(count)
    count = count + 1

print("--- Block 12: break ---")
count = 1
while True:
    print(count)
    if count == 3:
        break
    count = count + 1

print("--- Block 13: continue ---")
count = 0
while count < 5:
    count = count + 1
    if count == 3:
        continue
    print(count)

print("--- Block 14: input basics ---")
name = input("What's your name? ")
print("Hello, " + name)

'''print("--- Block 15: input returns a string, always ---")
age = input("How old are you? ")
print(type(age))
next_year = age + 1'''


print("--- Block 16: converting input properly ---")
age = int(input("How old are you? "))
print(type(age))
next_year = age + 1
print(next_year)

print("---Calculator menu---")
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = (input("Enter your choice: "))
    if choice == "5":
        print ("GoodBye!")
        break
    elif choice == "1":
        num1 = float(input("Enter the number"))
        num2 = float(input("Enter the number"))
        print("The sum is ", num1 + num2)
    elif choice == "2":
        num1 = float(input("Enter the number"))
        num2 = float(input("Enter the number"))
        print("The difference is ", num1 - num2)
    elif choice == "3":
        num1 = float(input("Enter the number"))
        num2 = float(input("Enter the number"))
        print("The product is ", num1 * num2)
    elif choice == "4":
        num1 = float(input("Enter the number"))
        num2 = float(input("Enter the number"))
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("The quotient is ", num1 / num2)
    else: 
        print("Invalid choice. Please try again.")

print("--- Grocery Calculator ---")
price = 0
while True:
    print("How many items have you purchsed?")
    print("Enter done once you have entered all the items")
    items = input("Enter the price of the item or type done to get the bill total:")
    if items == "done":
        break
    elif items.replace(".", "", 1).isdigit():
        price += float(items)
    else:
        print("Invalid input. Please enter a valid price or type done.")
print("The total bill is: ", price)
if price > 100:
    print("You have spent more than $100. You get a 10% discount!")
    discount = price * 0.10
    total = price - discount
    print("Your total after discount is: ", total)
