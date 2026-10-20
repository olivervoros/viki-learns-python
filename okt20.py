"""
=========================================================================
OOP  -  FELADATOK                                    12 feladat + záró projekt
=========================================================================

  Az OOP alapjai    1-3
  Öröklés           4-6
  Egységbezárás     7-8
  Polimorfizmus     9-10
  Absztrakció       11-12
  Záró projekt      13   (mind az öt témakör együtt)

HOGYAN HASZNÁLD
---------------
  Minden feladatnál ott van egy üres váz: írd a megoldást a
  # TODO: ide írd a megoldást  sor helyére, és töröld a  pass  sort.

  A próba-sorok (# print(...)) ki vannak kommentezve, hogy a fájl
  hibátlanul fusson akkor is, ha még nem vagy kész. Ha megírtad a
  feladatot, vedd ki a # jelet a próba-sorok elől, és futtasd:

      python oop_feladatok.py

  Először mindig te próbáld meg - a megoldások az  oop_megoldasok.py
  fájlban vannak. Egy hibás, de lefuttatott megoldás többet ér, mint
  egy jó, amit csak elolvastál.

  Nehézség:  ⭐ könnyű   ⭐⭐ közepes   ⭐⭐⭐ nehéz
"""

import math
from abc import ABC, abstractmethod


# =========================================================================
# AZ OOP ALAPJAI
# =========================================================================

# -------------------------------------------------------------------------
# 1. ⭐  Az első osztályod
# -------------------------------------------------------------------------
# Készíts egy  Book  osztályt: title, author, pages.
# Legyen egy  describe()  metódusa, ami ezt adja vissza:
#     Dűne - Frank Herbert (412 oldal)
# Hozz létre két könyvet, és írasd ki mindkettőt.

class Book:
    # TODO: ide írd a megoldást
    pass

# dune = Book("Dűne", "Frank Herbert", 412)
# hobbit = Book("A hobbit", "J.R.R. Tolkien", 310)
# print(dune.describe())
# print(hobbit.describe())


# -------------------------------------------------------------------------
# 2. ⭐  A süti címkéje: __str__
# -------------------------------------------------------------------------
# Írasd ki:  print(dune)  - mit látsz?
# Adj a Book-nak  __str__  metódust, hogy a print szépen írja ki.
# Tipp: ne írd le kétszer ugyanazt a szöveget - hívd meg a describe()-ot.
# (Az 1. feladat Book osztályát bővítsd, ne írj újat.)

# print(dune)


# -------------------------------------------------------------------------
# 3. ⭐⭐ A lámpa
# -------------------------------------------------------------------------
# Készíts egy  Lamp  osztályt. Induláskor nem ég (is_on = False).
# A  switch()  metódus átkapcsolja (égből nem ég, nem égből ég).
# Az  __str__  ezt adja: "A lámpa ég." vagy "A lámpa nem ég."
# Az __str__-ben használj ternary-t (x if feltétel else y).

class Lamp:
    # TODO: ide írd a megoldást
    pass

# lamp = Lamp()
# print(lamp)            # A lámpa nem ég.
# lamp.switch()
# print(lamp)            # A lámpa ég.


# =========================================================================
# ÖRÖKLÉS
# =========================================================================
"""
Képzeld el, hogy a videojátékod szuper népszerű lett, és elhatározod, hogy beteszel még 50 újféle lényt: medvéket, lovakat, oroszlánokat, és még repülő griffmadarakat is.

Az öröklődés (angolul inheritance) olyan, mintha csinálnál egy "szuper-sablont", amiről az összes többi lényt másolod, hogy megspórolj magadnak egy csomó munkát.

Így működik a gyakorlatban:

Öröklődés nélkül (Unalmas és lassú): Minden egyes új lénynél teljesen elölről, nulláról meg kellene tanítanod a játéknak, hogy a lény hogyan mozog, hogyan alszik, vagy hogy mindegyiknek van egy "Éhség" száma. Ha 50 lényed van, 50-szer kell beírnod ugyanazokat a szabályokat. És ha rájössz, hogy elrontottad az alvás gombot, mind az 50 helyen ki kell javítanod a kódot!

Öröklődéssel (Okos és gyors): Csinálsz egyetlen, általános „Alap Állat” nevű sablont. Ebbe beleteszed azokat a szabályokat, amik mindenkire igazak: például az evést, az alvást, és a sebzést.

Amikor ezután létrehozod a Sárkányt a játékban, nem kell mindent elölről leírnod. Csak annyit mondasz a kódnak:
"A Sárkány is egy Alap Állat! Örökölje meg az alap sablon összes képességét... DE ezen felül kapjon egy egyedi, Tűzokádás() nevű szuperképességet is!"

Amikor létrehozod a Sast, azt mondod:
"A Sas is egy Alap Állat, mindent tud, amit az, DE ezen felül legyen neki egy Repülés() képessége is!"

Miért nagyszerű dolog ez?
A programozásban az öröklődés egyszerűen azt jelenti, hogy egy új dolog automatikusan átveheti (megörökölheti) egy már létező dolog összes tulajdonságát és szabályát.

Így a programozóknak nem kell feltalálniuk a spanyolviaszt minden egyes új szereplőnél. A kód sokkal rövidebb marad, és ha ki akarnak találni egy új szabályt (például hogy az összes állat tudjon úszni), elég csak az "Alap Állat" sablonba beírni, és varázsütésre mind az 50 lény megtanul úszni!
 """
