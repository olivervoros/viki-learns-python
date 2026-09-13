# =============================================================
# 02. LECKE - GYAKORLÓ FELADATOK
# Témák: változók és típuskonverzió, listák, ciklusok (for/while),
#        elágazások, hibakezelés, input és f-string, függvények,
#        fájlkezelés
# =============================================================
#
# HOGYAN HASZNÁLD
# ---------------
# Minden témánál ugyanaz a sorrend:
#
#   1. EMLÉKEZTETŐ  - rövid magyarázat és példa, amit lefuttathatsz
#   2. FELADATOK    - töröld ki a "pass" szót, és írd oda a megoldást
#
# A fájl így is elindul, hiba nélkül. Futtasd gyakran, ne csak a
# legvégén! Egy program, amit százszor futtattál, sosem lesz akkora
# meglepetés, mint egy, amit egyszer sem.
#
# ⭐      alap
# ⭐⭐    gondolkodni kell rajta
# ⭐⭐⭐  összetett, több téma együtt
#
# =============================================================


# =============================================================
# 1) VÁLTOZÓK ÉS TÍPUSKONVERZIÓ
# =============================================================
#
# EMLÉKEZTETŐ
# -----------
# A változó egy feliratozott doboz. A TÍPUS azt mondja meg, MI van
# a dobozban.
#
# Hasonlat: az "5" egy kártya, amire rá van írva az öt.
#           Az 5 pedig öt darab valódi érme.
# Két kártyát egymás mellé téve hosszabb felirat lesz - nem tíz érme.

print("2" + "3")  # 23   -> két kártya egymás mellett
print(2 + 3)  # 5    -> két marék érme összeöntve

# Az átváltó automata: int(), float(), str()
print(int("42") + 8)  # 50
print(float("3.14"))  # 3.14
print(str(2026) + "-os év")  # 2026-os év

# ⚠️ Két csapda, amibe MINDENKI belesétál egyszer:
print(int(9.99))  # 9   -> LEVÁGJA a tizedeseket, NEM kerekít!
print(round(9.99))  # 10  -> ez kerekít
# int("3.9") pedig egyenesen hibát dob. Előbb float(), aztán int().

# 💡 A type() bármikor megmondja, mi van a dobozban:
print(type("szia"), type(7), type(1.5), type(True))


# --- 1.1 FELADAT ⭐ ------------------------------------------
# Két szöveg érkezett egy űrlapról: "12" és "8".
# Írd ki az ÖSSZEGÜKET számként (tehát 20-at, ne "128"-at).

szoveg_a = "12"
szoveg_b = "8"



# TODO: ide írd a megoldást
print(int("12") + int("8"))


# --- 1.2 FELADAT ⭐ ------------------------------------------
# Egy webshopban minden adat szövegként érkezik.
# Számold ki a végösszeget, és írd ki:  "3 db x 1490 Ft = 4470 Ft"

darab = "3"
egysegar = "1490"

# TODO: ide írd a megoldást
darab = int(darab)
egysegar = int(egysegar)
osszeg = darab * egysegar
print(f"{darab} db x {egysegar} Ft = {osszeg} Ft")


# --- 1.3 FELADAT ⭐⭐ -----------------------------------------
# Adott egy tizedes szám szövegként: "7.8"
# Írd ki egymás alá:
#   a) a számot tizedesként (float)
#   b) ugyanezt egész számmá alakítva LEVÁGÁSSAL   -> 7
#   c) ugyanezt egész számmá KEREKÍTVE             -> 8
# ⚠️ Az int("7.8") hibát dob! Gondold végig, mi legyen a sorrend.

merteg = "7.8"

# TODO: ide írd a megoldást
print(float(merteg))
print(int(float(merteg)))
print(round(float(merteg)))


# =============================================================
# 2) LISTÁK ÉS LISTAMŰVELETEK
# =============================================================
#
# EMLÉKEZTETŐ
# -----------
# A lista a hűtőre kitett bevásárlólista: írsz rá, kihúzol róla,
# átrendezed. Minden elemnek van SORSZÁMA, és a számolás 0-tól indul.

