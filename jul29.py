# ===========================================================
#   🐍 PYTHON ALAPOK – Első lecke
#   Témakörök: Változók, Megváltoztathatatlanság, Listák,
#              print & input, f-stringek
# ===========================================================


# ===========================================================
# 1. VÁLTOZÓK (Variables)
# ===========================================================
# Képzeld el, hogy a változó egy doboz, amire rá van írva
# egy felirat (a neve), és abban van eltárolva valami érték.
#
#   [ nev ] --> "Anna"
#   [ kor  ] --> 25
#   [ magassag ] --> 1.68
#
# Pythonban nem kell megmondani előre, milyen típusú lesz
# az érték – Python kitalálja magától!

nev = "Anna"  # szöveg (string)
kor = 25  # egész szám (integer)
magassag = 1.68  # tizedes szám (float)
diak_e = True  # igaz/hamis érték (boolean)

# Egy változó értékét bármikor felülírhatjuk:
kor = 26  # most kor már 26, nem 25

# Több változónak egyszerre is adhatunk értéket:
x, y, z = 1, 2, 3


# ------ FELADATOK ------

# 1. feladat: Hozz létre egy 'varos' nevű változót,
#             és add neki értékül a lakóhelyed nevét!
# Ide írd a megoldást:


# 2. feladat: Hozz létre egy 'kedvenc_szam' változót,
#             és add neki a kedvenc számodat értékül!
# Ide írd a megoldást:

# 3. feladat: Írd ki a 'nev' és 'kor' változók értékeit
#             a print() függvénnyel!
# Ide írd a megoldást:


# ===========================================================
# 2. MEGVÁLTOZTATHATATLANSÁG (Immutability)
# ===========================================================
# Pythonban néhány típus "megváltoztathatatlan" (immutable).
# Ez azt jelenti, hogy miután létrehoztuk, nem lehet
# módosítani – csak egy teljesen új értéket hozhatunk létre.
#
# Például a szöveg (string) ilyen!
# Képzelj el egy falba vésett feliratot – nem tudod
# átírni az egyes betűket, csak egy teljesen új feliratot
# véshetsz a falba.

szoveg = "hello"
print(id(szoveg))
# Ez HIBÁT ad – nem tudjuk megváltoztatni az egyes betűket:
# print(szoveg[0])
# szoveg[0] = "H"

# Helyette egy új változót hozunk létre:
szoveg = "Hello"  # ez már egy teljesen új szöveg
print(id(szoveg))
# Más megváltoztathatatlan típusok: int, float, bool, tuple
# Megváltoztatható (mutable) típus például: list, dictionary

# Miért fontos ez? Hogy ne lepődjünk meg, ha egy
# szövegen nem tudunk "helyben" változtatni!


# ------ FELADATOK ------

# 4. feladat: Próbáld ki! Hozz létre egy 'gyumolcs'
#             nevű változót "alma" értékkel.
#             Ezután adj neki új értéket: "körte".
#             Írd ki mindkét esetben a változó értékét!
# Ide írd a megoldást:


# 5. feladat: Mit gondolsz, mi fog történni, ha ezt futtatod?
#             Próbáld ki, és olvasd el a hibaüzenetet!
#
# gyumolcs = "alma"
# gyumolcs[0] = "A"
#
# Ide írd a tapasztalatod kommentként (#):


# ===========================================================
# 3. LISTÁK LÉTREHOZÁSA ÉS KEZELÉSE (Lists)
# ===========================================================
# A lista olyan, mint egy bevásárlócédula:
# sorban egymás után tároljuk benne az elemeket.
# Minden elemnek van egy sorszáma (indexe), de FIGYELEM:
# Pythonban a számozás 0-tól indul!
#
#   gyumolcsok[0] --> "alma"
#   gyumolcsok[1] --> "banán"
#   gyumolcsok[2] --> "körte"

gyumolcsok = ["alma", "banán", "körte"]

# Egy elem elérése index alapján:
print(gyumolcsok[0])  # "alma"
print(gyumolcsok[-1])  # "körte" (az utolsó elem!)

