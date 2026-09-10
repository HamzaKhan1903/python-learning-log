# Functions — Notes & Roadmap

*What's covered so far (Week 2, Day 1), and what's still coming.*

---

## COVERED TONIGHT

### What a function actually is
A block of code, packaged once under a name, that can be run again anywhere just by calling that name — instead of retyping or copy-pasting the same logic every time it's needed.

### Defining vs calling — these are two separate steps
```python
def greet():
    print("Hello!")
```
Writing this **defines** the function — it does NOT run it. The code inside only executes when you actually **call** it:
```python
greet()
```
Forgetting the `()` when calling, or expecting the code to run just because it's defined, is a common early mistake.

### Parameters — giving a function input
```python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Hamza")   # prints "Hello, Hamza!"
greet_person("Sara")     # same function, different output, because different input
```
`name` is a **parameter** — a placeholder that receives whatever value gets passed in at call time. Same function body, different result each call, based on the input given.

### `return` vs `print` — genuinely different jobs
- `print()` — displays something in the terminal. Nothing is handed back to the program; once displayed, it's gone.
- `return` — hands a value **back** to wherever the function was called from, so it can be stored in a variable, used in further calculations, or printed by the caller.

```python
def add(a, b):
    return a + b

result = add(5, 3)   # result now holds 8
print(result)

print(add(2, 3))      # or use it immediately, no variable needed — prints 5
```

**If a function has no `return` at all**, calling it and trying to store the result gives you `None`:
```python
def add_no_return(a, b):
    print(a + b)        # displays 7

result = add_no_return(3, 4)
print(result)             # None — nothing was ever returned to store
```

### `return` is call-specific, not shared storage
Every function call is completely independent. `return` sends its value directly to the exact spot where that specific call happened — it is NOT a shared slot that different calls or different functions write into and overwrite.
```python
def add(a, b):
    return a + b

x = add(2, 3)     # x = 5
y = add(10, 20)   # y = 30
print(x)            # still 5 — completely unaffected by the second call
```

### The real payoff — one function, reused everywhere
Once a function is defined, it's available **anywhere in the rest of the program**, not just where it was first used — inside a menu's `elif` chain, inside a loop, inside another function. Write the logic once; call it as many times and in as many places as needed, instead of duplicating the same calculation throughout the file.

```python
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

if choice == "1":
    result = add(num1, num2)
elif choice == "2":
    result = subtract(num1, num2)
```
This is the direct upgrade path for the calculator project — each menu option calls a focused, single-purpose function instead of writing the math inline.

---

## STILL TO COME

### Default parameter values
Giving a parameter a fallback value so it's optional when calling:
```python
def greet(name="friend"):
    print(f"Hello, {name}!")
greet()          # uses the default — "Hello, friend!"
greet("Hamza")    # overrides it — "Hello, Hamza!"
```

### Scope — local vs global
Where a variable "lives" and whether code outside a function can see it. A genuinely common source of confusing bugs — variables created *inside* a function normally don't exist outside it, and variables from outside aren't automatically changeable from inside a function without extra care.

### `*args` and `**kwargs`
Ways to let a function accept a flexible, unknown number of arguments, rather than a fixed, exact list of parameters.

### Rebuilding the calculator using functions
Taking the actual calculator project and refactoring it to use one function per operation, called from the menu's `elif` chain — the direct, practical payoff of everything above, applied to real existing code.

### (Later, separate topic) Functions vs. Methods
Why `.append()`, `.get()`, etc. look similar to functions but are technically called "methods" — belonging to a specific object type, called with the dot syntax already used all through Week 1.

---

## Quick Self-Check Before Next Session
- Can I explain, out loud, the difference between defining and calling a function?
- Can I explain why `print()` inside a function and `return` inside a function behave differently when I try to store the result in a variable?
- Do I understand why `return` from one function call doesn't affect or get overwritten by a different call to the same function?