# Python OOP Reference — Classes, Objects & Everything Between

*Every topic shows the generic syntax template first, then a real working example.*

---

## 1. Class & Object — The Basics

**Generic syntax:**
```python
class ClassName:
    pass

object_name = ClassName()
```

**Real example:**
```python
class Employee:
    pass

emp1 = Employee()
```
A class is a blueprint. An object (instance) is a real thing built from it. Defining a class does NOT create any objects — nothing runs until you actually call `ClassName(...)`.

---

## 2. `__init__` and Attributes

**Generic syntax:**
```python
class ClassName:
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2

object_name = ClassName(value1, value2)
```

**Real example:**
```python
class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

emp1 = Employee("Sara", 25, 45)
print(emp1.name)          # "Sara"
```
`__init__` runs automatically the instant an object is created. `self` is always the first parameter — Python fills it in automatically at call time; you never pass it yourself. `self.attribute = value` creates a piece of data permanently stored ON that specific object (proven via `object_name.__dict__`).

**Parameter vs Attribute — the critical distinction:**
- **Parameter** (`name` in the `def` line) — a temporary local variable, exists only during that one function call, gone after. Works identically in any function, class or not.
- **Attribute** (`self.name`) — permanently stored on the object itself. Accessible any time the object exists, from any method, or from outside.

---

## 3. Methods & `self`

**Generic syntax:**
```python
class ClassName:
    def method_name(self, param):
        return self.attribute * param

object_name.method_name(value)
```

**Real example:**
```python
class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def is_overtime(self):
        return self.hours_worked > 40

emp1 = Employee("Sara", 25, 45)
print(emp1.calculate_pay())      # 1125
print(emp1.is_overtime())         # True
```
A method is just a function that lives inside a class and always takes `self` first. `self` refers to whichever specific object the method was called on — re-bound fresh on every call, so `emp1.calculate_pay()` and `emp2.calculate_pay()` never interfere with each other.

**A method only executes when explicitly called** — defining `calculate_pay` does not run it; only `emp1.calculate_pay()` does.

---

## 4. Multiple Objects, Storing Them in a List

**Generic syntax:**
```python
items = []
items.append(ClassName(value1, value2))

for item in items:
    print(item.attribute)
```

**Real example:**
```python
emp = []
emp.append(Employee("Ravi", 25, 45))
emp.append(Employee("John", 30, 40))

for employee in emp:
    print(employee.name, employee.calculate_pay())
```
Each object created from the same class has its own completely separate storage — proven directly via `id(emp1) != id(emp2)` and `emp1.__dict__ != emp2.__dict__`. A list just holds multiple independent objects together; the list itself has no attributes belonging to the objects inside it (`emp.name` → `AttributeError`, only `emp[0].name` works).

---

## 5. `__str__` — Controlling How an Object Prints

**Generic syntax:**
```python
class ClassName:
    def __str__(self):
        return f"description using {self.attribute}"
```

**Real example:**
```python
class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked
    def __str__(self):
        return f"{self.name}: ${self.calculate_pay()}"

emp1 = Employee("Sara", 25, 45)
print(emp1)          # "Sara: $1125" — instead of <__main__.Employee object at 0x...>
```
Without `__str__`, `print(obj)` shows the default, useless memory-address representation. `__str__` is a "dunder method" (double-underscore) — Python calls it automatically whenever the object needs to become a string (mainly `print()`). Note: `print(a_list_of_objects)` does NOT call `__str__` on each item — it shows raw defaults for each; you must loop and `print()` each object individually to trigger `__str__`.

---

## 6. Class Attributes vs Instance Attributes

**Generic syntax:**
```python
class ClassName:
    shared_value = "same for everyone"     # CLASS attribute — defined directly in class body

    def __init__(self, unique_value):
        self.unique_value = unique_value      # INSTANCE attribute — unique per object
```

