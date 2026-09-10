# Python Concepts & Projects — Week 1 Complete (Day 1-6)

*The "why" behind each pattern. For pure syntax, see Python-Formulas-Reference.md*

---

## PART 1: CONCEPTS

### Variables Are Labels, Not Boxes
A variable is a name that points to an object in memory — it doesn't "contain" the value. `x = 5` creates the object first, then attaches the label. `y = x` makes a second label point at the same object, no copy.

### The Object Model & CPython Optimizations
Every object bundles type + value + reference count together. Small ints (-5 to 256) are cached and reused. Repeated literals in the same file may get constant-folded into one shared object. Neither applies to mutable types — sharing a mutable object between labels would let a change through one label corrupt the other.

### `==` vs `is`
`==` asks "same value?" `is` asks "same object in memory?" Use `==` almost always; `is` specifically for `None` checks.

### Mutability — The Master Rule
Mutable (list, dict, set): change in place, same `id()`. Immutable (int, float, str, bool, tuple): any "change" creates a new object. Only immutable types are hashable, which is why only they can go inside a set or be used as a dictionary key.

### Type Conversion & Error Categories
Python never auto-converts incompatible types. Three distinct error categories, each diagnostic:
- **`ValueError`**: right type, bad content — `int("hello")`
- **`TypeError`**: operation invalid for the type itself — `"a" + 1`, `tuple[0] = x`, a list inside a set
- **`KeyError`**: dictionary key doesn't exist
- **`ZeroDivisionError`**: dividing by zero
- **`NameError`**: referencing a variable that was never created — a real, common bug from copy-pasting code between different loop contexts and reusing a variable name that only existed in the other one
Knowing the exact error name matters for two reasons: it tells you precisely what kind of mistake to look for before you've even reread the code, and it's required to write correctly targeted `except` blocks.

### Slicing & Range — Start Included, End Excluded
Consistent everywhere: strings, lists, tuples, `range()`. `s[1:4]` gives indexes 1,2,3. `range(1,4)` gives 1,2,3.

