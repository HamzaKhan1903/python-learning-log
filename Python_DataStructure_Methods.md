# Python Data Structure Methods — Quick Reference

*Method name, what it does, example. Organized by data structure.*

---

## LIST METHODS
*Lists are mutable — most of these change the list in place.*

| Method | What it does | Example |
|---|---|---|
| `.append(x)` | Adds `x` to the end of the list | `fruits.append("cherry")` |
| `.insert(i, x)` | Inserts `x` at position `i`, shifts everything after it right | `fruits.insert(0, "mango")` |
| `.remove(x)` | Removes the **first** matching value `x`. Raises `ValueError` if not found | `fruits.remove("banana")` |
| `.pop()` | Removes and **returns** the last item | `last = fruits.pop()` |
| `.pop(i)` | Removes and returns the item at position `i` | `first = fruits.pop(0)` |
| `.sort()` | Sorts the list **in place**, ascending by default | `numbers.sort()` |
| `.sort(reverse=True)` | Sorts in place, descending | `numbers.sort(reverse=True)` |
| `.reverse()` | Reverses the list in place | `fruits.reverse()` |
| `.index(x)` | Returns the position of the first match of `x`. Raises `ValueError` if not found | `fruits.index("banana")` |
| `.count(x)` | Counts how many times `x` appears | `numbers.count(3)` |
| `.extend(other_list)` | Adds all items from another list onto the end | `fruits.extend(more_fruits)` |
| `.clear()` | Removes everything, leaves an empty list | `fruits.clear()` |
| `len(my_list)` | Not a method (a built-in function), but the most common check — number of items | `len(fruits)` |

---

## TUPLE METHODS
*Tuples are immutable — genuinely only 2 real methods exist, since nothing can be added/removed/changed.*

| Method | What it does | Example |
|---|---|---|
| `.count(x)` | Counts how many times `x` appears | `point.count(5)` |
| `.index(x)` | Returns the position of the first match of `x` | `point.index(10)` |
| `len(my_tuple)` | Number of items (built-in function, not a method) | `len(point)` |

*No `.append()`, `.remove()`, `.sort()`, etc. — none of these exist for tuples, since they'd all require modifying the tuple, which is not allowed.*

---

## SET METHODS
*Sets are mutable, but items are unordered and duplicates are never allowed.*

| Method | What it does | Example |
|---|---|---|
| `.add(x)` | Adds `x` to the set. No effect if `x` is already present | `fruits.add("cherry")` |
| `.remove(x)` | Removes `x`. Raises `KeyError` if not found | `fruits.remove("banana")` |
| `.discard(x)` | Removes `x` if present — does **NOT** error if it's missing (safer than `.remove()`) | `fruits.discard("banana")` |
| `.pop()` | Removes and returns an **arbitrary** item (sets have no order, so you can't choose which) | `item = fruits.pop()` |
| `.clear()` | Removes everything | `fruits.clear()` |
| `.union(other)` | Same as `\|` — everything in either set | `a.union(b)` |
| `.intersection(other)` | Same as `&` — only what's in both | `a.intersection(b)` |
| `.difference(other)` | Same as `-` — in this set, not the other | `a.difference(b)` |
| `len(my_set)` | Number of items (built-in function) | `len(fruits)` |

---

## DICTIONARY METHODS
*Dictionaries are mutable. Key-value pairs, accessed by key, not position.*

| Method | What it does | Example |
|---|---|---|
| `.get(key)` | Safely retrieves a value — returns `None` if the key doesn't exist (no crash) | `person.get("name")` |
| `.get(key, default)` | Same, but returns your custom fallback instead of `None` | `person.get("country", "Unknown")` |
| `.pop(key)` | Removes the key and **returns** its value. Raises `KeyError` if missing | `age = person.pop("age")` |
| `.pop(key, default)` | Same, but returns your fallback instead of crashing if missing | `person.pop("country", "N/A")` |
| `del dict[key]` | Removes the key. Not a method — a statement. Raises `KeyError` if missing, no fallback option | `del person["city"]` |
| `.keys()` | Returns a view of just the keys | `person.keys()` |
| `.values()` | Returns a view of just the values | `person.values()` |
| `.items()` | Returns a view of `(key, value)` pairs — used for looping with `for k, v in ...items():` | `person.items()` |
| `.update(other_dict)` | Merges another dictionary in, overwriting any matching keys | `person.update({"age": 31})` |
| `.clear()` | Removes everything | `person.clear()` |
| `key in my_dict` | Checks if a key exists — `True`/`False`, no crash either way | `"name" in person` |
| `len(my_dict)` | Number of key-value pairs (built-in function) | `len(person)` |

---

## Quick Comparison — Which One Fails, and How

| Structure | Missing item lookup | Error type |
|---|---|---|
| List | `my_list[99]` (index out of range) | `IndexError` |
| List | `.remove(x)` when `x` isn't present | `ValueError` |
| Tuple | `.index(x)` when `x` isn't present | `ValueError` |
| Set | `.remove(x)` when `x` isn't present | `KeyError` |
| Set | `.discard(x)` when `x` isn't present | No error — safe |
| Dict | `my_dict[key]` when key doesn't exist | `KeyError` |
| Dict | `.get(key)` when key doesn't exist | No error — returns `None` or your default |
| Dict | `.pop(key)` when key doesn't exist, no default given | `KeyError` |

*This table exists because knowing exactly which error a given operation throws is what lets you write correct, targeted `try`/`except` handling later.*