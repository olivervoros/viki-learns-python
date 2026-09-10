from datetime import date
# --- Exercise 2.2 ⭐⭐ — Ticket Price ---
# A cinema charges different prices:
#   - Children (under 12): 5 EUR
#   - Teens (12-17): 8 EUR
#   - Adults (18-64): 12 EUR
#   - Seniors (65+): 7 EUR
#   - If it's a Tuesday (is_tuesday=True), EVERYONE gets 2 EUR off.
"""
today = date.today()
today_formated = today.strftime("%A")
if today_formated == "Tuesday":
    is_tuesday = True
else:
    is_tuesday = False
"""
customer_age = 0
customer_age = int(input("Hány éves vagy ? "))
ar = 0
nap = input("Milyen nap van ma?(írd angolul) ")
if nap == "Tuesday":
    is_tuesday = True
else:
    is_tuesday = False
if customer_age < 12:
    ar = 5
elif customer_age >= 12 and customer_age <=17:
    ar = 8
elif customer_age >= 18 and customer_age <65:
    ar = 12
else:
    ar = 7
if is_tuesday :
    ar = ar-2
else:
    pass
print(f"A jegy ára {ar} EUR")
# TODO: calculate and print the ticket price
# ticket_price = ...

# print(f"Ticket price: {ticket_price} EUR")
# Expected output: Ticket price: 10 EUR


# --- Exercise 2.3 ⭐⭐⭐ — Password Validator ---
# Check if a password meets ALL these rules:
#   - At least 8 characters long
#   - Contains at least one digit / integer
#   - Contains at least one uppercase letter
# Print which rules FAIL (not just "invalid").

password =input("Adj meg egy jelszót: ")
password_has_digit = False
password_has_uppercase = False
if len(password) < 8:
    print("A jelszó rövidebb mint nyolc karakter")
elif password :
    for value in password:
        if value.isdigit():
            password_has_digit = True
            break
        elif value.isupper():
            password_has_uppercase = True
            break
        else:
            print("A jelszóban nincsen szám.")
elif password_has_uppercase = False:
    print("A jelszóban nincs nagybetűs karakter")
else:
    print("A jelszó megfelel")
# TODO: check each rule and print specific feedback
# 💡 Hint: you can use any() with a generator, or a simple for loop
#    to check for digits and uppercase letters.

# Expected output for "Hello1":
# "❌ Too short (6 chars, need at least 8)"
# (the other rules pass, so don't print them)


# ============================================================
# SECTION 3 — FOR LOOPS
# ============================================================
# A for loop is like a conveyor belt in a factory:
# items come one by one, you do something to each, done.
# ============================================================

# --- Exercise 3.1 ⭐ — Sum Machine ---
# Calculate the sum of all numbers from 1 to 100 using a for loop.

# TODO: use a for loop and range() to calculate the sum
szamok = range(1,101)
osszeg = 0
for szam in szamok:
    osszeg = osszeg + szam
print(f"Sum of 1 to 100 = {osszeg}")
# Expected output: Sum of 1 to 100 = 5050


# --- Exercise 3.2 ⭐⭐ — Word Counter ---
# Count how many words in the list are longer than 5 characters.

words = ["apple", "banana", "cherry", "fig", "dragonfruit", "kiwi", "strawberry"]
long_word_count = 0
for word in words:
    if len(word) > 5:
        long_word_count = long_word_count + 1
    else:
        continue
print(f"Az ötnél hosszabb szavak száma : {long_word_count}")
    


# print(f"Words longer than 5 chars: {long_word_count}")
# Expected output: Words longer than 5 chars: 4


# --- Exercise 3.3 ⭐⭐ — Multiplication Table ---
# Print a multiplication table for a given number (1 through 10).

number = input

# TODO: print the multiplication table
# Expected output:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70


# --- Exercise 3.4 ⭐⭐⭐ — FizzBuzz ---
# The classic! For numbers 1 to 30:
#   - if divisible by 3 → print "Fizz"
#   - if divisible by 5 → print "Buzz"
#   - if divisible by BOTH 3 and 5 → print "FizzBuzz"
#   - otherwise → print the number

