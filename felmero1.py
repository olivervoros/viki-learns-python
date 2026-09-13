# =========================================================================
#  PYTHON FELMÉRŐ 2 / 1. RÉSZ  -  DIÁK VÁLTOZAT
#  Típusok • Függvények • Elágazások • Ciklusok
#
#  kb. 40 perc   •   12 feladat   •   24 pont
# =========================================================================
#
#  Témakör                               Feladat     Pont
#  -------------------------------------------------------
#  A  Típusok és típuskonverzió          1-3          6
#  B  Függvény definiálás                4-6          6
#  C  Elágazások                         7-9          6
#  D  Ciklusok                           10-12        6
#  -------------------------------------------------------
#                                        összesen    24
#
#  ⭐ = 1 pont     ⭐⭐ = 2 pont     ⭐⭐⭐ = 3 pont
#
#  Folytatás:  felmero_02b.py  (2. rész, 13-22. feladat)
#
#  HOGYAN HASZNÁLD
#  ---------------
#  • Haladj sorban, felülről lefelé. Minden témakör egy rövid
#    EMLÉKEZTETŐ-vel indul: olvasd el, futtasd le, és csak utána
#    kezdj a feladatokba.
#  • A megoldásod a  # TODO: ide írd a megoldást  sor alá kerül.
#    A  pass  sort ilyenkor töröld ki.
#  • A fájl már most is hiba nélkül lefut. Ahol még nincs megoldás,
#    ott None jelenik meg - ez teljesen rendben van. A  # várt:
#    megjegyzés mutatja, mit kell látnod, ha jó a megoldásod.
#  • A 💡 tipp segítség. Nyugodtan megnézheted, csak a pontozásnál
#    légy őszinte (a szabályt a fájl végén találod).
#
#  Egy hibás megoldás, amit tényleg lefuttattál, többet ér egy jónál,
#  amit csak fejben raktál össze.
#
#  Python 3.8 vagy újabb kell hozzá.
# =========================================================================


# =========================================================================
# A) TÍPUSOK ÉS TÍPUSKONVERZIÓ                                      6 pont
# =========================================================================
#
# 📌 EMLÉKEZTETŐ
# ---------------
# Van a zsebedben egy cetli, amire az van írva: "5". És van öt darab
# százforintosod. Ránézésre mindkettő "öt" - de a cetliket csak egymás
# mellé tudod ragasztani, a pénzt viszont össze tudod adni.
#
# Ez a típus: nem az számít, hogyan NÉZ KI egy érték, hanem hogy MI.
#
#     str     szöveg            "5"    "alma"   ""
#     int     egész szám         5     -12      0
#     float   tört szám          3.14   0.5     2.0
#     bool    igaz / hamis       True   False
#
# Átváltás:   int("42")    float("3.5")    str(42)    bool(...)
#
# ⚠️ Az input() MINDIG szöveget ad - akkor is, ha a felhasználó számot
#    gépel be. Számolás előtt tehát át kell váltani.

print("\n--- A) emlékeztető ---")
print(type("5"), type(5), type(5.0), type(True))
print("5" + "3", "<- két szöveg egymás mellé ragasztva")
print(5 + 3, "<- két szám összeadva")
print(int("42") + 1, "<- szövegből szám lett")
print(str(42) + "!", "<- számból szöveg lett")


# -------------------------------------------------------------------------
# 1. ⭐  Jósold meg a kimenetet!                                  (1 pont)
# -------------------------------------------------------------------------
# NE futtasd le rögtön! Minden sor mögé írd oda a tippedet, utána vedd
# ki a # jelet a sorok elejéről, és futtasd le.
#
print("7" + "3")                       # tipp: 73
print(int("7") + int("3"))             # tipp: 10
print("ha" * 3)                        # tipp: hahaha
print(int(3.99))                       # tipp: 3
print(float("2") + 1)                  # tipp: 3.0
print(bool(""), bool("0"), bool(0))    # tipp: False True False
#
# Legalább két sor szinte mindenkit meglep. Melyik kettő, és miért?
#
# 💡 Tipp: A bool() csak annyit kérdez: "üres-e a doboz?" - azt nem
#    nézi, mi van beleírva.

# TODO: ide írd a megoldást (melyik két sor lepett meg, és miért)
#print(int(3.99)) → 3, mert az int() nem kerekít, csak levágja a tizedesrészt.
#Azért meglepő ez a sor, mert a bool() nem azt nézi, hogy mi van a szövegben, hanem azt, hogy üres-e. A "" üres, ezért False, viszont a "0" nem üres, ezért True. A 0 viszont számként False érték.
# -------------------------------------------------------------------------
# 2. ⭐⭐  Ami az input()-ból jön, az szöveg                        (2 pont)
# -------------------------------------------------------------------------
# Ez a két változó úgy viselkedik, mintha a felhasználó írta volna be.
# (Az "élő" változat mögöttük, megjegyzésben.)

kor_szoveg = "17"  # kor_szoveg = input("Hány éves vagy? ")
magassag_szoveg = "1.75"  # magassag_szoveg = input("Milyen magas vagy (m)? ")

# Írasd ki ezt a mondatot - a számokat a két változóból számold ki:
#
#     Jövőre 18 éves leszel, és 175 cm magas vagy.
#
# 💡 Tipp: Előbb válts: a korhoz int(), a magassághoz float() kell.
#    Méterből centi: szorozd meg 100-zal. A round() eltünteti a
#    felesleges ".0"-t a végéről.

print("\n--- 2. feladat ---")
# TODO: ide írd a megoldást
kor = int(kor_szoveg)
magassag = float(magassag_szoveg)

print(f"Jövőre {kor + 1} éves leszel, és {round(magassag * 100)} cm magas vagy.")

# -------------------------------------------------------------------------
# 3. ⭐⭐⭐  A kávézó kasszája                                      (3 pont)
# -------------------------------------------------------------------------

termek = "kávé"
ar = "1290"  # egy webes űrlapról jött, ezért szöveg
darab = 3  # ez már szám
kedvezmeny = "0.1"  # 10% - ez is szöveg

# a) Írasd ki mind a négy változó típusát.
# b) Számold ki a fizetendő összeget (ár x darab, 10% kedvezménnyel),
#    és írasd ki így:
#
#        3 db kávé: 3483 Ft
#
# c) Válaszolj megjegyzésben: az  ar * darab  NEM ad hibát, hanem egy
#    furcsa eredményt. Mit ad, és miért? Az  ar * kedvezmeny  viszont
#    hibát dob. Mi a különbség?
#
# ⚠️ A c) rész a veszélyesebb: ami nem omlik össze, csak csendben
#    rossz eredményt ad, azt sokáig senki nem veszi észre.
#
# 💡 Tipp: szöveg * egész szám = a szöveg többször egymás után.
#    Kedvezménnyel a fizetendő:  ár x darab x (1 - kedvezmény).

print("\n--- 3. feladat ---")
# TODO: ide írd a megoldást

print(type(termek))
print(type(ar))
print(type(darab))
print(type(kedvezmeny))


ar = int(ar)
kedvezmeny = float(kedvezmeny)

fizetendo = ar * darab * (1 - kedvezmeny)

print(f"{darab} db {termek}: {round(fizetendo)} Ft")


# ar * darab eredménye: "129012901290", mert az ar szöveg,
# a darab pedig egész szám, ezért a szöveget háromszor megismétli.
#
# ar * kedvezmeny viszont hibát ad, mert szöveget nem lehet
# tizedes számmal megszorozni.


# =========================================================================
# B) FÜGGVÉNY DEFINIÁLÁS                                            6 pont
# =========================================================================
#
# 📌 EMLÉKEZTETŐ
# ---------------
# A függvény olyan, mint egy kávéautomata. Egyszer megépíted (def),
# utána akárhányszor használhatod (hívás). Bedobod a hozzávalókat
# (paraméterek), és kijön a kávé (return).
#
# ⚠️ A print és a return NEM ugyanaz!
#    print  = az automata kiteszi a kávét a kirakatba: látod, de nem
#             kapod meg.
#    return = a kezedbe adja: elviheted, számolhatsz vele, továbbadhatod.
#    Ha egy függvényben nincs return, a kezedbe None kerül.
#
# Egy paraméternek adhatsz alapértelmezett értéket (nev="idegen") -
# ha a hívó nem mond mást, azt használja.

print("\n--- B) emlékeztető ---")


def udvozol(nev="idegen"):
    return f"Szia, {nev}!"


print(udvozol("Anna"))
print(udvozol())


def min_max(szamok):
    return min(szamok), max(szamok)  # egyszerre két értéket ad vissza


legkisebb, legnagyobb = min_max([4, 9, 2])
print("legkisebb:", legkisebb, " legnagyobb:", legnagyobb)


