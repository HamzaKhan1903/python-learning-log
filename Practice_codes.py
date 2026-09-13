'''for i in range(1, 6):
    stars = i * "*"
    print(stars)'''

for i in range(1,6):
    i = i * "*"
    print(i)

for i in range(1, 6):
    stars = i * "*"
    print(stars)

for i in range(1, 6):
    i = i * "*"
    print(i)

rows = 5
for i in range(1, rows + 1):
    spaces = (rows - i) * " "
    stars = i * "*"
    print(spaces + stars)

rows = 5
for i in range(1, rows + 1):
    spaces = (rows - i) * " "
    stars = (2 * i - 1) * "*"
    # what goes in the print line, using both spaces and stars?
    print(spaces + stars + spaces)

rows = 5
for i in range(rows):
    for j in range(rows):
        print("*", end = " ")
    print()
    
