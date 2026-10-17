# =========================================================================
# ORSZÁGOK ALKOHOLFOGYASZTÁSA  -  megoldás magyarázatokkal
# =========================================================================
# A fájl mellé tedd be a HappinessAlcoholConsumption.csv állományt
# (ugyanabba a mappába), aztán futtasd:  python alkohol_fogyasztas.py
#
# A CSV oszlopai (0-tól számolva):
#   0 Country   1 Region   2 Hemisphere   3 HappinessScore   4 HDI
#   5 GDP_PerCapita   6 Beer_PerCapita   7 Spirit_PerCapita   8 Wine_PerCapita
# A feldolgozás után a sor végére kerül egy 9. oszlop: a teljes alkohol.


# =========================================================================
# 1. FÁJL BETÖLTÉSE  (3 pont)
# =========================================================================
# EMLÉKEZTETŐ: a fájl olyan, mint egy könyvtári könyv. Kikölcsönzöd
# (open), elolvasod (readlines), és VISSZAVISZED (close). A `with`
# blokk egy automata könyvtáros: a blokk végén magától visszaviszi.

def fajl_betoltes(fajlnev):
    with open(fajlnev, "r", encoding="utf-8") as f:   # UTF-8 kódolás!
        sorok = f.readlines()
    # itt a fájl már be van zárva - ezt a `with` intézte
    return sorok


# =========================================================================
# 2. TELJES ALKOHOL SZÁZALÉK  (5 pont)
# =========================================================================
# EMLÉKEZTETŐ: mint a bevásárlás. 5 Ft-os, 11 Ft-os és 40 Ft-os termékből
# veszel valamennyit: darab * ár, összeadod, és itt még elosztjuk 100-zal.

def teljes_alkohol(sor, bor, rovid):
    return (sor * 5 + bor * 11 + rovid * 40) / 100

# ⚠️ A paraméterek sorrendje: SÖR, BOR, RÖVIDITAL.


# =========================================================================
# 3. ADATOK FELDOLGOZÁSA  (17 pont)
# =========================================================================
# EMLÉKEZTETŐ: mint a krumplipucolás egy futószalagon. Minden krumpli
# (sor) ugyanazt kapja: megmosod (strip), felszeleteled (split),
# a számokat számmá alakítod, rárakod a címkét (teljes alkohol),
# és beteszed a nagy tálba (adatok lista).

def adatok_feldolgozasa(fajlnev):
    sorok = fajl_betoltes(fajlnev)        # 2. lépés
    sorok.pop(0)                          # 3. a fejléc kidobása

    adatok = []                           # 4. az üres "nagy tál"

    for sor in sorok:                     # 5. végig a sorokon
        darabok = sor.strip().split(",")  #    sortörés le, feldarabolás

        # 6. számok átalakítása
        darabok[3] = float(darabok[3])    # HappinessScore
        darabok[4] = int(darabok[4])      # HDI
        darabok[5] = float(darabok[5])    # GDP_PerCapita
        darabok[6] = int(darabok[6])      # Beer_PerCapita
        darabok[7] = int(darabok[7])      # Spirit_PerCapita
        darabok[8] = int(darabok[8])      # Wine_PerCapita

        # 7. teljes alkohol - figyelj a sorrendre: sör, BOR, rövid!
        teljes = teljes_alkohol(darabok[6], darabok[8], darabok[7])
        darabok.append(teljes)

        adatok.append(darabok)            # 8. lista a listába

    return adatok

# ⚠️ CSAPDA: a feladat a 7. lépésben Beer, Spirit, Wine sorrendben
#    sorolja az oszlopokat, de a függvény sör, BOR, rövid sorrendet vár.
#    Ha sorban adod át (6, 7, 8), a bort 40-nel szorzod - és senki sem
#    szól, csak rossz lesz az eredmény.
# 💡 Ha valamelyik oszlopban tizedes szám is előfordulna, a float()
#    mindig biztonságos választás az int() helyett.


# =========================================================================
# 4. SZŰRÉS ÉS MENTÉS  (15 pont)
# =========================================================================
# EMLÉKEZTETŐ: mint egy szórakozóhely kidobója. Bekéri a határt
# ("csak X feletti mehet be"), végignézi a sort, a megfelelőket
# beengedi, és csak a nevüket, pontszámukat írja fel egy listára.

def szures_es_mentes(adatok):
    beirt = input("Add meg a minimális teljes alkoholfogyasztást: ")

    try:
        hatar = int(beirt)                # 2. számmá alakítás
    except ValueError:
        return None                       #    nem egész szám -> üres érték

    kiirando = []                         # 3. új lista
    for sor in adatok:
        if sor[-1] > hatar:               # a) utolsó oszlop > határ
            # b) + c) ország, boldogság, teljes alkohol - vesszővel
            kiirando.append(f"{sor[0]},{sor[3]},{sor[-1]}")

    # 4. fájlba írás UTF-8 kódolással
    with open("eredmenyek.txt", "w", encoding="utf-8") as f:
        for sor in kiirando:
            f.write(sor + "\n")

    print(f"{len(kiirando)} ország adata elmentve az eredmenyek.txt fájlba.")

# ⚠️ A sor[-1] mindig az UTOLSÓ elem - pont a teljes alkohol, amit a
#    feldolgozáskor a végére fűztünk.
# ⚠️ A write() nem tesz magától sortörést, a "\n" kell a végére.
# 💡 Másik megoldás a 3.c lépésre:
#    ",".join([sor[0], str(sor[3]), str(sor[-1])])
#    A join csak szövegeket tud összefűzni, ezért kell az str().


# =========================================================================
# 5. MENÜ  (10 pont)
# =========================================================================
# EMLÉKEZTETŐ: mint egy italautomata. Addig várja a gombnyomást, amíg
# ki nem kapcsolod (Q). Rossz gombra csak újra kiírja a választékot.

adatok = adatok_feldolgozasa("HappinessAlcoholConsumption.csv")   # 1.

while True:
    print("********FŐMENÜ*******************")
    print("(M) Adott fogyasztás feletti értékek fájlba írása")
    print("(Q) Kilépés")

    valasztas = input("Választás: ").upper()    # 5. kis- és nagybetű is jó

    if valasztas == "M":
        szures_es_mentes(adatok)                # 4.
    elif valasztas == "Q":
        print("Viszlát!")
        break
    # bármi más: nincs teendő, a ciklus újra kiírja a menüt (3.)

# ⚠️ Az .upper() miatt az "m" is "M" lesz - így elég egyetlen
#    összehasonlítás a  valasztas == "M" or valasztas == "m"  helyett.