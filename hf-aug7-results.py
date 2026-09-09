# ===========================================================
#   🐍 PYTHON ALAPOK – Házi feladat (augusztus 7.) – MEGOLDÁSOK
#   Témakör: Listák módosítása – a legfontosabb lista-metódusok
# ===========================================================
# ⚠️  Ez a fájl a TANÁRI MEGOLDÁSKULCS.
#     A diákoknak szánt fájlt NE add ki ezzel együtt!
# ===========================================================


# ===========================================================
# 1. ELEMEK HOZZÁADÁSA A LISTÁHOZ – Megoldások
# ===========================================================

gyumolcsok = ["alma", "banán", "körte"]
gyumolcsok.append("mangó")
gyumolcsok.insert(1, "eper")
uj_gyumolcsok = ["dinnye", "szilva"]
gyumolcsok.extend(uj_gyumolcsok)

# 1. feladat
zoldsegek = ["répa", "brokkoli", "saláta"]
zoldsegek.append("paprika")
print(zoldsegek)
# 💡 Bármilyen 3 induló zöldség elfogadható.

# 2. feladat
zoldsegek.insert(0, "hagyma")
print(zoldsegek)
# ⚠️ Gyakori hiba: az .insert() két paramétert vár (index, érték) –
#    ha csak az értéket adják meg, TypeError lesz belőle.

# 3. feladat
uj_zoldsegek = ["cukkini", "retek"]
zoldsegek.extend(uj_zoldsegek)
print(zoldsegek)
# ⚠️ Gyakori hiba: .append(uj_zoldsegek) helyett .extend()-et kell
#    használni, különben egy beágyazott lista jön létre!


# ===========================================================
# 2. ELEMEK ELTÁVOLÍTÁSA A LISTÁBÓL – Megoldások
# ===========================================================

szamok = [10, 20, 30, 40, 50]
szamok.remove(30)
utolso = szamok.pop()
masodik = szamok.pop(1)
del szamok[0]
szamok.clear()

# 4. feladat
osztaly = ["Anna", "Béla", "Cili", "Dani", "Eszter"]
osztaly.remove("Cili")
print(osztaly)
# 💡 Bármilyen 5 név elfogadható, a lényeg, hogy ÉRTÉK alapján
#    törölnek, nem indexszel.

# 5. feladat
kiesett = osztaly.pop()
print(f"Kiesett: {kiesett}")
# ⚠️ Gyakori hiba: osztaly.pop() eredményét nem tárolják el,
#    így nem tudják kiírni, mi esett ki.

# 6. feladat
del osztaly[0]
print(osztaly)
# 💡 A del kulcsszó nem metódus, hanem utasítás – nincs utána zárójel
#    a lista neve után, hanem lista[index] szerepel.


# ===========================================================
# 3. RENDEZÉS ÉS SORREND – Megoldások
# ===========================================================

pontok = [15, 3, 42, 8, 23]
pontok.sort()
pontok.sort(reverse=True)
betuk = ["b", "d", "a", "c"]
betuk.reverse()
eredeti_pelda = [5, 1, 4, 2]
uj_lista_pelda = sorted(eredeti_pelda)

# 7. feladat
szamok2 = [12, 45, 3, 78, 22]
szamok2.sort(reverse=True)
print(szamok2)  # [78, 45, 22, 12, 3]
# 💡 Bármilyen 5 szám elfogadható.

# 8. feladat
nevek = ["Anna", "Béla", "Cili"]
print(nevek)
nevek.reverse()
print(nevek)  # ["Cili", "Béla", "Anna"]
# 💡 Fontos tapasztalat: a reverse() NEM ABC sorrendbe rendez,
#    csak megfordítja a lista JELENLEGI sorrendjét!

# 9. feladat
eredeti = [7, 2, 9, 4]
rendezett = sorted(eredeti)
print(eredeti)  # [7, 2, 9, 4]  <- változatlan!
print(rendezett)  # [2, 4, 7, 9]
# ⚠️ Gyakori hiba: eredeti.sort() paranccsal próbálják megoldani,
#    de az HELYBEN módosítja az eredetit – itt kifejezetten
#    a sorted() függvényt kell használni!


# ===========================================================
# 4. KERESÉS A LISTÁBAN – Megoldások
# ===========================================================

kosarba = ["alma", "banán", "alma", "körte"]
print("banán" in kosarba)
print(kosarba.index("alma"))
print(kosarba.count("alma"))

# 10. feladat
gyumolcs_keres = input("Melyik gyümölcsöt keresed? ")
print(f"Benne van: {gyumolcs_keres in kosarba}")
# ⚠️ Hardcoded érték a teszteléshez: gyumolcs_keres = "banán" --> True
# ⚠️ Gyakori hiba: kosarba.index(gyumolcs_keres)-szel próbálják
#    megoldani, ami ValueError-t dob, ha a gyümölcs nincs a listában.

# 11. feladat
print(kosarba.count("alma"))  # 2
# 💡 A .count() sosem dob hibát, akkor sem, ha az elem 0-szor
#    szerepel – ez a nagy különbség az .index()-hez képest.


