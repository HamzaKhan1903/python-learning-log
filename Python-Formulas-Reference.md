# Python Formulas & Syntax Reference — Day 1-3

*Syntax patterns and formulas only. For the "why" behind each, see Python-Concepts-and-Projects.md*

---

## Checking Type & Identity

```python
type(x)        # returns the type of the object x points to
id(x)          # returns the memory address of the object x points to
x == y         # value equality
x is y         # identity — same object in memory
```

---

## Type Conversion

```python
int("5")       # str -> int
str(5)         # int -> str
float("3.14")  # str -> float
int(3.9)       # -> 3   (truncates toward zero)
round(3.9)     # -> 4   (rounds to nearest)
```

---

## Arithmetic Operators

```python
a + b     # addition
a - b     # subtraction
a * b     # multiplication
a / b     # true division — ALWAYS returns float
a // b    # floor division — rounds down, discards remainder
a % b     # modulo — remainder only
a ** b    # exponentiation (a to the power of b)
```

## Comparison Operators
```python
a > b   a < b   a >= b   a <= b   a == b   a != b
```

## Logical Operators
```python
a and b   # both must be True
a or b    # at least one must be True
not a     # flips True/False
```

---

## Strings

**Indexing (zero-based):**
```python
s[0]      # first character
s[-1]     # last character
```

**Slicing — start INCLUDED, end EXCLUDED:**
```python
s[a:b]    # characters from index a up to (not including) b
s[:b]     # from beginning up to b
s[a:]     # from a to the end
s[:]      # full copy
```

**Common methods (all return a NEW string, original untouched):**
```python
s.upper()
s.lower()
s.strip()               # removes leading/trailing whitespace
s.replace(old, new)
s.split()                # splits into a LIST, default on whitespace
s.replace(".", "", 1).isdigit()   # manual "is this a valid number" check
```

**F-strings:**
```python
f"text {variable} more text"
f"{a + b}"          # code inside {} is evaluated live
```

---

## Conditionals

```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...
```

**Truthy / Falsy check (what `if` does internally):**
```python
bool(x)   # False for: 0, 0.0, "", [], {}, set(), None — True for everything else
```

---

## Loops

**For loop — over a list:**
```python
for item in my_list:
    ...
```

**For loop — with index (enumerate):**
```python
for index, item in enumerate(my_list):
    print(f"{index + 1}. {item}")
```

**Range — start included, stop EXCLUDED:**
```python
range(5)          # 0,1,2,3,4
range(2, 10, 2)   # 2,4,6,8   (start, stop, step)
```

**Nested loops:**
```python
for i in range(a, b):
    for j in range(c, d):
        ...
```

**Accumulator pattern (initialize OUTSIDE the loop):**
```python
total = 0
for num in numbers:
    total = total + num     # or: total += num
```

**While loop — condition-based:**
```python
while condition:
    ...
    # something inside MUST eventually make condition False
```

**Infinite loop + manual exit:**
```python
while True:
    ...
    if exit_condition:
        break
```

**Skip current pass only:**
```python
while condition:
    ...
    if skip_condition:
        continue
    ...
```

---

## Input

```python
x = input("prompt text: ")     # ALWAYS returns a string
x = int(input("prompt: "))     # convert immediately if you need a number
x = float(input("prompt: "))   # use float if decimals are possible
```

---

## Lists

```python
my_list = []                  # empty list
my_list = [1, 2, 3]
my_list.append(item)          # adds to the end, modifies in place
list1 is list2                # False unless list2 = list1 (same object)
list1 == list2                # True if values match, regardless of identity
```

---

## Menu / Exit Loop Template (calculator pattern)

```python
while True:
    print("menu options...")
    choice = input("Enter your choice: ")
    if choice == "exit_value":
        break
    elif choice == "option_1":
        ...
    elif choice == "option_2":
        ...
    else:
        print("Invalid choice.")
```

## Collect-Until-Done Loop Template (grocery/to-do pattern)

```python
result = []          # or 0 if accumulating a number
while True:
    entry = input("Enter value or 'done' to finish: ")
    if entry == "done":
        break
    elif entry.replace(".", "", 1).isdigit():   # validation, for numbers
        result.append(float(entry))              # or accumulate: result += float(entry)
    else:
        print("Invalid input.")
```