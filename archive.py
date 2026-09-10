item_name = "Notebook"  # keep as string
item_price_text = "4.99"  # convert to float
item_quantity_text = "3"  # convert to int

# TODO:
item_price = float(item_price_text)
item_quantity = int(item_quantity_text)
print(f"Total price : {item_price*item_quantity}")

messy_price = "€12.50"
# TODO:
print(messy_price) 
# remove the '€' sign, convert to float, and store in clean_price
# clean_price = ...
clean_price = float(messy_price.replace("€", ""))
print(clean_price)


# --- Exercise 1.3 ⭐⭐ — Type Detective ---
# Print the type of each variable below. Then convert all of them
# into strings and join them into one sentence.


age = 25
height = 1.75
is_student = True
print(type(age))
print(type(height))
print(type(is_student))
print(f"Age : {str(age)} Height: {str(height)} Is Student : {str(is_student)}")

# ============================================================
# Conditionals are like a traffic light:
#   🟢 Green (if)       → go
#   🟡 Yellow (elif)    → slow down
#   🔴 Red (else)       → stop
# Python checks conditions top-to-bottom and takes the FIRST match.
# ============================================================

# --- Exercise 2.1 ⭐ — Grade Calculator ---
# Given a score, print the letter grade.
try:
    score = int(input("Adj meg egy számot : "))
except ValueError:
     score = int(input("Ez nem egy szám"))

if score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")

# TODO:
#  write if/elif/else to print the grade:
#   90-100 → "A"
#   80-89  → "B"
#   70-79  → "C"
#   60-69  → "D"
#   below 60 → "F"

# Expected output for score=73: "C"

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
elif password_has_uppercase ==False:
    print("A jelszóban nincs nagybetűs karakter")
else:
    print("A jelszó megfelel")


# --- Exercise 3.1 ⭐ — Sum Machine ---
# Calculate the sum of all numbers from 1 to 100 using a for loop.

# TODO: use a for loop and range() to calculate the sum
szamok = range(1,101)
osszeg = 0
for szam in szamok:
    osszeg = osszeg + szam
print(f"Sum of 1 to 100 = {osszeg}")

#--- Exercise 3.2 ⭐⭐ — Word Counter ---
# Count how many words in the list are longer than 5 characters.

words = ["apple", "banana", "cherry", "fig", "dragonfruit", "kiwi", "strawberry"]
long_word_count = 0
for word in words:
    if len(word) > 5:
        long_word_count = long_word_count + 1
    else:
        continue
print(f"Az ötnél hosszabb szavak száma : {long_word_count}")

# --- Exercise 3.3 ⭐⭐ — Multiplication Table ---
# Print a multiplication table for a given number (1 through 10).
try: 
    number = int(input("Adjon meg egy számot 1 és 10 között: "))
    if number < 1 and number > 10:
        number = int(input("Nem 1 és 10 közötti számot adtál meg "))
    else:
        for value in range(1,11):
            print(f"{value} szorozva {number} egyenlő : {value * number}")
except ValueError:
    number = int(input("Nem számot adtál meg.Adjon meg egy számot 1 és 10 között: "))


 #The long way, for comparison:
result = []
for n in range(1,11):
    result.append(n * n)
print(result)

uj_lista = [n * n for n in range(1,11)]

result2 = ["bmw","toyota","mercedes","opel","suzuki"]
new_list = []
for res in result2:
   new_list.append(res.upper())
print(new_list)

uj_lista = [n.upper() for n in result2]
print(uj_lista)
