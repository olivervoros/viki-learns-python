# =============================================================
# 01. LECKE - A PROGRAMOZÁS ALAPJAI
# Témák: algoritmus, változó, adattípusok, kiírás, beolvasás,
#        elágazás, ciklus
# =============================================================
#
# MI AZ A PROGRAMOZÁS?
# --------------------
# Képzeld el, hogy egy nagyon szorgalmas, de nagyon buta szakácsot
# irányítasz. Mindent megcsinál, amit mondasz neki - de PONTOSAN
# csak azt, és pont abban a sorrendben.
# Ha azt mondod: "üsd fel a tojást", akkor felüti. Ha elfelejted
# mondani, hogy vedd le a héját, akkor a héj is a tálba kerül.
#
# A programozás = utasítások pontos leírása a gépnek.
#
#
# 1) MI AZ AZ ALGORITMUS?
# -----------------------
# Az algoritmus egy RECEPT: lépések sorozata, ami egy feladatot
# megold. Nem kell hozzá számítógép! A reggeli fogmosás is
# algoritmus:
#
#   1. lépés: fogkefét a kézbe venni
#   2. lépés: fogkrémet rányomni
#   3. lépés: 2 percig mosni
#   4. lépés: kiöblíteni
#
# Fontos: a SORREND számít. Ha előbb öblítesz és utána mosol,
# az már nem működik. A gépnél is így van.
#
#
# 2) MI AZ A VÁLTOZÓ?
# -------------------
# A változó egy FELIRATOZOTT DOBOZ a polcon.
# - A doboz oldalára ráírsz egy nevet (pl. "cukor")
# - A dobozba beleteszel valamit (pl. 500 grammot)
# - Ha később kell, elég a nevét mondani, és tudod, mi van benne
# - A tartalma kicserélhető -> ezért hívjuk VÁLTOZÓnak
#
# Pythonban a doboz készítése és a feltöltése egy lépés:

nev = "Anna"  # egy doboz "nev" felirattal, benne: Anna
eletkor = 15  # egy doboz "eletkor" felirattal, benne: 15

print(nev)  # a print() kiírja a képernyőre a doboz tartalmát
print(eletkor)

# A doboz tartalma bármikor felülírható:
eletkor = 16
print(eletkor)  # most már 16-ot ír ki, a régi 15 eltűnt


# 3) ADATTÍPUSOK - MILYEN HOLMI VAN A DOBOZBAN?
# ---------------------------------------------
# Nem mindegy, hogy lisztet vagy tojást teszel a dobozba.
# A Python 4 alap "holmit" ismer a kezdéshez:

szoveg = "Szia!"  # str   -> szöveg, MINDIG idézőjelben
egesz = 42  # int   -> egész szám
tort = 3.14  # float -> tizedes szám (PONTTAL, nem vesszővel!)
igaz_hamis = True  # bool  -> igaz vagy hamis (True / False)

# A type() megmondja, mi van a dobozban:
print(type(szoveg))
print(type(egesz))
print(type(tort))
print(type(igaz_hamis))

# ⚠️ FIGYELEM: a "42" (idézőjelben) NEM szám, hanem szöveg!
# Olyan, mint a 42-es rendszám: számjegyekből áll, de nem tudsz
# vele számolni.
print(2 + 3)  # 5      -> összeadás
print("2" + "3")  # 23     -> szövegek összeragasztása!


# 4) SZÁMOLÁS A VÁLTOZÓKKAL
# -------------------------
a = 10
b = 3

print(a + b)  # 13  összeadás
print(a - b)  # 7   kivonás
print(a * b)  # 30  szorzás
print(a / b)  # 3.33...  osztás (mindig float lesz!)
print(a // b)  # 3   egész osztás (a maradékot eldobja)
print(a % b)  # 1   maradék
print(a**b)  # 1000  hatványozás


# 5) SZÉP KIÍRÁS: f-STRING
# ------------------------
# Ha szöveget és változót akarsz együtt kiírni, az f-string a
# legkényelmesebb. Olyan, mint egy űrlap: a { } helyére a Python
# behelyettesíti a doboz tartalmát.

nev = "Béla"
kor = 20
print(f"{nev} {kor} éves.")  # Béla 20 éves.
print(f"Jövőre {kor + 1} lesz.")  # Jövőre 21 lesz.


# 6) BEOLVASÁS A FELHASZNÁLÓTÓL
# -----------------------------
# Az input() megkérdezi a felhasználót valamiről.
# ⚠️ Az input() MINDIG szöveget (str) ad vissza, még akkor is,
# ha a felhasználó számot ír be! Ezért gyakran át kell alakítani:
#
#   int("5")   -> 5      (szövegből egész szám)
#   float("5") -> 5.0    (szövegből tizedes szám)
#   str(5)     -> "5"    (számból szöveg)
#
# Próbáld ki (most kikommentezve, hogy a fájl megállás nélkül fusson):

#felhasznalo_nev = input("Hogy hívnak? ")
#felhasznalo_kor = int(input("Hány éves vagy? "))
#print(f"Szia {felhasznalo_nev}! 10 év múlva {felhasznalo_kor + 10} leszel.")
#idáig 08.03.

# 7) ELÁGAZÁS (if) - AZ ÚTELÁGAZÁS
# --------------------------------
# Hasonlat: érkezel egy útkereszteződéshez. Ha zöld a lámpa,
# átmész. Egyébként vársz. A program is tud dönteni.

homerseklet = 28

if homerseklet > 25:
    print("Meleg van, vegyél rövidnadrágot!")
elif homerseklet > 15:
    print("Kellemes idő van.")
elif homerseklet > 0:
    print("Hideg van de még nem fagy")
else:
    print("Hideg van, vegyél kabátot!")

# ⚠️ Két dolgot NAGYON könnyű elrontani:
#   - a sor végén kell a kettőspont ( : )
#   - a belső sorokat BE KELL HÚZNI (4 szóköz). A behúzás
#     Pythonban nem díszítés, hanem a program szerkezete!
#
# 💡 Összehasonlító jelek:  ==  egyenlő,  !=  nem egyenlő,
#    <  kisebb,  >  nagyobb,  <=  kisebb vagy egyenlő,  >=  ...


# 8) CIKLUS (for) - AZ ISMÉTLÉS
# -----------------------------
# Hasonlat: 10 borítékot kell megcímezned. Nem írod le tízszer a
# teendőt, hanem azt mondod: "minden borítékra írd rá a címet."

for i in range(5):
    print(f"Ez a(z) {i}. kör")

# ⚠️ A range(5) az 0-tól 4-ig megy, tehát 5 darab számot ad, de
#    NEM tartalmazza az 5-öt. A programozók 0-tól számolnak!

# 💡 A range-nek megadható kezdet és lépésköz is:
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i, end=" ")
print()  # egy üres sor a végére


