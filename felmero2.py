# =========================================================================
#  PYTHON FELMÉRŐ 2 / 2. RÉSZ  -  DIÁK VÁLTOZAT
#  Függvény manipuláció • Hibakezelés • Listák • Záró feladat
#
#  kb. 50 perc   •   10 feladat   •   26 pont
# =========================================================================
#
#  Témakör                               Feladat     Pont
#  -------------------------------------------------------
#  E  Függvény manipuláció               13-15        6
#  F  Hibakezelés                        16-18        6
#  G  Listák és manipulációjuk           19-21        6
#  Z  Záró feladat - minden együtt       22           8
#  -------------------------------------------------------
#                                        összesen    26
#
#  ⭐ = 1 pont     ⭐⭐ = 2 pont     ⭐⭐⭐ = 3 pont     (a záró feladat 8)
#
#  Előzmény:  felmero_02a.py  (1. rész, 1-12. feladat). A feladatok
#  számozása onnan folytatódik. A záró feladathoz az 1. rész témái
#  (típusok, függvények, elágazások, ciklusok) is kellenek.
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
# E) FÜGGVÉNY MANIPULÁCIÓ                                           6 pont
# =========================================================================
#
# 📌 EMLÉKEZTETŐ
# ---------------
# A függvény is csak egy érték - olyan, mint egy szerszám. Elteheted
# a fiókba (változóba), odaadhatod valakinek (paraméterként), és ő
# majd használja.
#
#     kalapacs      = maga a szerszám (nem csinál semmit)
#     kalapacs()    = HASZNÁLOD a szerszámot (lefut)
#
# lambda = eldobható mini-függvény, egy sorban. Mint a papírpohár:
#          gyors, egyszeri használatra jó. Ami bonyolultabb, annak
#          rendes def jár.
#
#     lambda x: x * 2      ugyanaz, mint      def f(x): return x * 2
#
# Beépített eszközök, amelyek függvényt várnak:
#     sorted(lista, key=fv)   a fv eredménye szerint rendez
#     map(fv, lista)          minden elemre alkalmazza a fv-t
#     filter(fv, lista)       csak azokat tartja meg, ahol a fv True
#
# ⚠️ A map és a filter nem listát ad, hanem egy "ígéretet". Tedd
#    list()-be, hogy lásd a tartalmát.

print("\n--- E) emlékeztető ---")
kiabal = str.upper  # nincs zárójel: a szerszámot tesszük el
print(kiabal("hahó"))


def ketszer(fv, ertek):  # függvényt kap paraméterként
    return fv(fv(ertek))


print(ketszer(lambda x: x + 10, 5))  # 5 -> 15 -> 25

szavak = ["alma", "kiwi", "banán", "fű"]
print(sorted(szavak, key=len))
print(list(map(len, szavak)))
print(list(filter(lambda s: len(s) > 3, szavak)))


# -------------------------------------------------------------------------
# 13. ⭐  Első lambdám                                            (1 pont)
# -------------------------------------------------------------------------


def duplaz_regi(x):
    return x * 2


# a) Írd át a fenti függvényt egyetlen lambdára, és tedd a  duplaz
#    nevű változóba.
# b) A map segítségével dupláztasd meg a [3, 5, 8] lista minden elemét.
#
# Ha kész vagy, vedd ki a # jelet a két próbasor elől.

print("\n--- 13. feladat ---")
# TODO: ide írd a megoldást
duplaz = lambda x: x * 2
print(duplaz(7))
print(list(map(duplaz, [3, 5, 8])))
# print(duplaz(7))                       # várt: 14
# print(list(map(duplaz, [3, 5, 8])))    # várt: [6, 10, 16]


# -------------------------------------------------------------------------
# 14. ⭐⭐  Rendezés, szűrés, átalakítás                            (2 pont)
# -------------------------------------------------------------------------

diakok = [("Anna", 87), ("Bence", 92), ("Cili", 78), ("Dávid", 92), ("Emese", 65)]

