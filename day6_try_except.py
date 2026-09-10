print("--- Block 1: basic try/except ---")
try:
    result = int("hello")
    print(result)
except ValueError:
    print("That wasn't a valid number.")
print("Program continues after this.")

print("--- Block 2: mismatched exception type ---")
try:
    result = int("hello")
except ValueError:
    print("This won't catch it.")

print("--- Block 3: multiple except blocks ---")
try:
    numbers = {"a": 1, "b": 2}
    value = numbers["c"]
except ValueError:
    print("That's not a valid value.")
except KeyError:
    print("That key doesn't exist.")


print("--- Block 4: catching anything ---")
try:
    result = 10 / 0
except Exception as e:
    print("Something went wrong:", e)


print("--- Grocery Calculator ---")
price = 0
while True:
    items = input("Enter the price of the item or type done to get the bill total:")
    if items == "done":
        break
    try:
       price += float(items)
    except ValueError:
       print("That's not a valid number")
print("The total bill is: ", price)
if price > 100:
    print("You have spent more than $100. You get a 10% discount!")
    discount = price * 0.10
    total = price - discount
    print("Your total after discount is: ", total)


print("--- Block 1: the long way ---")
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)

print("--- Block 2: list comprehension ---")
squares = [n ** 2 for n in numbers]
print(squares)

print("--- Block 3: comprehension with a condition ---")
evens = [n for n in numbers if n % 2 == 0]
print(evens)

print("--- Block 4: transform + filter together ---")
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]
print(squared_evens)


print("--- Block 5: dictionary comprehension ---")
word_lengths = {word: len(word) for word in ["python", "is", "fun"]}
print(word_lengths)

print("--- Block 5: dictionary comprehension ---")
sentence = "Pyhton is fun"
word_lengths = {word: len(word) for word in sentence.split()}
print(word_lengths)