# TODO: write the FizzBuzz loop

# ⚠️ Common mistake: checking divisible-by-3 BEFORE checking
#    divisible-by-both. Order matters! Check the strictest condition first.


# ============================================================
# SECTION 4 — WHILE LOOPS
# ============================================================
# A while loop is like a security guard at the door:
# "Keep checking. If the condition is still True, keep going.
#  The moment it's False, stop."
# ============================================================

# --- Exercise 4.1 ⭐ — Countdown ---
# Print a countdown from 10 to 1, then print "Liftoff! 🚀"

# TODO: use a while loop

# Expected output:
# 10
# 9
# ...
# 1
# Liftoff! 🚀


# --- Exercise 4.2 ⭐⭐ — Guess the Number (simulated) ---
# The secret number is 42. Simulate guesses from a list.
# The loop should stop when the right number is found.

secret = 42
guesses = [10, 25, 42, 99, 50]  # simulated guesses (no input() needed)

# TODO: use a while loop to go through guesses one by one.
#       Print "Too low", "Too high", or "Correct! 🎉" for each guess.
#       STOP the loop when the correct guess is found.

# 💡 Hint: use an index variable to step through the list.

# Expected output:
# Guess: 10 → Too low
# Guess: 25 → Too low
# Guess: 42 → Correct! 🎉


# --- Exercise 4.3 ⭐⭐⭐ — Collatz Conjecture ---
# Start with any positive number. Repeat:
#   - If even → divide by 2
#   - If odd  → multiply by 3 and add 1
# Keep going until you reach 1. Count the steps.

start_number = 27

# TODO: implement the Collatz sequence, print each step,
#       and count how many steps it takes to reach 1.

# Expected output (first few lines):
# Step 1: 82
# Step 2: 41
# Step 3: 124
# ...
# Reached 1 in ??? steps


# ============================================================
# SECTION 5 — LISTS & LIST OPERATIONS
# ============================================================
# A list is like a train: wagons in order, you can add wagons,
# remove wagons, or look at any wagon by its position number.
# ============================================================

# --- Exercise 5.1 ⭐ — List Basics ---
# Given the list below, do the following (one operation per line):

fruits = ["apple", "banana", "cherry"]

# TODO:
# a) Add "dragonfruit" to the END of the list
# b) Insert "avocado" at the BEGINNING (index 0)
# c) Remove "banana"
# d) Print the list and its length

# Expected output:
# ['avocado', 'apple', 'cherry', 'dragonfruit']
# Length: 4


# --- Exercise 5.2 ⭐⭐ — List Statistics ---
# Calculate the min, max, average, and sum WITHOUT using
# the built-in min(), max(), sum() functions.
# Build it yourself with a loop!

numbers = [34, 67, 12, 89, 45, 23, 56, 78, 90, 11]

# TODO: calculate using loops only
# my_min = ...
# my_max = ...
# my_sum = ...
# my_avg = ...

# print(f"Min: {my_min}, Max: {my_max}, Sum: {my_sum}, Avg: {my_avg}")
# Expected output: Min: 11, Max: 90, Sum: 505, Avg: 50.5


# --- Exercise 5.3 ⭐⭐ — List Filtering ---
# From the list of numbers, create TWO new lists:
#   - even_numbers (only even ones)
#   - odd_numbers  (only odd ones)

mixed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# TODO: split into even and odd lists
# even_numbers = ...
# odd_numbers = ...

# print(f"Even: {even_numbers}")
# print(f"Odd: {odd_numbers}")


# --- Exercise 5.4 ⭐⭐⭐ — Remove Duplicates (keep order) ---
# Remove duplicate elements but keep the ORIGINAL order.
# Do NOT use set() — that loses order.

items = ["a", "b", "a", "c", "b", "d", "e", "c", "a"]

# TODO: create a new list 'unique_items' with duplicates removed
# unique_items = ...

# print(unique_items)
# Expected output: ['a', 'b', 'c', 'd', 'e']

# 💡 Hint: use a helper list or the `in` keyword to track
#    what you've already seen.