# -------------------------------------------------------------------------
# 4. ⭐  Állatok
# -------------------------------------------------------------------------
# Készíts egy  Animal  osztályt (name) és egy  speak()  metódust, ami
# "Bodri: ..." formát ad. Készíts  Dog  és  Cat  gyerekosztályt, amik
# felülírják a speak()-et:   "Bodri: Vau!",   "Cirmi: Miaú!"

class Animal:
    # TODO: ide írd a megoldást
    pass


class Dog(Animal):
    # TODO: ide írd a megoldást
    pass


class Cat(Animal):
    # TODO: ide írd a megoldást
    pass

# for a in [Dog("Bodri"), Cat("Cirmi"), Animal("Nemo")]:
#     print(a.speak())


# -------------------------------------------------------------------------
# 5. ⭐⭐ Járművek
# -------------------------------------------------------------------------
# Vehicle(brand, wheels)   describe() -> "Skoda, 4 kerék"
# Car(brand)               mindig 4 kerék, a describe() végére: ", 5 ülés"
# Motorbike(brand)         mindig 2 kerék
# Használd a super()-t az __init__-ben ÉS a Car describe()-jában.

class Vehicle:
    # TODO: ide írd a megoldást
    pass


class Car(Vehicle):
    # TODO: ide írd a megoldást
    pass


class Motorbike(Vehicle):
    # TODO: ide írd a megoldást
    pass

# print(Car("Skoda").describe())          # Skoda, 4 kerék, 5 ülés
# print(Motorbike("Honda").describe())    # Honda, 2 kerék


# -------------------------------------------------------------------------
# 6. ⭐  Az "EGY" próba  (gondolkodós feladat, nem kell kódot írni)
# -------------------------------------------------------------------------
# Melyik pár jó öröklésre, és melyik nem?
#     a) Teacher - Person      b) Car - Engine
#     c) Square - Shape        d) Library - Book
# Ahol nem jó, mi lenne helyette?
#
# A válaszod:
#   a)
#   b)
#   c)
#   d)


# =========================================================================
# EGYSÉGBEZÁRÁS
# =========================================================================
"""

Képzeld el, hogy egy olyan videojátékkal játszol, amiben van egy saját virtuális sárkányod.

A játék kódjában a sárkányodnak van egy „Éhség” nevű száma.

Az egységbezárás (angolul encapsulation) olyan, mintha egy láthatatlan, kulccsal zárható széfbe tennénk ezt az Éhség számot, hogy senki se tudja csak úgy elrontani.

Így működik a gyakorlatban:

Egységbezárás nélkül (Veszélyes): Bárki, aki játszik a játékkal, csak úgy belenyúlhatna a kódba, és átírhatná a sárkány éhségét mondjuk -1000-re, vagy szám helyett beírhatná azt a szót, hogy "Pizza". A játék nem tudná, mit kezdjen ezzel, összezavarodna és lefagyna.

Egységbezárással (Biztonságos): A sárkány Éhség száma biztonságosan el van rejtve a széfben. Te, mint játékos, nem nyúlhatsz közvetlenül ehhez a számhoz.

De akkor hogyan eteted meg a sárkányt?
Ahelyett, hogy a játék engedné, hogy csak úgy átírd a számot, ad neked egy külön gombot, amit megnyomhatsz: ez az Etetés() gomb.

Amikor megnyomod az Etetés() gombot, a játék úgy viselkedik, mint egy okos biztonsági őr. Mielőtt bármit csinálna, ellenőrzi a szabályokat:

Van egyáltalán virtuális kaja a hátizsákodban?

Tényleg éhes a sárkány?

Ha a válasz mindkettőre igen, akkor maga a játék kinyitja a széfet, szépen lecsökkenti az éhség számát, aztán újra biztonságosan bezárja a széfet.

A programozásban az egységbezárás tehát egyszerűen azt jelenti, hogy a fontos adatokat elrejtjük egy biztonságos dobozba, és csak bizonyos, előre megírt, biztonságos gombokon (úgynevezett "metódusokon") keresztül engedjük megváltoztatni őket. Ez megvédi a játékot (vagy programot) attól, hogy elromoljon!
"""


