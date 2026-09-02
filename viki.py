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