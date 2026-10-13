# ============================================================
#   OBJEKTUMORIENTÁLT PROGRAMOZÁS (OOP) – ALAPOK
#   Python | Magyar magyarázatok | Példákkal
# ============================================================


# ============================================================
# 1. MI AZ OSZTÁLY (CLASS)?
# ============================================================

# Képzeld el, hogy egy TERVRAJZ vagy SABLON.
# Például: egy "Kutya" tervrajz leírja, hogy minden kutyának
# van neve, kora, és tud ugatni.
# Az osztály maga még NEM egy konkrét kutya – csak a terv!


class Kutya:
    pass  # egyelőre üres osztály – csak a keret létezik


# ============================================================
# 2. MI AZ OBJEKTUM (OBJECT)?
# ============================================================

# Ha az osztály a tervrajz, az objektum a KÉSZ TERMÉK.
# Például: "Bodri" egy konkrét kutya, akit a tervrajz alapján "gyártottunk".

bodri = Kutya()  # létrehozunk egy Kutya objektumot
rex = Kutya()  # egy másik Kutya objektum

# bodri és rex két KÜLÖNBÖZŐ objektum, de ugyanabból az osztályból.
print(type(bodri))  # <class '__main__.Kutya'>


# ============================================================
# 3. AZ __init__ METÓDUS – AZ "SZÜLETÉSI PILLANAT"
# ============================================================

# Az __init__ automatikusan lefut, amikor létrehozunk egy objektumot.
# Itt adjuk meg az objektum kezdeti adatait (attribútumait).
# Olyan, mint a születési anyakönyvi kivonat kitöltése.


class Kutya:
    def __init__(self, nev, kor):
        # 'self' jelenti magát az objektumot (Bodrit, Rexet stb.)
        # self.nev = az objektum saját neve
        self.nev = nev
        self.kor = kor


# Most már tudunk névre és korra szóló kutyákat létrehozni:
bodri = Kutya("Bodri", 3)
rex = Kutya("Rex", 7)

print(bodri.nev)  # Bodri
print(rex.kor)  # 7


# ============================================================
# 4. METÓDUSOK – AZ OBJEKTUM "TUDÁSA"
# ============================================================

# A metódus egy függvény, ami az osztályon BELÜL van.
# Leírja, hogy az objektum mit TUD CSINÁLNI.


class Kutya:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

    def ugat(self):
        # self segítségével elérjük az objektum saját adatait
        print(f"{self.nev} azt mondja: Vau!")

    def bemutatkozik(self):
        print(f"Szia! {self.nev} vagyok, {self.kor} éves.")


bodri = Kutya("Bodri", 3)
bodri.ugat()  # Bodri azt mondja: Vau!
bodri.bemutatkozik()  # Szia! Bodri vagyok, 3 éves.


# ============================================================
# 5. ATTRIBÚTUMOK MÓDOSÍTÁSA
# ============================================================

# Az objektum adatait (attribútumait) bármikor megváltoztathatjuk.


class Kutya:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

    def szuletesnap(self):
        self.kor += 1
        print(f"{self.nev} most lett {self.kor} éves. Boldog születésnapot!")


bodri = Kutya("Bodri", 3)
bodri.szuletesnap()  # Bodri most lett 4 éves. Boldog születésnapot!
print(bodri.kor)  # 4


# ============================================================
# 6. ÖRÖKLÉS (INHERITANCE)
# ============================================================

# Az öröklés azt jelenti, hogy egy osztály ÁTVESZI egy másik
# osztály tulajdonságait és metódusait – és hozzáadhat sajátokat.
#
# Valós analógia: Minden kutya egyben állat is.
# Az "Állat" az általános sablon, a "Kutya" egy speciálisabb verzió.


class Allat:
    def __init__(self, nev):
        self.nev = nev

    def lelegzik(self):
        print(f"{self.nev} lélegzik.")


