# ===========================================================
#   🐍 PYTHON ALAPOK – Első lecke – MEGOLDÁSOK (Tanári kulcs)
#   Témakörök: Változók, Megváltoztathatatlanság, Listák,
#              print & input, f-stringek, Típuskonverzió
# ===========================================================
# ⚠️  Ez a fájl a TANÁRI MEGOLDÁSKULCS.
#     A diákoknak szánt fájlt NE add ki ezzel együtt!
# ===========================================================


# ===========================================================
# 1. VÁLTOZÓK – Megoldások
# ===========================================================

nev = "Anna"
kor = 25
magassag = 1.68
diak_e = True
kor = 26
x, y, z = 1, 2, 3

# 1. feladat
varos = "Budapest"
# 💡 Bármilyen városnév helyes, a lényeg a szintaxis.

# 2. feladat
kedvenc_szam = 7
# 💡 Bármilyen szám helyes.

# 3. feladat
print(nev)
print(kor)
# 💡 Két külön print() is elfogadható, egy sorban is megoldható:
# print(nev, kor)


# ===========================================================
# 2. MEGVÁLTOZTATHATATLANSÁG – Megoldások
# ===========================================================

# 4. feladat
gyumolcs = "alma"
print(gyumolcs)  # alma
gyumolcs = "körte"
print(gyumolcs)  # körte
# 💡 A változó maga megváltozhat – de az "alma" string objektum
#    nem módosult, egy teljesen új "körte" objektum jött létre.

# 5. feladat – tapasztalat (kommentként)
# gyumolcs = "alma"
# gyumolcs[0] = "A"
# ⚠️ TypeError: 'str' object does not support item assignment
# A hiba azt mondja: szöveg karaktereit nem lehet helyben cserélni!


# ===========================================================
# 3. LISTÁK – Megoldások
# ===========================================================

gyumolcsok = ["alma", "banán", "körte"]
gyumolcsok[1] = "eper"
gyumolcsok.append("mangó")
gyumolcsok.remove("alma")
szamok = [5, 2, 8, 1, 9]
szamok.sort()

# 6. feladat
osztaly = ["Anna", "Béla", "Cili", "Dani"]
# 💡 Bármilyen 4 név elfogadható.

# 7. feladat
print(osztaly[0])  # első elem
print(osztaly[-1])  # utolsó elem
# 💡 osztaly[3] is helyes az utolsó elemnél, de [-1] az elegánsabb.

# 8. feladat
osztaly.append("Péter")
print(osztaly)
# ⚠️ Gyakori hiba: osztaly = osztaly.append("Péter") – az append()
#    None-t ad vissza, nem kell az eredményt visszaadni!

# 9. feladat
for nev in osztaly:
    print(nev)
# 💡 A ciklusváltozó neve tetszőleges lehet (pl. 'tanulo' is jó).


# ===========================================================
# 4. PRINT ÉS INPUT – Megoldások
# ===========================================================

# 10. feladat
nev_bekeres = input("Mi a neved? ")
kor_bekeres = int(input("Hány éves vagy? "))
print(f"Szia, {nev_bekeres}! {kor_bekeres} éves vagy.")
# ⚠️ Gyakori hiba: elfelejtik az int()-et a kornál,
#    és aztán szövegként próbálják kezelni.

# 11. feladat
szam1 = float(input("Add meg az első számot: "))
szam2 = float(input("Add meg a második számot: "))
print(f"Az összegük: {szam1 + szam2}")
# 💡 int() is elfogadható, ha egész számokkal dolgoznak.
# ⚠️ Gyakori hiba: "+" jellel próbálják összefűzni szövegként.


# ===========================================================
# 5. F-STRINGEK – Megoldások
# ===========================================================

nev = "Béla"
kor = 30
magassag = 1.75
szam = 3.14159

# 12. feladat
varos = "Budapest"
laksz_ott_evek = 5
print(f"{varos}-ban/ben {laksz_ott_evek} éve laksz.")
# 💡 A -ban/-ben ragot a diák maga igazítja a városhoz.

# 13. feladat
nev_bekeres = input("Mi a neved? ")
kedvenc = int(input("Mi a kedvenc számod? "))
print(f"Szia, {nev_bekeres}! A kedvenc számod kétszerese: {kedvenc * 2}.")
# 💡 A számítást közvetlenül a {} belsejében is el lehet végezni!

# 14. feladat (Összetett)
tantargyak = ["Matek", "Fizika", "Torma"]
nev_bekeres = input("Mi a neved? ")
for tantargy in tantargyak:
    print(f"{nev_bekeres} tantárgya: {tantargy}")
# ⚠️ Gyakori hiba: az input()-ot a for cikluson belülre teszik –
#    ekkor minden iterációban bekéri a nevet!


# ===========================================================
# 6. TÍPUSKONVERZIÓ – Megoldások
# ===========================================================

# 15. feladat
kor_input = int(input("Hány éves vagy? "))
print(f"5 év múlva {kor_input + 5} éves leszel.")
# ⚠️ Hardcoded érték a teszteléshez: kor_input = 20
# ⚠️ Gyakori hiba: elfelejtik az int() konverziót,
#    ekkor "20" + 5 --> TypeError!

# 16. feladat
ar = float(input("Add meg a termék árát (Ft): "))
darab = int(input("Hány darabot szeretnél? "))
vegosszeg = ar * darab
print(f"Fizetendő összeg: {vegosszeg} Ft")
# 💡 Ha az ár mindig egész, int() is elfogadható.
# ⚠️ Gyakori hiba: mindkettőt float()-tal kezelik –
#    ez nem hiba, de darabszámnál int() logikusabb.

# 17. feladat
ertek = "7.5"
ertek_float = float(ertek)
eredmeny = ertek_float * 4
eredmeny_szoveg = str(eredmeny) + " pont"
print(eredmeny_szoveg)  # "30.0 pont"
# 💡 f-stringgel is megoldható: print(f"{ertek_float * 4} pont")

# 18. feladat (Összetett)
szam1 = float(input("Add meg az első számot: "))
szam2 = float(input("Add meg a második számot: "))
szam3 = float(input("Add meg a harmadik számot: "))
szamok_lista = [szam1, szam2, szam3]
osszeg = sum(szamok_lista)
atlag = osszeg / len(szamok_lista)
print(f"Az összegük: {osszeg}")
print(f"Az átlaguk: {atlag:.2f}")
# 💡 sum() és len() helyett manuálisan is kiszámolható:
#    osszeg = szam1 + szam2 + szam3  (szintén elfogadható)
# ⚠️ Hardcoded tesztértékek: szam1=10, szam2=20, szam3=30
#    Elvárt kimenet: összeg=60, átlag=20.00


# ===========================================================
# TANÁRI MEGJEGYZÉSEK
# ===========================================================
# ⏱️  Javasolt időkeret:
#     - 1–3. feladat:  ~10 perc (változók)
#     - 4–5. feladat:  ~5 perc  (immutability)
#     - 6–9. feladat:  ~15 perc (listák)
#     - 10–11. feladat: ~10 perc (print/input)
#     - 12–14. feladat: ~15 perc (f-stringek)
#     - 15–18. feladat: ~15 perc (típuskonverzió)
#
# 💡 Leggyakoribb hibák összefoglalva:
#     1. Elfelejtik az int()/float() konverziót input() után
#     2. append() visszatérési értékét visszaadják (None bug)
#     3. Stringet és számot "+" jellel próbálnak összefűzni
#     4. input()-ot for cikluson belülre teszik véletlenül
#     5. Negatív index (-1) koncepcióját nehezen értik kezdetben
