print("--- Block 1: writing to a file ---")
with open("notes.txt", "w") as file:
    file.write("Hello, this is my first file.")

print("--- Block 2: reading a file ---")
with open("notes.txt", "r") as file:
    content = file.read()
print(content)

print("--- Block 3: writing to a file ---")
with open("notes.txt", "w") as file:
    file.write("Hello, this is my edited file.")

print("--- Block 4: reading a file ---")
#reading edited file
with open("notes.txt", "r") as file:
    content = file.read()
print(content)


print("--- Block 5: append mode ---")
with open("notes.txt", "a") as file:
    file.write("\nThis is a new line added without deleting the old content.")

with open("notes.txt", "r") as file:
    content = file.read()
print(content)

print("--- Block 6: reading line by line ---")
with open("notes.txt", "r") as file:
    lines = file.readlines()
print(lines)

print("--- Block 7: looping through lines ---")
with open("notes.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print(line)

print("--- Block 8: seeing the double newline directly ---")
with open("notes.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print(repr(line))

for line in lines:
    print(line.strip())


print("--- Testing raw strings ---")
normal_string = "Line 1\nLine 2"
raw_string = r"Line 1\nLine 2"
print(normal_string)
print(raw_string)

'''print("--- Testing 'r' mode on a missing file ---")
with open("does_not_exist.txt", "r") as file:
    content = file.read()'''

print("--- Testing 'a' mode on a missing file ---")
with open("does_not_exist.txt", "a") as file:
    file.write("First line ever.")

with open("does_not_exist.txt", "r") as file:
    content = file.read()
print(content)


print("=====To-Do List======")
tasks = []
try:
    with open("todo.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    print("No existing to-do list found, starting fresh.")
print(f"Here are you existing tasks: {tasks}")
while True:
    print("1- Add a new task")
    print("2- View tasks")
    print("3- exit")
    choice = input("Select an option: ")
    if choice == "3":
        break
    elif choice == "1":
        task = input("What would you like ot add?")
        tasks.append(task)
        with open("todo.txt", "a") as file:
            file.write(f"\n {task}")
    elif choice == "2":
        with open("todo.txt", "r") as file:
            content = file.readlines()
        for line in content:
            print(line.strip())
            #content = file.read()
        #print(content.strip())
    else:
        print("Invalid choice. Select an appropriate option: ")


print("=====Simple Logger====")
def log_message(message):
    with open("log.txt", "a") as file:
        file.write(message + "\n")

log_message("KeyError-Missing Key")
log_message("ValueError-incorrect data type")
log_message("FileNotFoudnError-Missing file")

with open("log.txt", "r") as file:
    logs = file.read()
print(logs)

print("=====Word counter =============")
words ={}
with open("does_not_exist.txt", "r") as file:
    content = file.read()
    word = content.split()
    for n in word:
        if n in words:
            words[n] = words[n] +1
        else:
            words[n] = 1
    print(content)
    print(word)
    print(words)


