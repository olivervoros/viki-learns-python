"""
=======================================================================
 PIE - LEARNING PYTHON
 SOLUTIONS: List Comprehensions, Tuples, Dictionaries and Sets
=======================================================================

These are worked answers to the exercises in python_collections_lesson.py.
Each one has a short note on WHY it is written that way, and several show
a longer alternative so you can see the loop hiding inside the one-liner.

Run it to check everything passes:
    python3 python_collections_solutions.py
=======================================================================
"""


# =====================================================================
# LIST COMPREHENSIONS
# =====================================================================


def ex1_squares(numbers):
    """[1, 2, 3] -> [1, 4, 9]"""
    # "Give me n times n, for every n in numbers."
    return [n * n for n in numbers]

    # The long way, for comparison:
    #   result = []
    #   for n in numbers:
    #       result.append(n * n)
    #   return result


def ex2_long_words(words):
    """["cat", "horse", "elephant"] -> ["horse", "elephant"]"""
    # No recipe here - we keep the word as it is - just a filter at the end.
    return [word for word in words if len(word) > 4]


def ex3_shout_short(words):
    """["cat", "Horse"] -> ["CAT", "horse"]"""
    # The if/else goes BEFORE the "for" because it decides the VALUE.
    # (An "if" placed after the "for" would decide whether to include it
    # at all - a filter. Two different jobs, two different positions.)
    return [w.upper() if len(w) < 5 else w.lower() for w in words]


def ex4_initials(full_names):
    """["Oliver Voros", "anna kis"] -> ["OV", "AK"]"""
    # An inner comprehension builds the letters, "".join glues them up.
    return ["".join(part[0].upper() for part in name.split()) for name in full_names]

    # Long way:
    #   result = []
    #   for name in full_names:
    #       letters = ""
    #       for part in name.split():
    #           letters += part[0].upper()
    #       result.append(letters)
    #   return result


# =====================================================================
# TUPLES
# =====================================================================


def ex5_first_and_last(items):
    """[3, 8, 1, 9] -> (3, 9)"""
    # The comma is what makes it a tuple - the brackets are only for clarity.
    return (items[0], items[-1])


def ex6_stats(numbers):
    """[2, 4, 9] -> (2, 9, 5.0)"""
    # Returning several values at once is exactly what tuples are for.
    average = round(sum(numbers) / len(numbers), 2)
    return min(numbers), max(numbers), average

    # The caller can then unpack it in one line:
    #   low, high, avg = ex6_stats([2, 4, 9])


def ex7_swap_pairs(pairs):
    """[(1, "a"), (2, "b")] -> [("a", 1), ("b", 2)]"""
    # Unpacking each tuple straight in the "for" makes this readable:
    # a and b get names instead of being pair[0] and pair[1].
    return [(b, a) for a, b in pairs]


# =====================================================================
# DICTIONARIES
# =====================================================================


def ex8_word_count(sentence):
    """ "the cat the" -> {"the": 2, "cat": 1}"""
    counts = {}
    for word in sentence.split():
        # .get(word, 0) means "the count so far, or 0 if this is the
        # first time I have seen it" - it avoids a KeyError.
        counts[word] = counts.get(word, 0) + 1
    return counts

    # Standard-library shortcut, once you know it exists:
    #   from collections import Counter
    #   return dict(Counter(sentence.split()))


def ex9_lengths(words):
    """["cat", "horse"] -> {"cat": 3, "horse": 5}"""
    # A dict comprehension: same sentence shape, but "key: value".
    return {word: len(word) for word in words}


def ex10_passing_students(scores, pass_mark=50):
    """{"a": 70, "b": 30} -> {"a": 70}"""
    # .items() hands back (key, value) tuples, which we unpack into
    # name and score - then filter on the score.
    return {name: score for name, score in scores.items() if score >= pass_mark}


def ex11_invert(mapping):
    """{"HU": "Budapest"} -> {"Budapest": "HU"}"""
    # Careful in real life: if two keys share a value, the flipped dict
    # keeps only the last one, because keys must be unique.
    return {value: key for key, value in mapping.items()}


# =====================================================================
# SETS
# =====================================================================


def ex12_unique_sorted(items):
    """[3, 1, 3, 2] -> [1, 2, 3]"""
    # set() throws the duplicates away; sorted() puts the result back
    # into a predictable order, because a set has no order of its own.
    return sorted(set(items))