# A Kutya osztály örökli az Allat osztályt:
class Kutya(Allat):
    def __init__(self, nev, fajta):
        super().__init__(nev)  # meghívja az Allat __init__-jét
        self.fajta = fajta

    def ugat(self):
        print(f"{self.nev} ({self.fajta}): Vau!")


class Macska(Allat):
    def nyavog(self):
        print(f"{self.nev}: Miau!")


bodri = Kutya("Bodri", "Labrador")
cicus = Macska("Cicus")

bodri.lelegzik()  # Bodrit az Allat-tól örökölte ezt!  → Bodri lélegzik.
bodri.ugat()  # Bodri (Labrador): Vau!
cicus.lelegzik()  # Cicus lélegzik.
cicus.nyavog()  # Cicus: Miau!


# ============================================================
# 7. EGYSÉGBEZÁRÁS (ENCAPSULATION) – "PRIVÁT" ADATOK
# ============================================================

# Néha nem akarjuk, hogy az objektum adatait kívülről
# közvetlenül módosítsák. Erre való az egységbezárás.
#
# Analógia: A bankszámlád egyenlegét nem írhatja felül bárki –
# csak a bank által jóváhagyott műveletek (befizetés, kifizetés).


class Bankszamla:
    def __init__(self, tulajdonos, egyenleg):
        self.tulajdonos = tulajdonos
        self.__egyenleg = egyenleg  # __ = "privát" – kívülről nem elérhető

    def befizet(self, osszeg):
        if osszeg > 0:
            self.__egyenleg += osszeg
            print(f"{osszeg} Ft befizetve. Új egyenleg: {self.__egyenleg} Ft")

    def kivesz(self, osszeg):
        if osszeg <= self.__egyenleg:
            self.__egyenleg -= osszeg
            print(f"{osszeg} Ft kivéve. Új egyenleg: {self.__egyenleg} Ft")
        else:
            print("Nincs elég pénz a számlán!")

    def egyenleg_lekerdezes(self):
        print(f"Egyenleg: {self.__egyenleg} Ft")


szamla = Bankszamla("Kovács Péter", 10000)
szamla.befizet(5000)  # 5000 Ft befizetva. Új egyenleg: 15000 Ft
szamla.kivesz(3000)  # 3000 Ft kivéve. Új egyenleg: 12000 Ft
szamla.egyenleg_lekerdezes()  # Egyenleg: 12000 Ft

# Ez HIBÁT adna – a privát adat kívülről nem elérhető:
# print(szamla.__egyenleg)


# ============================================================
# 8. ÖSSZEFOGLALÁS
# ============================================================

# ┌─────────────────┬──────────────────────────────────────────────┐
# │ Fogalom         │ Mit jelent?                                  │
# ├─────────────────┼──────────────────────────────────────────────┤
# │ class           │ Tervrajz / sablon                            │
# │ object          │ A tervrajzból létrehozott valódi példány      │
# │ __init__        │ Lefut az objektum létrehozásakor (konstruktor)│
# │ self            │ Maga az objektum (pl. "én, Bodri")            │
# │ metódus         │ Az osztályhoz tartozó függvény                │
# │ öröklés         │ Egy osztály átveszi egy másik tulajdonságait  │
# │ egységbezárás   │ Privát adatok védelme (__ előtag)             │
# └─────────────────┴──────────────────────────────────────────────┘

print("\n✅ Gratulálok! Megismerkedtél az OOP alapjaival!")

# ============================================================
#   OOP 1 – ALAPOK: GYAKORLÓ FELADATOK                (DIÁK)
#   Osztály | Objektum | __init__ | Metódusok | Attribútumok
#   Öröklés | Egységbezárás
# ============================================================
#
#   HOGYAN HASZNÁLD?
#   1. Olvasd el az EMLÉKEZTETŐT és futtasd le a példát.
#   2. Oldd meg a feladatot a "TODO" helyén (a `pass` sort töröld ki).
#   3. A feladat alatti TESZT sorok elől vedd ki a # jelet, és futtasd.
#   4. Hasonlítsd össze az eredményt az "Elvárt kimenet" résszel.
#
#   Nehézség:  ⭐ könnyű   ⭐⭐ közepes   ⭐⭐⭐ kihívás
#   13 feladat – a fájl úgy is lefut, ha még semmit nem oldottál meg.
# ============================================================