bevasarlas = ["tej", "kenyér", "tojás"]

bevasarlas.append("sajt")  # a végére
bevasarlas.insert(0, "kávé")  # a legelejére
bevasarlas.remove("kenyér")  # ÉRTÉK szerint töröl
print(bevasarlas)

# Rész kivétele - a szeletelés:
szamok = [10, 20, 30, 40, 50, 60, 70]
print(szamok[0])  # 10          az első
print(szamok[-1])  # 70          az utolsó (hátulról az első)
print(szamok[:3])  # [10,20,30]  az első három
print(szamok[-2:])  # [60,70]     az utolsó kettő
print(szamok[2:5])  # [30,40,50]  a 3., 4. és 5. elem
#
# 💡 Képzeld a számokat az elemek KÖZÖTTI résekre: [2:5] azt jelenti,
#    "vágj a 2-es és az 5-ös résnél, és tartsd meg a közepét".

# Beépített segítők:
print(len(szamok), sum(szamok), max(szamok), min(szamok))
print(30 in szamok)  # True - benne van?

# ⚠️ A LEGGYAKORIBB LISTAHIBA a világon:
#       lista = lista.sort()      <- a lista NONE lesz és eltűnik!
#    Mert a .sort() helyben rendez, és nem ad vissza semmit.
nevek = ["Cili", "Anna", "Béla"]
print(sorted(nevek))  # ÚJ listát ad, az eredetit békén hagyja
print(nevek)  # az eredeti változatlan
nevek.sort()  # ez viszont helyben rendez
print(nevek)


# --- 2.1 FELADAT ⭐ ------------------------------------------
# Adott az alábbi lista.
#   a) tedd a végére: "teknős"
#   b) tedd a legelejére: "papagáj"
#   c) töröld belőle: "macska"
#   d) írd ki a kész listát

allatok = ["kutya", "macska", "nyúl"]

# TODO: ide írd a megoldást
allatok.append("teknős")
print(allatok)
allatok.insert(0, "papagáj")
print(allatok)
allatok.remove("macska")
print(allatok)


# --- 2.2 FELADAT ⭐ ------------------------------------------
# Írd ki egymás alá szeleteléssel:
#   a) az első elemet
#   b) az utolsó elemet (a 6-os számot NE használd!)
#   c) az első három elemet
#   d) az utolsó két elemet

pontok = [3, 8, 1, 9, 4, 7, 2]

# TODO: ide írd a megoldást
print(pontok[0])
print(pontok[-1])
print(pontok[:3])
print(pontok[-2:])


# --- 2.3 FELADAT ⭐⭐ -----------------------------------------
# Írd ki a hőmérsékleteket növekvő sorrendben ÚGY, hogy az eredeti
# lista sorrendje NE változzon meg. Bizonyításképp írd ki utána az
# eredeti listát is.

homersekletek = [12, 25, 8, 19, 4]

# TODO: ide írd a megoldást



# --- 2.4 FELADAT ⭐⭐ -----------------------------------------
# Írd ki a lista átlagát 1 tizedesjegyre kerekítve.
# (Segítség: sum() és len() együtt, a végén round(..., 1).)

jegyek = [4, 5, 3, 5, 2]

# TODO: ide írd a megoldást
atlag = sum(jegyek) / len(jegyek)
print(round(atlag, 1))


# =============================================================
# 3) CIKLUSOK - FOR ÉS WHILE
# =============================================================
#
# EMLÉKEZTETŐ
# -----------
# A FOR ciklus a postás: van egy kötegnyi levele, és mindet
# bedobja. ELŐRE tudja, hány darab van.
#
# A WHILE ciklus a vízforraló: addig melegít, AMÍG fel nem forr.
# Nem tudja előre, hány másodperc lesz - csak a feltételt figyeli.

for szam in range(1, 6):  # 1, 2, 3, 4, 5
    print(szam, end=" ")
print()

# A "vödör-minta": gyűjtés ciklusban
osszeg = 0  # az üres vödör a ciklus ELŐTT!
for szam in range(1, 101):
    osszeg = osszeg + szam  # rövidebben: osszeg += szam
