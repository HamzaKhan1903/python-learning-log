# Python Concepts & Projects — Day 1-4

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

### Mutability vs Immutability — The Master Rule
- **Mutable** (list, dict, set): can change in place — same object, same `id()`, before and after a change like `.append()`.
- **Immutable** (int, float, str, bool, tuple): any "change" creates a brand-new object; the original is untouched.
- Python never lets mutable objects share memory automatically — if it did, changing one label's list would silently corrupt every other label pointing at it. Caching/sharing is only ever safe for immutable types.

### Hashability — Why Sets Can't Hold Lists
A set needs a fast, reliable way to check "have I seen this value before" — it does this using a **hash** (a fixed fingerprint computed from the value). Only immutable types can be hashed reliably, because if a value could change after its hash was computed and filed away, the hash would go stale and silently corrupt the set's internal organization. This is why **only hashable (immutable) types can go inside a set** — a list inside a set raises `TypeError`, not because the values are wrong, but because the type itself is fundamentally incompatible with the operation.

### Type Conversion Rules
Python never auto-converts between incompatible types (`"5" + 1` fails). Conversion must be explicit (`int()`, `str()`, `float()`). `int()` truncates toward zero; `round()` actually rounds — not the same operation.

### `ValueError` vs `TypeError`
- **`ValueError`**: the type is correct but the content doesn't make sense for the conversion — e.g. `int("hello")`.
- **`TypeError`**: two genuinely incompatible types/operations are being combined — e.g. `"25" + 1` (string + int), `tuple[0] = 99` (item assignment not supported on tuples), or a list inside a set (not hashable).
Both are unhandled by default, meaning they stop the entire program immediately — nothing after them runs.

### Strings Are Immutable
No string method changes the original — `.upper()`, `.replace()` etc. all return a **new** string. Must reassign (`s = s.upper()`) to actually keep the change.

### String Repetition (`*`) vs String Addition (`+`)
`+` between a string and an int is undefined and always raises `TypeError` — Python has no sensible universal meaning for "text plus a number." `*` between a string and an int IS defined — it means "repeat this string N times" (`"=" * 40` gives 40 equal signs). Each operator's valid behavior depends on the specific pair of types involved, not a general rule about which operator is "more forgiving."

### Slicing Rule (strings, lists, tuples, and `range()`)
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

### If/Elif Chains Do NOT Require an Else — and Why That's Dangerous
An `else` is entirely optional. If none of the conditions match and there's no `else`, Python silently does nothing and moves on — no error, no output, no trace that anything happened. This is a genuinely more dangerous failure mode than a crash, because a crash tells you something went wrong; a silent no-op doesn't. **Lesson learned live tonight**: when new options are added to a validity check (an outer `elif choice in (...)`) but not mirrored inside a nested chain handling those options, the nested chain silently does nothing for the new option — the amount gets collected and thrown away with zero feedback. Two independent chains checking the same variable against the same values only stay in sync because a programmer manually keeps them consistent — nesting the specific-case chain inside the validity gate removes this risk structurally, since there's only one list of valid options to maintain, not two.

### Format Specifiers in F-Strings
`f"{value:.2f}"` — everything after the colon is a display instruction, not a substitution. `.2f` means: display as fixed-point notation (`f`), with exactly 2 digits after the decimal (`.2`). Useful for currency and any output where consistent decimal display matters. Note: a space before the format spec (`{value: .2f}`) has its own separate meaning (adds a leading space for positive numbers) — easy to type by accident, worth removing unless intentional.

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

### Project 5 — Currency Converter
**What it does:** menu-driven converter (USD↔INR, CAD↔INR), hardcoded exchange rates, formatted output using `.2f`.
**Concepts exercised:** planning with a flowchart before writing any code, string repetition (`"=" * 40` for menu dividers), nested `if`/`elif` inside a validity gate, format specifiers.
**Real bugs caught during build, in order:**
1. `elif choice == 2:` comparing a string against an int — same category as Project 1's bug, caught independently this time.
2. Unconditional `amount = float(input(...))` running even for invalid menu choices, before validity was checked — fixed by nesting the amount-collection inside a validity gate (`elif choice in ("1","2","3","4"):`).
3. Deliberately reproduced the "missing else" bug by adding a 6th menu option to the outer gate without adding a matching branch to the inner chain — confirmed live that the program silently collects and discards the input with zero feedback when no `else` exists to catch the unhandled case.

---

## Still Open for Week 1
Dictionaries, `try`/`except`, list/dict comprehensions.