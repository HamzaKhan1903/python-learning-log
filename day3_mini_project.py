'''print("---Calculator menu---")
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
    #print("How many items have you purchsed?")
    #print("Enter done once you have entered all the items")
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


print("----To do list---- ")
my_list = []
while True:
    task = input("Enter a task or type done to finish: ")
    if task == "done":
        break
    my_list.append(task)
    print(f"Task added: {task}")
print("Your to do list:")
for index, task in enumerate(my_list):
    print(f"{index + 1}. {task}")
print("Your to do list is complete!")


print("----Fizzbuzz----")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)'''

print("----Currency Converter---")
print("Ready to use the coverter. \n Please select an option.")
while True:
    print("=" * 40)
    print("1. Press 1 for USD to INR conversion")
    print("2. Press 2 for INR to USD conversion")
    print("3. Press 3 for CAD to INR conversion")
    print("4. Press 4 for INR to CAD conversion")
    print("5. Press 5 to exit")
    print("6. Press 6 for USD to CAD conversion")
    print("=" * 40)
    choice = input("Enter choice: ")
    if choice == "5":
        print("Thank you for using the converter.")
        break
    elif choice in ("1", "2", "3", "4", "6"):
        amount = float(input("Enter the amount: "))
        if choice == "1":
            result = amount * 90
            print(f"USD ${amount:.2f} = INR Rs{result:.2f}")
        elif choice == "2":
            result = amount / 90
            print(f"INR Rs{amount:.2f} = USD ${result:.2f}")
        elif choice == "3":
            result = amount * 68
            print(f"CAD ${amount:.2f} = INR Rs{result:.2f}")
        elif choice == "4":
            result = amount / 68
            print(f"INR Rs{amount:.2f} = CAD ${result:.2f}")
    else:
        print("Invalid choice. Select an appropirate option from the menu.")
    