# -------------------------------------------------------------------------
# 4. ⭐  Négyzet                                                  (1 pont)
# -------------------------------------------------------------------------
# Írj egy  negyzet(szam)  függvényt, amely VISSZAADJA (return!) a szám
# négyzetét.

print("\n--- 4. feladat ---")


def negyzet(szam):
    # TODO: ide írd a megoldást
    return szam ** 2





print("negyzet(4)  ->", negyzet(4))  # várt: 16
print("negyzet(-3) ->", negyzet(-3))  # várt: 9


# -------------------------------------------------------------------------
# 5. ⭐⭐  Téglalap - két eredmény egyszerre                        (2 pont)
# -------------------------------------------------------------------------
# Írj egy  teglalap(a, b)  függvényt, amely a téglalap területét ÉS
# kerületét is visszaadja. Aztán bontsd ki az eredményt két változóba,
# és írasd ki így:
#
#     Terület: 12, kerület: 14
#
# 💡 Tipp: Nézd meg a min_max függvényt fent. Kerület = 2 x (a + b).

print("\n--- 5. feladat ---")


def teglalap(a, b):
    # TODO: ide írd a megoldást
    terulet = a * b
    kerulet = 2 * (a + b)
    return terulet, kerulet

terulet, kerulet = teglalap(3, 4)
print("teglalap(3, 4) ->", teglalap(3, 4))  # várt: (12, 14)

# TODO: ide írd a kibontást és a kiírást
print("Terület:", terulet, "kerület:", kerulet)
# -------------------------------------------------------------------------
# 6. ⭐⭐⭐  Hová tűnt a bruttó ár?                                 (3 pont)
# -------------------------------------------------------------------------
# Valaki ezt írta. Futtasd le, és nézd meg, mit kapsz:

print("\n--- 6. feladat ---")


def ar_afaval(netto):
    print(netto * 1.27)


brutto = ar_afaval(1000)
print("brutto =", brutto)

# a) Megjegyzésben: miért None a brutto, ha fölötte kiírta az 1270-et?
# b) Írd meg jól:  ar_afaval_javitott(netto, afa=0.27)
#    - VISSZAADJA a bruttó árat, egész számra kerekítve
#    - az áfakulcs alapból 27%, de meg lehet adni mást is
# c) Megjegyzésben: miért működik az utolsó próbasor, pedig a két
#    érték "fordított" sorrendben van?
#
# 💡 Tipp: bruttó = nettó x (1 + áfa). A kerekítés: round(...).

# TODO: ide írd az a) választ


def ar_afaval_javitott(netto, afa=0.27):
    # TODO: ide írd a megoldást
    pass


print(ar_afaval_javitott(1000))  # várt: 1270
print(ar_afaval_javitott(1000, 0.05))  # várt: 1050
print(ar_afaval_javitott(afa=0.18, netto=500))  # várt: 590

# TODO: ide írd a c) választ


# =========================================================================
# C) ELÁGAZÁSOK                                                     6 pont
# =========================================================================
#
# 📌 EMLÉKEZTETŐ
# ---------------
# Az if / elif / else egy folyosó, ajtókkal. Végigmész rajta, és az
# ELSŐ ajtón, amelyik kinyílik, bemész - a többit meg sem nézed.
# Az else a folyosó végén lévő ajtó: az mindig nyitva van.
#
# Két külön if viszont két külön folyosó: mindkettőn végigmész.
#
#     ==   egyenlő-e?          !=   nem egyenlő-e?
#     and  mindkettő igaz      or   legalább az egyik     not  megfordítja
#
# ⚠️  =  azt jelenti: "tedd a dobozba".  ==  azt: "egyformák?"

print("\n--- C) emlékeztető ---")
homerseklet = 24

if homerseklet > 30:
    print("Kánikula")
elif homerseklet > 20:
    print("Kellemes")
else:
    print("Hűvös")

print(18 <= homerseklet <= 26, "<- a 'matekos' alakot is ismeri a Python")


# -------------------------------------------------------------------------
# 7. ⭐  Páros vagy páratlan                                      (1 pont)
# -------------------------------------------------------------------------
# Írj egy  paros_vagy_paratlan(n)  függvényt, amely a "páros" vagy a
# "páratlan" szót adja vissza.
#
# 💡 Tipp: A % a maradékot adja. Ami 2-vel osztva 0 maradékot ad, az páros.