# --- Exercise 5.5 ⭐⭐⭐ — Matrix (List of Lists) ---
# Given a 3x3 grid (list of lists), calculate the sum of each row
# and the sum of each column.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# TODO: print the sum of each row and each column.

# Expected output:
# Row 1 sum: 6
# Row 2 sum: 15
# Row 3 sum: 24
# Col 1 sum: 12
# Col 2 sum: 15
# Col 3 sum: 18


# ============================================================
# SECTION 6 — FILE OPERATIONS
# ============================================================
# Working with files is like writing in a notebook:
#   "w" = rip out all pages and start fresh
#   "a" = open to the last page and keep writing
#   "r" = just read, don't change anything
# Always close the notebook when you're done (or use `with`).
# ============================================================

# --- Exercise 6.1 ⭐ — Write and Read ---
# Write 5 names to a file (one per line), then read and print them.

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# TODO:
# a) Write all names to "names.txt" (one per line)
# b) Read the file back and print each name

# 💡 Hint: use `with open(...)` — it closes the file automatically.

# ⚠️ Common mistake: forgetting "\n" when writing — all names end up
#    on one line!


# --- Exercise 6.2 ⭐⭐ — Log Analyzer ---
# A log file has lines like "INFO: User logged in", "ERROR: Disk full".
# Count how many ERROR lines and how many INFO lines there are.

# First, let's create the sample log file:
log_lines = [
    "INFO: User logged in",
    "ERROR: Disk full",
    "INFO: Page loaded",
    "ERROR: Connection timeout",
    "INFO: File saved",
    "ERROR: Permission denied",
    "INFO: User logged out",
]

# Step 1: write log_lines to "app.log"
# Step 2: read "app.log" and count INFO vs ERROR lines

# TODO: implement both steps
# info_count = ...
# error_count = ...

# print(f"INFO: {info_count}, ERROR: {error_count}")
# Expected output: INFO: 4, ERROR: 3


# --- Exercise 6.3 ⭐⭐⭐ — CSV Parser ---
# Read a CSV-like file and calculate each student's average score.

# First, create the data file:
csv_data = """name,math,science,english
Alice,85,92,78
Bob,90,88,95
Charlie,72,68,80
Diana,95,97,93
"""

with open("students.csv", "w") as f:
    f.write(csv_data)

# TODO: Read "students.csv", skip the header line,
#       and for each student print their name and average score.

# Expected output:
# Alice — average: 85.0
# Bob — average: 91.0
# Charlie — average: 73.33
# Diana — average: 95.0

# 💡 Hint: use .split(",") to break each line into parts.
# ⚠️ Common mistake: forgetting to strip the "\n" from the last value
#    before converting to int — this causes a ValueError!


# ============================================================
# SECTION 7 — ERROR HANDLING
# ============================================================
# Error handling is like a safety net under a tightrope walker.
# You hope you never need it, but if something goes wrong,
# the net catches you instead of letting the program crash.
# ============================================================

# --- Exercise 7.1 ⭐ — Safe Division ---
# Write a function that divides two numbers but handles:
#   - Division by zero → print a friendly message
#   - Non-numeric input → print a friendly message


def safe_divide(a, b):
    # TODO: use try/except to handle errors gracefully
    pass


# Test cases (uncomment to test):
# safe_divide(10, 3)     # Expected: 3.333...
# safe_divide(10, 0)     # Expected: friendly error message
# safe_divide("ten", 2)  # Expected: friendly error message


# --- Exercise 7.2 ⭐⭐ — Safe File Reader ---
# Write a function that reads a file but handles:
#   - File not found
#   - Permission errors
#   - Any other unexpected error
# Use a finally block to print "Operation complete."


def safe_read(filename):
    # TODO: implement with try/except/finally
    pass


# Test cases (uncomment to test):
# safe_read("students.csv")         # Should work (we created it above)
# safe_read("nonexistent_file.txt") # Should handle gracefully


# --- Exercise 7.3 ⭐⭐⭐ — Robust Number Processor ---
# Given a list of mixed data, extract only the valid numbers.
# Use try/except to skip bad values silently, and count how many
# values were skipped.

mixed_data = ["42", "hello", "3.14", "", "100", "abc", "0", "7.5", None, "99"]