def ex13_in_both(list_a, list_b):
    """[1, 2, 3], [2, 3, 4] -> [2, 3]"""
    # & is intersection: "on both guest lists".
    return sorted(set(list_a) & set(list_b))


def ex14_only_in_first(list_a, list_b):
    """[1, 2, 3], [2, 3, 4] -> [1]"""
    # - is difference: "on the first list, not on the second".
    return sorted(set(list_a) - set(list_b))


def ex15_distinct_letters(sentence):
    """ "Hello, hi!" -> 5"""
    # A set comprehension: lowercase every character, keep the letters,
    # and duplicates disappear on their own. Then just count them.
    letters = {ch.lower() for ch in sentence if ch.isalpha()}
    return len(letters)


# =====================================================================
# THE COMBINED ONE
# =====================================================================


def ex16_class_report(records):
    """records: list of (name, subject, score) tuples."""

    # 1. Unique subjects - a set does the de-duplicating for us.
    subjects = sorted({subject for _, subject, _ in records})
    # "_" is the usual name for "I have to unpack this slot but I do
    # not care about it".

    # 2. Group the scores by subject in a dictionary of lists.
    by_subject = {}
    for _, subject, score in records:
        by_subject.setdefault(subject, []).append(score)
        # setdefault: "give me the list for this subject, creating an
        # empty one first if it does not exist yet".

    # 3. Turn each list of scores into an average.
    averages = {
        subject: round(sum(scores) / len(scores), 1)
        for subject, scores in by_subject.items()
    }

    # 4. The single best result. max() with a key says "compare the
    #    records by their score", and it hands back the whole tuple.
    best = max(records, key=lambda record: record[2])
    top = (best[0], best[2])

    return {"subjects": subjects, "averages": averages, "top": top}


# =====================================================================
# CHECK
# =====================================================================


def _check():
    tests = [
        ("ex1", lambda: ex1_squares([1, 2, 3]), [1, 4, 9]),
        (
            "ex2",
            lambda: ex2_long_words(["cat", "horse", "elephant"]),
            ["horse", "elephant"],
        ),
        ("ex3", lambda: ex3_shout_short(["cat", "Horse"]), ["CAT", "horse"]),
        ("ex4", lambda: ex4_initials(["Oliver Voros", "anna kis"]), ["OV", "AK"]),
        ("ex5", lambda: ex5_first_and_last([3, 8, 1, 9]), (3, 9)),
        ("ex6", lambda: ex6_stats([2, 4, 9]), (2, 9, 5.0)),
        ("ex7", lambda: ex7_swap_pairs([(1, "a"), (2, "b")]), [("a", 1), ("b", 2)]),
        ("ex8", lambda: ex8_word_count("the cat the"), {"the": 2, "cat": 1}),
        ("ex9", lambda: ex9_lengths(["cat", "horse"]), {"cat": 3, "horse": 5}),
        ("ex10", lambda: ex10_passing_students({"a": 70, "b": 30}), {"a": 70}),
        ("ex11", lambda: ex11_invert({"HU": "Budapest"}), {"Budapest": "HU"}),
        ("ex12", lambda: ex12_unique_sorted([3, 1, 3, 2]), [1, 2, 3]),
        ("ex13", lambda: ex13_in_both([1, 2, 3], [2, 3, 4]), [2, 3]),
        ("ex14", lambda: ex14_only_in_first([1, 2, 3], [2, 3, 4]), [1]),
        ("ex15", lambda: ex15_distinct_letters("Hello, hi!"), 5),
        (
            "ex16",
            lambda: ex16_class_report(
                [("anna", "maths", 80), ("peter", "maths", 60), ("anna", "art", 90)]
            ),
            {
                "subjects": ["art", "maths"],
                "averages": {"art": 90.0, "maths": 70.0},
                "top": ("anna", 90),
            },
        ),
    ]

    print("=" * 60)
    print("SOLUTIONS - CHECK")
    print("=" * 60)
    passed = 0
    for name, run, expected in tests:
        got = run()
        ok = got == expected
        passed += ok
        print(f"  {name:<5} {'PASS' if ok else 'FAIL'}   {got!r}")
    print(f"\n  {passed}/{len(tests)} passing")