print(osszeg)  # 5050

# Új lista építése:
negyzetek = []
for szam in range(1, 6):
    negyzetek.append(szam**2)
print(negyzetek)  # [1, 4, 9, 16, 25]

# Ha a SORSZÁM is kell, ott az enumerate:
diakok = ["Anna", "Béla", "Cili"]
for sorszam, diak in enumerate(diakok, start=1):
    print(f"{sorszam}. {diak}")

# WHILE - amíg a feltétel igaz:
szamlalo = 3
while szamlalo > 0:
    print(szamlalo, end=" ")
    szamlalo -= 1  # ⚠️ EZ a sor menti meg a végtelen ciklustól!
print("Indulás!")
#
# ⚠️ Ha a while-on belül semmi nem változtatja a feltételt, a program
#    ÖRÖKKÉ fut. Ctrl+C állítja meg. Egyszer érdemes megtapasztalni.
#
# 💡 break = azonnal kilép a ciklusból
#    continue = ezt az egy kört kihagyja, de megy tovább


# --- 3.1 FELADAT ⭐ ------------------------------------------
# Írd ki 1-től 10-ig minden szám négyzetét, ilyen formában:
#   "3 négyzete: 9"

# TODO: ide írd a megoldást
for szam in range(1, 11):
    print(f"{szam} négyzete: {szam**2}")


# --- 3.2 FELADAT ⭐ ------------------------------------------
# Írd ki a diákokat sorszámozva, enumerate segítségével:
#   1. Anna
#   2. Béla
#   ...

osztaly = ["Anna", "Béla", "Cili", "Dóra"]

# TODO: ide írd a megoldást
for sorszam, diak in enumerate(osztaly, start=1):
    print(f"{sorszam}. {diak}")


# --- 3.3 FELADAT ⭐⭐ -----------------------------------------
# Gyűjtsd össze egy ÚJ listába a 20 fok feletti hőmérsékleteket,
# majd írd ki a listát és azt is, hány ilyen nap volt.
# (Üres lista + for + if + append.)

napi_homerseklet = [12, 25, 31, 8, 19, 27, 33, 4]

# TODO: ide írd a megoldást
meleg_napok = []
for i in napi_homerseklet:
    if i > 20:
        meleg_napok.append(homerseklet)
print(meleg_napok)
print(len(meleg_napok))


# --- 3.4 FELADAT ⭐⭐ -----------------------------------------
# WHILE ciklussal: indulj a 100-ról, és addig felezd, amíg 1 fölött
# van. Minden lépést írj ki. (100, 50.0, 25.0, 12.5, ...)

szam = 100

# TODO: ide írd a megoldást
while szam > 1:
    print(szam)
    szam = szam / 2


# =============================================================
# 4) ELÁGAZÁSOK - IF / ELIF / ELSE
# =============================================================
#
# EMLÉKEZTETŐ
# -----------
# Az if/elif/else egy FOLYOSÓ AJTÓKKAL. Végigmész rajta, és az ELSŐ
# ajtón mész be, amelyik kinyílik. A többit meg sem látod.


def minosites(pont):
    if pont >= 90:
        return "jeles"
    elif pont >= 75:
        return "jó"
    elif pont >= 60:
        return "közepes"
    else:
        return "elégtelen"


print(minosites(95), minosites(80), minosites(65), minosites(30))

# ⚠️ A SORREND maga a logika. Ha a "pont >= 60" ág lenne legfelül,
#    a 95 is "közepes" lenne - mert 95 valóban több 60-nál.
#    Szabály: a legszigorúbb feltétel megy legfelülre.
#
# ⚠️ Négy KÜLÖN if nem ugyanaz, mint egy elif-lánc! Négy külön if
#    négy külön folyosó - mindegyikbe belépsz.
#
# ⚠️  =  berak valamit a dobozba (értékadás)
#    ==  megkérdezi, egyformák-e (összehasonlítás)
#
# 💡 Két feltétel egyszerre:
ho = 32
print(ho > 30 and ho < 35)  # mindkettőnek igaznak kell lennie
print(30 < ho < 35)  # ugyanaz, csak szebb
print(ho < 0 or ho > 35)  # elég, ha az egyik igaz