**Real example:**
```python
class Employee:
    company_name = "Acme Corp"      # class attribute

    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name              # instance attribute
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

emp1 = Employee("Sara", 25, 45)
emp2 = Employee("John", 30, 40)
print(emp1.company_name)   # "Acme Corp"
print(emp2.company_name)   # "Acme Corp" — same shared value

emp1.company_name = "New Corp"     # does NOT change the shared value
print(emp1.company_name)     # "New Corp" — a NEW instance attribute was created on emp1 only
print(emp2.company_name)     # "Acme Corp" — untouched
print(Employee.company_name)  # "Acme Corp" — the real class attribute, still untouched
```
**Lookup rule, proven via `__dict__`:** Python checks the instance's own dictionary first. `emp1.company_name = "New Corp"` doesn't modify the shared class attribute — it creates a brand-new entry directly inside `emp1.__dict__`, which then shadows (wins over) the class-level value whenever accessed through `emp1` specifically. Every other instance, having no such entry in its own dictionary, still falls through to the real class attribute untouched.

---

## 7. Type Hints

**Generic syntax:**
```python
def function_name(param: type) -> return_type:
    ...
```

**Real example:**
```python
def __init__(self, name: str, hourly_rate: float, hours_worked: float) -> None:
    self.name = name
    self.hourly_rate = hourly_rate
    self.hours_worked = hours_worked

def calculate_pay(self) -> float:
    return self.hourly_rate * self.hours_worked
```
Type hints are NOT enforced by Python at runtime — `add("5", "3")` with hints `a: int, b: int` still runs and does string concatenation, no error. They're purely documentation, read by tools (IDEs, linters) and, critically, by agent frameworks: LangChain/OpenAI SDK etc. read a function's type hints via introspection to auto-generate the JSON schema an LLM needs to know what a "tool" expects — this is precisely why hints matter more in agentic AI code than in a small standalone script.

**Parameter hint + default value order:**
```python
param: type = default_value      # hint BEFORE the =, not after
```

---

## 8. Composition — "HAS-A"

**Generic syntax:**
```python
class Container:
    def __init__(self, contained_object: ContainedClass):
        self.contained_object = contained_object

container.contained_object.attribute      # chained dot access, like nested dict brackets
```

**Real example:**
```python
class Customer:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

class Order:
    def __init__(self, order_id: int, customer: Customer) -> None:
        self.order_id = order_id
        self.customer = customer      # this attribute IS a whole object, not plain data

sara = Customer("Sara", "sara@email.com")
order1 = Order(101, sara)
print(order1.customer.name)      # "Sara" — chained dot access
```

**A larger composition example — a class holding a LIST of other objects:**
```python
class Library:
    def __init__(self, books: list[Book]):
        self.books = books

    def list_available_books(self):
        for book in self.books:
            if not book.is_checked_out:
                print(book.title)

my_library = Library(books)
my_library.list_available_books()
```
Composition = one class **contains** another as an attribute (or a list of them). No special class-declaration syntax — just a normal parameter/attribute, where the value happens to be an object instead of a plain string/number. Test: "is a Library a Book?" — no → composition, not inheritance.

**Reference note:** if `Book` gets a new method tomorrow, `Library` does NOT need any update to use it — `library.books[0].new_method()` already works, since the objects inside the list already have it.

---

## 9. Inheritance — "IS-A"

**Generic syntax:**
```python
class Child(Parent):
    def __init__(self, parent_params, child_param):
        super().__init__(parent_params)
        self.child_attribute = child_param
```

**Real example:**
```python
class Employee:
    def __init__(self, name: str, hourly_rate: float, hours_worked: float) -> None:
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_pay(self) -> float:
        return self.hourly_rate * self.hours_worked

class Manager(Employee):
    def __init__(self, name: str, hourly_rate: float, hours_worked: float, team_size: int) -> None:
        super().__init__(name, hourly_rate, hours_worked)     # reuses Employee's setup
        self.team_size = team_size

    def team_info(self):
        print(f"{self.name} manages {self.team_size} people.")

mike = Manager("Mike", 40, 45, 5)
print(mike.name)             # "Mike" — inherited, never written in Manager
print(mike.calculate_pay())   # 1800 — inherited method
mike.team_info()                # only exists because Manager wrote it
```
`class Child(Parent):` — the parentheses mean "inherit everything." This is the ONLY reliable, name-independent test for inheritance (never guess from class names — check the parentheses in the declaration).