if __name__ == "__main__":
    _check()
"""
=========================================================================
LESSON  -  TUPLES, RANGES, LIST COMPREHENSION      about 75 minutes
=========================================================================

  Part 1   Tuples                20 min
  Part 2   Ranges                20 min
  Part 3   List comprehension    25 min
  Part 4   The three together    10 min

  Then:    12 tasks at the bottom.

WHY THESE THREE, IN THIS ORDER
------------------------------
  They are not three unrelated topics. They are one chain.

      a tuple   is a fixed group of values
      a range   is a fixed group of NUMBERS, described instead of stored
      a comprehension  is the machine that turns one group into another

  By Part 4 you will be writing [n * n for n in range(1, 11)] and every
  single piece of that line will be something you met earlier today.

HOW TO USE IT
-------------
  python tuples_ranges_comprehensions.py             read it, see it run
  python tuples_ranges_comprehensions.py tasks       just the 12 tasks
  python tuples_ranges_comprehensions.py solutions   the answers

Keep this file open on one side of the screen and an empty practice.py on
the other. Type the examples out yourself. Typing them is what makes them
stick; reading them is not.

Everything here was run on Python 3.11 before it was written down, so the
outputs in the comments are real.
"""

import sys


def head(text):
    print("\n" + "=" * 70)
    print(text)
    print("=" * 70)


def sub(text):
    print("\n" + text)
    print("-" * len(text))


# =========================================================================
# PART 1 - TUPLES
# =========================================================================


def part1_tuples():
    head("PART 1 - TUPLES  (20 min)")

    print("""
WHAT IT IS
  A tuple is a list that has been sealed shut.

  A list is a shopping list on a whiteboard. You add things, cross things
  off and reorder them all day long.
  A tuple is a letter you have already put in an envelope and sealed. You
  can read the address on it. You cannot change what is inside.

  Round brackets instead of square ones:

      shopping = ["milk", "bread"]     <- list, can change
      point    = (3, 5)                <- tuple, sealed

WHY BOTHER
  1. Some things should not change. A pair of coordinates, a date of
     birth, the two numbers a function hands back. Sealing them stops a
     whole family of accidents.
  2. Because it can never change, Python trusts it. Only a tuple can be
     a dictionary key or go inside a set. A list never can.
  3. It says something to the next reader: "these belong together and
     the order means something". (x, y) is a point. [x, y] is two numbers
     that happen to be next to each other.

WHEN A LIST IS BETTER
  When items get added or removed, when it is "many of the same thing"
  of unknown length, or when you need to sort it in place.
""")

    sub("See it run")
    point = (3, 5)
    print("point       =", point)
    print("point[0]    =", point[0], "  (reading is fine)")

    try:
        point[0] = 99  # changing is not
    except TypeError as e:
        print("point[0]=99 ->", type(e).__name__ + ":", e)

    sub("Unpacking - taking the values back out")
    x, y = point
    print("x, y = point   ->", x, "and", y)

    first, *rest = (1, 2, 3, 4)  # the star soaks up the remainder
    print("first, *rest   ->", first, rest, " (rest is a LIST)")

    a, b = 1, 2
    a, b = b, a  # the famous one-line swap
    print("a, b = b, a    ->", a, b, " (a tuple is built and unpacked)")

    sub("The most common use: a function that returns two things")

    def min_and_max(numbers):
        return min(numbers), max(numbers)  # this is a tuple

    low, high = min_and_max([4, 9, 2])
    print("min_and_max([4, 9, 2]) ->", low, "and", high)

    sub("The thing a list can never do")
    locations = {(51.5, -0.12): "London", (47.5, 19.04): "Budapest"}
    print("dictionary key ->", locations[(47.5, 19.04)])

    visited = {(0, 0), (1, 2)}  # a SET of coordinate pairs
    print("inside a set   ->", (1, 2) in visited)
    print("A list cannot do either of those. It might change, so Python")
    print("cannot trust it to stay the same key.")

    sub("The trap everybody hits once")
    print("(7)  is just the number seven ->", (7), type((7)).__name__)
    print("(7,) is a tuple               ->", (7,), type((7,)).__name__)
    print("It is the COMMA that makes a tuple, not the brackets.")

    sub("The second trap: sealed envelope, unsealed contents")
    box = (1, [2, 3])
    box[1].append(4)  # the tuple is fixed, the list is not
    print("box = (1, [2, 3]) then box[1].append(4) ->", box)
    print("The tuple still holds the same two things. One of those things")
    print("just happens to be a list, and lists can always change.")