# --- 4.1 FELADAT ⭐ ------------------------------------------
# Írj elágazást, ami a BMI alapján kiír egy kategóriát:
#   18.5 alatt      -> "sovány"
#   18.5 - 25       -> "normál"
#   25 - 30         -> "túlsúlyos"
#   30 fölött       -> "elhízott"

bmi = 26.4

# TODO: ide írd a megoldást
if bmi < 18.5:
    print("sovány")
elif bmi < 25:
    print("normál")
elif bmi < 30:
    print("túlsúlyos")
else:
    print("elhízott")

# --- 4.2 FELADAT ⭐⭐ -----------------------------------------
# Mozijegy ára:
#     3 év alatt     ingyenes (0)
#     3 - 15 év      1200 Ft
#     16 - 64 év     2500 Ft
#     65 évtől       1500 Ft
# ÉS: szerdán minden FIZETŐS jegy 500 Ft-tal olcsóbb.
#
# Számold ki és írd ki a jegy árát az alábbi adatokkal.
# ⚠️ Az ingyenes jegy maradjon 0 - ne legyen -500 Ft!

latogato_kor = 2
nap = "szerda"

# TODO: ide írd a megoldást
if latogato_kor < 3:
    ar = 0
elif latogato_kor <= 15:
    ar = 1200
elif latogato_kor <= 64:
    ar = 2500
else:
    ar = 1500
if nap == "szerda" and ar > 0:
    ar = ar - 500
print(ar)


# --- 4.3 FELADAT ⭐⭐ -----------------------------------------
# Írd ki, hogy szökőév-e az adott év.
# Szökőév, ha osztható 4-gyel, DE nem osztható 100-zal,
# KIVÉVE, ha osztható 400-zal (akkor mégis szökőév).
# Próbáld ki ezekkel is: 1900 (nem), 2000 (igen), 2023 (nem).

ev = 2024

# TODO: ide írd a megoldást
if ev % 4 == 0 and ev % 100 > 0:
    print("Szökőév")
elif ev % 400 ==0:
    print("Szökőév")
else:
    print("nem szökőév")


# =============================================================
# 5) HIBAKEZELÉS - TRY / EXCEPT
# =============================================================
#
# EMLÉKEZTETŐ
# -----------
# A try/except a VÉDŐHÁLÓ a trapézművész alatt. Nem az esést
# akadályozza meg - azt akadályozza meg, hogy az esés véget vessen
# az előadásnak.
#
#     try:
#         a kockázatos sor
#     except HibaNeve:
#         mit csináljunk helyette

try:
    szam = int("alma")
except ValueError:
    print("Ez nem szám - de a program megy tovább.")

print("...és tényleg megy tovább.")

# A HAT HIBA, AMIT ISMERNI KELL:
#   ValueError         jó típus, rossz tartalom:  int("alma")
#   TypeError          rossz típus:               "szöveg" + 5
#   ZeroDivisionError  nullával osztás:           10 / 0
#   IndexError         nincs ilyen sorszám:       [1,2,3][7]
#   KeyError           nincs ilyen kulcs:         {"a":1}["b"]
#   FileNotFoundError  nincs ilyen fájl
#
# ⚠️ MINDIG nevezd meg, milyen hibára számítasz! A csupasz "except:"
#    mindent elkap - a saját elgépeléseidet is -, és akkor napokig
#    keresed, miért nem működik.
#
# ⚠️ A try CSAK azt a sort ölelje körbe, ami tényleg elszállhat.
#    Ha az egész ciklust körbeveszed, az első hibás elem megöli
#    az összes többit is.
#
# 💡 A hibaüzenet UTOLSÓ sora majdnem mindig megmondja a megoldást.
#    Olvasd el, ne ijedj meg tőle.


