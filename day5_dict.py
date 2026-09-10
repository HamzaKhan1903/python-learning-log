print("--- Block 1: dictionary basics ---")
person = {"name": "Hamza", "age": 30, "city": "Mississauga"}
print(person["name"])
print(person["age"])

'''print("--- Block 2: missing key ---")
print(person["country"])'''

print("--- Block 3: safe access with .get() ---")
print(person.get("name"))
print(person.get("country"))
print(person.get("country", "Unknown"))

print("--- Block 4: word count ---")
sentence = "the cat sat on the mat the cat ran"
words = sentence.split()
print(words)

print("--- Testing 'in' with a dictionary ---")
word_counts = {}
print("cat" in word_counts)
word_counts["cat"] = 1
print("cat" in word_counts)

print("--- Block 5b: running the same logic again ---")
word = "cat"
if word in word_counts:
    word_counts[word] = word_counts[word] + 1
else:
    word_counts[word] = 1
print(word_counts)

'''print("--- Testing + 1 on a string value ---")
person = {"name": "Hamza"}
print(person["name"] + 1)'''

person["name"] = "khan"    # quotes make it a literal string, not a key lookup
print(person["name"])

print("--- Full word count ---")
sentence = "the cat sat on the mat the cat ran"
words = sentence.split()
word_counts = {}
print(words)
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1
print(word_counts)

print("--- Block 6: keys, values, items ---")
person = {"name": "Hamza", "age": 30, "city": "Mississauga"}
print(person.keys())
print(person.values())
print(person.items())

print("--- Block 7: looping over a dictionary ---")
for key in person:
    print(key)

print("--- looping over .items() ---")
for key, value in person.items():
    print(key, value)

'''print("--- Block 8: removing keys ---")
person = {"name": "Hamza", "age": 30, "city": "Mississauga"}
del person["city"]
print(person)

removed_value = person.pop("age")
print(person)
print(removed_value)

print("---edge case---")
person = {"name": "Hamza", "age": "30", "city": "Mississauga"}
del person["country"]
print(person)

print("--- Safe pop with a default ---")
person = {"name": "Hamza"}
result = person.pop("country", "no such key")
print(result)'''

print("--- Block 9: nested dictionary ---")
person = {
    "name": "Hamza",
    "age": "30",
    "address": {
        "city": "Mississauga",
        "Province": "Ontario"
    }
}
print(person)
print(person["address"])
print(person["address"]["city"])

person["address"]["city"] = "Toronto"
print(person)


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