# Lista módosítása:
gyumolcsok[1] = "eper"  # csere
gyumolcsok.append("mangó")  # hozzáadás a végéhez
gyumolcsok.remove("alma")  # eltávolítás érték alapján

# Lista hossza:
print(len(gyumolcsok))  # hány elem van benne?

# Lista bejárása ciklussal:
for gyumolcs in gyumolcsok:
    print(gyumolcs)

# Lista rendezése:
szamok = [5, 2, 8, 1, 9]
szamok.sort()  # növekvő sorrend
print(szamok)

# Lista vágása (slicing) – mint egy kenyér felszeletelése:
print(gyumolcsok[0:2])  # az első két elem


# ------ FELADATOK ------

# 6. feladat: Hozz létre egy 'osztaly' nevű listát,
#             amelyben 4 tanuló neve szerepel!
# Ide írd a megoldást:


# 7. feladat: Írd ki a lista első és utolsó elemét!
# Ide írd a megoldást:


# 8. feladat: Add hozzá a saját nevedet a listához
#             az .append() metódussal, majd írd ki
#             az egész listát!
# Ide írd a megoldást:


# 9. feladat: Írd ki for ciklussal az összes nevet
#             a 'osztaly' listából!
# Ide írd a megoldást:

# ===========================================================
# 4. PRINT ÉS INPUT HASZNÁLATA
# ===========================================================
# print() --> Kiír valamit a képernyőre.
#             Olyan, mint egy hangszóró: hangosan felolvassa
#             azt, amit beleadsz.
#
# input() --> Megvárja, hogy a felhasználó beírjon valamit.
#             Olyan, mint egy kérdőív: vár a válaszra.

print("Szia, világ!")  # egyszerű szöveg kiírása
# print("---")  # elválasztó vonal

# Az input() mindig szöveget (string) ad vissza!
# Ha számot várunk, át kell alakítani:

# nev_bekeres = input("Mi a neved? ")
# kor_bekeres = int(input("Hány éves vagy? "))
# Fontos: futtasd ezeket a sorokat a # jel törlése után!

# print() hasznos paraméterei:
print("alma", "banán", "körte", sep=" | ")  # elválasztó jel
print("Sor 1", end=" ")  # ne legyen sortörés
print("Sor 2")  # ez ugyanabba a sorba kerül


# ------ FELADATOK ------

# 10. feladat: Kérd be a felhasználó nevét és korát,
#              majd írd ki: "Szia, [nev]! [kor] éves vagy."
#              (A kort számként kezeld!)
# Ide írd a megoldást:


# 11. feladat: Kérd be két számot a felhasználótól,
#              add össze őket, és írd ki az eredményt!
# Ide írd a megoldást:


# ===========================================================
# 5. F-STRINGEK (f-strings)
# ===========================================================
# Az f-string egy okos módszer arra, hogy változókat
# szúrjunk bele egy szövegbe.
# Képzeld el, mint egy levélsablont:
#   "Kedves [NÉV]! A számlád összege: [ÖSSZEG] Ft."
# Az f-string pontosan így működik!
#
# Hogyan néz ki? Az f betű kerül a string elé, a változókat
# pedig kapcsos zárójelek {} közé írjuk.

nev = "Béla"
kor = 30
magassag = 1.75

# Régi módszer (kevésbé szép):
print("Szia, " + nev + "! " + str(kor) + " éves vagy.")

# f-string (sokkal elegánsabb!):
print(f"Szia, {nev}! {kor} éves vagy.")
print(f"A magasságod: {magassag} méter.")

# Számítás is végezhető az {} belsejében:
print(f"10 év múlva {kor + 10} éves leszel.")

# Tizedes számok formázása (pl. 2 tizedesjegy):
szam = 3.14159
print(f"Pi értéke kb: {szam:.2f}")


# ------ FELADATOK ------

# 12. feladat: Hozz létre 'varos', 'laksz_ott_evek' változókat,
#              és írd ki f-string segítségével:
#              "[varos]-ban/ben [laksz_ott_evek] éve laksz."
# Ide írd a megoldást:


# 13. feladat: Kérd be a felhasználó nevét és kedvenc számát,
#              majd f-string segítségével írd ki:
#              "Szia, [nev]! A kedvenc számod kétszerese: [szam*2]."
# Ide írd a megoldást:


# 14. feladat (Összetett): Hozz létre egy listát 3 tárgy nevével
#              (pl. "Matek", "Fizika", "Torma").
#              Kérd be a felhasználó nevét.
#              Írd ki f-string-gel és for ciklussal:
#              "[nev] tantárgya: [tantargy]"
# Ide írd a megoldást:


# ===========================================================
# 6. TÍPUSKONVERZIÓ – Változók típusának megváltoztatása
#    (Type Conversion / Type Casting)
# ===========================================================
# Képzeld el, hogy különböző "dobozformák" léteznek:
#   - kerek doboz  --> szöveg (str)
#   - szögletes doboz --> egész szám (int)
#   - ovális doboz --> tizedes szám (float)
#
# Néha át kell "csomagolni" az értéket egy másik formájú
# dobozba – ezt hívjuk típuskonverziónak.
#
# Miért van erre szükség?
# Az input() MINDIG szöveget ad vissza – még akkor is,
# ha a felhasználó egy számot ír be!
# Ha pl. össze akarunk adni két bekért számot, előbb
# át kell alakítani őket számmá.

# A legfontosabb konverziós függvények:
#
#   int()   --> egész számmá alakít
#   float() --> tizedes számmá alakít
#   str()   --> szöveggé alakít
#   bool()  --> igaz/hamis értékké alakít

# ---- Szövegből szám ----
szoveg_szam = "42"
egesz_szam = int(szoveg_szam)  # "42" --> 42
print(egesz_szam + 8)  # 50  (szövegnél ez hibát adna!)

szoveg_tizedes = "3.14"
tizedes_szam = float(szoveg_tizedes)  # "3.14" --> 3.14
print(tizedes_szam * 2)  # 6.28

# ---- Számból szöveg ----
szam = 100
szoveg = str(szam)  # 100 --> "100"
print("Az eredmény: " + szoveg)  # most már össze lehet fűzni!

# ---- Egészből tizedes ----
egesz = 5
tizedes = float(egesz)  # 5 --> 5.0
print(tizedes)

# ---- Tizedesből egész (a tizedes rész ELVÉSZ!) ----
tizedes2 = 9.99
egesz2 = int(tizedes2)  # 9.99 --> 9  (nem kerekít, levágja!)
print(egesz2)

# ---- Mire figyeljünk? ----
# Nem minden konverzió működik! Ha olyan szöveget próbálsz
# számmá alakítani, ami nem szám, Python hibát dob.
# int("hello")  --> ValueError! ❌
# int("42")     --> 42          ✅

# A típust bármikor megnézhetjük a type() függvénnyel:
x = 42
print(type(x))  # <class 'int'>
y = "42"
print(type(y))  # <class 'str'>
z = float(x)
print(type(z))  # <class 'float'>


# ------ FELADATOK ------

# 15. feladat: Kérd be a felhasználó életkorát (input),
#              alakítsd egész számmá, majd írd ki f-string-gel:
#              "5 év múlva [kor+5] éves leszel."
# Ide írd a megoldást:

# 16. feladat: Kérd be a felhasználótól egy termék árát
#              és a darabszámot. Számold ki a végösszeget,
#              és írd ki: "Fizetendő összeg: [vegosszeg] Ft"
#              (Ügyelj a típuskonverzióra!)
# Ide írd a megoldást:


# 17. feladat: Hozz létre egy 'ertek' változót "7.5" értékkel
#              (ez szöveg!). Alakítsd float-tá, szorozd meg 4-gyel,
#              majd az eredményt alakítsd vissza szöveggé,
#              és fűzd hozzá: " pont" (pl. "30.0 pont").
#              Írd ki az eredményt!
# Ide írd a megoldást:


# 18. feladat (Összetett): Kérj be 3 számot a felhasználótól.
#              Tárold el őket egy listában (figyelj a konverzióra!),
#              majd írd ki f-string-gel az összegüket és
#              az átlagukat (2 tizedesjegyre kerekítve).
# Segítség: az átlag = összeg / darabszám
# Ide írd a megoldást:
