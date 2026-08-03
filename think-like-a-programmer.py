"""
╔══════════════════════════════════════════════════════════════════════╗
║       THINKING LIKE A PROGRAMMER: From Beginner to Expert          ║
║                                                                     ║
║  This lesson is NOT about memorizing syntax.                        ║
║  It's about rewiring your brain to THINK like a problem solver.     ║
║                                                                     ║
║  Run this file section by section, read every comment,              ║
║  and do every exercise. The code is simple on purpose —             ║
║  the THINKING is the hard part.                                     ║
╚══════════════════════════════════════════════════════════════════════╝
"""

# https://archive.org/details/think-like-a-programmer/page/n19/mode/2up

# https://archive.org/details/howtothinklikepr0000vick

# ════════════════════════════════════════════════════════════════════
# PHASE 1: THE MINDSET SHIFT (Beginner)
# ════════════════════════════════════════════════════════════════════
#
# 🧠 THE BIG IDEA:
# A computer is NOT smart. At all. Not even a little bit.
# It is the most obedient, precise, and utterly STUPID machine
# you will ever work with.
#
# 🥾 THE SHOE ANALOGY:
# Imagine the most expensive, top-of-the-line gaming computer
# in the world — RGB lights, liquid cooling, 128 GB of RAM.
#
# Now imagine a shoe.
#
# In terms of "understanding what you want"... they are EQUAL.
# Neither the computer nor the shoe can GUESS your intention.
# The only difference? The computer can follow instructions
# incredibly fast. The shoe can't even do that.
#
# A computer is basically a shoe that can do math at the speed
# of light — but ONLY if you tell it EXACTLY what to do.
#
# 📌 RULE #1: THE "STUPID COMPUTER" RULE
# The computer does EXACTLY what you tell it to do.
# Not what you MEANT to tell it.
# Not what you WANTED it to do.
# Not what would be "obvious" to a human.
# EXACTLY. WHAT. YOU. TYPED.


# --- Demo 1.1: The computer does EXACTLY what you say ---

# You THINK this will greet someone nicely:
name = "Alice"
print("Hello" + name)  # Output: HelloAlice  (no space! You didn't ask for one!)

# The computer didn't "forget" the space.
# YOU forgot to TELL it about the space.
# The computer is not being difficult — it's being PRECISE.

# Fixed version — you must be EXPLICIT about everything:
print("Hello " + name)  # Output: Hello Alice  ✅

# Another classic: you THINK this adds two numbers:
a = "5"
b = "3"
print(a + b)  # Output: 53  (string concatenation, not addition!)

# The computer isn't wrong. YOU told it to work with text ("5"),
# not with a number (5). It did EXACTLY what you asked.

# Fixed:
a = 5
b = 3
print(a + b)  # Output: 8  ✅


# --- Demo 1.2: Logic over Syntax ---
#
# 🍳 THE RECIPE ANALOGY:
# Learning to code by memorizing syntax is like learning to cook
# by memorizing the names of kitchen utensils.
#
# Knowing that a "whisk" (habverő) exists doesn't teach you how to make
# an omelette. Understanding the PROCESS (crack eggs, beat them,
# heat pan, pour, fold) is what matters.
#
# The whisk is just a tool. Python is just a tool.
# The LOGIC is the recipe.

# Here's the same logic in three "languages":

# ENGLISH (pseudocode):
#   If the student's grade is 90 or above, they get an A.
#   Otherwise, if it's 80 or above, they get a B.
#   Otherwise, they get C.

# PYTHON:
grade = 85
if grade >= 90:
    result = "A"
elif grade >= 80:
    result = "B"
else:
    result = "C"
print(f"Grade: {result}")  # Output: Grade: B

# JAVASCRIPT (for comparison — same logic, different "accent"):
# if (grade >= 90) { result = "A"; }
# else if (grade >= 80) { result = "B"; }
# else { result = "C"; }