print("\n--- 7. feladat ---")


def paros_vagy_paratlan(n):
    # TODO: ide írd a megoldást
    if n % 2 == 0:
        return "páros"
    else:
        return "páratlan"



print(4, "->", paros_vagy_paratlan(4))  # várt: páros
print(7, "->", paros_vagy_paratlan(7))  # várt: páratlan
print(0, "->", paros_vagy_paratlan(0))  # várt: páros


# -------------------------------------------------------------------------
# 8. ⭐⭐  Szállítási díj                                          (2 pont)
# -------------------------------------------------------------------------
# Egy webshop szállítási díja:
#
#     törzsvásárló             mindig 0 Ft
#     20 000 Ft-tól            0 Ft
#     10 000 - 19 999 Ft       990 Ft
#     10 000 Ft alatt          1990 Ft
#
# Írd meg:  szallitasi_dij(osszeg, torzsvasarlo=False)
#
# 💡 Tipp: A két "ingyenes" eset egyetlen if-be is belefér, ha or-ral
#    kötöd össze őket. És kezdd a legnagyobb határral!

print("\n--- 8. feladat ---")


def szallitasi_dij(osszeg, torzsvasarlo=False):
    # TODO: ide írd a megoldást
    if torzsvasarlo or osszeg >= 20000:
        return 0
    elif osszeg >= 10000:
        return 990
    else:
        return 1990


print(szallitasi_dij(25000))  # várt: 0
print(szallitasi_dij(15000))  # várt: 990
print(szallitasi_dij(10000))  # várt: 990
print(szallitasi_dij(5000))  # várt: 1990
print(szallitasi_dij(5000, True))  # várt: 0


# -------------------------------------------------------------------------
# 9. ⭐⭐⭐  A hibás jegyadó                                        (3 pont)
# -------------------------------------------------------------------------
# A ponthatárok:  0-49: 1   50-64: 2   65-74: 3   75-84: 4   85-100: 5
# Valaki ezt írta, és a 95 pontos diák 2-est kapott:

print("\n--- 9. feladat ---")


def jegy(pont):
    if pont >= 50:
        return 2
    elif pont >= 65:
        return 3
    elif pont >= 75:
        return 4
    elif pont >= 85:
        return 5
    else:
        return 1


print("jegy(95) ->", jegy(95), "  ...pedig ötösnek kellene lennie")

# a) Megjegyzésben: miért ad 95 pontra 2-est? (Gondolj a folyosóra!)
# b) Írd meg jól:  jegy_javitott(pont)
#    Plusz: ha a pont 0 alatt vagy 100 fölött van, adja vissza az
#    "érvénytelen" szót.
#
# 💡 Tipp: Az érvénytelen esetet vizsgáld ELŐSZÖR. Utána a jegyeket
#    fentről lefelé: az 5-össel kezdd.

# TODO: ide írd az a) választ


def jegy_javitott(pont):
    # TODO: ide írd a megoldást
    if pont < 0 or pont > 100:
        return "érvénytelen"
    elif pont >= 85:
        return 5
    elif pont >= 75:
        return 4
    elif pont >= 65:
        return 3
    elif pont >= 50:
        return 2
    else:
        return 1


for p in [95, 85, 84, 70, 50, 49, 101, -5]:
    print(p, "->", jegy_javitott(p))
# várt: 5, 5, 4, 3, 2, 1, érvénytelen, érvénytelen


# =========================================================================
# D) CIKLUSOK                                                       6 pont
# =========================================================================
#
# 📌 EMLÉKEZTETŐ
# ---------------
# for   = "tudom, hányszor". Mint a lépcső: tudod, hány foka van,
#         és végigmész rajta.
# while = "addig, amíg". Mint a leves: addig kanalazol, amíg van a
#         tányérban. Ha a tányér sosem ürül ki, sosem állsz fel.
#
# A VÖDÖR minta: a ciklus ELŐTT fogsz egy üres vödröt, minden körben
# beleteszel valamit, és a ciklus UTÁN belenézel.
#
#     break      = azonnal kiszállsz a ciklusból
#     continue   = ezt a kört kihagyod, jön a következő
#
# ⚠️ range(1, 11) -> 1, 2, ..., 10. A második szám előtt MEGÁLL.

print("\n--- D) emlékeztető ---")
osszeg = 0  # az üres vödör
for i in range(1, 6):
    osszeg += i  # ugyanaz, mint: osszeg = osszeg + i