# ============================================================
# 1. OSZTÁLY ÉS OBJEKTUM
# ============================================================

# EMLÉKEZTETŐ
# Az osztály olyan, mint a SÜTIKISZÚRÓ FORMA.
# A forma maga nem süti – nem lehet megenni.
# De akárhány sütit ki tudsz vele szúrni, és mind ugyanolyan alakú.
#
#     forma  = osztály  (class)
#     süti   = objektum (object)

class Suti:
    pass


suti1 = Suti()      # kiszúrtunk egy sütit
suti2 = Suti()      # és még egyet

print(type(suti1))          # <class '__main__.Suti'>
print(suti1 is suti2)       # False – két KÜLÖN süti, ugyanabból a formából

# 💡 Az osztály nevét Nagybetűvel kezdjük (Suti), az objektumét kicsivel (suti1).
# ⚠️ A zárójel kell!  Suti  = maga a forma,  Suti()  = egy új süti.


# ------------------------------------------------------------
# 1. feladat ⭐  –  Az első saját osztályod
# ------------------------------------------------------------
# a) Hozz létre egy üres osztályt Auto néven.
# b) Készíts belőle két objektumot: auto1 és auto2.
# c) Írd ki az auto1 típusát.
# d) Írd ki, hogy auto1 és auto2 ugyanaz az objektum-e (is).

# TODO: ide írd a megoldást
pass

# Elvárt kimenet:
#   <class '__main__.Auto'>
#   False


# ============================================================
# 2. AZ __init__ ÉS AZ ATTRIBÚTUMOK
# ============================================================

# EMLÉKEZTETŐ
# Amikor beiratkozol egy edzőterembe, kitöltesz egy ADATLAPOT:
# név, életkor. Enélkül nem kapsz bérletet.
#
# Az __init__ ez az adatlap: automatikusan "kitöltődik", amikor
# létrejön az objektum. A self pedig azt jelenti: "ez az ÉN adatlapom".

class Tag:
    def __init__(self, nev, kor):
        self.nev = nev      # az ÉN nevem
        self.kor = kor      # az ÉN korom


anna = Tag("Anna", 28)
bela = Tag("Béla", 35)

print(anna.nev)     # Anna
print(bela.kor)     # 35

# ⚠️ A self MINDIG az első paraméter, de híváskor NEM írjuk ki:
#    Tag("Anna", 28)   ← csak két adatot adunk, a self-et a Python intézi.
# ⚠️ self.nev = nev   ← a self. nélkül az adat elvész az __init__ végén!


# ------------------------------------------------------------
# 2. feladat ⭐  –  Könyv
# ------------------------------------------------------------
# Készíts Konyv osztályt három attribútummal: cim, szerzo, oldalszam.
# Hozz létre két könyvet, és írd ki az első címét és a második oldalszámát.

class Konyv:
    # TODO: ide írd a megoldást
    pass


# TESZT:
# konyv1 = Konyv("Egri csillagok", "Gárdonyi Géza", 560)
# konyv2 = Konyv("A Pál utcai fiúk", "Molnár Ferenc", 190)
# print(konyv1.cim)
# print(konyv2.oldalszam)

# Elvárt kimenet:
#   Egri csillagok
#   190


# ------------------------------------------------------------
# 3. feladat ⭐  –  Hibakeresés
# ------------------------------------------------------------
# Az alábbi kódban TÖBB hiba is van (mind a self-fel kapcsolatos).
# Keresd meg őket, és írd le lent a javított változatot.
#
#     class Diak:
#         def __init__(nev, evfolyam):
#             nev = nev
#             evfolyam = evfolyam
#
#         def koszon():
#             print(f"Szia, {nev} vagyok!")
#
#     d = Diak("Anna", 9)
#     d.koszon()