# --- 5.1 FELADAT ⭐ ------------------------------------------
# Írj try/except-et, ami elosztja a-t b-vel, és nullával osztás
# esetén kiírja: "Nullával nem lehet osztani."
# Próbáld ki b = 0 és b = 4 értékkel is!

a = 10
b = 0
eredmeny = []

# TODO: ide írd a megoldást
try:
    eredmeny = a / b
    print(eredmeny)
except ZeroDivisionError:
    print("Nullával nem lehet osztani.")

# --- 5.2 FELADAT ⭐⭐ -----------------------------------------
# Menj végig a listán, és minden elemet próbálj meg egész számmá
# alakítani.
#   - a jókat gyűjtsd egy új listába
#   - a hibásakat SZÁMOLD MEG, és írd ki a nevüket
# A végén írd ki: "6 jó, 2 hibás"
#
# ⚠️ Az üres szöveg ("") is hibát dob!

meresek = ["12", "8", "alma", "31", "", "19", "0", "25"]

# TODO: ide írd a megoldást
jok = []
hibas = 0

for meres in meresek:
    try:
        szam = int(meres)
        jok.append(szam)
    except ValueError:
        print(meres)


# --- 5.3 FELADAT ⭐⭐ -----------------------------------------
# Írj egy try/except/else/finally szerkezetet, ami:
#   - megpróbálja a lista 5. elemét kiírni
#   - IndexError esetén kiírja: "Nincs ennyi elem a listában."
#   - ha sikerült, az else ágban kiírja: "Megvan!"
#   - a finally ágban mindig kiírja: "Kész."

rovid_lista = [1, 2, 3]

# TODO: ide írd a megoldást



# =============================================================
# 6) BEMENET (input) ÉS f-STRING
# =============================================================
#
# EMLÉKEZTETŐ
# -----------
# Az input() egy POSTALÁDA: bármit dobnak be rajta, LEVÉLKÉNT
# érkezik - vagyis szövegként. Akkor is, ha számot írtak be.
# Ezért kell azonnal átváltani:
#
#     kor = int(input("Hány éves vagy? "))
#
# Az f-string a kirakat: f betű a szöveg elé, és a { } helyére a
# Python behelyettesíti az értéket.

nev = "Anna"
ar = 1490.5
nagy_szam = 1250000

print(f"{nev} vagyok.")
print(f"{ar:.2f}")  # 1490.50    két tizedesjegy
print(f"{nagy_szam:,}")  # 1,250,000  ezres tagolás
print(f"{ar:,.2f}")  # 1,490.50   mindkettő
print(f"[{nev:>10}]")  # jobbra igazítva 10 karakteren
print(f"[{nev:<10}]")  # balra igazítva
print(f"{7} x {8} = {7 * 8}")  # számolni is lehet benne

# ⚠️ Ha lemarad az f betű, a Python szó szerint kiírja: {nev}
#    Nem száll el, csak csúnya lesz - ezért nehéz észrevenni.
#
# 💡 Az igazítás táblázatos kiíráshoz aranyat ér. Próbáld ki!


# --- 6.1 FELADAT ⭐ ------------------------------------------
# Írd ki egy f-stringgel ebben a formában:
#   "kávé x3 = 4,470.00 Ft"
# (Ezres tagolás ÉS két tizedesjegy.)

termek = "kávé"
mennyiseg = 3
egyseg_ar = 1490

# TODO: ide írd a megoldást
print(f"{termek} x{mennyiseg} = {mennyiseg * egyseg_ar:,.2f} Ft")


# --- 6.2 FELADAT ⭐⭐ -----------------------------------------
# Írj ki egy szép, igazított árlistát, soronként ilyen formában:
#       kávé            1,490 Ft
#       sajttorta         890 Ft
#       ásványvíz         350 Ft
# (A név balra igazítva 15 karakteren, az ár jobbra 8-on.)

arlista = [("kávé", 1490), ("sajttorta", 890), ("ásványvíz", 350)]

# TODO: ide írd a megoldást
for termek, ar in arlista:
    print(f"{termek:<15}{ar:>8,} Ft")


