#shopping = ["milk", "bread"]     #<- list, can change
#point    = (3, 5)                #<- tuple, sealed

#tuple1 = ("apple", "banana", "cherry")
#tuple2 = (1, 5, 7, 9, 3)
#tuple3 = (True, False, False)
#list1 = ["apple", "banana", "cherry"]
#print(tuple1[1] = "plum")
#list1[1] = "plum"
#print(list1)
#list1.append("pear")
#print(list1)
#tuple2.count()

kor_szoveg = "17"  # kor_szoveg = input("Hány éves vagy? ")
magassag_szoveg = "1.75"  # magassag_szoveg = input("Milyen magas vagy (m)? ")

# Írasd ki ezt a mondatot - a számokat a két változóból számold ki:
#
#     Jövőre 18 éves leszel, és 175 cm magas vagy.
#
# 💡 Tipp: Előbb válts: a korhoz int(), a magassághoz float() kell.
#    Méterből centi: szorozd meg 100-zal. A round() eltünteti a
#    felesleges ".0"-t a végéről.


print("\n--- 5. feladat ---")


def teglalap(a, b):
    # TODO: ide írd a megoldást
    terulet = a * b
    kerulet = 2 * (a + b)
    return terulet, kerulet

terulet, kerulet = teglalap(3, 4)



print("teglalap(3, 4) ->", teglalap(3, 4))  # várt: (12, 14)
