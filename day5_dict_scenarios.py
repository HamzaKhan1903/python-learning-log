print("---dictionary building with two lists----")
students = ["Ravi", "Meera", "John", "Sana", "Priya"]
scores = [45, 78, 32, 91, 60]
student_score = {}
for index, student in enumerate(students):
    student_score[student] = scores[index]
print(student_score)
pass_count = 0
fail_count = 0
for student, score in student_score.items():
    if score > 40:
        print( student, "Pass")
        pass_count += 1
    else:
        print(student, "Fail")
        fail_count += 1
print(pass_count)
print(fail_count)

print("-----Inventory checker -----")
items = ["apples", "bananas", "oranges", "grapes"]
quantities = [12, 5, 0, 8]
item_quantity = {}
for index, item in enumerate(items):
    item_quantity[item] = quantities[index]
print(item_quantity)
in_stock_items = 0
out_of_stock_items = 0
for item, quantity in item_quantity.items():
    if quantity > 0:
        print(item, "In stock")
        in_stock_items += 1
    else:
        print(item, "Out of stock")
        out_of_stock_items += 1
print("Total items in stock:", in_stock_items)
print("Total items of stock:", out_of_stock_items)

print("=== longest word finder ====")
sentence = "python is a genuinely powerful and flexible programming language"
split_word = sentence.split()
print(split_word)
word_length = {}
for word in split_word:
    word_length[word] = len(word)
print(word_length)
longest_length = 0
longest_word = ""
for word, length in word_length.items():
    if length > longest_length:
        longest_length = length
        longest_word = word 
print(longest_length)
print(longest_word)

'''
print("=== Shopping cart by category====")
item_names = ["bread", "milk", "notebook", "eggs", "pen"]
prices = [3.5, 2.8, 1.2, 4.0, 0.9]
categories = ["grocery", "grocery", "stationery", "grocery", "stationery"]
category_total ={}
for index, item in enumerate(item_names):
    category_total[item] = prices[index]
print(category_total)
print(category_total.items())


print("=== Shopping cart by category====")
item_names = ["bread", "milk", "notebook", "eggs", "pen"]
prices = [3.5, 2.8, 1.2, 4.0, 0.9]
categories = ["grocery", "grocery", "stationery", "grocery", "stationery"]
category_total ={}
running_total=0
for index, categories in enumerate(categories):
    category_total[categories] = item_names[index]
print(category_total)

print("=== Shopping cart by category====")
item_names = ["bread", "milk", "notebook", "eggs", "pen"]
prices = [3.5, 2.8, 1.2, 4.0, 0.9]
categories = ["grocery", "grocery", "stationery", "grocery", "stationery"]
category_total ={}
running_total=0
for index, category in enumerate(categories):
    category_total[category] = prices[index]
print(category_total)
'''

print("=== Shopping cart by category====")
item_names = ["bread", "milk", "notebook", "eggs", "pen"]
prices = [3.5, 2.8, 1.2, 4.0, 0.9]
categories = ["grocery", "grocery", "stationery", "grocery", "stationery"]
category_total = {}
for index, category in enumerate(categories):
    if category in category_total:
        category_total[category] = category_total[category] + prices[index]
    else:
        category_total[category] = prices[index]
print(category_total)
highest_category = ""
highest_total = 0
for category, total in category_total.items():
    if total > highest_total:
        highest_category = category
        highest_total = total
print(highest_category)
print(highest_total)

