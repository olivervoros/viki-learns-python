def avg(numbers):
    sum = 0
    for a in numbers:
        sum += a
    avg = sum / len(numbers)
    print(avg)


avg([2, 5, 1])


a = 5
is_number = isinstance(a, (int, float))
print(is_number)  # TRUE


def avg(numbers):
    sum = 0
    for a in numbers:
        sum += a
    avg = sum / len(numbers)
    return avg


atlag = avg([2, 5, 1])
print(atlag)


def parity(x):
    if x % 2 == 0:
        return "páros"
    else:
        return "páratlan"
    print("Ez már nem fut le")


a = 5
print(f"A megadott szám {parity(a)}")


def paros_szamok(x):
    szamok = []
    for i in range(1, x + 1):
        if i % 2 == 0:
            szamok.append(i)
    return szamok


a = 20
print(paros_szamok(a))


def parity(x):
    if x % 2 == 0:
        return "páros"


a = 5
p = parity(a)
if p is None:
    print("Nem érkezett válasz")
else:
    print(f"A megadott szám {p}")


def parity(x):
    if x % 2 == 0:
        return "páros"


def display_result(p):
    if p is None:
        print("Nem érkezett válasz")
    else:
        print(f"A megadott szám {p}")


display_result(parity(5))
display_result(parity(6))


def factor(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factor(n - 1)


print(factor(5))

"""
=========================================================================
GYAKORLÓ FELADATOK  -  Palindróma, pangramma, harmonikus közép
=========================================================================

HOGYAN HASZNÁLD
---------------
  Olvasd el az EMLÉKEZTETŐ részt, futtasd le a példákat, és csak utána
  írd meg a feladatot a  # TODO  sor helyére. A  pass  szót töröld ki,
  amikor megírtad a saját kódodat.

  A fájl akkor is lefut, ha még egy feladatot sem oldottál meg. Ilyenkor
  a tesztsorok None-t írnak ki. Ez nem hiba, csak azt jelenti, hogy ott
  még vár rád a munka.

  Egy rossz megoldás, amit lefuttattál, többet ér egy jónál, amit csak
  végiggondoltál.
"""


# =========================================================================
# 1. TÉMA  -  SZÖVEG MEGFORDÍTÁSA ÉS TAKARÍTÁSA
# =========================================================================
#
# EMLÉKEZTETŐ
# -----------
#   A palindróma olyan, mint egy vonat, aminek mindkét végén mozdony van:
#   bármelyik oldalról nézed, ugyanazt látod.
#     "Géza, kék az ég"   "Indul a görög aludni"
#
#   Két eszköz kell hozzá:
#
#   1. MEGFORDÍTÁS - a szeletelés visszafelé is tud lépkedni:
#          szoveg[::-1]   "az elejétől a végéig, hátrafelé"
#
#   2. TAKARÍTÁS - a szóközök, vesszők és nagybetűk elrontják a tükörképet,
#      ezért előbb ki kell dobni őket:
#          .lower()      mindent kisbetűre
#          .isalnum()    True, ha a karakter betű vagy szám

print("alma"[::-1])  # amla
print([1, 2, 3][::-1])  # [3, 2, 1]
print("Kék!".lower())  # kék!
print("k".isalnum(), ",".isalnum())  # True False

# Takarítás egy lépésben, list comprehension-nel:
print([b for b in "Szia, Ö!" if b.isalnum()])  # ['S', 'z', 'i', 'a', 'Ö']

# ⚠️ Az isalnum() az ékezetes betűket (á, ö, ő, ű...) is betűnek tekinti,
#    így a magyar szövegekkel nincs gond.
#
# 💡 A takarítás sorrendje mindegy: előbb kisbetűsíthetsz, és utána
#    szűrhetsz, vagy fordítva.


# -------------------------------------------------------------------------
# 1. FELADAT  -  Palindróma                                              ⭐
# -------------------------------------------------------------------------
#   Készíts függvényt, amely egy adott bemenetről megállapítja, hogy
#   palindróma-e vagy sem! A szóközök, írásjelek és kis/nagybetűk ne
#   számítsanak.


def palindroma_e(szoveg):
    # TODO: ide írd a megoldást
    pass


print(palindroma_e("Géza, kék az ég"))  # várt: True
print(palindroma_e("Indul a görög aludni"))  # várt: True
print(palindroma_e("Python"))  # várt: False


# =========================================================================
# 2. TÉMA  -  HALMAZOK: "BENNE VAN-E?"
# =========================================================================
#
# EMLÉKEZTETŐ
# -----------
#   A pangramma olyan mondat, amelyben az ábécé MINDEN betűje szerepel.
#   Az ellenőrzése egy bingókártya: minden betű egy mező, és a mondat
#   minden betűjével áthúzol egyet. A végén minden mezőnek áthúzva kell
#   lennie.
#
#   Erre a HALMAZ a tökéletes eszköz, mert:
#     - egy elem csak egyszer lehet benne (a duplikátum eltűnik)
#     - nincs sorrendje
#     - a "benne van-e?" kérdésre villámgyorsan válaszol
#
#   Egy stringből egy lépésben halmaz lesz:  set("alma") -> {'a', 'l', 'm'}
#
#   A halmazok kivonása megmondja, mi MARADT ki:
#       {1, 2, 3} - {2}   ->  {1, 3}

kartya = set("abcde")
athuzva = set("bababa")
print(sorted(kartya - athuzva))  # ['c', 'd', 'e']  <- ezek hiányoznak még
print(set("aaaa"))  # {'a'}
print({"a", "b"} <= {"a", "b", "c"})  # True  <- részhalmaza-e?

# ⚠️ Üres halmaz: set()   NEM {}  -  a {} üres szótár!
#
# ⚠️ A halmaz érzékeny a kis- és nagybetűre: "Q" és "q" két különböző elem.


# -------------------------------------------------------------------------
# 2. FELADAT  -  Pangramma                                              ⭐⭐
# -------------------------------------------------------------------------
#   Készíts függvényt, amely egy adott bemenetről megállapítja, hogy
#   (magyar nyelvű) pangramma-e vagy sem!
#
#   Először sorold fel a magyar betűket a MAGYAR_BETUK változóban.
#   Ne felejtsd el az ékezeteseket, és a q, w, x, y is a magyar ábécé része!
#   (Egykarakteres betűkből 35 van. A kettős betűkkel, mint a "cs" vagy
#   az "sz", most nem kell foglalkoznod.)

MAGYAR_BETUK = set()  # TODO: töltsd ki a betűkkel


def pangramma_e(szoveg):
    # TODO: ide írd a megoldást
    pass


print(len(MAGYAR_BETUK))  # várt: 35
mondat = "Egy hűtlen vejét fülöncsípő, dühös mexikói úr Wesselényinél mázol Quitóban."
print(pangramma_e(mondat))  # várt: True
print(pangramma_e("Szia, Oliver!"))  # várt: False

# 💡 Ha nem True jön ki a híres mondatra, írasd ki, melyik betű hiányzik:
#        print(sorted(MAGYAR_BETUK - set(mondat.lower())))


# =========================================================================
# 3. TÉMA  -  ELLENŐRZÉS ÉS HIBÁK DOBÁSA
# =========================================================================
#
# EMLÉKEZTETŐ
# -----------
#   A hibakezelés olyan, mint egy portás a bejáratnál: mielőtt bárki
#   beléphet a számolásba, megnézi a papírjait. Aki nem felel meg, azt
#   egy érthető üzenettel visszaküldi.
#
#   Három eszköz kell hozzá:
#
#     isinstance(x, (int, float))   "szám-e x?"
#     raise ValueError("üzenet")    a portás visszaküld valakit
#     try / except                  a hívó elkapja a visszaküldést


def csak_pozitiv(x):
    if x <= 0:
        raise ValueError(f"Nem pozitív: {x}")
    return x


print(isinstance(5, (int, float)))  # True
print(isinstance("5", (int, float)))  # False

for probalkozas in [3, -1]:
    try:
        print(csak_pozitiv(probalkozas))
    except ValueError as hiba:
        print("hiba:", hiba)  # hiba: Nem pozitív: -1

# ⚠️ TypeError = rossz FAJTA dolog (szöveg szám helyett).
#    ValueError = jó fajta, de lehetetlen értékkel (például negatív szám).
#
# ⚠️ Pythonban a True valójában az 1 szám: isinstance(True, int) -> True.
#    Ha ezt ki akarod szűrni, külön kell ellenőrizned.


# -------------------------------------------------------------------------
# 3. FELADAT  -  Harmonikus közép                                      ⭐⭐⭐
# -------------------------------------------------------------------------
#   Elmész a Balatonra 60 km/h-val, és hazajössz 40 km/h-val. Az
#   átlagsebességed nem 50, hanem 48, mert a lassú úton több időt
#   töltöttél. Ezt számolja ki a harmonikus közép:
#
#       darabszám / (1/x1 + 1/x2 + ... + 1/xn)
#
#   Készíts függvényt, amely egy lista bemenetből kiszámolja a megadott
#   számok harmonikus közepét! Kezeld a potenciális hibás bemeneteket is!
#
#   Gondold végig, mi romolhat el. Legalább ezekre dobj érthető hibát:
#     - a bemenet nem lista
#     - a lista üres
#     - van benne valami, ami nem szám
#     - van benne nulla vagy negatív szám


def harmonikus_kozep(szamok):
    # TODO: ide írd a megoldást
    pass


for bemenet in [[60, 40], [1, 2, 4], [], [3, 0], [2, "alma"], "hello"]:
    try:
        print(bemenet, "->", harmonikus_kozep(bemenet))
    except (TypeError, ValueError) as hiba:
        print(bemenet, "-> hiba:", hiba)

# várt kimenet (az üzenetek szövege lehet más):
#   [60, 40] -> 48.0
#   [1, 2, 4] -> 1.7142857142857142
#   [] -> hiba: ...
#   [3, 0] -> hiba: ...
#   [2, 'alma'] -> hiba: ...
#   hello -> hiba: ...
#
# 💡 Az összeg egy sorban is megvan:  sum(1 / x for x in szamok)
#
# ⚠️ Ne a sima átlagot számold! (60 + 40) / 2 = 50, ami itt rossz válasz.


# =========================================================================
# 4. FELADAT  -  ÖSSZEFOGLALÓ: SZÖVEGELEMZŐ                            ⭐⭐⭐
# =========================================================================
#   Írj egy  elemzes(mondatok)  függvényt, amely egy mondatokból álló
#   listán végigmegy, és mindegyikről kiír egy sort:
#
#     - palindróma-e (1. feladat)
#     - pangramma-e (2. feladat)
#     - a mondat szavai hosszának harmonikus közepe, 2 tizedesre
#       kerekítve (3. feladat)
#
#   Ha egy mondat üres, a harmonikus közép hibát dob. Ezt kapd el, és
#   írd ki helyette, hogy "nincs szó". A program ne álljon le!
#
#   Minta:
#     'Géza, kék az ég' -> palindróma: True, pangramma: False, szóhossz-közép: 2.61
#     '' -> palindróma: True, pangramma: False, szóhossz-közép: nincs szó
#
#   💡 A szavak hossza:  [len(szo) for szo in mondat.split()]


def elemzes(mondatok):
    # TODO: ide írd a megoldást
    pass


elemzes(["Géza, kék az ég", mondat, "Python", ""])


# =========================================================================
# AMIT MA GYAKOROLTUNK
# =========================================================================
#
#   ✔ szöveg megfordítása szeleteléssel:  szoveg[::-1]
#   ✔ szöveg takarítása:  .lower()  és  .isalnum()
#   ✔ halmaz készítése stringből:  set(szoveg)
#   ✔ halmazkivonás: "mi hiányzik még?"  A - B
#   ✔ típusellenőrzés:  isinstance(x, (int, float))
#   ✔ saját hiba dobása:  raise ValueError("...")
#   ✔ hiba elkapása:  try / except
#
#   A nagy tanulság: előbb takaríts és ellenőrizz, csak utána számolj.
# =========================================================================
from statistics import harmonic_mean  # csak a 3. feladat 💡 tippjéhez


# =========================================================================
# 1. FELADAT  -  PALINDRÓMA                                       ⭐  ~15 perc
# =========================================================================
#
# EMLÉKEZTETŐ
# -----------
#   A palindróma olyan, mint egy vonat, aminek mindkét végén mozdony van:
#   bármelyik oldalról nézed, ugyanazt látod.
#
#   Mielőtt összehasonlítunk, KITAKARÍTJUK a szöveget: kisbetűre váltunk,
#   és eldobunk mindent, ami nem betű vagy szám (szóköz, vessző, felkiáltójel).
#   Enélkül a "Géza, kék az ég" nem lenne palindróma, pedig az.
#
#   A megfordítás eszköze a szeletelés:  lista[::-1]
#   Ez azt jelenti: "az elejétől a végéig, de hátrafelé lépkedve".
#
# FELADAT
#   Készíts függvényt, amely egy adott bemenetről megállapítja, hogy
#   palindróma-e vagy sem!


def palindroma_e(szoveg):
    tiszta = [b for b in szoveg.lower() if b.isalnum()]  # csak betű és szám
    return tiszta == tiszta[::-1]  # előre == hátra?


print(palindroma_e("Géza, kék az ég"))  # True
print(palindroma_e("Indul a görög aludni"))  # True
print(palindroma_e("Python"))  # False
print(palindroma_e(""))  # True  (az üres szöveg tükörképe önmaga)

# Élő, interaktív változat (kikommentezve, hogy a fájl megálljon nélküle):
# szoveg = input("Írj be egy szöveget: ")
# print("Palindróma!" if palindroma_e(szoveg) else "Nem palindróma.")

# ⚠️ GYAKORI HIBA: a tisztítás kihagyása.
#    szoveg == szoveg[::-1]  a "Géza, kék az ég" mondatra False-t ad, mert a
#    vessző és a nagy G elrontja a tükörképet.
#
# ⚠️ GYAKORI HIBA: .lower() elfelejtése. A "Görög" és a "görÖG" csak
#    kisbetűsítés után egyezik.
#
# ⚠️ Az isalnum() az ékezetes betűket (á, ö, ő, ű...) is betűnek tekinti,
#    így a magyar szövegekkel nincs gond.
#
# 💡 Lista helyett stringet is építhetsz, ugyanúgy működik:
#        tiszta = "".join(b for b in szoveg.lower() if b.isalnum())
#
# 💡 HALADÓ: a magyar ábécében a kettős betűk (sz, cs, gy...) egy betűnek
#    számítanak. Szigorú, "betűszintű" palindrómánál ezeket egy egységként
#    kellene kezelni. Az iskolai feladatokhoz a karakterszintű megoldás
#    elég, de jó beszélgetési téma.


# =========================================================================
# 2. FELADAT  -  PANGRAMMA                                       ⭐⭐  ~15 perc
# =========================================================================
#
# EMLÉKEZTETŐ
# -----------
#   A pangramma ellenőrzése egy bingókártya. Minden magyar betű egy mező,
#   és a mondat minden betűjével áthúzol egyet. A kérdés csak az, hogy a
#   végén minden mező át van-e húzva.
#
#   Erre a HALMAZ a tökéletes eszköz:
#     - nem számít, hányszor fordul elő egy betű (duplikátum nincs)
#     - nem számít a sorrend
#     - csak az érdekel, hogy "benne van-e"
#
#   A halmazok kivonása (-) megmondja, mi maradt áthúzatlanul a kártyán.
#
# FELADAT
#   Készíts függvényt, amely egy adott bemenetről megállapítja, hogy
#   (magyar nyelvű) pangramma-e vagy sem! A magyar betűket fel kell
#   sorolni a kódban.

MAGYAR_BETUK = set("aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz")  # 35 egykarakteres betű


def pangramma_e(szoveg):
    hianyzik = MAGYAR_BETUK - set(szoveg.lower())  # ami áthúzatlan maradt
    return len(hianyzik) == 0


def hianyzo_betuk(szoveg):
    """Segédfüggvény hibakereséshez: melyik betű hiányzik?"""
    return sorted(MAGYAR_BETUK - set(szoveg.lower()))


mondat = "Egy hűtlen vejét fülöncsípő, dühös mexikói úr Wesselényinél mázol Quitóban."

print(pangramma_e(mondat))  # True
print(pangramma_e("Szia, Oliver!"))  # False
print(len(hianyzo_betuk("Árvíztűrő tükörfúrógép")))  # 18 betű hiányzik

# Élő, interaktív változat:
# szoveg = input("Írj be egy mondatot: ")
# if pangramma_e(szoveg):
#     print("Pangramma!")
# else:
#     print("Hiányzik:", ", ".join(hianyzo_betuk(szoveg)))

# ⚠️ GYAKORI HIBA: üres halmazt {} írással létrehozni. Az üres szótár!
#    Üres halmaz: set()
#
# ⚠️ GYAKORI HIBA: a nagybetűk. Kisbetűsítés nélkül a "Q" nem húzza át
#    a "q" mezőt.
#
# ⚠️ GYAKORI HIBA: az ékezetes betűk kihagyása a felsorolásból. A magyar
#    pangrammának ezeket is tartalmaznia kell: á é í ó ö ő ú ü ű.
#
# ⚠️ A q, w, x, y a magyar ábécé része, ezért benne vannak a listában.
#
# 💡 Rövidebb, halmaz-összehasonlításos változat ("részhalmaza-e?"):
#        return MAGYAR_BETUK <= set(szoveg.lower())
#
# 💡 HALADÓ: a kettős és hármas betűk (cs, dz, dzs, gy, ly, ny, sz, ty, zs)
#    szigorú ellenőrzése:
#        KETTOS_BETUK = ["cs", "dz", "dzs", "gy", "ly", "ny", "sz", "ty", "zs"]
#        szigoru = pangramma_e(szoveg) and all(k in szoveg.lower() for k in KETTOS_BETUK)
#    Érdekesség: a fenti híres mondat ezen már elbukik (nincs benne pl. "sz").

KETTOS_BETUK = ["cs", "dz", "dzs", "gy", "ly", "ny", "sz", "ty", "zs"]
szigoru = pangramma_e(mondat) and all(k in mondat.lower() for k in KETTOS_BETUK)
print(szigoru)  # False


# =========================================================================
# 3. FELADAT  -  HARMONIKUS KÖZÉP                               ⭐⭐⭐  ~15 perc
# =========================================================================
#
# EMLÉKEZTETŐ
# -----------
#   Elmész a Balatonra 60 km/h-val, és hazajössz 40 km/h-val. Mennyi volt
#   az átlagsebességed? Nem 50, hanem 48! A lassú úton több időt töltöttél,
#   ezért az többet számít. A harmonikus közép pontosan ezt számolja:
#
#       darabszám / (1/x1 + 1/x2 + ... + 1/xn)
#
#   A hibakezelés olyan, mint egy portás a bejáratnál: mielőtt bárki
#   beléphet a számolásba, megnézi a papírjait. Aki nem felel meg, azt
#   egy érthető üzenettel visszaküldi (raise), és nem hagyja, hogy bent
#   okozzon zavart.
#
# FELADAT
#   Készíts függvényt, amely egy lista bemenetből kiszámolja a megadott
#   számok harmonikus közepét! Kezeld a potenciális hibás bemeneteket is!


def harmonikus_kozep(szamok):
    if not isinstance(szamok, (list, tuple)):
        raise TypeError(f"Listát kérek, nem ezt: {type(szamok).__name__}")
    if len(szamok) == 0:
        raise ValueError("Üres listának nincs közepe.")
    for x in szamok:
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError(f"Nem szám: {x!r}")
        if x <= 0:
            raise ValueError(f"Csak pozitív számokkal működik, ez nem az: {x}")
    return len(szamok) / sum(1 / x for x in szamok)


for bemenet in [
    [60, 40],
    [1, 2, 4],
    [],
    [3, 0],
    [5, -2],
    [2, "alma"],
    [True, 2],
    "hello",
]:
    try:
        print(bemenet, "->", round(harmonikus_kozep(bemenet), 2))
    except (TypeError, ValueError) as hiba:
        print(bemenet, "-> hiba:", hiba)

# [60, 40] -> 48.0
# [1, 2, 4] -> 1.71
# [] -> hiba: Üres listának nincs közepe.
# [3, 0] -> hiba: Csak pozitív számokkal működik, ez nem az: 0
# [5, -2] -> hiba: Csak pozitív számokkal működik, ez nem az: -2
# [2, 'alma'] -> hiba: Nem szám: 'alma'
# [True, 2] -> hiba: Nem szám: True
# hello -> hiba: Listát kérek, nem ezt: str

# Élő, interaktív változat (vesszővel elválasztott számok):
# sor = input("Számok vesszővel elválasztva: ")
# try:
#     szamok = [float(s) for s in sor.split(",")]
#     print("Harmonikus közép:", round(harmonikus_kozep(szamok), 2))
# except ValueError as hiba:
#     print("Hibás bemenet:", hiba)

# ⚠️ GYAKORI HIBA: a nulla. Az 1 / 0 ZeroDivisionError-t dob. Ezt vagy
#    előre kiszűrjük (mint fent), vagy try/except-tel elkapjuk.
#
# ⚠️ GYAKORI HIBA: az üres lista. len([]) == 0, ezért 0 / 0 lenne a
#    vége. Mindig ellenőrizd az ürességet osztás előtt.
#
# ⚠️ GYAKORI HIBA: a bool. Pythonban a True valójában az 1 szám
#    (isinstance(True, int) -> True). A külön ellenőrzés nélkül a
#    [True, 2] csendben átmenne a portáson.
#
# ⚠️ GYAKORI HIBA: a számtani átlag használata. (60 + 40) / 2 = 50,
#    ami sebességeknél ROSSZ válasz.
#
# ⚠️ Negatív számokra a harmonikus közép nincs értelmezve, ezért azokat
#    is kiszűrjük.
#
# 💡 raise vs. return None: a raise hangosan szól, ha baj van, a hívó
#    pedig try/except-tel dönti el, mit kezd vele. A None csendben
#    továbbmegy, és később, egy távoli helyen okoz rejtélyes hibát.
#
# 💡 Kész megoldás a standard könyvtárban:
#        from statistics import harmonic_mean
#        harmonic_mean([60, 40])   -> 48.0
#    Érdemes viszont először kézzel megírni, hogy értsd, mi történik.

print(harmonic_mean([60, 40]))  # 48.0


# =========================================================================
# ÖSSZEFOGLALÓ  -  PUSKA
# =========================================================================
#
#   Feladat            Kulcseszköz              Egy sorban
#   -----------------  -----------------------  ----------------------------------
#   Palindróma         szeletelés [::-1]        tiszta == tiszta[::-1]
#                      .lower(), .isalnum()     tisztítás összehasonlítás előtt
#   Pangramma          halmaz (set)             MAGYAR_BETUK - set(szoveg.lower())
#                      halmazkivonás, <=        üres maradék = pangramma
#   Harmonikus közép   isinstance, raise        len(x) / sum(1 / v for v in x)
#                      try / except             0, üres lista, bool, nem szám
#
#   Amit mindhárom megerősít:
#     - Előbb takaríts / ellenőrizz, csak utána számolj.
#     - A halmaz a "benne van-e?" kérdés eszköze.
#     - A generátor kifejezés (sum(1 / x for x in ...)) nem tárol listát.
#     - A hibát nevezd meg (TypeError, ValueError), ne nyeld le csendben.
# =========================================================================