# --- 6.3 FELADAT ⭐⭐ -----------------------------------------
# Kilométer -> mérföld átváltó. (1 km = 0.621371 mérföld)
# Most a bemenet szövegként van beégetve, mintha input()-ból jönne.
#   - alakítsd át számmá
#   - ha nem szám, írd ki: "Ez nem szám."
#   - ha szám, írd ki: "10.0 km = 6.21 mérföld"
#
# 💡 Ha kész vagy, kommentezd ki a beégetett sort, és próbáld ki
#    élesben ezzel:   km_szoveg = input("Hány km? ")

km_szoveg = "10"

# TODO: ide írd a megoldást
pass


# =============================================================
# 7) FÜGGVÉNYEK
# =============================================================
#
# EMLÉKEZTETŐ
# -----------
# A függvény egy RECEPT. Egyszer leírod, aztán bármikor
# "elkészíted", anélkül hogy újra végiggondolnád.
#
#     def sutemeny(liszt, cukor):    <- a hozzávalók = PARAMÉTEREK
#         ...
#         return torta               <- amit kiadsz = VISSZATÉRÉSI ÉRTÉK


def koszon(nev="Világ"):  # alapértelmezett érték
    return f"Szia, {nev}!"


print(koszon())
print(koszon("Oliver"))


def min_max(szamok):
    return min(szamok), max(szamok)  # két érték egyszerre


also, felso = min_max([4, 9, 2])  # és rögtön kicsomagolható
print(also, felso)

# ⚠️ A print és a return NEM ugyanaz!
#    print = kimondja hangosan az eredményt, aztán elveszik
#    return = ODAADJA, hogy tovább lehessen dolgozni vele
#
# ⚠️ Ha nincs return, a függvény None-t ad vissza. Ez a leggyakoribb
#    "de nálam nem működik semmi" oka.
#
# ⚠️ Az alapértelmezett paraméterek MINDIG hátul állnak:
#    def f(a=1, b)  ->  SyntaxError
#
# 💡 SOHA ne adj alapértéknek listát: def f(x=[]) - az a lista
#    egyszer jön létre, és a hívások között MEGMARAD. Csúnya csapda.


# --- 7.1 FELADAT ⭐ ------------------------------------------
# Írj egy terulet(szelesseg, magassag) függvényt, ami a téglalap
# területét adja VISSZA (nem kiírja!).
# A magasság alapértelmezett értéke legyen 1.
# Próbáld ki: terulet(3, 4) és terulet(5)


# TODO: ide írd a megoldást
def terulet(szelesseg, magassag=1):
    return szelesseg * magassag
print(terulet(3, 4))
print(terulet(5))


# --- 7.2 FELADAT ⭐⭐ -----------------------------------------
# Írj egy statisztika(szamok) függvényt, ami HÁROM értéket ad
# vissza egyszerre: (legkisebb, legnagyobb, átlag 1 tizedesre).
# Hívd meg, csomagold ki három változóba, és írd ki f-stringgel.


# TODO: ide írd a megoldást
def statisztika(szamok):
    also = min(szamok)
    felso = max(szamok)
    atlag = round(sum(szamok) / len(szamok), 1)
    return also, felso, atlag
also, felso, atlag = statisztika([4, 9, 2, 7, 5])
print(f"Legkisebb: {also}, Legnagyobb: {felso}, Átlag: {atlag}")


# --- 7.3 FELADAT ⭐⭐ -----------------------------------------
# Írj egy leghosszabb_szo(mondat) függvényt, ami visszaadja a mondat
# leghosszabb szavát.
#   leghosszabb_szo("a kutya nagyon gyorsan futott")  ->  "gyorsan"
#
# 💡 A "bajnok"-minta: tarts fenn egy jelenlegi legjobbat, és cseréld
#    le, ha jobbat találsz. (mondat.split() szavakra bontja.)


# TODO: ide írd a megoldást
def leghosszabb_szo(mondat):
    pass