# =========================================================================
# PART 2 - RANGES
# =========================================================================


def part2_ranges():
    head("PART 2 - RANGES  (20 min)")

    print("""
WHAT IT IS
  A range is a set of instructions for counting - not a list of numbers.

  A bus timetable does not print every departure for the next ten years.
  It says: "every 10 minutes, from 06:00 until 22:00". Three facts, and
  from those three you can work out any departure you like.

  A range is exactly that:

      range(start, stop, step)
             ^      ^     ^
             from   until how big a jump

  Leave parts off and Python fills them in:

      range(5)          0 1 2 3 4          start=0, step=1
      range(2, 6)       2 3 4 5            step=1
      range(0, 10, 2)   0 2 4 6 8

WHY BOTHER
  1. It is how you say "do this 10 times".
  2. It costs almost nothing. range(1_000_000) does not build a million
     numbers - it remembers three numbers and hands them out one at a
     time, as asked. A list of a million numbers eats memory. A range
     does not.

THE ONE RULE THAT CATCHES EVERYBODY
  The stop is NOT included. range(1, 11) gives you 1 to 10.
  Read it as "up to but not including". It matches the way slices work,
  and it means range(0, n) has exactly n items - which is usually what
  you want, once you stop fighting it.
""")

    sub("See it run")
    print("range(5)          ->", range(5), " <- it does not print the numbers!")
    print("list(range(5))    ->", list(range(5)), " <- ask for a list to SEE them")
    print("list(range(2, 6)) ->", list(range(2, 6)))
    print("list(range(0,10,2))->", list(range(0, 10, 2)))

    sub("Counting backwards - the step goes negative")
    print("list(range(10, 0, -1)) ->", list(range(10, 0, -1)))
    print("list(range(10, 0, -2)) ->", list(range(10, 0, -2)))
    print("Watch the stop: 0 is never printed, because stop is excluded.")

    sub("An empty range is not an error")
    print(
        "list(range(5, 1))  ->",
        list(range(5, 1)),
        " (you asked to count up, from 5, to 1)",
    )
    print("A loop over that simply never runs. No crash, no message.")
    print("If a loop of yours does nothing, check the direction of the step.")

    sub("It behaves like a sequence without being a list")
    r = range(0, 20, 3)
    print("r                  ->", r)
    print("len(r)             ->", len(r))
    print("r[0], r[-1]        ->", r[0], r[-1])
    print("9 in r             ->", 9 in r)
    print("10 in r            ->", 10 in r)
    print("list(r)            ->", list(r))

    sub("The everyday use: repeating something")
    total = 0
    for n in range(1, 101):  # 1 to 100
        total = total + n
    print("sum of 1 to 100    ->", total)

    for _ in range(3):  # _ means 'I do not need the value'
        print("   knock")

    sub("Two things that catch people out")
    print("1. range(1, 6) stops at 5, but random.randint(1, 6) CAN give 6.")
    print("   They disagree on purpose. It causes real bugs.")
    try:
        range(1, 10, 0)
    except ValueError as e:
        print("2. A step of 0 ->", type(e).__name__ + ":", e)
    print("   Sensible: a step of 0 would never arrive anywhere.")

    sub("And one habit to unlearn")
    students = ["Anna", "Bela", "Cili"]
    for i in range(len(students)):  # works, but it is the long way round
        print("   range(len(...)) ->", i, students[i])
    for i, name in enumerate(students, start=1):
        print("   enumerate       ->", i, name)
    print("Use range when you need NUMBERS. Use the list itself when you")
    print("need ITEMS, and enumerate when you honestly need both.")


# =========================================================================
# PART 3 - LIST COMPREHENSION
# =========================================================================


