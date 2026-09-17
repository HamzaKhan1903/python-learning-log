# JSON Reference — Data Types, Structure & Python Integration

*Every topic shows the generic syntax template first, then a real working example.*

---

## What JSON Actually Is, and Why It Exists

Python is a programming language. JSON (**J**ava**S**cript **O**bject **N**otation) is a **plain-text data format** — not a competitor to Python, a *translation layer* between systems.

**The core problem it solves:** a Python dictionary only exists in memory while your program runs, and no other language can read a raw Python object directly. JSON is a minimal, universal text structure that virtually every language can read and write — the common format systems use to exchange data regardless of what either side is written in.

**Directly relevant to the roadmap:** every LLM API request/response, every agent tool call, most framework config files — all JSON, because the API server is a separate system that doesn't run your Python code.

---

## Data Types — JSON vs Python

| JSON type | Python equivalent | Example |
|---|---|---|
| `object` | `dict` | `{"name": "Priya"}` |
| `array` | `list` | `[1, 2, 3]` |
| `string` | `str` | `"Priya"` — **double quotes only, never single** |
| `number` | `int` or `float` | `30`, `3.14` |
| `boolean` | `bool` | `true`, `false` — **lowercase, not Python's `True`/`False`** |
| `null` | `None` | `null` |

That's the entire type system — deliberately minimal so it's universally readable. No tuples, no sets — a Python tuple becomes a plain JSON array on conversion, losing its "immutable" distinction entirely.

**Tested, real strictness rules (not stylistic — genuine parse errors):**
```python
json.loads("{'name': 'Priya'}")     # FAILS — JSONDecodeError, single quotes not allowed
json.loads('{"name": "Priya"}')      # works

json.loads('{"active": True}')        # FAILS — capital True is invalid JSON
json.loads('{"active": true}')         # works, and correctly returns Python's True once parsed
```

---

## Memory Model — The Critical Distinction

**A JSON string, in memory, is just a plain string object** — no dictionary structure, no hashing, no key-based lookup. It's character data, same as any other string.

**Only once `json.loads()` parses it does Python build a genuine dictionary** — real `__dict__`-style storage, real hash-table lookup. Before parsing, JSON text only *looks* dictionary-shaped; it has none of that structure until converted.

---

## `dumps` / `loads` — Strings

**Generic syntax:**
```python
import json
json_string = json.dumps(python_object)
python_object = json.loads(json_string)
```

**Real example:**
```python
data = {"name": "Priya", "age": 30, "skills": ["Python", "SQL"]}

json_string = json.dumps(data)
print(json_string)          # '{"name": "Priya", "age": 30, "skills": ["Python", "SQL"]}'
print(type(json_string))      # <class 'str'>

parsed = json.loads(json_string)
print(parsed)                    # {'name': 'Priya', 'age': 30, 'skills': ['Python', 'SQL']}
print(type(parsed))                # <class 'dict'>
print(parsed["name"])                # "Priya" — normal dict access
```
`dumps` = Python → JSON text (so any other system can read it). `loads` = JSON text → real Python dict (so Python can work with it using everything already known about dictionaries).

**Readable formatting:**
```python
json.dumps(data, indent=2)     # adds line breaks and indentation, purely cosmetic, for debugging
```

---

## `dump` / `load` — Files (no `s`)

**Generic syntax:**
```python
with open("file.json", "w") as file:
    json.dump(python_object, file)

with open("file.json", "r") as file:
    python_object = json.load(file)
```

**Real example:**
```python
data = {"name": "Priya", "age": 30, "skills": ["Python", "SQL"]}

with open("employee.json", "w") as file:
    json.dump(data, file)

with open("employee.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data)
```
Same `with open(...) as file:` pattern from file handling — `json.dump`/`load` just handle the text conversion automatically instead of manually using `.write()`/`.read()`. Note the naming: **with an `s` (`dumps`/`loads`) = strings; without (`dump`/`load`) = files.**

---

## Nested JSON — Same Chaining as Nested Dictionaries

```python
data = {
    "name": "Priya",
    "address": {"city": "Toronto", "postal_code": "M5V 1A1"},
    "skills": ["Python", "SQL", "AI"]
}
data["address"]["city"]      # "Toronto" — identical chaining to Week 1 nested dicts
```
This nested shape is exactly what real API responses look like.

---

## When You Actually Write Raw JSON vs. Just Use Dictionaries

**Most common — you never hand-write JSON at all.** Work entirely with normal Python dictionaries; `json.dump()`/`dumps()` convert automatically at the boundary (saving to a file, sending to an API).

**You DO hand-write raw JSON for:** standalone config files (e.g. `config.json`) — edited directly, independent of the Python code, often by someone who isn't even reading the program:
```json
{
  "model": "gpt-4",
  "temperature": 0.7,
  "max_tokens": 500
}
```
Read it back with `json.load()`, same as any file.

**Receiving JSON — the most common real scenario:** an API response arrives already JSON-formatted from the *other* system — you never type it, only parse and navigate it (`response.json()` in the upcoming `requests` module hands you a ready-made dict directly).

---

## Hashing — Recap (Why Sets/Dict Keys Work, and Why It Matters at Scale)

Only **immutable** types can be hashed — if a value could change after its hash was computed, the hash would go stale and corrupt the lookup structure. This is why `{1, 2, [3, 4]}` raises `TypeError` (lists are mutable), and it's directly why JSON object keys are always strings — the universally simple, hashable choice across every language.

**Real, measured stakes — not theoretical:**
```python
customer_ids_set = set(range(1_000_000))
customer_ids_list = list(range(1_000_000))

# 10,000 repeated lookups of the worst-case (last) item:
# SET:  0.000000 seconds
# LIST: 57.443474 seconds
```
A set/dict gives near-constant-time lookup via hashing, regardless of size. A list requires a linear, item-by-item scan — genuinely catastrophic at scale. **Concrete relevance:** an agent's "have I seen this query/document before" cache must be a `set` or `dict`, not a `list`, or a long-running system can become unusably slow purely from the wrong data structure choice — not a bug, an architecture mistake.

---

## Quick Vocabulary Reference

| Term | Definition |
|---|---|
| `json.dumps()` | Python object → JSON string |
| `json.loads()` | JSON string → Python object |
| `json.dump()` | Python object → written directly to a file |
| `json.load()` | Read directly from a file → Python object |
| `null` | JSON's `None` |
| `true` / `false` | JSON's lowercase `True` / `False` |
| Hashing | Fixed-size "fingerprint" enabling near-instant lookup; only immutable types qualify |