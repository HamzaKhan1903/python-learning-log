# Python Data Types & Structures — Quick Reference

---

## CORE DATA TYPES

**Definition:** The basic building-block types every value in Python belongs to.

| Type | Example | Mutable? | Notes |
|---|---|---|---|
| `int` | `5`, `-12` | No | Whole numbers |
| `float` | `5.0`, `3.14` | No | Decimal numbers |
| `str` | `"hello"` | No | Text |
| `bool` | `True`, `False` | No | Boolean |
| `None` | `None` | — | "No value" |

**Key Points:**
- All 5 are **immutable** — any "change" creates a new object, original untouched
- `type(x)` tells you which one you're dealing with

---

## LIST vs TUPLE

**Definition:**
**List:** Ordered collection of items that is CHANGEABLE (Mutable).
**Tuple:** Ordered collection of items that is UNCHANGEABLE (Immutable).

**Comparison Table:**

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[ ]` | `( )` |
| Mutable/Immutable | Mutable | Immutable |
| Ordered | Yes | Yes |
| Allows duplicates | Yes | Yes |
| Can index/slice | Yes | Yes |
| Can reassign an item | Yes | **No** — TypeError |
| Use case | Data that will change | Data that's fixed (coordinates, dates) |

**Examples:**

```python
# List
a = [1, 2, 3]
a.append(4)
a[0] = 10
print(a)          # [10, 2, 3, 4]

# Tuple
t = (1, 2, 3)
print(t[0])        # 1
print(t[1:])        # (2, 3)
t[0] = 10           # TypeError — not allowed
```

**Key Points:**
- Use **list** when data can change.
- Use **tuple** when data should not change.
- A list of identical values written twice is still 2 separate objects (mutable types never auto-share memory). A tuple assigned from another (`t2 = t1`) IS the same object.

**Exam tip:**
→ Use list for operations like add, remove, modify.
→ Use tuple to signal "this is fixed and shouldn't change" directly in the code.

---

## SET

**Definition:** Unordered collection where every item is automatically unique — duplicates are silently dropped.

**Comparison Table:**

| Feature | List | Set |
|---|---|---|
| Syntax | `[ ]` | `{ }` |
| Ordered | Yes | No — no guaranteed order |
| Allows duplicates | Yes | **No** — auto-removed |
| Indexable (`x[0]`) | Yes | **No** — not supported |
| Can hold mutable items (e.g. a list) | Yes | **No** — TypeError, items must be hashable |

**Examples:**

```python
numbers = {1, 2, 3, 2, 1}
print(numbers)          # {1, 2, 3} — duplicates gone

fruits = {"apple", "banana"}
fruits.add("cherry")
fruits.remove("banana")
print(fruits)            # {'apple', 'cherry'}
```

**Set operations (real set-theory math):**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)     # union — everything in either:      {1,2,3,4,5,6}
print(a & b)     # intersection — in both:              {3,4}
print(a - b)     # difference — in a, not in b:          {1,2}
```

**Key Points:**
- Use **set** when you need automatic de-duplication, or fast "is this in here?" checks.
- Sets can't contain lists/dicts/other sets — only immutable (hashable) items.

**Exam tip:**
→ "Give me only unique values" or "find common items between two groups" = set is the right tool.

---

## MUTABLE vs IMMUTABLE — the master rule

| | Mutable | Immutable |
|---|---|---|
| Types | list, dict, set | int, float, str, bool, tuple |
| Changes in place? | Yes — same `id()` before/after | No — any "change" makes a new object |
| Can two labels share one object safely? | Never automatically (would corrupt) | Yes — small-int caching, string interning, `t2 = t1` |
| Can go inside a set? | No — not hashable | Yes — hashable |

**Exam tip:**
→ If it can be indexed AND changed after creation → mutable.
→ If "changing" it actually means "making a new one" → immutable.

---

*Still to add once covered: Dictionaries, and how they compare to lists/sets for key-based lookup.*