def part3_comprehension():
    head("PART 3 - LIST COMPREHENSION  (25 min)")

    print("""
WHAT IT IS
  A conveyor belt. Items travel along it, a machine does the same thing
  to every one, and a gate near the end lets only some of them through.

  Written out the long way:

      squares = []
      for n in numbers:
          squares.append(n * n)

  The same thing as a comprehension:

      squares = [n * n for n in numbers]
                 ^^^^^     ^^^^^^^^^^^
                 do this   to each n

  Add a gate on the end to keep only some of them:

      [n * n for n in numbers if n % 2 == 0]
                                ^^^^^^^^^^^ only the even ones get through

  Read it left to right: "n times n, for every n in numbers, if n is
  even."

  The order looks backwards at first, because the ANSWER comes first and
  the loop comes after. That is deliberate: the answer is the part you
  care about, so it gets the front seat.

HOW TO WRITE ONE WITHOUT GETTING LOST
  Write the loop first, the boring way. Then fold it up:

      1. new = []                        ->  [                    ]
      2. for n in numbers:               ->  [        for n in numbers]
      3.     if n % 2 == 0:              ->  [        for n in numbers if n % 2 == 0]
      4.         new.append(n * n)       ->  [n * n   for n in numbers if n % 2 == 0]

WHEN TO USE IT
  When you are building a NEW list out of an old one. That is it.

WHEN NOT TO
  When the loop body DOES something rather than produces something -
  printing, saving a file, sending an email. And whenever the one-liner
  is harder to read than four honest lines. Shorter is not better.
  Clearer is better, and usually shorter is clearer, but not always.
""")

    sub("See it run")
    numbers = [1, 2, 3, 4, 5, 6]
    print("numbers                                 ->", numbers)
    print("[n * n for n in numbers]                ->", [n * n for n in numbers])
    print(
        "[n * n for n in numbers if n % 2 == 0]  ->",
        [n * n for n in numbers if n % 2 == 0],
    )

    sub("The same thing, folded and unfolded")
    long_way = []
    for n in numbers:
        if n % 2 == 0:
            long_way.append(n * n)
    short_way = [n * n for n in numbers if n % 2 == 0]
    print("long way  ->", long_way)
    print("short way ->", short_way)
    print("identical ->", long_way == short_way)

    sub("The real everyday use: tidying data")
    names = ["  anna ", "BELA", " cili"]
    print("messy ->", names)
    print("tidy  ->", [n.strip().title() for n in names])

    sub("It works with the other containers too - only the brackets change")
    words = ["cat", "dog", "horse", "cow"]
    print("a list  [len(w) for w in words]     ->", [len(w) for w in words])
    print("a dict  {w: len(w) for w in words}  ->", {w: len(w) for w in words})
    print(
        "a set   {len(w) for w in words}     ->",
        {len(w) for w in words},
        " (3 appears once)",
    )

    sub("Two loops in one line - and where to stop")
    matrix = [[1, 2], [3, 4]]
    print("flatten a table ->", [cell for row in matrix for cell in row])
    print("Read the loops in the order you would have written them:")
    print("  for row in matrix:  then  for cell in row.")
    print("Two is already plenty. At three, write the honest loop.")

    sub("Where NOT to use one")
    print("  [print(w) for w in words]     <- wrong. print does something,")
    print("                                   it does not produce a value.")
    print("  You would get [None, None, None, None] and throw it away.")
    print("  Just write:   for w in words: print(w)")


# =========================================================================
# PART 4 - THE THREE TOGETHER
# =========================================================================


def part4_together():
    head("PART 4 - THE THREE TOGETHER  (10 min)")

    print("""
Look at this line and name every part of it:

      squares = [n * n for n in range(1, 11)]

      [ ... ]        a list is being built            Part 3
      n * n          the machine on the belt          Part 3
      range(1, 11)   the numbers 1 to 10, described   Part 2

A range is the most common thing to put on the right of a comprehension,
because so often you do not have a list yet - you just need the numbers.

And when each item on the belt is a TUPLE, unpacking works there too.
""")

    sub("A range feeding a comprehension")
    print("[n * n for n in range(1, 11)]        ->", [n * n for n in range(1, 11)])
    print(
        "[n for n in range(1, 21) if n % 3 == 0] ->",
        [n for n in range(1, 21) if n % 3 == 0],
    )

    sub("Tuples on the belt, unpacked as they go past")
    people = [("Anna", 34), ("Bela", 28), ("Cili", 41)]
    print("people                              ->", people)
    print("[name for name, age in people]      ->", [name for name, age in people])
    print("[n for n, a in people if a > 30]    ->", [n for n, a in people if a > 30])
    print("Each item is a tuple, so 'for name, age in people' unpacks it")
    print("on the way past. Part 1 doing real work inside Part 3.")

    sub("Building tuples, and zip - which hands you tuples")
    print("[(n, n * n) for n in range(1, 6)]   ->", [(n, n * n) for n in range(1, 6)])
    names = ["Anna", "Bela", "Cili"]
    ages = [34, 28, 41]
    print("list(zip(names, ages))              ->", list(zip(names, ages)))
    print("dict(zip(names, ages))              ->", dict(zip(names, ages)))
    print("zip is a zip fastener: two rows of teeth, joined into pairs.")