# See? The LOGIC is identical. Only the "accent" changes.
# If you understand the logic, switching languages is like
# switching from British English to American English —
# a few spelling differences, same meaning.


# ════════════════════════════════════════════════════════════════════
# 🏋️ EXERCISE 1: "Instruct the Robot"
# ════════════════════════════════════════════════════════════════════
#
# ⭐ Exercise 1a:
# Below is a "robot" that makes a sandwich. But the instructions
# are WRONG — they assume the robot has common sense.
# Fix every step so a "stupid computer" could follow them.

# BROKEN instructions (a human would understand, a computer won't):
sandwich_steps = [
    "Get bread",  # Which bread? From where? How many slices?
    "Add stuff",  # What stuff?? How much??
    "Close it",  # Close WHAT? How?
    "Done",  # Done with what?
]

# YOUR TASK: Rewrite the list with PRECISE steps.
# Example of ONE fixed step:
# "Open the bread bag on the kitchen counter"
# "Take out exactly 2 slices of white bread"
# Now do the rest!

sandwich_steps_fixed = [
    # TODO: Write at least 8 precise steps here
    # "Open the bread bag on the kitchen counter",
    # "Take out exactly 2 slices of white bread",
    # ... add more steps ...
]


# ⭐⭐ Exercise 1b: Variable Mechanics Blueprint
#
# Every variable answers THREE questions:
#   1. What is its NAME?     (age, total_price, username)
#   2. What is its TYPE?     (int, float, str, bool, list)
#   3. What is its VALUE?    (25, 19.99, "Alice", True, [1,2,3])
#
# 📦 THE BOX ANALOGY:
# A variable is a labeled box.
# - The NAME is the label on the outside of the box.
# - The TYPE is the shape of things that fit inside.
# - The VALUE is what's actually IN the box right now.
#
# Fill in the blueprint below before writing any code:

# BLUEPRINT (write in plain English first):
# Name: student_age    | Type: integer | Starting Value: 0
# Name: ____________   | Type: _______ | Starting Value: _______
# Name: ____________   | Type: _______ | Starting Value: _______

# NOW translate your blueprint into Python:
student_age = 0  # Name: student_age, Type: int, Value: 0
# TODO: Create 2 more variables from your blueprint above


# ════════════════════════════════════════════════════════════════════
# PHASE 2: ALGORITHM FIRST, CODE LATER (Advanced Beginner)
# ════════════════════════════════════════════════════════════════════
#
# 🧠 THE BIG IDEA:
# Never start by typing code. Start by THINKING.
# Professional programmers spend more time with a whiteboard
# and a marker than with a keyboard.
#
# 🏗️ THE ARCHITECT ANALOGY:
# An architect doesn't start building a house by carrying bricks.
# They draw a BLUEPRINT first.
#
# If you start coding before you have a plan, you're basically
# carrying bricks into an empty field and hoping a house appears.
# Spoiler: it won't.


# --- Demo 2.1: Comment-Driven Development ---
#
# 💡 THE TRANSLATION ANALOGY:
# Think of coding as TRANSLATION. You are a translator.
# The "original text" is your plain-English plan.
# The "translated text" is Python code.
#
# Step 1: Write the plan in comments (YOUR language)
# Step 2: Translate each comment into code (COMPUTER's language)
#
# The comments are the REAL program. The code is just
# how you explain it to the computer.

# EXAMPLE: Calculate the average of a list of scores.

# Step 1: PLAN FIRST (comments only, no code!)
# 1. Start with a list of test scores
# 2. Add up all the scores to get the total
# 3. Count how many scores there are
# 4. Divide the total by the count to get the average
# 5. Show the result

# Step 2: NOW translate each comment into code:

# 1. Start with a list of test scores
scores = [85, 92, 78, 95, 88]

# 2. Add up all the scores to get the total
total = sum(scores)

# 3. Count how many scores there are
count = len(scores)

# 4. Divide the total by the count to get the average
average = total / count