class Diak:
    # TODO: ide írd a javított változatot
    pass


# TESZT:
# d = Diak("Anna", 9)
# d.koszon()

# Elvárt kimenet:
#   Szia, Anna vagyok!


# ============================================================
# 3. METÓDUSOK
# ============================================================

# EMLÉKEZTETŐ
# A TÁVIRÁNYÍTÓN gombok vannak: hangosít, csatornát vált.
# Az attribútum az, amit a tévé TUD MAGÁRÓL (hangerő, csatorna).
# A metódus az, amit a tévé MEG TUD CSINÁLNI (a gombok).
#
#     attribútum = adat      (főnév)
#     metódus    = művelet   (ige)

class Teve:
    def __init__(self, marka):
        self.marka = marka
        self.csatorna = 1

    def bemutat(self):
        print(f"{self.marka} tévé, {self.csatorna}. csatorna")

    def kovetkezo_csatorna(self):
        return self.csatorna + 1        # visszaad egy értéket


teve = Teve("Samsung")
teve.bemutat()                          # Samsung tévé, 1. csatorna
print(teve.kovetkezo_csatorna())        # 2

# 💡 print = csak kiírja.  return = visszaadja, tovább tudsz vele számolni.
# ⚠️ teve.bemutat   ← zárójel nélkül NEM fut le!  teve.bemutat()  a helyes.


# ------------------------------------------------------------
# 4. feladat ⭐  –  A könyv bemutatkozik
# ------------------------------------------------------------
# Írd meg újra a Konyv osztályt (cim, szerzo, oldalszam), és adj hozzá
# egy leiras() metódust, ami ezt írja ki:
#     Egri csillagok – Gárdonyi Géza (560 oldal)

class Konyv:
    # TODO: ide írd a megoldást
    pass


# TESZT:
# konyv = Konyv("Egri csillagok", "Gárdonyi Géza", 560)
# konyv.leiras()

# Elvárt kimenet:
#   Egri csillagok – Gárdonyi Géza (560 oldal)


# ------------------------------------------------------------
# 5. feladat ⭐⭐  –  Téglalap
# ------------------------------------------------------------
# Készíts Teglalap osztályt (szelesseg, magassag) három metódussal:
#   terulet()    → VISSZAADJA a területet     (szélesség * magasság)
#   kerulet()    → VISSZAADJA a kerületet     (2 * (szélesség + magasság))
#   negyzet_e()  → True, ha a két oldal egyenlő, különben False
# Figyelem: itt return kell, nem print!

class Teglalap:
    # TODO: ide írd a megoldást
    pass


# TESZT:
# t = Teglalap(4, 6)
# print(t.terulet())
# print(t.kerulet())
# print(t.negyzet_e())
# print(Teglalap(5, 5).negyzet_e())

# Elvárt kimenet:
#   24
#   20
#   False
#   True


# ============================================================
# 4. ATTRIBÚTUMOK MÓDOSÍTÁSA
# ============================================================

# EMLÉKEZTETŐ
# Az autó KILOMÉTERÓRÁJA nem marad ugyanannyi, mint a szalonban:
# minden út után többet mutat. Az autó ugyanaz, az adata változik.
#
# Az objektum attribútumai is változhatnak az "élete" során –
# legszebben úgy, ha egy metódus módosítja őket.

class Auto:
    def __init__(self, marka):
        self.marka = marka
        self.km = 0                 # minden új autó 0 km-rel indul

    def megy(self, tavolsag):
        self.km += tavolsag
        print(f"{self.marka}: {self.km} km")


skoda = Auto("Skoda")
skoda.megy(120)     # Skoda: 120 km
skoda.megy(80)      # Skoda: 200 km

# 💡 A km-t nem kérjük be paraméterként: az __init__ maga állítja 0-ra.
# ⚠️ Minden objektumnak SAJÁT km-e van. Egy másik autóé ettől nem változik.