# =========================================================================
# TASKS
# =========================================================================

TASKS = """
=========================================================================
TASKS  -  write these in your own practice.py
=========================================================================

TUPLES
  1. Make a tuple holding your name and the city you live in. Unpack it
     into two variables and print a sentence using both.

  2. Write  first_and_last(items)  that takes a list and returns a TUPLE
     of its first and its last item.
         first_and_last([3, 8, 1, 9])   ->  (3, 9)

  3. Write  swap(pair)  that returns the two items the other way round.
     Use unpacking, not indexing.
         swap((1, 2))   ->  (2, 1)

  4. Why does this crash, and what is the smallest fix?
         seen = set()
         seen.add([0, 0])

RANGES
  5. Print the numbers 1 to 10, one per line. Then print them backwards,
     10 down to 1.

  6. Print every third number from 0 to 30 (0, 3, 6 ... 30). Careful:
     30 must actually appear.

  7. Without running it, say how many numbers are in each of these. Then
     check yourself with len().
         range(10)        range(1, 10)        range(0, 10, 2)
         range(5, 5)      range(10, 0, -1)

  8. This loop prints nothing. Why, and what are the TWO different ways
     to fix it?
         for n in range(10, 0):
             print(n)

LIST COMPREHENSION
  9. Turn each of these into a one-line comprehension:
       a) the first 10 square numbers
       b) from ["python", "is", "fun"], a list of the word lengths
       c) from range(1, 21), only the numbers divisible by 3

 10. From  words = ["apple", "fig", "banana", "kiwi", "plum"]  build a
     list of the words with more than 4 letters, in UPPERCASE.

 11.     prices = {"tea": 450, "coffee": 700, "cake": 900}
     Build a list of "tea costs 450 HUF" style strings, one per item.
     (Remember what .items() hands you each time round.)

 12. Putting all three together.
         readings = [("Mon", 12), ("Tue", 25), ("Wed", 31), ("Thu", 8)]
     a) a list of just the temperatures
     b) a list of the day names where it was warmer than 20
     c) a list of (day, fahrenheit) tuples, F rounded to a whole number
     d) using range, a list of the first 5 triangular numbers - that is
        1, 1+2, 1+2+3, and so on. (sum() and range() together.)

When you are done:  python tuples_ranges_comprehensions.py solutions
"""