**Class order matters — a class referenced (in inheritance OR in a type hint) must already be defined ABOVE the line referencing it, or `NameError`.** Python reads top to bottom; nothing is "pre-scanned."

`super()` reaches the parent class. `super().__init__(...)` calls the parent's existing `__init__` instead of retyping its logic — pure DRY (Don't Repeat Yourself), not a mechanism for selectively choosing which attributes to inherit (inheritance itself is automatic and total; `super()` is just a convenience for reusing code).

**Method Overriding:**
```python
class Manager(Employee):
    def calculate_pay(self) -> float:        # same name as parent's method
        base_pay = super().calculate_pay()      # call parent's original version
        return base_pay + 200                     # then extend it

mike.calculate_pay()   # uses Manager's version, not Employee's — child's method wins
```
Python checks the object's own class first for a method; only if not found there does it walk up to the parent. A child's method with the same name takes priority (overrides), and the parent's own class is completely unaffected — same idea as a git branch, edited independently of `main`.

---

## 10. Encapsulation — The Underscore Convention

**Generic syntax:**
```python
class ClassName:
    def __init__(self, param):
        self._protected_attribute = param      # leading underscore = "internal, don't touch directly"

    def set_value(self, new_value):
        if <validation condition>:
            print("rejected")
        else:
            self._protected_attribute = new_value
```

**Real example:**
```python
class Employee:
    def __init__(self, name: str, hourly_rate: float, hours_worked: float) -> None:
        self.name = name
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    def calculate_pay(self) -> float:
        return self._hourly_rate * self._hours_worked

    def set_hourly_rate(self, new_rate: float):
        if new_rate < 0:
            print("Hourly rate cannot be negative.")
        else:
            self._hourly_rate = new_rate
```
**Critical, tested truth: the underscore enforces NOTHING mechanically.** `mike._hourly_rate = -500` still works, completely unguarded, proven directly (`-500 * 45` really does print). The underscore is purely a convention/signal to other developers — "treat this as internal." The ONLY real protection comes from routing changes through a method with actual validation logic (`set_hourly_rate`'s `if` check) — the attribute name alone never stops anything.

**Consistency requirement:** whatever name you choose (`hourly_rate` vs `_hourly_rate`) must be used identically in EVERY place that reads or writes it (`__init__`, every method). A mismatch (writing `self._hourly_rate` in one place, `self.hourly_rate` in another) silently creates two separate, disconnected attributes — no error, just quietly wrong behavior, since `self.x = value` always succeeds whether `x` already existed or not.

**A subclass inherits encapsulation for free** — `Manager` never wrote `set_hourly_rate`, but `mike.set_hourly_rate(-500)` still works correctly and rejects the bad value, purely through inheritance.

---

## Quick Vocabulary Reference

| Term | Definition |
|---|---|
| Class | The blueprint/template |
| Object / Instance | One real thing built from the blueprint |
| Attribute | Data belonging to a specific object (`self.x`), or shared by the whole class (`ClassName.x`) |
| Method | A function belonging to a class, first parameter always `self` |
| `self` | Refers to whichever specific object a method was called on — re-bound fresh each call |
| `__init__` | Dunder method, runs automatically at object creation, sets up initial attributes |
| `__str__` | Dunder method, runs automatically when the object is printed/stringified |
| `__dict__` | Reveals an object's (or class's) actual underlying storage — proves everything above directly |
| Composition | A class contains another object as an attribute — "HAS-A" |
| Inheritance | `class Child(Parent):` — child automatically gets everything the parent has — "IS-A" |
| `super()` | Calls the parent class's version of a method (usually `__init__`), to avoid duplicating code |
| Method Overriding | Child class defines a method with the same name as the parent's — child's version wins |
| Encapsulation | Underscore-prefixed attribute = convention signal only, not enforced; real protection needs a validating method |