# a) Rendezd pontszám szerint CSÖKKENŐ sorrendbe (sorted + key + lambda).
# b) A filter-rel tartsd meg csak a legalább 80 pontosokat.
# c) A map-pel készíts egy listát, amelyben csak a nevek vannak.
#
# 💡 Tipp: Minden elem egy (név, pont) pár. Ha a lambda d-nek hívja,
#    akkor d[0] a név, d[1] a pont. Csökkenő sorrend: reverse=True.

print("\n--- 14. feladat ---")
# TODO: ide írd a megoldást (a None helyére)
rendezett = None
jok = None
nevek = None

print(rendezett)
# várt: [('Bence', 92), ('Dávid', 92), ('Anna', 87), ('Cili', 78), ('Emese', 65)]
print(jok)
# várt: [('Anna', 87), ('Bence', 92), ('Dávid', 92)]
print(nevek)
# várt: ['Anna', 'Bence', 'Cili', 'Dávid', 'Emese']


# -------------------------------------------------------------------------
# 15. ⭐⭐⭐  A saját map-em                                          (3 pont)
# -------------------------------------------------------------------------
# a) Írd meg:  alkalmaz(fv, lista)  - egy ÚJ listát ad vissza, amelyben
#    a lista minden elemére lefuttattad az fv-t.
#    A beépített map-et NEM használhatod: ciklussal csináld!
# b) A próbasorok három különböző függvényt adnak neki: abs, str és
#    egy lambda. Nézd meg, mindhárommal működik-e.
# c) Megjegyzésben: mi a különbség e két hívás között, és melyik ad
#    hibát? Miért?
#
#        alkalmaz(abs, [-3, 2, -1])
#        alkalmaz(abs(), [-3, 2, -1])
#
# 💡 Tipp: A függvény belseje a vödör minta. Az fv-t ugyanúgy hívod,
#    mint bármelyik függvényt:  fv(elem)

print("\n--- 15. feladat ---")


def alkalmaz(fv, lista):
    # TODO: ide írd a megoldást
    eredmeny = []

    for elem in lista:
        eredmeny.append(fv(elem))

    return eredmeny
print(alkalmaz(abs, [-3, 2, -1]))  # várt: [3, 2, 1]
print(alkalmaz(str, [1, 2, 3]))  # várt: ['1', '2', '3']
print(alkalmaz(lambda x: x**2, [1, 2, 3]))  # várt: [1, 4, 9]

# TODO: ide írd a c) választ
alkalmaz(abs, [-3, 2, -1])

# =========================================================================
# F) HIBAKEZELÉS                                                    6 pont
# =========================================================================
#
# 📌 EMLÉKEZTETŐ
# ---------------
# A try/except olyan, mint a háló a trapéz alatt. Nem akadályozza meg,
# hogy leess - de az előadás nem ér véget miatta.
#
#     try:
#         kockázatos lépés
#     except HibaNeve:
#         mit tegyünk helyette
#
# ⚠️ Mindig NEVEZD MEG a hibát, amire számítasz. A csupasz  except:
#    mindent elkap - a saját elírásaidat is -, és elrejti előled, mi
#    romlott el.
#
# raise-zel TE is jelezhetsz hibát, ha valami nem stimmel:
#     raise ValueError("Ez így nem jó")
#
# Gyakori hibák:  ValueError   TypeError   ZeroDivisionError
#                 IndexError   KeyError

print("\n--- F) emlékeztető ---")
try:
    szam = int("tizenkettő")
except ValueError as e:
    print("Nem sikerült:", e)

print("A program megy tovább.")


# -------------------------------------------------------------------------
# 16. ⭐  Merre megy a program?                                    (1 pont)
# -------------------------------------------------------------------------
# a) Mit ír ki ez a kód? Írd le a tippedet, CSAK UTÁNA vedd ki a
#    # jeleket és futtasd.
#
# try:
#     print("A")
#     x = int("12a")
#     print("B")
# except ValueError:
#     print("C")
# print("D")
#
# b) Milyen hibát dob ez a két sor?
#        "kor: " + 25
#        [1, 2, 3][5]
#
# 💡 Tipp: Ha a try-ban hiba történik, a maradék try-sorok kimaradnak,
#    és a program egyenesen az except-hez ugrik.