# 5. Show the result
print(f"Average score: {average}")  # Output: Average score: 87.6


# Notice: the COMMENTS came first. Each one is a tiny, clear task.
# The code is just the translation. If you can write the comments,
# you can write the code — it's just a lookup exercise at that point.


# --- Demo 2.2: The 8 Universal Programming Blocks ---
#
# 🧱 THE LEGO ANALOGY:
# Every LEGO set — from a tiny car to the Millennium Falcon —
# is built from the same basic brick shapes.
#
# Every program — from a calculator to Instagram —
# is built from the same 8 basic building blocks.
# The only difference is how you COMBINE them.
#
# Here are ALL of them. Once you know these, you can build anything.

# Block 1: VARIABLES — storing information
player_name = "Hero"
player_health = 100

# Block 2: INPUT — getting information from the user
# user_answer = input("What is your name? ")  # (commented to not pause the lesson)
user_answer = "TestUser"  # Simulated input for demo

# Block 3: OUTPUT — showing information to the user
print(f"Welcome, {user_answer}!")

# Block 4: ARITHMETIC — doing math
damage = 25
player_health = player_health - damage
print(f"Health after hit: {player_health}")  # 75

# Block 5: CONDITIONALS (BRANCHES) — making decisions
if player_health > 50:
    status = "healthy"
elif player_health > 20:
    status = "wounded"
else:
    status = "critical"
print(f"Status: {status}")

# Block 6: LOOPS — repeating things
print("Healing 3 times:")
for i in range(3):
    player_health += 10
    print(f"  Health: {player_health}")


# Block 7: FUNCTIONS — reusable recipes
def calculate_damage(base_attack, defense):
    """Like a recipe card: give me ingredients, I give you the dish."""
    actual_damage = base_attack - defense
    if actual_damage < 0:
        actual_damage = 0
    return actual_damage


hit = calculate_damage(30, 12)
print(f"Damage dealt: {hit}")  # 18

# Block 8: DATA STRUCTURES — organized storage
#   (Lists, dictionaries — ways to group related data)
inventory = ["sword", "shield", "potion"]
player_stats = {"name": "Hero", "level": 5, "gold": 120}
print(f"Inventory: {inventory}")
print(f"Player: {player_stats['name']}, Level {player_stats['level']}")

# That's it. That's ALL of programming.
# Everything else is just clever combinations of these 8 blocks.


# ════════════════════════════════════════════════════════════════════
# 🏋️ EXERCISE 2: Comment-Driven Development Practice
# ════════════════════════════════════════════════════════════════════
#
# ⭐ Exercise 2a:
# Below are comments describing a tip calculator.
# YOUR JOB: translate each comment into Python code.

# 1. The meal costs 45.00 dollars
# TODO: create a variable

# 2. The tip percentage is 18%
# TODO: create a variable (use 0.18, not 18)

# 3. Calculate the tip amount (meal cost times tip percentage)
# TODO: write the math

# 4. Calculate the total bill (meal cost plus tip)
# TODO: write the math

# 5. Display: "Tip: $X.XX" and "Total: $X.XX"
# TODO: print the results


# ⭐⭐ Exercise 2b:
# Now do it BACKWARDS. Write the COMMENTS FIRST for a program
# that converts Celsius to Fahrenheit. Formula: F = C × 9/5 + 32
# Write at least 4 comment-steps, THEN translate them to code.

# TODO: Write your comments first, THEN the code under each one


# ════════════════════════════════════════════════════════════════════
# PHASE 3: DECOMPOSITION AND ITERATION (Intermediate)
# ════════════════════════════════════════════════════════════════════
#
# 🧠 THE BIG IDEA:
# Big problems are scary. Small problems are easy.
# Your ONLY job is to turn big problems into small ones.
#
# 🍕 THE PIZZA ANALOGY:
# Nobody eats a whole pizza in one bite. You cut it into slices.
# Nobody solves a big programming problem in one step.
# You cut it into pieces.
#
# "Write a student grade management system" = TERRIFYING.
# "Store one student's name" = easy.
# "Store one student's grade" = easy.
# "Calculate one average" = easy.
# "Print one report card" = easy.
#
# Stack enough easy things together, and you've built something big.
# That's the secret. There is no other secret.


