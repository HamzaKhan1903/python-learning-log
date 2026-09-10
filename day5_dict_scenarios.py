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

print("==== Temperature Classifier===")
cities = ["Toronto", "Dubai", "Moscow", "Mumbai", "Reykjavik"]
temps = [22, 41, -5, 34, 8]
city_temp ={}
for index, city in enumerate(cities):
    city_temp[city] = temps[index]
print(city_temp)
for city, temp in city_temp.items():
    if temp >= 30:
        print(city, "Hot")
    elif temp < 10:
        print(city, "Cold")
    else:
        print(city, "Moderate")
hottest_city = cities[0]
hottest_temp = temps[0]
for city, temp in city_temp.items():
    if temp > hottest_temp:
        hottest_city = city
        hottest_temp = temp
print(hottest_city)
print(hottest_temp)
print(hottest_city, hottest_temp)



print("====student scores list of lists=====")
students = ["Ravi", "Meera", "John"]
test_scores = [[80, 90, 70], [60, 65, 70], [95, 88, 92]]
#pair each student with their avg score
# avg = sum(n)/n
#create a new list first
avg_score = []
for score in test_scores:
    average = sum(score)/len(score)
    avg_score.append(average)
print(avg_score)
#create empty dict
student_avg = {}
# fill value in dict
for index, student in enumerate(students):
    student_avg[student] = avg_score[index]
print(student_avg)
highest_avg = 0
highest_avg_student = ""
for student, average in student_avg.items():
    if average > highest_avg:
        highest_avg = average
        highest_avg_student = student
print("The student with highest average is ", highest_avg_student, " with an average of ", highest_avg)