# ------------------------------------------------------------
# 6. feladat ⭐⭐  –  Játékos
# ------------------------------------------------------------
# Készíts Jatekos osztályt:
#   - __init__(nev): a pontszam induláskor mindig 0
#   - pontot_szerez(pont): hozzáadja a pontot a pontszámhoz
#   - szint(): VISSZAADJA a szintet:
#         0–99    → "Kezdő"
#         100–499 → "Haladó"
#         500-tól → "Mester"

class Jatekos:
    # TODO: ide írd a megoldást
    pass


# TESZT:
# j = Jatekos("Zoli")
# print(j.szint())
# j.pontot_szerez(150)
# print(j.pontszam, j.szint())
# j.pontot_szerez(400)
# print(j.pontszam, j.szint())

# Elvárt kimenet:
#   Kezdő
#   150 Haladó
#   550 Mester


# ------------------------------------------------------------
# 7. feladat ⭐⭐  –  Bevásárlókosár
# ------------------------------------------------------------
# Készíts Kosar osztályt:
#   - __init__: egy üres lista, a neve termekek
#   - hozzaad(termek): beteszi a terméket a listába
#   - kivesz(termek): kiveszi, ha benne van; ha nincs, kiírja:
#         Nincs a kosárban: <termék>
#   - darab(): VISSZAADJA, hány termék van a kosárban

class Kosar:
    # TODO: ide írd a megoldást
    pass


# TESZT:
# kosar = Kosar()
# kosar.hozzaad("tej")
# kosar.hozzaad("kenyér")
# kosar.hozzaad("sajt")
# kosar.kivesz("kenyér")
# kosar.kivesz("csoki")
# print(kosar.termekek)
# print(kosar.darab())

# Elvárt kimenet:
#   Nincs a kosárban: csoki
#   ['tej', 'sajt']
#   2


# ============================================================
# 5. ÖRÖKLÉS
# ============================================================

# EMLÉKEZTETŐ
# A nagymama PALACSINTARECEPTJÉT megkapod. Nem kell újra kitalálnod:
# ami benne van, azt tudod. De hozzátehetsz valami sajátot (pl. nutellát).
#
#     nagymama receptje = szülő osztály
#     a te változatod   = gyerek osztály (mindent tud, amit a szülő + a sajátját)

class Etel:
    def __init__(self, nev):
        self.nev = nev

    def talal(self):
        print(f"Tálalva: {self.nev}")


class Palacsinta(Etel):                 # a zárójelben a SZÜLŐ
    def __init__(self, nev, toltelek):
        super().__init__(nev)           # a szülő elintézi a nevet
        self.toltelek = toltelek        # ez a saját, új adat

    def feltekercsel(self):
        print(f"{self.nev} feltekerve, benne {self.toltelek}.")


p = Palacsinta("Palacsinta", "nutella")
p.talal()           # ezt ÖRÖKÖLTE:  Tálalva: Palacsinta
p.feltekercsel()    # ez a SAJÁTJA:  Palacsinta feltekerve, benne nutella.

# 💡 Teszt: ki tudod mondani, hogy "a palacsinta EGY étel"? Akkor jó az öröklés.
# ⚠️ Ha a gyereknek saját __init__-je van, a super().__init__(...) NE maradjon ki,
#    különben a szülő adatai (itt: nev) nem jönnek létre.


# ------------------------------------------------------------
# 8. feladat ⭐⭐  –  Járművek
# ------------------------------------------------------------
# a) Jarmu osztály: marka attribútum + halad() metódus, ami kiírja:
#        <marka> halad.
# b) Auto(Jarmu): plusz dudal() metódus →  <marka>: Tü-tű!
# c) Bicikli(Jarmu): plusz csenget() metódus →  <marka>: Csing-csing!
# A gyerek osztályokba NE írj __init__-et és halad()-ot – örököljék!

class Jarmu:
    # TODO: ide írd a megoldást
    pass


# TODO: ide írd az Auto és a Bicikli osztályt