# ===========================================================
# 5. LISTA MÁSOLÁSA – EGY REJTETT CSAPDA – Megoldások
# ===========================================================

# 12. feladat
lista1 = ["kutya", "macska"]
lista2 = lista1
lista2.append("hörcsög")
print(lista1)  # ["kutya", "macska", "hörcsög"]  <- ez is megváltozott!
print(lista2)  # ["kutya", "macska", "hörcsög"]
# 💡 A "meglepetés" a lényeg: mindkét lista megváltozott, mert
#    lista2 = lista1 nem másolatot, csak egy új nevet ad
#    UGYANANNAK a listának.

# 13. feladat
lista3 = ["kutya", "macska"]
lista4 = lista3.copy()
lista4.append("hörcsög")
print(lista3)  # ["kutya", "macska"]        <- változatlan!
print(lista4)  # ["kutya", "macska", "hörcsög"]
# 💡 lista3[:] is ugyanezt az eredményt adja, mint a .copy().


# ===========================================================
# 6. ÖSSZETETT FELADATOK (bónusz) – Megoldások
# ===========================================================

# 14. feladat
bevasarlas = []
for i in range(3):
    termek = input(f"{i + 1}. termék: ")
    bevasarlas.append(termek)
print(bevasarlas)

megvett = input("Melyik terméket vetted meg? ")
bevasarlas.remove(megvett)

bevasarlas.sort()
print(bevasarlas)
# ⚠️ Hardcoded tesztértékek: "tej", "kenyér", "vaj", majd megvett="tej"
#    Elvárt végeredmény: ["kenyér", "vaj"]
# ⚠️ Gyakori hiba: ha a felhasználó olyan terméket ír be a
#    "megvett" kérdésre, ami nincs pontosan úgy leírva a listában
#    (pl. elgépelés, nagy/kis betű), ValueError-t kapnak a
#    .remove()-nál. Ez jó alkalom megbeszélni, miért érdemes
#    előbb 'in'-nel ellenőrizni.

# 15. feladat (Összetett)
lista = [4, 12, 4, 7, 12, 4, 9]

print(lista.count(4))  # 3

utolso_ertek = lista[-1]
print(lista.index(utolso_ertek))  # 6
# 💡 Tanulságos eset: mivel a 9-es csak egyszer szerepel, itt
#    valóban az utolsó pozíciót adja vissza – de ha az utolsó elem
#    értéke ismétlődne (pl. 4), az .index() akkor is a LEGELSŐ
#    előfordulást találná meg, nem az utolsót! Érdemes ezt
#    megbeszélni a diákkal.

lista.sort(reverse=True)
print(lista)  # [12, 12, 9, 7, 4, 4, 4]

masolat = lista.copy()
while 4 in masolat:
    masolat.remove(4)

print(lista)  # [12, 12, 9, 7, 4, 4, 4]  <- eredeti változatlan!
print(masolat)  # [12, 12, 9, 7]
# ⚠️ Gyakori hiba: for elem in masolat: ... masolat.remove(elem)
#    ciklusban próbálják törölni az elemeket – ez hibás, mert
#    a lista mérete menet közben változik, és a ciklus "kihagy"
#    elemeket! Ezért kell while ciklust használni.
# ⚠️ Másik gyakori hiba: masolat = lista helyett a .copy()
#    hiányában az eredeti lista is módosulna.


# ===========================================================
# TANÁRI MEGJEGYZÉSEK
# ===========================================================
# ⏱️  Javasolt időkeret:
#     - 1–3. feladat:   ~10 perc (append / insert / extend)
#     - 4–6. feladat:   ~10 perc (remove / pop / del / clear)
#     - 7–9. feladat:   ~10 perc (sort / reverse / sorted)
#     - 10–11. feladat: ~10 perc (in / index / count)
#     - 12–13. feladat: ~10 perc (másolás csapdája – FONTOS!)
#     - 14–15. feladat: ~15–20 perc (összetett, bónusz)
#
# 💡 Leggyakoribb hibák összefoglalva:
#     1. .append(masik_lista) helyett .extend()-et kellene
#        használni, ha az elemeket külön-külön akarjuk hozzáadni
#     2. .remove() értéket vár, nem indexet – ValueError, ha
#        az érték nincs a listában
#     3. .pop() visszatérési értékét nem tárolják el változóba
#     4. lista.sort() / lista.reverse() eredményét visszaadják
#        egy változónak (None bug) – ugyanaz a hiba, mint az
#        append()-nél az előző órán
#     5. .index() csak az ELSŐ előfordulást találja meg –
#        ismétlődő elemeknél ez meglepetést okozhat
#     6. lista2 = lista1 NEM másolat! Ez a legfontosabb, gyakran
#        félreértett fogalom ebben a leckében – szánj rá extra
#        időt, és ha van rá mód, rajzold le táblán a "két címke,
#        egy doboz" analógiát
#     7. Ciklus közben elemet törölni ugyanabból a listából,
#        amin éppen végigmegyünk (for-ral) – emiatt hagy ki
#        elemeket a ciklus. Erre jó megoldás a while ciklus,
#        vagy egy másolaton dolgozni.