# --- Demo 3.1: Divide and Conquer ---
#
# PROJECT: Build a simple shopping cart calculator.
#
# ❌ BAD approach: Try to build everything at once.
#     (This is how beginners get stuck and frustrated.)
#
# ✅ GOOD approach: Break it into tiny pieces and solve ONE at a time.

# PIECE 1: Can I store ONE item with a price?
item = {"name": "Apple", "price": 1.50}
print(f"Item: {item['name']}, Price: ${item['price']}")
# ✅ That works! Move on.

# PIECE 2: Can I store MULTIPLE items?
cart = [
    {"name": "Apple", "price": 1.50},
    {"name": "Bread", "price": 3.00},
    {"name": "Milk", "price": 2.50},
]
print(f"Cart has {len(cart)} items")
# ✅ That works! Move on.

# PIECE 3: Can I calculate the total?
total = 0
for item in cart:
    total += item["price"]
print(f"Total: ${total:.2f}")
# ✅ That works! Move on.

# PIECE 4: Can I apply a discount?
discount_percent = 10
discount_amount = total * (discount_percent / 100)
final_total = total - discount_amount
print(f"Discount: -${discount_amount:.2f}")
print(f"Final total: ${final_total:.2f}")
# ✅ That works!

# NOW you can combine all pieces into one clean program.
# But you PROVED each piece works BEFORE combining them.
# No guessing. No hoping. Just facts.


# --- Demo 3.2: The Terminal-First MVP ---
#
# 🚗 THE CAR ANALOGY:
# Before building a beautiful sports car, engineers build
# an ugly prototype that just DRIVES. No paint, no leather seats,
# no fancy dashboard. Just: does it move? Does it steer? Does it stop?
#
# Your first version should be UGLY but FUNCTIONAL.
# No fancy menus, no colors, no graphics.
# Just: does it WORK in the terminal?
#
# Pretty comes LATER. Working comes FIRST.

# MVP of a to-do list app — ugly but functional:
todos = []

# Simulating user actions (in a real app, these would be input()):
todos.append("Buy groceries")
todos.append("Finish homework")
todos.append("Call dentist")

print("=== MY TO-DO LIST ===")
for i, task in enumerate(todos, 1):
    print(f"  {i}. {task}")

# Mark one as done:
done_task = todos.pop(1)  # Remove "Finish homework"
print(f"\n✅ Completed: {done_task}")

print("\n=== UPDATED LIST ===")
for i, task in enumerate(todos, 1):
    print(f"  {i}. {task}")

# This is UGLY. No menus, no colors, no error handling.
# But it WORKS. That's an MVP.
# Now you can improve it piece by piece.


# ════════════════════════════════════════════════════════════════════
# 🏋️ EXERCISE 3: Decomposition Practice
# ════════════════════════════════════════════════════════════════════
#
# ⭐ Exercise 3a: Break It Down
# You need to build a "Classroom Grade Book" that:
#   - Stores student names and their test scores
#   - Calculates each student's average
#   - Finds the student with the highest average
#   - Prints a summary report
#
# DON'T write any code yet!
# Instead, list at least 5 SMALL pieces you'd build one at a time.
#
# Example:
#   Piece 1: Store ONE student name with ONE score
#   Piece 2: ____________
#   Piece 3: ____________
#   Piece 4: ____________
#   Piece 5: ____________

# ⭐⭐ Exercise 3b: Build the MVP
# Now build ONLY Piece 1 and Piece 2 from your list above.
# Don't try to build the whole thing. Just two pieces.

# TODO: your code here


# ⭐⭐⭐ Exercise 3c: Combine
# If you got Pieces 1-2 working, add Piece 3. Then 4. Then 5.
# One at a time. Test after EVERY addition.

# TODO: your code here


# ════════════════════════════════════════════════════════════════════
# PHASE 4: THE SCIENTIST MINDSET & EDGE CASES (Advanced)
# ════════════════════════════════════════════════════════════════════
#
# 🧠 THE BIG IDEA:
# Bugs are not failures. They are CLUES.
# When something goes wrong, you are not bad at coding.
# You just discovered something you didn't know about
# how the computer thinks. That's valuable information.
#
# 🔬 THE SCIENTIST ANALOGY:
# A scientist doesn't cry when an experiment "fails."
# They say: "Interesting! That didn't do what I expected.
# WHY? What does this tell me?"
#
# A programmer should do the same thing:
# "The output is wrong. Interesting. Let me figure out WHERE
# and WHY the computer's logic diverged from MY logic."


# --- Demo 4.1: Hypothesis-Driven Debugging ---
#
# Here's a buggy program. Let's debug it like a scientist.


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    for num in numbers:
        total = 0  # 🐛 BUG! (Can you spot it?)
        total += num
    average = total / len(numbers)
    return average


test_scores = [80, 90, 100]
result = calculate_average(test_scores)
print(f"Average (buggy): {result}")  # Expected: 90.0, Got: 33.33... Why??

# 🔬 SCIENTIST'S APPROACH:
#
# Step 1: OBSERVE — What happened?
#   "The average should be 90.0 but I got 33.33. That's way too low."
#
# Step 2: HYPOTHESIZE — What COULD be wrong?
#   "Maybe not all numbers are being added up properly."
#
# Step 3: TEST — Add print statements to check:


def calculate_average_debug(numbers):
    for num in numbers:
        total = 0
        total += num
        print(f"  Processing {num}: total is now {total}")
        # 👆 This is our "microscope" — we can see inside the loop!
    average = total / len(numbers)
    return average


print("\nDebugging output:")
result = calculate_average_debug([80, 90, 100])
# AHA! The total keeps resetting to 0 every loop iteration!
# Because `total = 0` is INSIDE the loop, it gets reset every time.

# Step 4: DIAGNOSE — The print reveals the bug!
#   "total = 0" is inside the loop, so it resets on EVERY pass.
#   Only the LAST number (100) actually survives. 100 / 3 = 33.33.

# Step 5: FIX — Move "total = 0" BEFORE the loop:


def calculate_average_fixed(numbers):
    total = 0  # ✅ BEFORE the loop — initialized only ONCE!
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average


print(f"\nAverage (fixed): {calculate_average_fixed([80, 90, 100])}")  # 90.0 ✅


# --- Demo 4.2: Anticipating Edge Cases ---
#
# 🛡️ THE BOUNCER ANALOGY:
# A good bouncer at a nightclub doesn't just check if you
# LOOK old enough. They check your ID, look for fakes,
# and handle the guy who "forgot his wallet."
#
# A good program doesn't just handle PERFECT input.
# It handles the WEIRD, WRONG, and MISSING input too.
#
# Ask yourself: "What's the WORST thing a user could type?"
# Then handle it.


# ❌ NAIVE version (crashes on bad input):
def divide_naive(a, b):
    return a / b


# divide_naive(10, 0)   # 💥 ZeroDivisionError!
# divide_naive("10", 2) # 💥 TypeError!


# ✅ DEFENSIVE version (handles edge cases):
def divide_safe(a, b):
    # Edge case 1: What if the inputs aren't numbers?
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("⚠️ Error: Both inputs must be numbers.")
        return None

    # Edge case 2: What if someone divides by zero?
    if b == 0:
        print("⚠️ Error: Cannot divide by zero.")
        return None

    return a / b


# Testing with edge cases:
print(f"\n10 / 3 = {divide_safe(10, 3)}")  # Normal: 3.333...
print(f"10 / 0 = {divide_safe(10, 0)}")  # Edge case: zero
print(f"'10' / 2 = {divide_safe('10', 2)}")  # Edge case: wrong type


# --- Demo 4.3: The Edge Case Checklist ---

# 🎯 Before you call a function "done", ask yourself:
#
# ┌─────────────────────────────────────────────────────┐
# │ EDGE CASE CHECKLIST:                                │
# │                                                     │
# │ □ What if the input is EMPTY?      ([], "", None)   │
# │ □ What if the input is ZERO?       (0, 0.0)         │
# │ □ What if the input is NEGATIVE?   (-5, -100)       │
# │ □ What if the input is the WRONG TYPE? ("abc", True)│
# │ □ What if there's only ONE item?   ([42])           │
# │ □ What if the input is HUGE?       (999999999)      │
# │ □ What if the user types nothing?  ("")             │
# └─────────────────────────────────────────────────────┘

# Example: a function that finds the maximum value in a list.


# ❌ No edge case handling:
def find_max_naive(numbers):
    biggest = numbers[0]  # 💥 Crashes on empty list!
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest


# ✅ With edge case handling:
def find_max_safe(numbers):
    # Edge case: empty list
    if not numbers:
        print("⚠️ Warning: empty list, no maximum exists.")
        return None

    # Edge case: not all items are numbers
    for item in numbers:
        if not isinstance(item, (int, float)):
            print(f"⚠️ Warning: '{item}' is not a number, skipping.")
            numbers = [n for n in numbers if isinstance(n, (int, float))]
            break

    if not numbers:
        print("⚠️ No valid numbers found.")
        return None

    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest


# Tests:
print(f"\nMax of [3, 7, 2, 9, 1]: {find_max_safe([3, 7, 2, 9, 1])}")  # 9
print(f"Max of []: {find_max_safe([])}")  # None
print(f"Max of [-5, -2, -8]: {find_max_safe([-5, -2, -8])}")  # -2


# --- Demo 4.4: Efficient Ignorance ---
#
# 🗺️ THE GPS ANALOGY:
# You don't need to memorize every street in the city.
# You need to know how to USE A GPS.
#
# A professional programmer doesn't memorize every function.
# They memorize HOW TO FIND the right function quickly.
#
# The three best "GPS tools" for programmers:
#
# 1. help() — Python's built-in documentation
# 2. dir()  — "What can this object do?"
# 3. Google/Stack Overflow — "Someone had this problem before me"

# Using help() — your in-code reference manual:
# help(str.upper)  # Uncomment to see docs for the .upper() method

# Using dir() — "What methods does a string have?"
text = "hello"
# print(dir(text))  # Uncomment to see ALL string methods

# Quick filtered search — find methods containing "up":
string_methods = [m for m in dir(text) if "up" in m.lower()]
print(f"\nString methods containing 'up': {string_methods}")

# The point: You don't need to KNOW everything.
# You need to know how to FIND everything.
# That's not cheating. That's being a professional.


# ════════════════════════════════════════════════════════════════════
# 🏋️ EXERCISE 4: The Scientist Mindset
# ════════════════════════════════════════════════════════════════════
#
# ⭐ Exercise 4a: Debug Like a Scientist
# This function is supposed to count how many VOWELS are in a word.
# It has a bug. Use the scientist approach to find and fix it.
# (Hint: add print statements to observe what's happening)


def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count  # This one actually works! But try it with "HELLO"...


print(f"\nVowels in 'hello': {count_vowels('hello')}")  # Should be 2
print(f"Vowels in 'HELLO': {count_vowels('HELLO')}")  # Should be 2, but...

# TODO: Why does 'HELLO' return 0? Fix it!


# ⭐⭐ Exercise 4b: Edge Case Fortress
# Write a function called safe_average(numbers) that:
#   - Returns the average of a list of numbers
#   - Returns None and prints a warning if the list is empty
#   - Skips any non-number items and warns about them
#   - Still works if only ONE number is given