# =============================================================
# FELADATOK
# Töröld ki a "pass" szót, és írd oda a saját megoldásodat!
# =============================================================

# --- 1. FELADAT ⭐ -------------------------------------------
# Hozz létre három változót: a kutyád neve (szöveg), a kora
# (egész szám) és a súlya kilóban (tizedes szám).
# Írd ki őket egy f-string segítségével ebben a formában:
# "Bodri 4 éves és 12.5 kg."


# TODO: ide írd a megoldást
kutyam_neve = "Leila"
kutyam_kora = 8
kutyam_sulya = 12.5
print(f"{kutyam_neve} {kutyam_kora} éves és {kutyam_sulya} kg.")


# --- 2. FELADAT ⭐ -------------------------------------------
# Két változóban tárolj el két számot: 17 és 5.
# Írd ki az összegüket, a különbségüket, a szorzatukat
# és az osztási maradékukat.

# TODO: ide írd a megoldást
szam1 = 17
szam2 = 5
print(f"A két szám összege:{szam1+szam2} A két szám különbsége:{szam1-szam2}")
print(f"A két szám szorzata:{szam1*szam2} és osztási maradékuk:{szam1%szam2}")


# --- 3. FELADAT ⭐⭐ ------------------------------------------
# Egy boltban egy alma 250 Ft. Hozz létre egy változót
# "darab" néven 7 értékkel, és számold ki a végösszeget.
# Írd ki: "7 db alma ára: 1750 Ft"

# TODO: ide írd a megoldást
alma_ara = 250
alma_darab = 7
print(f"7 db alma ára:{alma_ara*alma_darab} ft")


# --- 4. FELADAT ⭐⭐ ------------------------------------------
# Adott egy változó: pontszam = 72
# Írj elágazást, ami kiírja az érdemjegyet:
#   85 fölött  -> "jeles"
#   70 - 85    -> "jó"
#   50 - 70    -> "közepes"
#   50 alatt   -> "elégtelen"

pontszam = 72

# TODO: ide írd a megoldást
if pontszam > 85:
    print("Jeles")
elif pontszam >= 70:
    print("Jó")
elif pontszam >=50:
    print("Közepes")
else: 
    print("Elégtelen")


# --- 5. FELADAT ⭐⭐ ------------------------------------------
# Írj ki egy ciklussal 1-től 10-ig minden számot, mellette
# a szám kétszeresét, ilyen formában:
# "3 kétszerese: 6"

# TODO: ide írd a megoldást
szamok = range(1,11)
for szam in szamok:
    print(f"{szam} kétszerese:{szam*2}")


# --- 6. FELADAT ⭐⭐⭐ (ÖSSZEFOGLALÓ) --------------------------
# Készíts egy kis "belépőjegy-pénztárt"!
#
# 1. Legyen egy változó "latogato_kor" néven, értéke 12.
# 2. Legyen egy változó "alapar" néven, értéke 2000.
# 3. Elágazással döntsd el a kedvezményt:
#      - 14 év alatt: az ár fele
#      - 65 év fölött: az ár 70%-a
#      - egyébként: teljes ár
# 4. Írd ki f-stringgel: "A jegy ára: ... Ft"
# 5. Végül egy ciklussal írd ki, mennyibe kerülne 1, 2 és 3 jegy.



# TODO: ide írd a megoldást
latogato_kor = 12
alapar = 2000
if latogato_kor < 14:
    print(f"A jegy ára:{alapar*0.5}Ft")
elif latogato_kor > 65:
    print(f"A jegy ára:{alapar*0.7}Ft")
else:
    print("A jegy ára:2000Ft")
jegy_darabszamok = range(1,4)
for jegy_darabszam in jegy_darabszamok:
    print(f"{jegy_darabszam} darab jegy ára :{jegy_darabszam*2000}Ft")


# =============================================================
# AMIT MA MEGTANULTUNK
# -------------------------------------------------------------
# algoritmus  -> lépések pontos sorrendje (recept)
# változó     -> feliratozott doboz, amiben adatot tárolunk
# str/int/float/bool -> a doboz tartalmának típusa
# print()     -> kiírás a képernyőre
# f"{...}"    -> szöveg és változó összefűzése
# input()     -> beolvasás (mindig szöveget STRINGET ad!)
# int()       -> szövegből szám
# if/elif/else-> döntés, útelágazás
# for + range -> ismétlés
# behúzás     -> 4 szóköz, ez adja a program szerkezetét
# =============================================================
