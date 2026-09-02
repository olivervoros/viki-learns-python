# ===========================================================
#   🐍 PYTHON ALAPOK – Házi feladat (augusztus 7.)
#   Témakör: Listák módosítása – a legfontosabb lista-metódusok
# ===========================================================
# Az előző órán megismerted a listákat. Ma ezt bővítjük ki: megnézzük,
# hogyan tudsz elemeket beszúrni, törölni, rendezni és
# megkeresni egy listában – és egy fontos csapdát is
# leleplezünk a lista másolásával kapcsolatban!


# ===========================================================
# 1. ELEMEK HOZZÁADÁSA A LISTÁHOZ
# ===========================================================
# Képzeld el a listát, mint egy sorban állást a boltban:
#
#   .append(x)   --> beállsz a sor VÉGÉRE
#   .insert(i,x) --> befurakodsz egy konkrét helyre a sorban
#   .extend(l)   --> egy egész CSAPAT csatlakozik a sor végéhez

gyumolcsok = ["alma", "banán", "körte"]

gyumolcsok.append("mangó")  # a lista végére kerül
print(gyumolcsok)  # ["alma", "banán", "körte", "mangó"]

gyumolcsok.insert(1, "eper")  # az 1-es indexre szúrja be,
print(gyumolcsok)  # a többi elem eggyel arrébb csúszik

uj_gyumolcsok = ["dinnye", "szilva"]
gyumolcsok.extend(uj_gyumolcsok)  # mindkét elemet hozzáadja
print(gyumolcsok)

# ⚠️ Gyakori hiba! Nézd meg a különbséget:
# gyumolcsok.append(uj_gyumolcsok)   --> egy LISTÁT told be
#                                        egyetlen elemként!
# gyumolcsok.extend(uj_gyumolcsok)   --> az elemeket adja hozzá
#                                        külön-külön


# ------ FELADATOK ------

# 1. feladat: Hozz létre egy 'zoldsegek' nevű listát 3 elemmel.
#             Az .append() metódussal tedd a lista VÉGÉRE
#             a "paprika" szót, majd írd ki a listát!
# Ide írd a megoldást:

zoldsegek = ["repa", "uborka", "paradicsom"]
zoldsegek.append("paprika")
print(zoldsegek)


# 2. feladat: Az előző listában az .insert() metódussal
#             szúrd be a "hagyma" szót a lista LEGELEJÉRE
#             (0-ás index)! Írd ki az eredményt!
# Ide írd a megoldást:
zoldsegek = ["repa", "uborka", "paradicsom"]
zoldsegek.append("paprika")
zoldsegek.insert(0,"hagyma")
print(zoldsegek)



# 3. feladat: Hozz létre egy másik listát 2 új zöldséggel,
#             majd az .extend() metódussal add hozzá az összes
#             elemét a 'zoldsegek' listához! Írd ki az eredményt!
# Ide írd a megoldást:

uj_zoldsegek= ["spenot", "cekla"]
zoldsegek.extend(uj_zoldsegek)
print(zoldsegek)

# ===========================================================
# 2. ELEMEK ELTÁVOLÍTÁSA A LISTÁBÓL
# ===========================================================
# Négyféle módon "veheted ki" az elemet a sorból:
#
#   .remove(x)  --> az ELSŐ x értékű elemet törli (érték alapján)
#   .pop(i)     --> törli az i. indexű elemet, ÉS VISSZA IS ADJA
#                   (index nélkül: az utolsó elemet törli és adja vissza)
#   del lista[i] --> törli az i. indexű elemet (nem ad vissza semmit)
#   .clear()    --> kiüríti az EGÉSZ listát

szamok = [10, 20, 30, 40, 50]

szamok.remove(30)  # a 30-as ÉRTÉKŰ elemet törli
print(szamok)  # [10, 20, 40, 50]

utolso = szamok.pop()  # levágja és visszaadja az utolsó elemet
print(utolso)  # 50
print(szamok)  # [10, 20, 40]

masodik = szamok.pop(1)  # az 1-es indexű elemet veszi ki
print(masodik)  # 20
print(szamok)  # [10, 40]

del szamok[0]  # törli a 0-ás indexű elemet
print(szamok)  # [40]

szamok.clear()  # üres lista marad
print(szamok)  # []

# ⚠️ Gyakori hiba: a .remove() ÉRTÉKET vár, nem indexet!
# Ha olyan értéket adsz meg, ami nincs a listában, ValueError-t kapsz.
# ⚠️ Másik gyakori hiba: .pop() eredményét el kell tárolni egy
# változóba, ha fel akarod használni – különben elvész!


# ------ FELADATOK ------

# 4. feladat: Hozz létre egy 'osztaly' listát 5 névvel.
#             Az .remove() metódussal töröld ki a 3. nevet
#             (az ÉRTÉKE alapján, ne indexszel)! Írd ki a listát!
# Ide írd a megoldást:
osztaly = ["Viki", "Anna", "Dorka", "Bogi", "Alma"]
osztaly.remove("Dorka")
print(osztaly)

# 5. feladat: Az előző listából a .pop() metódussal vedd ki
#             az utolsó elemet, tárold el egy 'kiesett' nevű
#             változóba, és írd ki: "Kiesett: [kiesett]"
# Ide írd a megoldást:
kiesett = osztaly.pop(3)
print(f"Kiesett:{kiesett}")

# 6. feladat: A del kulcsszóval töröld ki a lista első elemét
#             (0-ás index), majd írd ki a maradék listát!
# Ide írd a megoldást:
del osztaly[0]
print(osztaly)

# ===========================================================
# 3. RENDEZÉS ÉS SORREND
# ===========================================================
# A .sort() metódust már ismered (növekvő sorrend).
# Van pár további trükk is:
#
#   lista.sort()               --> növekvő sorrend, HELYBEN rendez
#   lista.sort(reverse=True)   --> csökkenő sorrend
#   lista.reverse()            --> csak MEGFORDÍTJA a sorrendet
#                                   (ez NEM rendezés!)
#   sorted(lista)               --> ÚJ, rendezett listát ad vissza,
#                                    az eredeti lista NEM változik!

pontok = [15, 3, 42, 8, 23]

pontok.sort()
print(pontok)  # [3, 8, 15, 23, 42]

pontok.sort(reverse=True)
print(pontok)  # [42, 23, 15, 8, 3]

betuk = ["b", "d", "a", "c"]
betuk.reverse()  # csak megfordítja a JELENLEGI sorrendet
print(betuk)  # ["c", "a", "d", "b"]  <- nincs rendezve!

eredeti = [5, 1, 4, 2]
uj_lista = sorted(eredeti)  # eredeti VÁLTOZATLAN marad
print(eredeti)  # [5, 1, 4, 2]
print(uj_lista)  # [1, 2, 4, 5]

# ⚠️ Gyakori hiba: a .sort() (és .reverse(), .append() is!)
# None-t ad vissza – ne írd: pontok = pontok.sort()
# A lista MÁR HELYBEN megváltozott, nem kell visszaadni!


# ------ FELADATOK ------

# 7. feladat: Hozz létre egy 5 elemű számlistát véletlenszerű
#             sorrendben. Rendezd CSÖKKENŐ sorrendbe a
#             .sort(reverse=True) segítségével! Írd ki!
# Ide írd a megoldást:
szamok = [2, 44, 77, 56, 4]
szamok.sort(reverse=True)
print(f"szamok 173.sor : {szamok}")


# 8. feladat: Hozz létre egy nevekből álló listát, és
#             a .reverse() metódussal fordítsd meg a sorrendjét!
#             Írd ki előtte és utána is a listát – figyeld meg
#             a különbséget a rendezéshez képest!
# Ide írd a megoldást:
nevek2 = ["Alma", "Mira", "Viki", "Bogi"]
print(nevek2)
nevek2.reverse()
print(f"nevek sor 184. :{nevek2}")

# 9. feladat: Hozz létre egy 'eredeti' nevű listát számokkal.
#             A sorted() függvénnyel hozz létre egy ÚJ,
#             rendezett listát 'rendezett' néven, úgy hogy
#             az 'eredeti' lista NE változzon! Írd ki mindkettőt!
# Ide írd a megoldást:
eredeti = [3, 5, 2, 33]
rendezett = sorted(eredeti)
print(eredeti)
print(rendezett)


# ===========================================================
# 4. KERESÉS A LISTÁBAN
# ===========================================================
# Három hasznos eszköz, ha meg akarod találni valaminek
# a helyét, vagy meg akarod nézni, benne van-e egy listában:
#
#   x in lista       --> True/False, benne van-e x
#   lista.index(x)   --> hányadik indexen van x (az ELSŐ találat)
#   lista.count(x)   --> hányszor fordul elő x a listában

kosarba = ["alma", "banán", "alma", "körte"]

print("banán" in kosarba)  # True
print("szilva" in kosarba)  # False

print(kosarba.index("alma"))  # 0  (az első "alma" indexe)
print(kosarba.count("alma"))  # 2  (kétszer szerepel)