# --- 7.4 FELADAT ⭐⭐ -----------------------------------------
# Írj egy jegy_ara(kor, nap="hétfő") függvényt a 4.2 feladat
# szabályaival - most már függvényként, return-nel.
# Hívd meg négyszer és írd ki az eredményeket:
#   (5, "hétfő"), (30, "szerda"), (70, "szerda"), (2, "szerda")


# TODO: ide írd a megoldást
def jegy_ara(kor, nap="hétfő"):
    pass


# =============================================================
# 8) FÁJLKEZELÉS
# =============================================================
#
# EMLÉKEZTETŐ
# -----------
# A fájl egy IRATSZEKRÉNY FIÓKJA. Ki kell húzni (megnyitni),
# dolgozni benne, majd VISSZA IS KELL TOLNI (bezárni).
#
# A "with" gondoskodik arról, hogy a fiók MINDIG visszazáródjon -
# akkor is, ha közben hiba történik. Ezért mindig ezt használjuk.

with open("gyakorlas_adatok.txt", "w", encoding="utf-8") as f:
    f.write("alma\n")
    f.write("körte\n")
    f.write("szilva\n")

with open("gyakorlas_adatok.txt", "a", encoding="utf-8") as f:
    f.write("barack\n")  # "a" = a végére fűz, a régit meghagyja