print("1+2+3+4+5 =", osszeg)

visszaszamlalo = 3
while visszaszamlalo > 0:
    print(visszaszamlalo, end=" ")
    visszaszamlalo -= 1  # e nélkül örökké futna!
print("Start!")


# -------------------------------------------------------------------------
# 10. ⭐  Szorzótábla és összeg                                    (1 pont)
# -------------------------------------------------------------------------
# a) Írasd ki a 7-es szorzótáblát:   7 x 1 = 7   ...   7 x 10 = 70
# b) Add össze a páros számokat 1-től 100-ig (a 100 is benne van!).
#    várt: 2550
#
# 💡 Tipp: A b)-hez a vödör minta kell, meg egy if a ciklusban.

print("\n--- 10. feladat ---")
# TODO: ide írd a megoldást

for i in range(1, 11):
    print("7 x", i, "=", 7 * i)
osszeg = 0
for i in range(1, 101):
    if i % 2 == 0:
        osszeg += i
print("A páros számok összege:", osszeg)

# -------------------------------------------------------------------------
# 11. ⭐⭐  Mikor lesz meg a pénz?                                  (2 pont)
# -------------------------------------------------------------------------
# Beteszel a bankba 100 000 Ft-ot, évi 5% kamatra. Hány év alatt nő
# legalább 150 000 Ft-ra? Írasd ki így:
#
#     9 év után: 155133 Ft
#
# Itt nem tudod előre, hányszor kell körbemenni - ezért while kell.
#
# ⚠️ Ha a ciklusban elfelejted növelni az egyenleget, a feltétel sosem
#    lesz hamis: végtelen ciklus. Ctrl+C állítja le.
#
# 💡 Tipp: Minden körben:  egyenleg = egyenleg * (1 + kamat),  és az
#    évek száma nő eggyel.

egyenleg = 100000  # Ft
kamat = 0.05  # évi 5%
cel = 150000  # Ft

print("\n--- 11. feladat ---")
# TODO: ide írd a megoldást
ev = 0

while egyenleg < cel:
    egyenleg = egyenleg * (1 + kamat)
    ev += 1
print(ev, "év után:", round(egyenleg), "Ft")


# -------------------------------------------------------------------------
# 12. ⭐⭐⭐  break és continue                                      (3 pont)
# -------------------------------------------------------------------------

szamok = [12, 45, 7, 63, 88, 91, 20]

# a) Keresd meg az ELSŐ olyan számot, amely nagyobb 50-nél ÉS osztható
#    7-tel. Amint megvan, a ciklus álljon meg (break). Ha nincs ilyen,
#    írd ki: "Nincs ilyen szám."            várt: 63
# b) Add össze csak a páros számokat úgy, hogy a páratlanokat
#    continue-val ugrod át.                  várt: 120
#
# 💡 Tipp: Az a)-hoz a ciklus előtt tegyél egy  talalat = None  sort.
#    Ha a ciklus után még mindig None, akkor nem volt találat.
#    Figyelem: a 91 is jó lenne - de nem ő az ELSŐ.

print("\n--- 12. feladat ---")
# TODO: ide írd a megoldást
pass


# =========================================================================
# AMIT MA GYAKOROLTUNK
# =========================================================================
#
#  • A típus azt mondja meg, MI egy érték, nem azt, hogyan néz ki.
#    "5" + "3" = "53",  5 + 3 = 8.  Az input() mindig szöveget ad.
#  • A függvény egy kávéautomata: def-fel építed, és a return adja a
#    kezedbe az eredményt. A print csak megmutatja.
#  • Az if / elif / else egy folyosó: az első nyitott ajtón mész be,
#    ezért a sorrend számít.
#  • for = tudom, hányszor.  while = addig, amíg.  Vödör minta,
#    break, continue.
#
#  Következik a 2. rész (felmero_02b.py): függvény manipuláció,
#  hibakezelés, listák és a záró feladat.
#
# PONTOZÁS - légy magadhoz őszinte
# ---------------------------------
#    teljes pont   működik, és nem néztél tippet
#    a pont fele   működik, de kellett hozzá a 💡 tipp
#    0 pont        nem sikerült (még)
#
# A végösszegnél fontosabb, HOL vesztettél pontot. Amelyik betűnél a
# legtöbbet, az a következő gyakorlás témája.
# =========================================================================