# ⚠️ Gyakori hiba: ha az .index() metódusnak olyan értéket adsz,
# ami nincs a listában, ValueError-t kapsz! Ezért érdemes előbb
# az 'in' kulcsszóval ellenőrizni, hogy tényleg benne van-e.


# ------ FELADATOK ------

# 10. feladat: Kérdezd meg (input) a felhasználótól egy
#              gyümölcs nevét, majd az 'in' kulcsszóval
#              ellenőrizd, benne van-e a 'kosarba' listában!
#              Írd ki: "Benne van: True" vagy "Benne van: False"
# Ide írd a megoldást:
#gyumolcs = int(input("Mondjon egy gyümölcsöt :"))
#print("gyumolcs" in kosarba)
valasz = input("Mondjon egy gyümölcsöt : ")
if valasz in kosarba:
    print("True")
else :
    print("False")





# 11. feladat: Írd ki, hányszor szerepel az "alma" szó
#              a 'kosarba' listában a .count() metódussal!
# Ide írd a megoldást:
print(kosarba.count("alma"))


# ===========================================================
# 5. LISTA MÁSOLÁSA – EGY REJTETT CSAPDA!
# ===========================================================
# Ez egy fontos, gyakran félreértett dolog Pythonban!
# Ha ezt írod:
#
#   lista2 = lista1
#
# ...azzal NEM másolatot készítesz! Csak egy ÚJABB FELIRATOT
# (címkét) ragasztasz UGYANARRA a dobozra. Ha az egyiket
# módosítod, a másik is megváltozik – mert valójában
# ugyanaz a lista, csak két néven!

lista1 = ["alma", "banán"]
lista2 = lista1  # NEM másolat! Ugyanarra a listára mutat!
lista2.append("körte")

print(lista1)  # ["alma", "banán", "körte"]  <- ez is megváltozott!
print(lista2)  # ["alma", "banán", "körte"]

# Ha VALÓDI, független másolatot akarsz, használd a .copy()
# metódust (vagy a lista[:] szeletelést):

lista3 = ["alma", "banán"]
lista4 = lista3.copy()  # ez már EGY ÚJ, FÜGGETLEN lista
lista4.append("körte")

print(lista3)  # ["alma", "banán"]       <- változatlan!
print(lista4)  # ["alma", "banán", "körte"]


# ------ FELADATOK ------

# 12. feladat: Próbáld ki a fenti csapdát a saját példáddal!
#              Hozz létre egy listát, add egy másik változóhoz
#              (lista2 = lista1), módosítsd lista2-t, majd
#              írd ki mindkettőt – figyeld meg, mi történik!
# Ide írd a megoldást:
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(lista1)
print(lista2)

# 13. feladat: Most javítsd ki az előző feladatot a .copy()
#              metódussal, hogy a módosítás már csak a
#              másolatot érintse! Írd ki mindkét listát!
# Ide írd a megoldást:
lista1 = [1, 2, 3]
lista2 = lista1.copy()
lista2.append(4)
print(lista1)
print(lista2)


# ===========================================================
# 6. ÖSSZETETT FELADATOK (bónusz)
# ===========================================================

# 14. feladat: Készíts egy egyszerű bevásárlólista-kezelőt!
#              - Hozz létre egy üres 'bevasarlas' listát.
#              - Kérj be 3 terméket a felhasználótól (input(),
#                for ciklusban vagy egyenként), és mindegyiket
#                add hozzá .append()-pel a listához.
#              - Írd ki a teljes listát.
#              - Kérdezd meg, melyik terméket vették már meg,
#                és .remove()-al vedd ki a listából.
#              - Írd ki a végleges, rendezett (sort()) listát!
# Ide írd a megoldást:
bevasarlas = []
for value in range(1,4):
    termek = input("Adj meg egy terméket : ")
    bevasarlas.append(termek)
print(bevasarlas)
mar_megvettem = input("Már megvettem : ")
bevasarlas.remove(mar_megvettem)
bevasarlas.sort()
print(bevasarlas)

# 15. feladat (Összetett): Van egy listád: [4, 12, 4, 7, 12, 4, 9]
#              - Írd ki, hányszor szerepel a 4-es szám (.count())
#              - Írd ki a lista leghosszabb (utolsó) elemének
#                indexét a .index() metódussal
#              - Rendezd csökkenő sorrendbe a listát
#              - Készíts egy FÜGGETLEN másolatot .copy()-val,
#                és a másolatból töröld ki az összes 4-es
#                számot egy while ciklus és a .remove()
#                segítségével (tipp: while 4 in masolat: ...)
#              - Írd ki mindkét listát a végén – az eredetinek
#                nem szabad megváltoznia!
# Ide írd a megoldást:
