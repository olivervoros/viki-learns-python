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
