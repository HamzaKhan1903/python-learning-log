print("--- Class attributes ---")
class Employee:
    company_name = "Acme Corp"      # CLASS attribute — one shared value, not per-object

    def __init__(self, name: str, hourly_rate: float, hours_worked: float) -> None:
        self.name = name                    # INSTANCE attribute — unique per object
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

emp1 = Employee("Sara", 25, 45)
emp2 = Employee("John", 30, 40)

print(emp1.company_name)
print(emp2.company_name)
print(Employee.__dict__)

print("--- Testing reassignment through one instance ---")
emp1.company_name = "New Corp"
print(emp1.company_name)
print(emp2.company_name)
print(Employee.company_name)

print("--- The actual proof: emp1's own dictionary ---")
print(emp1.__dict__)
print(emp2.__dict__)



print("--- Type hints ---")
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 3))

print("--- Type hints don't actually enforce anything ---")
print(add("5", "3"))

print("====Library tracker=====")
class Book:
    def __init__(self, title: str, author: str, is_checked_out: bool = False) ->None:
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out
    def check_out(self):
        self.is_checked_out = True
    def return_book(self):
        self.is_checked_out = False
    def __str__(self):
        return f"{self.title} by {self.author} is {'unavailable' if self.is_checked_out else 'available'}"

class Library:
    def __init__(self, books: list[Book]):
        self.books = books 
    def list_available_books(self):
        for book in self.books:
            if not book.is_checked_out:
                print(book.title)


books = [
    Book("Python Basics", "Alice"),
    Book("SQL Fundamentals", "Bob"),
    Book("Clean Code", "Robert"),
    Book("AI Engineering", "Sarah")
]
for book in books:
    print(book)

books[0].check_out()
print(books[0].is_checked_out)
for book in books:
    print(book)

my_library = Library(books)
print("====printing available books====")
my_library.list_available_books()