# TODO: def safe_average(numbers):
#           pass

# Test with these:
# safe_average([10, 20, 30])        # Should return 20.0
# safe_average([])                   # Should return None with warning
# safe_average([5])                  # Should return 5.0
# safe_average([10, "oops", 30])    # Should skip "oops", average 10 and 30


# ════════════════════════════════════════════════════════════════════
# PHASE 5: ABSTRACT SYSTEMS AND PARADIGMS (Expert)
# ════════════════════════════════════════════════════════════════════
#
# 🧠 THE BIG IDEA:
# At this level, you stop thinking about ONE language
# and start thinking about PATTERNS that work EVERYWHERE.
#
# 🎸 THE MUSICIAN ANALOGY:
# A beginner guitarist learns songs. ("I can play Wonderwall!")
# An intermediate guitarist learns techniques. ("I can fingerpick!")
# An expert musician understands MUSIC THEORY. They can pick up
# a piano, a ukulele, or a saxophone and STILL make music —
# because they understand the STRUCTURE underneath.
#
# An expert programmer understands COMPUTATIONAL THINKING.
# Python, JavaScript, Java, C++ — they're just different instruments
# playing the same music.


# --- Demo 5.1: Language Agnosticism ---
#
# Here's the SAME program in Python and pseudo-JavaScript.
# Focus on how the STRUCTURE is identical:


# PYTHON:
def fizzbuzz_python():
    results = []
    for i in range(1, 16):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results


print(f"\nFizzBuzz: {fizzbuzz_python()}")

# JAVASCRIPT (same structure, different "accent"):
# function fizzbuzz() {
#     let results = [];
#     for (let i = 1; i <= 15; i++) {
#         if (i % 3 === 0 && i % 5 === 0) results.push("FizzBuzz");
#         else if (i % 3 === 0) results.push("Fizz");
#         else if (i % 5 === 0) results.push("Buzz");
#         else results.push(String(i));
#     }
#     return results;
# }
#
# Notice: variable → let, append → push, elif → else if,
# % works the same, if/else works the same.
# If you UNDERSTAND the logic, switching is trivial.


# --- Demo 5.2: Managing Abstraction ---
#
# 🏨 THE HOTEL ANALOGY:
# When you stay at a hotel, you trust that the plumbing works.
# You don't need to know how the pipes connect underground.
# You just turn the faucet and water comes out.
#
# BUT — if the water stops flowing, SOMEONE needs to understand
# the pipes. That someone might be you, if you're building
# the hotel.
#
# In programming:
# - Most of the time, TRUST the abstractions. Use len(), sorted(),
#   open(), etc. without worrying about how they work internally.
# - But KNOW that there's a deeper layer, and be ready to go there
#   when you need to.

# TRUSTING abstractions (everyday coding):
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sorted(numbers)  # You don't need to know the algorithm!
print(f"\nSorted: {sorted_numbers}")


# UNDERSTANDING the abstraction (when you need to):
# Here's what sorted() does under the hood (simplified):
def my_simple_sort(items):
    """A simple bubble sort — inefficient, but shows the concept."""
    result = items.copy()  # Don't modify the original
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


print(f"My sort: {my_simple_sort(numbers)}")
# Same result! But sorted() is MUCH faster because it uses
# a more sophisticated algorithm (Timsort) written in C.
# You don't need to know this — until you do.


# --- Demo 5.3: Knowing When to Look Deeper ---
#
# 🎯 RULE OF THUMB:
#
# Level 1 (Use it):   sorted([3,1,2]) → [1,2,3]  — just works
# Level 2 (Tweak it): sorted(students, key=lambda s: s["grade"])
#                      — you customize its behavior
# Level 3 (Build it): Write your own sorting algorithm
#                      — you need something sorted() can't do
#
# MOST of the time, Level 1 is enough. Level 2 is common.
# Level 3 is rare but powerful when needed.