# TESZT:
# auto = Auto("Suzuki")
# bicikli = Bicikli("Csepel")
# auto.halad()
# auto.dudal()
# bicikli.halad()
# bicikli.csenget()

# Elvárt kimenet:
#   Suzuki halad.
#   Suzuki: Tü-tű!
#   Csepel halad.
#   Csepel: Csing-csing!


# ------------------------------------------------------------
# 9. feladat ⭐⭐  –  Alkalmazott és menedzser
# ------------------------------------------------------------
# a) Alkalmazott osztály: nev, fizetes + bemutatkozik() metódus:
#        Kiss Éva, fizetés: 450000 Ft
# b) Menedzser(Alkalmazott): plusz egy csapat_letszam attribútum.
#    Használd a super().__init__()-et!
#    Plusz metódus: csapat() →  Kiss Éva csapata: 8 fő

class Alkalmazott:
    # TODO: ide írd a megoldást
    pass


# TODO: ide írd a Menedzser osztályt


# TESZT:
# m = Menedzser("Kiss Éva", 450000, 8)
# m.bemutatkozik()
# m.csapat()

# Elvárt kimenet:
#   Kiss Éva, fizetés: 450000 Ft
#   Kiss Éva csapata: 8 fő


# ============================================================
# 6. EGYSÉGBEZÁRÁS
# ============================================================

# EMLÉKEZTETŐ
# A BANKAUTOMATÁBAN ott a pénz, de nem nyúlhatsz bele kézzel.
# Csak a gombokon keresztül kérhetsz – és a gép ELLENŐRIZ:
# van-e elég a számládon? Jó-e a PIN-kódod?
#
#     a pénz a gép belsejében = privát attribútum  (__ a neve elején)
#     a gombok                = metódusok, amik ellenőriznek

class Automata:
    def __init__(self, keszlet):
        self.__keszlet = keszlet            # privát!

    def kivesz(self, osszeg):
        if osszeg <= 0:
            print("Érvénytelen összeg!")
        elif osszeg > self.__keszlet:
            print("Nincs ennyi pénz az automatában!")
        else:
            self.__keszlet -= osszeg
            print(f"Kiadva: {osszeg} Ft")

    def keszlet(self):
        return self.__keszlet


atm = Automata(50000)
atm.kivesz(20000)       # Kiadva: 20000 Ft
atm.kivesz(-5)          # Érvénytelen összeg!
atm.kivesz(99999)       # Nincs ennyi pénz az automatában!
print(atm.keszlet())    # 30000

# 💡 A lényeg nem a titkolózás, hanem az ELLENŐRZÉS:
#    az adat csak úgy változhat, ahogy az osztály megengedi.
# ⚠️ print(atm.__keszlet)  ← AttributeError! Kívülről nem érhető el.


# ------------------------------------------------------------
# 10. feladat ⭐⭐  –  Malacpersely
# ------------------------------------------------------------
# Készíts Persely osztályt:
#   - privát __osszeg attribútum, induláskor 0
#   - bedob(osszeg): csak POZITÍV összeget fogad el, különben kiírja:
#         Ilyet nem lehet bedobni!
#   - mennyi_van(): VISSZAADJA az összeget

class Persely:
    # TODO: ide írd a megoldást
    pass


# TESZT:
# persely = Persely()
# persely.bedob(500)
# persely.bedob(200)
# persely.bedob(-1000)
# print(persely.mennyi_van())

# Elvárt kimenet:
#   Ilyet nem lehet bedobni!
#   700


# ------------------------------------------------------------
# 11. feladat ⭐⭐  –  Termosztát
# ------------------------------------------------------------
# Készíts Termosztat osztályt:
#   - privát __fok attribútum, induláskor 20
#   - beallit(fok): csak 10 és 30 közötti értéket fogad el (a 10 és a 30 is jó),
#     különben kiírja:  Érvénytelen érték: <fok>
#   - lekerdez(): VISSZAADJA a beállított fokot

