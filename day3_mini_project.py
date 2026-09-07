'''print("--- Grocery Calculator ---")
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
print("Your to do list is complete!")'''


print("----Fizzbuzz----")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
