print("--- Block 1: importing a module ---")
import math
print(math.sqrt(16))
print(math.pi)

print("--- Block 2: datetime ---")
import datetime
now = datetime.datetime.now()
print(now)

print("--- Block 4: importing your own file ---")
import my_helpers
print(my_helpers.double(5))

print("--- Block 5: importing your own file ---")
import my_helpers
print(my_helpers.square(5))

print("--- Block 6: importing your own file ---")
print(my_helpers.cube(5))

print("====Randome dice generator====")
import random
dice1 = random.randint(1, 6)   # gives a random whole number, 1 through 10, both ends included
dice2 = random.randint(1, 6)
print(f"This is dice1: {dice1}, and this is {dice2}")