with open("gyakorlas_adatok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        print(sor.strip())  # .strip() levágja a sorvégi \n-t

# A HÁROM MÓD:
#   "r"  olvasás      (ha nincs ilyen fájl -> FileNotFoundError)
#   "w"  írás         (⚠️ LETÖRLI a régi tartalmat, kérdés nélkül!)
#   "a"  hozzáfűzés   (a végére ír, a régit meghagyja)
#
# ⚠️ Magyar ékezetekhez MINDIG kell: encoding="utf-8"
# ⚠️ Az f.write() NEM tesz sortörést - kézzel kell a "\n".
# ⚠️ .strip() nélkül minden sor végén ott marad a "\n", és a
#    sor == "alma" összehasonlítás hamis lesz. Néma, kegyetlen hiba.
#
# 💡 A "for sor in f:" memóriakímélő - 10 GB-os fájlon is működik,
#    míg az f.read() megpróbálná az egészet betölteni.


# --- 8.1 FELADAT ⭐ ------------------------------------------
# Írd ki a listát a "nevek.txt" fájlba, minden nevet külön sorba.
# Utána olvasd vissza és írd ki a képernyőre.

nevek_listaja = ["Anna", "Béla", "Cili"]

# TODO: ide írd a megoldást
with open("nevek.txt", "w", encoding="utf-8") as f:
    for nev in nevek_listaja:
        f.write(nev + "\n")
with open("nevek.txt", "r", encoding="utf-8") as f:
    for sor in f:
        print(sor.strip())

# --- 8.2 FELADAT ⭐ ------------------------------------------
# Olvasd be a "gyakorlas_adatok.txt" sorait EGY LISTÁBA,
# sorvégi \n nélkül, majd írd ki a listát és a hosszát.
#   ->  ['alma', 'körte', 'szilva', 'barack']   4

# TODO: ide írd a megoldást
nevek = []
with open("gyakorlas_adatok.txt", "r", encoding="utf-8") as f:
    for sor in f:
        nevek.append(sor.strip())

print(nevek)
print(len(nevek))


# --- 8.3 FELADAT ⭐⭐ -----------------------------------------
# Készíts egy naplo(uzenet) függvényt, ami HOZZÁFŰZI az üzenetet a
# "naplo.txt" fájl végéhez, új sorba.
# Hívd meg háromszor, majd írd ki, hány sor lett a fájlban.
# ⚠️ Ha "w" módot használsz, minden hívás letörli az előzőt!


# TODO: ide írd a megoldást
def naplo(uzenet):
    pass


# --- 8.4 FELADAT ⭐⭐ -----------------------------------------
# Írj egy szavak_szama(fajlnev) függvényt, ami visszaadja, hány SZÓ
# van a fájlban. Ha nincs ilyen fájl, adjon vissza 0-t
# (try / except FileNotFoundError).
# Próbáld ki a "gyakorlas_adatok.txt" és a "nincs_ilyen.txt" néven is.


# TODO: ide írd a megoldást
def szavak_szama(fajlnev):
    pass


# =============================================================
# 9) ÖSSZEFOGLALÓ FELADAT ⭐⭐⭐ - MÉRÉSI NAPLÓ FELDOLGOZÓ
# =============================================================
#
# Ez a feladat MIND A NYOLC témát használja. Ne siess vele, és ne
# próbáld egyben megírni! Írd meg az 1. lépést, FUTTASD. Aztán a
# 2.-at, FUTTASD. Így hét kis sikerélmény lesz belőle egy nagy
# kudarc helyett.
#
# A "meresek.txt" fájl már elkészült alattad, ez van benne:
#       12
#       8
#       alma
#       31
#       (üres sor)
#       19
#       0
#       25
#
# A FELADAT - írj egy feldolgoz(bemenet, kimenet) függvényt, ami:
#
#   1. beolvassa a fájlt soronként                    (fájlkezelés)
#   2. minden sort számmá próbál alakítani             (típuskonverzió)
#   3. a hibás sorokat kihagyja, de MEGSZÁMOLJA őket   (hibakezelés)
#   4. a jó számokat listába gyűjti                    (lista + ciklus)
#   5. kiszámolja: darabszám, összeg, átlag, maximum
#   6. minősítést ad az átlagra:                       (elágazás)
#          20 fölött  -> "magas"
#          10 - 20    -> "közepes"
#          10 alatt   -> "alacsony"
#   7. a jelentést f-stringgel formázza                (f-string)
#   8. a jelentést fájlba írja ÉS visszaadja szövegként
#
#   Ha egyetlen jó szám sincs, a jelentés legyen:
#       "Nincs használható mérés."
#
# A VÁRT KIMENET:
#       6 jó mérés, 2 hibás
#       összeg: 95 | átlag: 15.8 | maximum: 31
#       minősítés: közepes
#
# ⚠️ HÁROM PONT, AHOL EL SZOKÁS BUKNI:
#   1. A try az EGÉSZ ciklust öleli körbe -> az "alma" megöli a
#      többit is. A try csak az int() sorát fogja körbe!
#   2. Elmarad a .strip() -> az üres sor miatt kapsz meglepetést.
#   3. Nincs védelem az üres listára -> ZeroDivisionError.
#      Teszteld le egy csupa hibás sorból álló fájllal is!

# A bemeneti fájl elkészítése - ezt NEM kell módosítanod:
with open("meresek.txt", "w", encoding="utf-8") as f:
    f.write("12\n8\nalma\n31\n\n19\n0\n25\n")


# TODO: ide írd a megoldást
def feldolgoz(bemenet, kimenet):
    pass


# print(feldolgoz("meresek.txt", "jelentes.txt"))


# =============================================================
# AMIT MA GYAKOROLTUNK
# -------------------------------------------------------------
# int() / float() / str() -> típusváltás; int("3.9") HIBÁT DOB,
#                            int(9.99) LEVÁG, round(9.99) KEREKÍT
# lista.append/insert/remove -> hozzáad, beszúr, töröl
# lista[2:5]                 -> szeletelés, a vége ELŐTT megáll
# sorted(l) vs l.sort()      -> új listát ad / helyben rendez (None!)
# for + range                -> ha tudod, hányszor
# while                      -> ha csak azt tudod, mikor állj meg
# enumerate(l, start=1)      -> ha a sorszám is kell
# if / elif / else           -> az első igaz ág nyer, a SORREND számít
# try / except HibaNév       -> védőháló, csak a kockázatos sor köré
# input()                    -> MINDIG szöveget ad, váltsd át azonnal
# f"{ar:,.2f}"               -> ezres tagolás + 2 tizedes
# def ... return             -> a return ODAADJA, a print csak kimondja
# with open(..., "utf-8")    -> a fájl mindig bezáródik
# "w" töröl, "a" hozzáfűz    -> naplózáshoz mindig "a"
# .strip()                   -> levágja a sorvégi \n-t
# =============================================================
