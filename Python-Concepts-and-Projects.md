# Python Concepts & Projects — Day 1-3

*The "why" behind each pattern. For pure syntax, see Python-Formulas-Reference.md*

---

## PART 1: CONCEPTS

### Variables Are Labels, Not Boxes
A variable is a name that points to an object sitting in memory — it does not "contain" the value directly. `x = 5` creates the object `5` first, then attaches the label `x` to it. `y = x` doesn't copy anything — it makes `y` a second label pointing to the same object.

### The Object Model
Every Python object bundles three things together in memory: its **type**, its **value**, and a **reference count** (tracking how many labels point to it, used to know when it's safe to free the memory). This is why even a simple integer is heavier (~28 bytes) than in C (4 bytes) — Python objects always carry this metadata.

### CPython Optimizations (implementation details, not language rules)
- **Small-int caching**: integers -5 to 256 are pre-created once and reused everywhere. Two variables with the same small int show the same `id()`.
- **Constant folding**: if the same literal appears twice in the same file, the compiler may share one object even outside the cached range — this is separate from small-int caching.

### `==` vs `is`
`==` asks "same value?" `is` asks "same object in memory?" Use `==` almost always. Use `is` specifically for `None` checks.

### Mutability vs Immutability
- **Mutable** (list, dict, set): can change in place — same object, same `id()`, before and after a change like `.append()`.
- **Immutable** (int, float, str, bool, tuple): any "change" creates a brand-new object; the original is untouched.
- Python never lets mutable objects share memory automatically — if it did, changing one label's list would silently corrupt every other label pointing at it. Caching/sharing is only ever safe for immutable types.

### Type Conversion Rules
Python never auto-converts between incompatible types (`"5" + 1` fails). Conversion must be explicit (`int()`, `str()`, `float()`). `int()` truncates toward zero; `round()` actually rounds — not the same operation.

### `ValueError` vs `TypeError`
- **`ValueError`**: the type is correct but the content doesn't make sense for the conversion — e.g. `int("hello")`.
- **`TypeError`**: two genuinely incompatible types are being combined — e.g. `"25" + 1` (string + int).
Both are unhandled by default, meaning they stop the entire program immediately — nothing after them runs.

### Strings Are Immutable
No string method changes the original — `.upper()`, `.replace()` etc. all return a **new** string. Must reassign (`s = s.upper()`) to actually keep the change.

### Slicing Rule (strings, and `range()`)
Start is **included**, end is **excluded** — consistently, everywhere in Python. `s[1:4]` gives indexes 1, 2, 3 — never 4. `range(1, 4)` gives 1, 2, 3 — same rule.

### Truthy / Falsy
`if x:` silently runs `bool(x)` on every condition, every time — there's no separate "truthy mode," it's how `if` always works. Falsy: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`. Everything else, including negative numbers, is truthy.

### How a List Actually Stores Items
A list doesn't contain its values directly — it holds **references** pointing to separate objects elsewhere in memory. This is why two lists with identical-looking values (`[1,2,3]` and `[1,2,3]`, written separately) are still two different objects, unless one was explicitly assigned from the other (`list2 = list1`).

### How a `for` Loop Actually Works
On each pass, the loop variable gets **re-pointed** to a different object — it doesn't hold anything fixed. The list itself never changes during a normal iteration; only what the loop variable currently points to changes.

### Why the Accumulator Must Be Initialized Outside the Loop
If `total = 0` sits inside the loop, it resets to zero on every single pass, wiping out everything accumulated so far — only the last addition ever survives. The starting point must exist once, before the loop begins, so each pass can build on the previous result.

### `while` Loop Danger — Infinite Loops
A `for` loop is inherently bounded (tied to a fixed list or `range()`). A `while` loop's stopping point depends entirely on the programmer correctly updating the right variable inside the loop body — forgetting that update causes an infinite loop, a genuinely common real-world bug at any experience level. (Ctrl+C in the terminal force-stops a runaway program.)

### `break` vs `continue`
`break` exits the loop entirely. `continue` skips only the rest of the current pass and moves to re-check the loop's condition for the next pass — the loop keeps running normally afterward.

### `input()` Always Returns a String
Even if the user types `25`, `input()` hands back `"25"`, not the number `25`. Must convert explicitly (`int(input(...))` or `float(input(...))`) before doing any math with it.

### Validating Numeric Input Without Exceptions
`.isnumeric()` / `.isdigit()` only recognize digit characters — neither accepts a decimal point, so they reject valid prices like `"4.99"`. A working manual check: `s.replace(".", "", 1).isdigit()` — strips the first decimal point, then checks the rest is all digits. (A cleaner but more advanced approach uses `try`/`except` — queued for a future session.)

### `elif` vs Separate `if` Statements
A chain of `if`/`elif`/`else` is checked in order and **stops at the first match** — the right choice for mutually exclusive options (a menu, a range of number bands). Separate standalone `if` statements are each checked independently every time, which is both wasteful and risks unintended double-execution if conditions ever overlap.

---

## PART 2: PROJECTS

### Project 1 — Simple Calculator
**What it does:** shows a menu (add/subtract/multiply/divide/exit), takes two numbers, performs the chosen operation, loops back until the user exits.
**Concepts exercised:** `while True` + `break` menu pattern, `elif` chains, `input()` + `float()` conversion, divide-by-zero guard (self-added).
**Real bug caught during build:** comparing `choice` (a string) against an integer instead of a string — the exit condition silently never matched.

### Project 2 — Grocery Bill Calculator
**What it does:** repeatedly collects item prices, running total, exits on typing "done", applies a 10% discount if the total exceeds $100.
**Concepts exercised:** collect-until-done loop pattern, accumulator pattern, manual input validation (`.replace(".", "", 1).isdigit()`), conditional logic running once after the loop ends.
**Real bug caught during build:** attempting to convert `"done"` to a float before checking whether it was the exit word — fixed by checking the exit condition first, converting second.

### Project 3 — To-Do List
**What it does:** collects tasks into a list one at a time until "done", then displays the full numbered list.
**Concepts exercised:** empty list initialization, `.append()`, `enumerate()` for human-friendly numbering (`index + 1`), same collect-until-done loop shape as Project 2 but building a list instead of a running total.

### Project 4 — FizzBuzz
**What it does:** loops through numbers 1-30, printing "FizzBuzz" for multiples of both 3 and 5, "Fizz" for multiples of 3 only, "Buzz" for multiples of 5 only, otherwise the number itself.
**Concepts exercised:** `%` (modulo) for divisibility checks, `elif` ordering — the combined condition (divisible by both) must be checked before the individual ones, or numbers like 15 would incorrectly stop at "Fizz".
**Real bug caught during build:** `range(1, 30)` excludes 30 itself — fixed to `range(1, 31)`, which also happened to be the one number that exercises the FizzBuzz branch.

---

## Still Open for Week 1
Tuples, sets, dictionaries, `try`/`except`, list/dict comprehensions.