# -------------------------------------------------------------------------
# 7. ⭐⭐ Termosztát
# -------------------------------------------------------------------------
# A hőmérséklet  _temperature  néven legyen tárolva, alapértéke 21.
# Készíts hozzá  temperature  property-t és settert.
# A setter dobjon ValueError-t, ha az érték nincs 5 és 30 °C között.
# Próbáld ki 24-gyel és 45-tel.

class Thermostat:
    # TODO: ide írd a megoldást
    pass

# t = Thermostat()
# t.temperature = 24
# print(t.temperature)
# try:
#     t.temperature = 45
# except ValueError as e:
#     print("Hiba:", e)


# -------------------------------------------------------------------------
# 8. ⭐⭐ Bankszámla előzményekkel
# -------------------------------------------------------------------------
# Az óra 3. részének BankAccount-ját bővítsd ki: minden be- és kifizetés
# kerüljön egy  _history  listába, pl. ("befizetés", 5000).
# Legyen egy  history  property, ami TUPLE-ként adja vissza.
# Kérdés: miért tuple, és miért nem maga a lista?

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        # TODO: ide jön a _history lista

    @property
    def balance(self):
        return self._balance

    # TODO: ide jön a history property

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Csak pozitív összeget lehet befizetni.")
        self._balance += amount
        # TODO: jegyezd fel a _history-ba

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Nincs elég fedezet.")
        self._balance -= amount
        # TODO: jegyezd fel a _history-ba

# acc = BankAccount("Anna")
# acc.deposit(10000)
# acc.withdraw(3000)
# print(acc.balance)      # 7000
# print(acc.history)      # (('befizetés', 10000), ('kifizetés', 3000))
#
# A válaszod (miért tuple?):
#


# =========================================================================
# POLIMORFIZMUS
# =========================================================================
"""
Képzeld el, hogy a videojátékodban most már nem csak egy állatod van, hanem több is: egy kutyád, egy macskád és egy kacsád.

A polimorfizmus (ami egy nagyon ijesztő szó, de igazából csak annyit jelent, hogy „többféle alak”) olyan, mint egy általános parancsszó, amit minden állat megért, de mindegyik a saját módján hajtja végre.

Így működik a gyakorlatban:

Van egyetlen gombod a játékban, amire az van írva: HangotAd().

Ha kiválasztod a kutyát, és megnyomod a gombot, ő azt fogja mondani: „Vau-vau!”

Ha kiválasztod a macskát, és megnyomod a gombot, ő azt mondja: „Miau!”

Ha kiválasztod a kacsát, és megnyomod a gombot, ő azt mondja: „Háp-háp!”

Miért jó ez?
A játéknak (és a kódnak) nem kell törődnie azzal, hogy pontosan milyen állat van éppen a képernyőn. Csak kiadja az utasítást, hogy „adj ki hangot!”, és biztos lehet benne, hogy az adott állat tudja a saját dolgát.

A programozásban a polimorfizmus egyszerűen azt jelenti, hogy nem kell ezerféle különböző gombot írnunk (például külön KutyaUgat(), MacskaNyávog() és KacsaHápog() parancsokat). Elég egyetlen közös HangotAd() parancs, és a kód elintézi, hogy mindenki a saját maga módján válaszoljon rá. Ez sokkal rövidebbé, egyszerűbbé és okosabbá teszi a programokat!
"""
# -------------------------------------------------------------------------
# 9. ⭐  Új alakzat
# -------------------------------------------------------------------------
# Itt van a Circle és a Rectangle az óráról. Írj hozzájuk egy
# Triangle(base, height)  osztályt (terület = alap * magasság / 2,
# __str__ legyen pl. "Háromszög (4, 5)"), és tedd a listába.
# Kérdés: mit kellett megváltoztatnod a ciklusban?

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return round(math.pi * self.r ** 2, 2)

    def __str__(self):
        return f"Kör (r={self.r})"


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __str__(self):
        return f"Téglalap ({self.w}x{self.h})"