### Truthy / Falsy
`if x:` always silently runs `bool(x)`. Falsy: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`. Everything else, including negative numbers, is truthy.

### How Lists and Loops Actually Work
A list stores references to separate objects, not the values directly — two lists with identical-looking contents are still separate objects unless explicitly assigned from one another. A `for` loop variable gets re-pointed to a different object each pass; the list itself never changes during normal iteration.

### The Accumulator Pattern
The starting variable (`total = 0`, or a dictionary key's first value) must exist **outside** the loop — if it's reset inside the loop, every pass wipes out the previous progress and only the last value survives.

### If/Elif Chains Without an Else Are Dangerous
An `else` is optional. With none, unmatched input causes Python to silently do nothing — no crash, no output, no trace. This is more dangerous than a crash because nothing signals the failure. **Lesson learned live**: when a validity gate (outer `elif choice in (...)`) gets a new option added but a nested chain handling specifics doesn't get updated to match, the nested chain silently drops that case with zero feedback — input gets collected and discarded. Nesting the specific-case chain inside the gate (one list of valid values, not two) removes this risk structurally.

### Dictionaries — Key-Value Access
`dict[key]` crashes with `KeyError` if missing. `dict.get(key, default)` never crashes — returns `None` or a custom fallback. `dict[key] = value` is the same syntax for both creating a new key and updating an existing one. `key in dict` checks membership safely. `.pop(key)` removes AND returns the value; `del dict[key]` only removes, no fallback option exists for `del`. Nested dictionaries are still fully mutable at any depth — `person["address"]["city"] = "Toronto"` works because the inner dictionary is a real, separate mutable object, nesting doesn't change that.

### The Zip-Two-Lists Pattern
When two separate lists are meant to correspond by position (names and scores, items and prices), `enumerate()` on one list gives an `index` that can be reused to look up the matching item in the *other* list at the same position — the index isn't tied to whichever list produced it, it's just a plain number usable anywhere. `dict(zip(list1, list2))` does the same pairing directly, more concisely, once the manual mechanism is understood.

### The "Find the Best/Max So Far" Pattern
Two tracking variables initialized before the loop (a "best value" and what it belongs to), updated together inside an `if` only when a new candidate beats the current best. The starting value matters: `0` works fine when the real values can never go below it (lengths, prices), but fails silently if the data can be negative (temperatures) — safer to start from the first real data point itself, or `float("-inf")` for guaranteed correctness regardless of the dataset.

### `try`/`except` — Catching Errors Without Crashing
Code inside `try:` runs normally until an error occurs; execution then jumps immediately to a matching `except`, and the program continues normally afterward — nothing after the crash point inside `try` runs, but the whole program does not stop. `except SpecificError:` only catches that exact category — a mismatched type sails through uncaught and the program still crashes. Multiple `except` blocks can target different error types; order matters only when using a broad `except Exception:` catch-all, which must always go **last** — placed first, it silently swallows every error before any more specific block below it ever gets a chance to run, making that code permanently unreachable.

### Why `try`/`except` Beats Manual Validation
Manually checking a string's format (`.isdigit()`, `.replace()` combinations) requires anticipating every edge case yourself — negative numbers, multiple decimal points, scientific notation — and each one needs its own patch. `try`/`except` instead lets Python's own, already-correct parser (`float()`) be the judge: attempt the real conversion, catch the failure if it happens. This was proven directly by rewriting the grocery calculator — the old manual check silently rejected valid negative prices; the `try`/`except` version handles them correctly with less code.

### Comprehensions
A compact way to build a list or dictionary from a loop, in one line: `[expression for item in iterable if condition]`. The `if` filter and the `expression` transform both operate independently on the same original loop item — the filter is not applied to the already-transformed value. Same idea in `{}` for dictionaries, with `key: value` in place of a single expression.

---

## PART 2: PROJECTS

### Project 1 — Simple Calculator
Menu loop, `elif` chain, divide-by-zero guard (self-added). **Bug caught:** comparing `choice` (string) against an int.

### Project 2 — Grocery Bill Calculator (v1, then rebuilt with try/except)
Collect-until-done loop, accumulator, discount logic after the loop. **v1 bug:** converting "done" before checking for it. **v1 limitation, later fixed:** manual `.isdigit()` validation silently rejected valid negative prices — rebuilt using `try`/`except`, confirmed working correctly on negative and malformed input through direct testing.

### Project 3 — To-Do List
Empty list, `.append()`, `enumerate()` for human-friendly numbering.

### Project 4 — FizzBuzz
`%` for divisibility, correct `elif` ordering (combined condition before individual ones). **Bug caught:** `range(1,30)` excludes 30.

### Project 5 — Currency Converter
Planned with a flowchart before writing code. String repetition for menu dividers, nested `if` inside a validity gate, `.2f` formatting. **Bugs caught, in sequence:** string/int comparison, unconditional input collection before validity check, and a deliberately reproduced "missing else" bug proving that unmatched nested cases fail completely silently with no error at all.

### Dictionary Scenario Set (6 of 10 target, ongoing)
1. **Inventory Tracker** — zip pattern, classify + count. Clean first attempt.
2. **Longest Word Finder** — find-max-so-far pattern, first use.
3. **Shopping Cart by Category** — dictionary-as-accumulator (`d[key] = d[key] + amount`), genuinely the hardest single line of the night to untangle (read-then-write on the same key), worked through by tracing all 5 passes by hand.
4. **Temperature Classifier** — three-way classification + find-max-so-far again, correctly reasoned that a negative-capable dataset needs a real starting value, not a guessed `0`.
5. **Grade Book Averager** — handled a list of lists correctly, independently learned and applied `zip()` as a cleaner alternative to manual `enumerate()`+indexing.
6. **Attendance Tracker** — clean, fast, first-attempt, including self-correcting `== True` to idiomatic `if attend:`.
**Observed trend:** error rate and correction needed dropped substantially from Scenario 1 to Scenario 6 — genuine evidence of the pattern becoming automatic, not just understood.

---

## WEEK 1: COMPLETE
Variables, all core data types, memory model, operators, strings, conditionals, loops (for/while), all four data structures (list/tuple/set/dict), exception handling, and comprehensions — all covered with tested depth, not just exposure.
**Next:** Week 2 — functions, scope, file handling, modules.