class Termosztat:
    # TODO: ide írd a megoldást
    pass


# TESZT:
# t = Termosztat()
# t.beallit(23)
# print(t.lekerdez())
# t.beallit(55)
# print(t.lekerdez())

# Elvárt kimenet:
#   23
#   Érvénytelen érték: 55
#   23


# ------------------------------------------------------------
# 12. feladat ⭐⭐  –  Jósold meg!
# ------------------------------------------------------------
# NE futtasd le rögtön! Először írd le, mit ír ki az A, C és D sor.
# Utána vedd ki a kommenteket, és ellenőrizd. Az egyik meglepő lesz.
#
#     class Szef:
#         def __init__(self):
#             self.__kod = 1234
#
#         def kod_helyes(self, tipp):
#             return tipp == self.__kod
#
#     szef = Szef()
#     print(szef.kod_helyes(1234))    # A
#     szef.__kod = 9999               # B
#     print(szef.kod_helyes(9999))    # C
#     print(szef.__kod)               # D

# A tippem:
#   A sor: TODO
#   C sor: TODO
#   D sor: TODO
#
# Kérdés: sikerült a B sorban átírni a széf kódját? Miért / miért nem?
#   TODO


# ============================================================
# 7. ZÁRÓFELADAT – MINDEN EGYBEN
# ============================================================

# ------------------------------------------------------------
# 13. feladat ⭐⭐⭐  –  Állatmenhely
# ------------------------------------------------------------
# a) Allat osztály: nev, kor
#      bemutatkozik() → VISSZAADJA:  "Bodri, 3 éves"
#
# b) Kutya(Allat): plusz fajta attribútum (super()!)
#      hang() → VISSZAADJA: "Vau!"
#
# c) Macska(Allat): nincs saját __init__
#      hang() → VISSZAADJA: "Miau!"
#
# d) Menhely osztály: nev + privát __allatok lista (induláskor üres)
#      befogad(allat)     → beteszi az állatot a listába
#      orokbe_ad(nev)     → kiveszi a listából az adott nevű állatot, és kiírja:
#                               <nev> gazdára talált!
#                           ha nincs ilyen nevű:
#                               Nincs ilyen állat: <nev>
#      letszam()          → VISSZAADJA, hány állat van
#      lista()            → kiírja a menhely nevét, a létszámot, majd soronként
#                           minden állatot (lásd az elvárt kimenetet)

class Allat:
    # TODO: ide írd a megoldást
    pass


# TODO: ide írd a Kutya, a Macska és a Menhely osztályt


# TESZT:
# menhely = Menhely("Mancs Menhely")
# menhely.befogad(Kutya("Bodri", 3, "labrador"))
# menhely.befogad(Macska("Cirmi", 2))
# menhely.befogad(Kutya("Rex", 7, "németjuhász"))
# menhely.lista()
# menhely.orokbe_ad("Cirmi")
# menhely.orokbe_ad("Pamacs")
# print(menhely.letszam())

# Elvárt kimenet:
#   Mancs Menhely – 3 lakó:
#    - Bodri, 3 éves: Vau!
#    - Cirmi, 2 éves: Miau!
#    - Rex, 7 éves: Vau!
#   Cirmi gazdára talált!
#   Nincs ilyen állat: Pamacs
#   2


# ============================================================
# AMIT MA GYAKOROLTUNK
# ============================================================
#
#   class Nev:              sütikiszúró forma – a terv
#   obj = Nev()             a kiszúrt süti – a kész példány
#   __init__                adatlap – lefut, amikor az objektum létrejön
#   self                    "én magam" – az objektum saját adatai
#   metódus                 a távirányító gombja – amit az objektum TUD
#   self.x += 1             kilométeróra – az adat változhat
#   class B(A):             nagymama receptje – B mindent tud, amit A
#   super().__init__()      a szülő elintézi a saját részét
#   self.__x                bankautomata – csak metóduson át érhető el
#
print("\n✅ A fájl végére értél. Szép munka!")