class Triangle:
    # TODO: ide írd a megoldást
    pass

# shapes = [Circle(1), Rectangle(2, 3), Triangle(4, 5)]
# for s in shapes:
#     print(f"{str(s):<20} területe: {s.area()}")


# -------------------------------------------------------------------------
# 10. ⭐⭐ Értesítések
# -------------------------------------------------------------------------
# Három osztály, NEM rokonok egymással:
#     Email(address)   send(text) -> "E-mail -> anna@example.com: ..."
#     SMS(number)      send(text) -> "SMS -> +36 30 123 4567: ..."
#     Push()           send(text) -> "Push értesítés: ..."
# Írj egy  notify_all(channels, text)  függvényt, ami mindegyiknek
# elküldi (kiírja) az üzenetet. Kell bele if?

class Email:
    # TODO: ide írd a megoldást
    pass


class SMS:
    # TODO: ide írd a megoldást
    pass


class Push:
    # TODO: ide írd a megoldást
    pass


def notify_all(channels, text):
    # TODO: ide írd a megoldást
    pass

# notify_all([Email("anna@example.com"), SMS("+36 30 123 4567"), Push()],
#            "Holnap 17:00-kor óra!")


# =========================================================================
# ABSZTRAKCIÓ
# =========================================================================
"""
Képzeld el, hogy a videojátékodban most beülsz egy menő virtuális sportautóba.

Az absztrakció (ami a lényeg kiemelését, a felesleg elrejtését jelenti) olyan, mint maga a kontroller, amit a kezedben tartasz vezetés közben. Eltünteti a felfoghatatlanul bonyolult dolgokat, és csak azt hagyja elöl, amire tényleg szükséged van az irányításhoz.

Így működik a gyakorlatban:

Absztrakció nélkül (Játszhatatlanul bonyolult): Ahhoz, hogy az autó elinduljon a játékban, neked kellene egyenként megmondanod a gépnek, hogy mennyi virtuális üzemanyag menjen a motorba, hogyan mozduljanak a dugattyúk, és milliméterre pontosan hogyan tapadjon a gumi az aszfalthoz. Mire ezt mind kiszámolnád, lemenne a nap.

Absztrakcióval (Egyszerű és élvezetes): A játék egyszerűen ad egy „Gáz” gombot, egy „Fék” gombot és egy kormányt.

Miért zseniális ez?
Amikor megnyomod a „Gáz” gombot, az autó kilő. Nem kell tudnod, hogy a motorház alatt (vagy a játék kódjában) milyen elképesztő matematika és fizika dolgozik azon, hogy a kerekek forogjanak. A játék megalkotói a bonyolult, nehéz részeket elrejtették egy nagy „dobozba”, és csak a legegyszerűbb, legfontosabb kapcsolókat adták a kezedbe.

A programozásban az absztrakció egyszerűen azt jelenti, hogy elrejtjük a nagyon bonyolult belső működést, és csak azokat az egyszerű, érthető parancsokat hagyjuk meg, amikkel az adott dolgot használni lehet. Így a programozóknak nem kell mindig megérteniük, hogy egy adott kód hogyan csinál meg egy nehéz feladatot, elég csak tudniuk, hogy melyik gombot kell megnyomni hozzá.
"""
# -------------------------------------------------------------------------
# 11. ⭐⭐ Munkavállalók
# -------------------------------------------------------------------------
# Absztrakt  Employee(ABC)  osztály: name, absztrakt  monthly_pay(),
# és egy kész  report()  metódus: "Anna: 450000 Ft".
# Két gyerek:
#     FullTime(name, salary)        havi fizetés = salary
#     Hourly(name, rate, hours)     havi fizetés = rate * hours
# Írasd ki mindenki report()-ját, és a teljes bérköltséget egy sorban
# (sum + generátor/comprehension).

class Employee(ABC):
    # TODO: ide írd a megoldást
    pass


class FullTime(Employee):
    # TODO: ide írd a megoldást
    pass


class Hourly(Employee):
    # TODO: ide írd a megoldást
    pass

# staff = [FullTime("Anna", 450000), Hourly("Bela", 3000, 80)]
# for e in staff:
#     print(e.report())
# print("Összesen:", sum(e.monthly_pay() for e in staff), "Ft")


# -------------------------------------------------------------------------
# 12. ⭐  Mi történik, ha megszeged a szerződést?
# -------------------------------------------------------------------------
# Ha a 11. kész: töröld ki (vagy kommentezd ki) a  monthly_pay  metódust a
# Hourly-ból, és futtasd újra. Mi történik, és MIKOR - létrehozáskor
# vagy a report() hívásakor? Miért jó ez így?
#
# A válaszod:
#


# =========================================================================
# ZÁRÓ PROJEKT  -  a tanár naplója (mind az öt témakör)
# =========================================================================

# -------------------------------------------------------------------------
# 13. ⭐⭐⭐
# -------------------------------------------------------------------------
# a) Absztrakt  Lesson(ABC)  osztály: student, minutes, subject.
#    - absztrakt  fee()  metódus
#    - a  minutes  legyen property + setter: 1 és 180 perc között fogadja
#      el, különben ValueError                     (egységbezárás)
#    - kész  __str__:  "Mate - Angol, 60 perc, 8000 Ft"   (absztrakció)
#
# b) Két gyerekosztály                             (öröklés)
#       EnglishLesson(student, minutes)   8000 Ft, ha >= 60 perc,
#                                         különben 5000 Ft
#       PythonLesson(student, minutes)    150 Ft percenként
#    (A subject-et a gyerek adja át a super().__init__-nek.)
#
# c) Diary  osztály:
#    - _lessons  belső lista
#    - add(lesson): csak Lesson-t fogad el, minden mást TypeError-ral
#      utasít vissza   (tipp: isinstance)
#    - total(): az összes bevétel            (polimorfizmus: l.fee())
#    - by_student(): {"Mate": 13000, ...}    (dict, .get)
#
# d) Próbáld ki ezzel:
#       Mate  angol   60 perc
#       Nora  python  90 perc
#       Mate  angol   45 perc
#       Kata  python  60 perc
#    Várt eredmény: összesen 35500 Ft,
#                   {'Mate': 13000, 'Nora': 13500, 'Kata': 9000}
#
# e) Bizonyítsd, hogy a védelem működik: egy 0 perces óra, egy sima
#    szöveg a naplóba, és egy Lesson(...) közvetlen létrehozása.

class Lesson(ABC):
    # TODO: ide írd a megoldást
    pass


class EnglishLesson(Lesson):
    # TODO: ide írd a megoldást
    pass


class PythonLesson(Lesson):
    # TODO: ide írd a megoldást
    pass


class Diary:
    # TODO: ide írd a megoldást
    pass

# diary = Diary()
# diary.add(EnglishLesson("Mate", 60))
# diary.add(PythonLesson("Nora", 90))
# diary.add(EnglishLesson("Mate", 45))
# diary.add(PythonLesson("Kata", 60))
# print("Összesen:", diary.total(), "Ft")
# print(diary.by_student())
#
# e) ide írd a három próbát try/except-tel


# =========================================================================
# AMIT MA GYAKOROLTUNK
# =========================================================================
#   ALAPOK          osztály = szaggató, objektum = süti, self = "melyik süti"
#   ÖRÖKLÉS         családi recept - class Gyerek(Szulo), super()
#                   próba: "X EGY Y?" igen -> öröklés, "VAN neki" -> attribútum
#   EGYSÉGBEZÁRÁS   bankautomata - _nev + @property + setter
#   POLIMORFIZMUS   ▶ gomb - ugyanaz a hívás, mindenki a maga módján válaszol
#   ABSZTRAKCIÓ     kormány - class Alap(ABC) + @abstractmethod = szerződés
#
# Ha kész vagy, nézd meg:  oop_megoldasok.py

print("A fájl lefutott. Vedd ki a # jelet a próba-sorok elől, ha egy feladat kész!")