SOLUTIONS = """
=========================================================================
SOLUTIONS
=========================================================================

# 1 -----------------------------------------------------------------
me = ("Oliver", "Budapest")
name, city = me
print(f"{name} lives in {city}.")
# The brackets are optional here - me = "Oliver", "Budapest" also works.
# The comma is what builds the tuple.

# 2 -----------------------------------------------------------------
def first_and_last(items):
    return (items[0], items[-1])          # -1 means "the last one"

print(first_and_last([3, 8, 1, 9]))       # (3, 9)
# A tuple, not a list, because it is always exactly two things and the
# order means something: first, then last.

# 3 -----------------------------------------------------------------
def swap(pair):
    a, b = pair
    return (b, a)

print(swap((1, 2)))                       # (2, 1)

# 4 -----------------------------------------------------------------
# TypeError: unhashable type: 'list'
# A set has to know each item stays the same forever, or it could never
# find it again. A list can change, so it is not allowed in. The fix is
# one character:
seen = set()
seen.add((0, 0))                          # a tuple, not a list
print(seen)                               # {(0, 0)}

# 5 -----------------------------------------------------------------
for n in range(1, 11):
    print(n)

for n in range(10, 0, -1):
    print(n)
# Going down needs THREE arguments. The stop is 0 and 0 is excluded, so
# the last number printed is 1. That is what we wanted.

# 6 -----------------------------------------------------------------
print(list(range(0, 31, 3)))
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# range(0, 30, 3) would stop at 27. To include 30 you must go past it.

# 7 -----------------------------------------------------------------
# range(10)        -> 10 numbers  (0 to 9)
# range(1, 10)     ->  9 numbers  (1 to 9)
# range(0, 10, 2)  ->  5 numbers  (0 2 4 6 8)
# range(5, 5)      ->  0 numbers  (start and stop are the same)
# range(10, 0, -1) -> 10 numbers  (10 down to 1)
print(len(range(10)), len(range(1, 10)), len(range(0, 10, 2)),
      len(range(5, 5)), len(range(10, 0, -1)))
# 10 9 5 0 10
# len() works on a range without building a list, because it can just do
# the arithmetic.

# 8 -----------------------------------------------------------------
# It prints nothing because range(10, 0) means "start at 10, count UP,
# stop before 0" - and you are already past 0. So it is empty. Python
# does not warn you; an empty loop is perfectly legal.
#
# Fix one: count down properly.
for n in range(10, 0, -1):
    print(n)
# Fix two: you meant to count up.
for n in range(0, 10):
    print(n)

# 9 -----------------------------------------------------------------
print([n ** 2 for n in range(1, 11)])
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([len(w) for w in ["python", "is", "fun"]])
# [6, 2, 3]

print([n for n in range(1, 21) if n % 3 == 0])
# [3, 6, 9, 12, 15, 18]
# Nothing changes each item here, so the front is just n. All the work
# is in the gate at the end.

# 10 ----------------------------------------------------------------
words = ["apple", "fig", "banana", "kiwi", "plum"]
print([w.upper() for w in words if len(w) > 4])
# ['APPLE', 'BANANA']
# Two jobs in one line: the gate at the end decides WHICH words survive,
# the front decides what happens to the survivors. The gate runs first,
# even though it is written last.

# 11 ----------------------------------------------------------------
prices = {"tea": 450, "coffee": 700, "cake": 900}
print([f"{item} costs {price} HUF" for item, price in prices.items()])
# ['tea costs 450 HUF', 'coffee costs 700 HUF', 'cake costs 900 HUF']
# .items() hands you a TUPLE each time round, and "for item, price"
# unpacks it on the spot. Part 1 and Part 3 in the same line.

# 12 ----------------------------------------------------------------
readings = [("Mon", 12), ("Tue", 25), ("Wed", 31), ("Thu", 8)]

# a)
print([temp for day, temp in readings])
# [12, 25, 31, 8]

# b)
print([day for day, temp in readings if temp > 20])
# ['Tue', 'Wed']

# c)
print([(day, round(temp * 9 / 5 + 32)) for day, temp in readings])
# [('Mon', 54), ('Tue', 77), ('Wed', 88), ('Thu', 46)]
# Tuples going in, tuples coming out. The shape survives the belt.

# d)
print([sum(range(1, n + 1)) for n in range(1, 6)])
# [1, 3, 6, 10, 15]
# The outer range says which triangular number; the inner range builds
# the numbers to add up. n + 1 because the stop is excluded - without
# it you would leave n itself out every time.

=========================================================================
IF YOU ONLY REMEMBER FIVE THINGS FROM TODAY
=========================================================================
  1. A tuple is a sealed list. The COMMA makes it, not the brackets.
  2. Only sealed things - tuples, strings, numbers - can be dictionary
     keys or set members.
  3. range(start, stop, step) and the stop is NEVER included.
  4. range() describes numbers, it does not store them. Wrap it in
     list() when you want to look at them.
  5. [do this  for each x in things  if this is true] - and the gate at
     the end runs first, even though it is written last.
"""


# =========================================================================
# runner
# =========================================================================


def main(argv):
    what = argv[1].lower() if len(argv) > 1 else "all"

    if what in ("tasks", "task"):
        print(TASKS)
        return 0

    if what in ("solutions", "solution", "answers"):
        print(SOLUTIONS)
        return 0

    part1_tuples()
    part2_ranges()
    part3_comprehension()
    part4_together()
    print(TASKS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
