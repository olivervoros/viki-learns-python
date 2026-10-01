# 100 SZÁM ALKALMAZÁS
# Fájl beolvasása, módosítás, keresés, mentés

# 2. Konstans a fájlnévvel
FILE_NAME = "szamok.txt"


# 3. Fájlolvasó függvény: bemenet a fájlnév, kimenet egy számokból álló lista
def read_numbers(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()          # 3.1 a sorok egy listába

    numbers = []                          # 3.2 üres lista
    for line in lines:                    # 3.3 végigmegyünk a sorokon
        numbers.append(int(line.strip())) # sortörés levágása + számmá alakítás
    return numbers                        # 3.4 visszaadjuk a listát


# 7. Fájlba író függvény: bemenet a fájlnév és egy számokból álló lista
def write_numbers(file_name, number_list):
    text_list = []                        # 7.1 üres lista a szöveges értékeknek
    for number in number_list:            # 7.2 végigmegyünk a számokon
        text_list.append(str(number))     # szöveggé alakítva hozzáadjuk
    text = "\n".join(text_list)           # 7.3 összefűzés sortörésekkel
    with open(file_name, "w", encoding="utf-8") as file:  # 7.4 "w" = felülírás
        file.write(text)


# 9. Keresés függvény (nincs bemeneti paramétere)
def search():
    value = input("Melyik szám indexét keresi? (üres = vissza a menübe) ")
    if value == "":                       # 9.2 üres -> vissza a menübe
        return
    if not value.isdigit():               # 9.3 nem szám -> hibaüzenet
        return "Hiba: csak számot lehet keresni!"
    number = int(value)
    if number in numbers:                 # 9.4 megkeressük az indexet
        index = numbers.index(number)     # 9.5 megvan -> kiírjuk, és vissza None-nal
        print(f"A(z) {number} a(z) {index}. indexen található.")
        return
    return f"A(z) {number} nem szerepel a listában."  # 9.6 nincs meg


# 10. Módosítás függvény (nincs bemeneti paramétere) – az indexet kéri be
def modify():
    index_text = input("Melyik indexet módosítja? (üres = vissza a menübe) ")
    if index_text == "":                  # 10.2 üres -> vissza a menübe
        return
    if not index_text.isdigit():          # 10.3 nem szám -> hibaüzenet
        return "Hiba: az index egy szám legyen!"
    index = int(index_text)
    if index >= 100:                      # 10.4 100-nál kisebbnek kell lennie
        return "Hiba: az index 100-nál kisebb legyen!"

    # 10.5 + 11. meghívjuk a második függvényt a megadott ciklus-szerkezettel
    while True:
        result = modify_value(index)
        if result is None:
            break
        else:
            print(result)
    return


# 11. Új érték beállítása adott indexre (bemenete az index)
def modify_value(index):
    value = input("Mi legyen az új érték? (üres = vissza a menübe) ")
    if value == "":                       # 11.2 üres -> vissza a menübe
        return
    if not value.isdigit():               # 11.3 nem szám -> hibaüzenet
        return "Hiba: az érték egy szám legyen!"
    numbers[index] = int(value)           # 11.4 felülírjuk az indexhez tartozó értéket
    print("A módosítás sikeres.")         # 11.5
    return


# ---------------------------------------------------------------------------
# 4. A fájlolvasó függvény meghívása a konstans változóval, mentés a numbers-be
numbers = read_numbers(FILE_NAME)
#print(numbers)   # 4. ideiglenes teszt-kiírás (a kész programban nincs rá szükség)


# 5. Induláskor megjelenő cím (ez csak egyszer látszik)
print("100 SZÁM ALKALMAZÁS")
print()

# 6. Főmenü ciklusa – az alsó rész és az adatbekérés Q-ig ismétlődik
while True:
    print("Válassza ki a kívánt funkciót:")
    print("    M - Szám módosítása")
    print("    K - Szám index keresése")
    print("    Q - Mentés és kilépés")
    print()

    choice = input("Választás: ").upper()  # 6.2 kisbetűt is elfogadunk

    if choice == "M":
        while True:
            result = modify()
            if result is None:
                break
            else:
                print(result)

    elif choice == "K":
        while True:
            result = search()
            if result is None:
                break
            else:
                print(result)

    elif choice == "Q":                    # 8. mentés és kilépés
        write_numbers(FILE_NAME, numbers)
        print("A mentés sikeres.")
        break

    else:                                  # 6.3 helytelen érték
        print("Hibás választás, próbálja újra!")
        print()