# Level 1: Just use it
words = ["banana", "apple", "cherry"]
print(f"\nSorted words: {sorted(words)}")

# Level 2: Customize it
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
]
by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print("Students by grade (highest first):")
for s in by_grade:
    print(f"  {s['name']}: {s['grade']}")


# ════════════════════════════════════════════════════════════════════
# 🏋️ EXERCISE 5: Think Like an Expert
# ════════════════════════════════════════════════════════════════════
#
# ⭐⭐ Exercise 5a: Translate the Logic
# Below is a Python function. Write comments explaining
# what each line does in plain English — so clearly that
# someone who doesn't know Python could understand the LOGIC.


def mystery_function(text):
    words = text.split()
    word_counts = {}
    for word in words:
        word_lower = word.lower()
        if word_lower in word_counts:
            word_counts[word_lower] += 1
        else:
            word_counts[word_lower] = 1
    return word_counts


result = mystery_function("the cat sat on the mat the cat")
print(f"\nMystery result: {result}")

# TODO: Add a plain-English comment above each line explaining
# what it does and WHY. What is this function's PURPOSE?


# ⭐⭐⭐ Exercise 5b: CAPSTONE — The Complete Thinker
# Build a simple CONTACT BOOK program that:
#   1. Stores contacts (name, phone, email) in a list of dicts
#   2. Can ADD a new contact
#   3. Can SEARCH for a contact by name (case-insensitive)
#   4. Can DISPLAY all contacts in a formatted way
#   5. Handles edge cases (empty search, duplicate names, etc.)
#
# RULES:
#   - Write your COMMENTS/PLAN first (Phase 2)
#   - Break it into small pieces (Phase 3)
#   - Handle edge cases (Phase 4)
#   - Test each piece before combining (Phase 3)
#
# This exercise uses ALL the phases together.

# TODO: Your plan (comments) first, then code.


# ════════════════════════════════════════════════════════════════════
# 📋 SUMMARY CHEAT SHEET
# ════════════════════════════════════════════════════════════════════
#
# ┌────────────┬────────────────────────┬──────────────────────────┐
# │ PHASE      │ KEY SKILL              │ ANALOGY                  │
# ├────────────┼────────────────────────┼──────────────────────────┤
# │ 1. Mindset │ Computer = precise,    │ Computer = shoe that     │
# │            │ not smart              │ does math                │
# ├────────────┼────────────────────────┼──────────────────────────┤
# │ 2. Plan    │ Comments first,        │ Architect draws          │
# │            │ code second            │ blueprint, then builds   │
# ├────────────┼────────────────────────┼──────────────────────────┤
# │ 3. Break   │ Divide big problems    │ Nobody eats a whole      │
# │  it down   │ into small pieces      │ pizza in one bite        │
# ├────────────┼────────────────────────┼──────────────────────────┤
# │ 4. Debug   │ Be a scientist:        │ Bugs are experiments,    │
# │  & defend  │ observe, hypothesize,  │ not failures.            │
# │            │ test, fix              │ Be a bouncer for input.  │
# ├────────────┼────────────────────────┼──────────────────────────┤
# │ 5. Abstract│ Think in patterns,     │ Expert musician plays    │
# │            │ not languages          │ any instrument            │
# └────────────┴────────────────────────┴──────────────────────────┘
#
# Remember:
# ✅ You are a TRANSLATOR (English → Python)
# ✅ Comments are the REAL program; code is the translation
# ✅ Plan FIRST, code SECOND
# ✅ Small pieces, tested one at a time
# ✅ Bugs = clues, not failures
# ✅ You don't need to memorize — you need to know how to SEARCH
# ✅ All languages are the same instrument with different tuning


print("\n" + "=" * 50)
print("🎓 End of lesson: Thinking Like a Programmer")
print("=" * 50)
print("The most important thing you learned today")
print("is NOT any Python syntax.")
print("It's HOW TO THINK.")
print("That skill works in ANY language, forever.")