# TODO: ide írd a tippjeidet
# a) A, C, D
# Azért, mert az int("12a") ValueError hibát okoz,
# ezért a "B" már nem íródik ki, hanem az except következik.

# b)
# "kor: " + 25 : TypeError
# [1, 2, 3][5] :IndexError


# -------------------------------------------------------------------------
# 17. ⭐⭐  Biztonságos osztás                                      (2 pont)
# -------------------------------------------------------------------------
# Írd meg:  biztonsagos_osztas(a, b)
#   - ha minden rendben, visszaadja a / b-t
#   - nullával osztásnál kiírja: "Nullával nem lehet osztani."
#     és None-t ad vissza
#   - ha valamelyik érték szöveg, kiírja: "Csak számokkal tudok osztani."
#     és None-t ad vissza
#
# 💡 Tipp: Egy try alatt több except ág is állhat, egymás alatt.
#    Melyik hiba jön, ha 5-öt osztasz "2"-vel? Próbáld ki!

print("\n--- 17. feladat ---")


def biztonsagos_osztas(a, b):
    # TODO: ide írd a megoldást
try:
        return a / b
except ZeroDivisionError:
        print("Nullával nem lehet osztani.")
        return None
except TypeError:
        print("Csak számokkal tudok osztani.")
        return None
print("(10, 4)  ->", biztonsagos_osztas(10, 4))  # várt: 2.5
print("(1, 0)   ->", biztonsagos_osztas(1, 0))  # várt: üzenet, aztán None
print("(5, '2') ->", biztonsagos_osztas(5, "2"))  # várt: üzenet, aztán None


# -------------------------------------------------------------------------
# 18. ⭐⭐⭐  Te dobod a hibát: raise                                 (3 pont)
# -------------------------------------------------------------------------
# a) Írd meg:  kor_ellenoriz(szoveg)
#    - a szöveget egész számmá alakítja, és visszaadja
#    - ha nem szám, az int() magától ValueError-t dob - ezt hagyd!
#    - ha a kor 0 alatt vagy 130 fölött van, dobj te egy
#      ValueError-t ezzel az üzenettel:  Irreális kor: <a szám>
# b) Menj végig a probak listán, és mindegyikre írd ki, rendben van-e.
#    A hibát try/except fogja el - a függvényen KÍVÜL.
#
# Várt kimenet:
#     25 - rendben
#     'abc' - hiba: invalid literal for int() with base 10: 'abc'
#     '-5' - hiba: Irreális kor: -5
#     '200' - hiba: Irreális kor: 200
#     42 - rendben
#
# 💡 Tipp: A hibaüzenetet így kapod meg:  except ValueError as e:
#    és utána  print(e).  A raise után a függvény azonnal kilép.

print("\n--- 18. feladat ---")


def kor_ellenoriz(szoveg):
    # TODO: ide írd a megoldást
    pass


probak = ["25", "abc", "-5", "200", "42"]

# TODO: ide írd a b) részt (ciklus + try/except)
pass


# =========================================================================
# G) LISTÁK ÉS MANIPULÁCIÓJUK                                       6 pont
# =========================================================================
#
# 📌 EMLÉKEZTETŐ
# ---------------
# A lista egy vonat: a kocsik sorban követik egymást, és mindegyiknek
# van sorszáma - de a számozás 0-tól indul! A mozdony utáni első kocsi
# a 0-s. Hátulról is számolhatsz: a -1 az utolsó kocsi.
#
# Két család - ezt érdemes fejben tartani:
#
#   HELYBEN MÓDOSÍT, None-t ad vissza:   append  insert  remove  sort  reverse
#   ÚJAT AD, az eredetit békén hagyja:   sorted()  lista[a:b]  len()  sum()
#   A pop a kivétel: módosít, ÉS visszaadja a kivett elemet.
#
# Szeletelés:  lista[eleje:vége]  - a vége már NEM kerül bele,
#              ugyanúgy, mint a range-nél.
#
# ⚠️  lista = lista.sort()   -> a listád None lesz. Soha ne így!

print("\n--- G) emlékeztető ---")
gyumolcsok = ["alma", "körte", "szilva"]
gyumolcsok.append("barack")
print(gyumolcsok, len(gyumolcsok))
print(gyumolcsok[0], gyumolcsok[-1], gyumolcsok[1:3])
print(sorted(gyumolcsok, reverse=True), "<- új lista")
print(gyumolcsok, "<- az eredeti nem változott")


# -------------------------------------------------------------------------
# 19. ⭐  Bevásárlólista                                          (1 pont)
# -------------------------------------------------------------------------

bevasarlas = ["tej", "kenyér", "tojás"]

# a) tedd a végére: "sajt"
# b) tedd a legelejére: "kávé"
# c) töröld: "kenyér"
# d) vedd ki pop-pal az utolsó elemet, és írasd ki, MIT vettél ki
# e) írasd ki a listát és a hosszát
#
# várt:   Kivettem: sajt
#         ['kávé', 'tej', 'tojás'] 3

print("\n--- 19. feladat ---")
# TODO: ide írd a megoldást
pass


# -------------------------------------------------------------------------
# 20. ⭐⭐  Szeletelés                                              (2 pont)
# -------------------------------------------------------------------------

honapok = [
    "jan",
    "feb",
    "már",
    "ápr",
    "máj",
    "jún",
    "júl",
    "aug",
    "szep",
    "okt",
    "nov",
    "dec",
]

# Mindegyiknél ELŐBB írd le a tippedet egy megjegyzésbe, aztán futtasd:
#   a) az első hónap
#   b) az utolsó hónap - a 11-es szám használata NÉLKÜL
#   c) az első negyedév (az első három hónap)
#   d) a nyári hónapok: jún, júl, aug
#   e) minden második hónap januártól: jan, már, máj, ...
#   f) a hónapok visszafelé - úgy, hogy az eredeti lista NE változzon
#
# 💡 Tipp:  [::2] = "minden második",  [::-1] = "visszafelé".
#    A jún az 5-ös indexen van (jan = 0).

print("\n--- 20. feladat ---")
# TODO: ide írd a megoldást
pass


# -------------------------------------------------------------------------
# 21. ⭐⭐⭐  A takarítás, ami félrement                             (3 pont)
# -------------------------------------------------------------------------
# Valaki ki akarta törölni az összes egyest a jegyek közül:

print("\n--- 21. feladat ---")
jegyek = [5, 1, 1, 4, 1, 5, 2, 1]
for j in jegyek:
    if j == 1:
        jegyek.remove(j)
print("A 'kitakarított' lista:", jegyek, "  ...tényleg nincs benne egyes?")

# a) Megjegyzésben: mi romlott el, és miért maradt benne egyes?
# b) Csináld jól: a lenti  eredeti  listából építs egy ÚJ listát, amely
#    minden jegyet tartalmaz, kivéve az egyeseket.
#    várt: [5, 4, 5, 2]
# c) Az új listából: az átlag 2 tizedesre (várt: 4.0) és az ötösök
#    száma (várt: 2). Az eredetiből: hány egyes volt (várt: 4).
#
# 💡 Tipp: Ne a listát töröld, amin épp végigmész - építs mellé egy
#    újat a vödör mintával. Megszámoláshoz:  lista.count(ertek)

eredeti = [5, 1, 1, 4, 1, 5, 2, 1]

# TODO: ide írd az a) választ
bevasarlas.append("sajt")
# TODO: ide írd a b) és c) megoldását
bevasarlas.insert(0, "kávé")
bevasarlas.remove("kenyér")
kivettem = bevasarlas.pop()
print("Kivettem:", kivettem)
print(bevasarlas, len(bevasarlas))


# b) kávé a legelejére
bevasarlas.insert(0, "kávé")

# c) kenyér törlése
bevasarlas.remove("kenyér")

# d) utolsó elem kivétele
kivettem = bevasarlas.pop()
print("Kivettem:", kivettem)

# e) lista és hossza
print(bevasarlas, len(bevasarlas))