# TODO:
# - Loop through mixed_data
# - Try to convert each to float
# - If it works → add to valid_numbers list
# - If it fails → increment skipped_count
# valid_numbers = ...
# skipped_count = ...

# print(f"Valid numbers: {valid_numbers}")
# print(f"Skipped: {skipped_count} bad values")

# Expected output:
# Valid numbers: [42.0, 3.14, 100.0, 0.0, 7.5, 99.0]
# Skipped: 4 bad values


# ============================================================
# SECTION 8 — COMBINED CHALLENGES 🏆
# ============================================================
# These exercises mix MULTIPLE topics together.
# This is how real programming works — nothing stays in a neat box.
# ============================================================

# --- Exercise 8.1 ⭐⭐⭐ — Student Report Generator ---
# Combine: lists, loops, conditionals, file writing, string formatting
#
# Given a list of student dictionaries, generate a report file
# that includes each student's name, average, and letter grade.

students = [
    {"name": "Alice", "scores": [85, 92, 78, 90]},
    {"name": "Bob", "scores": [90, 88, 95, 87]},
    {"name": "Charlie", "scores": [72, 68, 80, 65]},
    {"name": "Diana", "scores": [95, 97, 93, 99]},
]

# TODO:
# a) For each student, calculate their average score
# b) Assign a letter grade (use the same scale from Exercise 2.1)
# c) Write the results to "student_report.txt" in this format:
#
#    === STUDENT REPORT ===
#    Alice      | Avg: 86.25 | Grade: B
#    Bob        | Avg: 90.00 | Grade: A
#    Charlie    | Avg: 71.25 | Grade: C
#    Diana      | Avg: 96.00 | Grade: A
#    =====================
#
# d) Also print the report to the console

# 💡 Hint: use f-strings with field width for alignment,
#    e.g., f"{'Alice':<10}" pads the name to 10 characters.


# --- Exercise 8.2 ⭐⭐⭐ — Word Frequency Counter ---
# Combine: file reading, string methods, dictionaries/lists, sorting
#
# Read the text below, count how often each word appears,
# and print the top 5 most common words.

sample_text = """
Python is a great programming language. Python is easy to learn.
Many developers love Python because Python is versatile.
Learning Python opens many doors. Python is fun and Python is powerful.
"""

with open("sample.txt", "w") as f:
    f.write(sample_text)

# TODO:
# a) Read "sample.txt"
# b) Convert to lowercase, split into words
# c) Remove punctuation (.,!? etc.) from each word
# d) Count how many times each word appears (use a dictionary)
# e) Print the top 5 most frequent words

# Expected output (order may vary for ties):
# 1. python — 7 times
# 2. is — 5 times
# 3. ...

# 💡 Hint: to sort a dictionary by value, look up sorted() with
#    a key parameter. Example: sorted(d.items(), key=lambda x: x[1])


# ============================================================
# 📋 QUICK REFERENCE CHEAT SHEET
# ============================================================
#
# TOPIC              | KEY SYNTAX                          | WATCH OUT FOR
# -------------------|-------------------------------------|---------------------------
# Type conversion    | int(), float(), str(), bool()       | int("3.5") crashes! Use float() first
# if/elif/else       | if x > 5:                          | = is assignment, == is comparison
# for loop           | for i in range(10):                 | range(10) goes 0-9, not 1-10
# while loop         | while condition:                    | Infinite loop if you forget to update!
# List append        | my_list.append(x)                   | .append() returns None, not the list
# List insert        | my_list.insert(0, x)                | First argument is the INDEX
# File write         | with open("f.txt", "w") as f:       | "w" erases the file! Use "a" to add
# File read          | with open("f.txt", "r") as f:       | Always strip "\n" from lines
# try/except         | try: ... except ValueError:         | Catch SPECIFIC errors, not bare except
# String split       | "a,b,c".split(",")                  | Returns a list: ["a", "b", "c"]
# f-string           | f"Hello {name}"                     | Don't forget the f before the quote!
#
# ============================================================
# 🎉 Nice work getting through these! Now go back and try the
#    ⭐⭐⭐ exercises you skipped. That's where the real learning is.
# ============================================================
