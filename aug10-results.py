# ==========================================================
# PYTHON LECKE 6. - TANÁRI MEGOLDÓKULCS
# Függvények, fájlkezelés, hibakezelés, while ciklus
# ==========================================================
#
# Ez a fájl a diákoknak kiadott lecke TELJES megoldását tartalmazza,
# hardcode-olt (fix) bemenetekkel, hogy hiba nélkül lefusson.
# Az interaktív (input()) verziók megjegyzésben szerepelnek.
#
# Jelölések:
#   ⚠️  = gyakori diákhiba, amire külön érdemes felhívni a figyelmet
#   💡  = alternatív / haladóbb megoldás
#   ⏱️  = ajánlott időzítés az adott részhez órán
# ==========================================================


# ==========================================================
# 1. RÉSZ - FÜGGVÉNYDEFINÍCIÓK: "A RECEPT"          ⏱️ kb. 15 perc
# ==========================================================


def keszits_teat(fajta="fekete", cukor=1):
    """Ez egy recept arra, hogyan készíts teát."""
    print("Forralj fel egy kis vizet.")
    print(f"Tegyél bele {fajta} teát.")
    print(f"Adj hozzá {cukor} kanál cukrot.")
    return f"{fajta} tea kész, {cukor} kanál cukorral."


eredmeny1 = keszits_teat()
eredmeny2 = keszits_teat("zöld", 2)
print(eredmeny1)
print(eredmeny2)


# ---------------- MEGOLDÁSOK ----------------


# Megoldás 1.1 ⭐
def koszontes(nev):
    return f"Szia, {nev}!"


print(koszontes("Anna"))  # -> Szia, Anna!


# Megoldás 1.2 ⭐⭐
def negyzetszam(szam=2):
    return szam**2


print(negyzetszam())  # -> 4  (alapértelmezett 2-vel)
print(negyzetszam(5))  # -> 25

# ⚠️ Gyakori diákhiba: szam * szam helyett szam * 2-t írnak (összeadás
# helyett szorzás keveredik a négyzetreemeléssel). Érdemes külön
# kiemelni a különbséget négyzetre emelés (szam ** 2 vagy szam * szam)
# és a "duplázás" (szam * 2) között.


# Megoldás 1.3 ⭐⭐⭐
def hozzaad_elem(elem, lista=None):
    if lista is None:
        lista = []
    lista.append(elem)
    return lista


# Teszteljük, hogy tényleg NEM osztja meg a listát a hívások között:
l1 = hozzaad_elem("alma")
l2 = hozzaad_elem("körte")
print(l1)  # -> ['alma']   (helyesen, NEM tartalmazza a körtét!)
print(l2)  # -> ['körte']

# ⚠️ Ha valaki a "def hozzaad_elem(elem, lista=[]):" hibás verziót írja
# meg, akkor a fenti teszt l1 = ['alma', 'körte']-t adna vissza - ez a
# klasszikus "megosztott alapértelmezett lista" hiba. Érdemes a diákkal
# élőben megnézetni ezt a hibás változatot is, hogy lássa a különbséget!
#
# 💡 Haladóbb megoldás: ugyanez default paraméterrel egy tuple-lel is
# demonstrálható, mivel a tuple nem módosítható (immutable), így az
# a fajta hiba tuple-lel eleve nem történhetne meg.


# ==========================================================
# 2. RÉSZ - FÁJLKEZELÉS: "A NAPLÓ"                  ⏱️ kb. 15 perc
# ==========================================================

with open("naplo.txt", "w", encoding="utf-8") as f:
    f.write("Ma tanultam Pythont!\n")
    f.write("Nagyon élveztem a leckét.\n")

with open("naplo.txt", "r", encoding="utf-8") as f:
    tartalom = f.read()
    print(tartalom)


# ---------------- MEGOLDÁSOK ----------------

# Megoldás 2.1 ⭐
with open("bevasarlolista.txt", "w", encoding="utf-8") as f:
    f.write("kenyér\n")
    f.write("tej\n")
    f.write("alma\n")


# Megoldás 2.2 ⭐⭐
with open("bevasarlolista.txt", "r", encoding="utf-8") as f:
    sorok = f.readlines()
    for i, sor in enumerate(sorok, start=1):
        print(f"{i}. {sor.strip()}")

# ⚠️ Gyakori diákhiba: elfelejtik a .strip()-et használni, így a
# sorvégi "\n" karakter is kiíródik, és a kimenet furcsán tördelődik.
#
# 💡 Alternatív megoldás "for" ciklus nélkül, sima indexeléssel:
# for i in range(len(sorok)):
#     print(f"{i + 1}. {sorok[i].strip()}")


# Megoldás 2.3 ⭐⭐⭐
with open("bevasarlolista.txt", "a", encoding="utf-8") as f:
    f.write("sajt\n")

with open("bevasarlolista.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ⚠️ Ha valaki "w" módot használ "a" helyett, az egész régi tartalom
# ELVESZIK, mert a "w" mindig felülírja (kiüríti) a fájlt megnyitáskor!
# Ez az egyik leggyakoribb és legveszélyesebb kezdő hiba fájlkezelésnél.


# ==========================================================
# 3. RÉSZ - HIBAKEZELÉS: "A BIZTONSÁGI HÁLÓ"         ⏱️ kb. 15 perc
# ==========================================================

try:
    szam = int("nem szám")
except ValueError:
    print("Hoppá! Ez nem volt érvényes szám.")
finally:
    print("Ez a sor MINDIG lefut, akár volt hiba, akár nem.")

try:
    eredmeny = 10 / 0
except ZeroDivisionError:
    print("Nullával nem lehet osztani!")
except ValueError:
    print("Ez egy másik típusú hiba lenne.")


# ---------------- MEGOLDÁSOK ----------------

# Megoldás 3.1 ⭐
try:
    eredmeny = 10 / 0
except ZeroDivisionError:
    print("Nullával nem lehet osztani!")


# Megoldás 3.2 ⭐⭐
try:
    with open("nincsilyen.txt", "r", encoding="utf-8") as f:
        tartalom = f.read()
except FileNotFoundError:
    print("A fájl nem található!")


# Megoldás 3.3 ⭐⭐⭐
szam1_szoveg = "20"
szam2_szoveg = "0"

# Interaktív verzió (csak megjegyzésben, hogy a fájl input() nélkül fusson):
# szam1_szoveg = input("Adj meg egy számot: ")
# szam2_szoveg = input("Adj meg egy másik számot: ")

try:
    szam1 = int(szam1_szoveg)
    szam2 = int(szam2_szoveg)
    eredmeny = szam1 / szam2
    print(f"Az eredmény: {eredmeny}")
except ValueError:
    print("Az egyik megadott érték nem szám!")
except ZeroDivisionError:
    print("Nullával nem lehet osztani!")

# ⚠️ Fontos didaktikai pont: a szam1_szoveg = "20", szam2_szoveg = "0"
# beállítással a ZeroDivisionError ágat mutatjuk be. Érdemes órán
# külön kipróbáltatni a diákokkal a szam2_szoveg = "kettő" esetet is,
# hogy lássák a ValueError ágat is lefutni.
#
# 💡 Haladóbb megoldás: egyetlen "except (ValueError, ZeroDivisionError)
# as hiba:" blokkal is összevonható a két hibatípus kezelése, ha nem
# szükséges külön üzenetet adni nekik.


# ==========================================================
# 4. RÉSZ - WHILE CIKLUS: "AMÍG... ADDIG"           ⏱️ kb. 15 perc
# ==========================================================

kapacitas = 5
bent_levok = 0

while bent_levok < kapacitas:
    bent_levok += 1
    print(f"Vendég beengedve. Bent van: {bent_levok}/{kapacitas}")

print("A klub megtelt, a bejárat bezárt!")


# ---------------- MEGOLDÁSOK ----------------

# Megoldás 4.1 ⭐
szamlalo = 5
while szamlalo >= 1:
    print(szamlalo)
    szamlalo -= 1


# Megoldás 4.2 ⭐⭐
osszeg = 0
i = 1
while i <= 10:
    osszeg += i
    i += 1
print(osszeg)  # -> 55

# 💡 Ugyanez for ciklussal sokkal rövidebb lenne:
# osszeg = sum(range(1, 11))
# Érdemes megemlíteni, hogy while akkor hasznos igazán, amikor előre
# NEM tudjuk, hányszor kell lefutnia a ciklusnak (pl. amíg a
# felhasználó ki nem találja a számot - lásd 4.3. feladat).


# Megoldás 4.3 ⭐⭐⭐
titkos_szam = 7
tippek = [3, 10, 5, 7, 9]

# Interaktív verzió (csak megjegyzésben):
# tipp = int(input("Találd ki a titkos számot: "))
# while tipp != titkos_szam:
#     tipp = int(input("Nem jó, próbáld újra: "))
# print(f"Eltaláltad! A szám: {titkos_szam}")

i = 0
while i < len(tippek):
    tipp = tippek[i]
    if tipp == titkos_szam:
        print(f"Eltaláltad! A szám: {titkos_szam}")
        break
    else:
        print(f"{tipp} nem jó, próbáld újra.")
    i += 1

# ⚠️ Gyakori diákhiba: elfelejtik az "i += 1"-et, ami VÉGTELEN ciklust
# okoz, mert "i" sosem nő, így a while feltétele sosem válik hamissá.
# Ezt érdemes élőben megmutatni (majd Ctrl+C-vel leállítani), hogy a
# diák lássa, mi történik egy valódi végtelen ciklusban.


# ==========================================================
# ÖSSZEFOGLALÓ TÁBLÁZAT - PUSKA
# ==========================================================
#
# TÉMA                | KULCSSZÓ / SZINTAXIS          | ANALÓGIA
# ---------------------|--------------------------------|---------------------------
# Függvény definíció   | def nev(parameterek):         | Recept megírása
#                       |     return ertek              |
# Függvény hívás       | nev(argumentumok)              | Recept elkészítése
# Fájl írás            | open(f, "w") / f.write(...)   | Napló, üres lappal
# Fájl olvasás         | open(f, "r") / f.read()        | Napló elolvasása
# Fájl hozzáírás       | open(f, "a")                   | Új bejegyzés a napló végére
# Hiba elkapása        | try / except Hibatipus:        | Biztonsági háló
# Mindig lefutó kód    | finally:                        | Az előadás mindig folytatódik
# Feltételes ismétlés  | while feltetel:                | "Amíg van hely, addig enged be"
# Kilépés ciklusból    | break                           | Az őr lezárja a bejáratot
#
# ⚠️ TOP 4 HIBA, AMIRE FIGYELJ:
#   1. Módosítható (lista) alapértelmezett paraméter -> használj None-t helyette
#   2. encoding="utf-8" hiánya -> az ékezetes betűk elromolhatnak
#   3. Csupasz "except:" -> mindig írd ki, milyen hibát vársz
#   4. Elfelejtett számlálónövelés while ciklusban -> végtelen ciklus
# ==========================================================
