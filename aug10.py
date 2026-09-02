# ==========================================================
# PYTHON LECKE 6.
# Függvények, fájlkezelés, hibakezelés, while ciklus
# ==========================================================
#
# Ebben a leckében 4 fontos témát tanulunk meg:
#   1. Függvénydefiníciók  -> "A recept"
#   2. Fájlkezelés          -> "A napló"
#   3. Hibakezelés           -> "A biztonsági háló"
#   4. While ciklus          -> "Amíg... addig"
#
# Minden résznél lesz egy magyarázat, egy futtatható példa,
# és utána gyakorló feladatok ⭐ (könnyű) - ⭐⭐⭐ (nehéz) jelöléssel.
#
# Fontos: a feladatokban lévő "pass" és "# TODO" részeket neked
# kell kicserélni saját kóddal!
# ==========================================================


# ==========================================================
# 1. RÉSZ - FÜGGVÉNYDEFINÍCIÓK: "A RECEPT"
# ==========================================================
#
# Képzeld el, hogy írsz egy receptet egy szakácskönyvbe.
#
#   - A recept megírása (def)       -> ezt csak EGYSZER írod le
#   - A recept elkészítése (hívás)  -> ez ANNYISZOR történhet, ahányszor akarod
#   - A hozzávalók (paraméterek)    -> ezeket változtathatod recept közben
#   - A kész étel (return érték)    -> amit a végén "kapsz" a függvénytől
#
# Tehát a def kulcsszó nem csinál semmit azonnal - csak megjegyzi
# a receptet. A függvény csak akkor "fő meg", amikor meghívod!


def keszits_teat(fajta="fekete", cukor=1):
    """Ez egy recept arra, hogyan készíts teát."""
    print("Forralj fel egy kis vizet.")
    print(f"Tegyél bele {fajta} teát.")
    print(f"Adj hozzá {cukor} kanál cukrot.")
    return f"{fajta} tea kész, {cukor} kanál cukorral."


# Hívjuk meg a receptünket kétféleképpen:
eredmeny1 = keszits_teat()  # az alapértelmezett hozzávalókkal
eredmeny2 = keszits_teat("zöld", 2)  # más hozzávalókkal

print(eredmeny1)
print(eredmeny2)


# ⚠️ FIGYELEM - GYAKORI KEZDŐ HIBA! ⚠️
# Sose használj módosítható (mutable) típust - pl. listát - alapértelmezett
# paraméterként! Nézd meg ezt a "hibás receptet":
#
#   def hozzaad_elem(elem, lista=[]):
#       lista.append(elem)
#       return lista
#
# Ez olyan, mintha a receptedben lenne egy "közös tál", amit SOHA nem
# mosnak el a vendégek között. Az első vendég beletesz egy almát, és a
# következő vendégnél a tál MÁR NEM ÜRES, hanem tartalmazza az előző
# vendég almáját is! Python ugyanis a lista objektumot csak EGYSZER
# hozza létre, amikor a függvényt definiálod - és utána minden hívás
# ugyanazt a listát használja újra.
#
# A helyes megoldás: alapértelmezett érték legyen None, és a függvényen
# belül hozz létre új listát, ha szükséges. Ezt a 3. feladatban ki is
# próbálhatod!


# ---------------- GYAKORLATOK ----------------

# Feladat 1.1 ⭐
# Írj egy "koszontes(nev)" nevű függvényt, ami visszaadja ezt a szöveget:
# "Szia, <nev>!"
# Például: koszontes("Anna") -> "Szia, Anna!"


def koszontes(nev = "Olivér"):
    print(f"Szia,{nev}")

koszontes()


# Feladat 1.2 ⭐⭐
# Írj egy "negyzetszam(szam)" nevű függvényt, ami visszaadja a szám
# négyzetét. Ha nem adunk meg számot, alapértelmezetten szam=2 legyen.


def negyzetszam(szam=2):
    print(f"A szám négyzete:{szam**2}")

negyzetszam(16)



# Feladat 1.3 ⭐⭐⭐
# Írj egy "hozzaad_elem(elem, lista=None)" nevű függvényt, ami HELYESEN
# kezeli az alapértelmezett listát (ne essél bele a fenti ⚠️ hibába!).
# A függvény tegye hozzá az "elem"-et a listához, és adja vissza a
# listát. Ha nem adunk meg listát, a függvény hozzon létre egy ÚJ,
# üres listát minden híváskor.


def hozzaad_elem(elem, lista=None):
    # TODO: hazi
    pass 


# ==========================================================
# 2. RÉSZ - FÁJLKEZELÉS: "A NAPLÓ"
# ==========================================================
#
# Gondolj a fájlkezelésre úgy, mint egy papír naplóra:
#
#   - open(fájlnév, "w")   -> kinyitod a naplót, hogy ÍRJ bele (write)
#   - open(fájlnév, "r")   -> kinyitod a naplót, hogy OLVASS belőle (read)
#   - open(fájlnév, "a")   -> kinyitod a naplót, hogy HOZZÁÍRJ a végéhez (append)
#   - f.close()            -> becsukod a naplót
#
# A "with" szó egy VARÁZS-napló: automatikusan becsukja saját magát,
# amint végeztél vele - még akkor is, ha közben hiba történt!
# Ezért mindig "with"-et használunk fájlok kezelésére.

# Írjunk valamit a naplónkba:
with open("naplo.txt", "w", encoding="utf-8") as f:
    f.write("Ma tanultam Pythont!\n")
    f.write("Nagyon élveztem a leckét.\n")

# Olvassuk vissza, amit írtunk:
with open("naplo.txt", "r", encoding="utf-8") as f:
    tartalom = f.read()
    print(tartalom)


# ⚠️ FIGYELEM! ⚠️
# 1. Mindig add meg az encoding="utf-8" paramétert, különben a magyar
#    ékezetes betűk (á, é, ő, ű...) elromolhatnak!
# 2. Ha megpróbálsz egy nem létező fájlt "r" (olvasás) módban megnyitni,
#    a program HIBÁVAL leáll - "FileNotFoundError". Ezt a 3. részben
#    (hibakezelés) fogjuk megtanulni kezelni!


# ---------------- GYAKORLATOK ----------------

# Feladat 2.1 ⭐
# Írj egy "bevasarlolista.txt" nevű fájlt, amibe 3 bevásárlós tételt
# írsz, mindegyiket külön sorba (pl. "kenyér", "tej", "alma").

# TODO: nyisd meg a fájlt írásra, és írd bele a 3 tételt


# Feladat 2.2 ⭐⭐
# Olvasd be a "bevasarlolista.txt" fájlt, és írasd ki minden sorát
# sorszámmal együtt, például:
# 1. kenyér
# 2. tej
# 3. alma
# Tipp: f.readlines() egy listát ad vissza a sorokból.

# TODO: nyisd meg a fájlt olvasásra, és írasd ki a sorokat sorszámmal


# Feladat 2.3 ⭐⭐⭐
# Nyisd meg a "bevasarlolista.txt" fájlt HOZZÁÍRÁS ("a") módban, és
# tegyél hozzá egy új tételt ("sajt") anélkül, hogy a régi tartalom
# eltűnne. Utána olvasd be újra a fájlt, és írasd ki az egészet.

# TODO: nyisd meg a fájlt "a" módban, írd hozzá az új tételt,
# majd olvasd vissza és írasd ki az egész tartalmat


# ==========================================================
# 3. RÉSZ - HIBAKEZELÉS: "A BIZTONSÁGI HÁLÓ"
# ==========================================================
#
# Képzelj el egy kötéltáncost a cirkuszban:
#
#   - try:      -> a kötéltáncos elindul a kötélen (kockázatos kód)
#   - except:   -> ha leesik, a biztonsági háló elkapja (hibát kezeljük,
#                  a program NEM áll le)
#   - finally:  -> az előadás ezután MINDIG folytatódik, essen le
#                  a táncos vagy sem (ez a kód mindig lefut)
#
# Anélkül, hogy a "try/except"-et használnánk, egy hiba (pl. nullával
# osztás) azonnal LEÁLLÍTJA a teljes programot. A try/except olyan,
# mint egy háló, ami elkapja a hibát, és a program tovább futhat.

try:
    szam = int("nem szám")
except ValueError:
    print("Hoppá! Ez nem volt érvényes szám.")
finally:
    print("Ez a sor MINDIG lefut, akár volt hiba, akár nem.")


# Többféle háló, többféle eséshez:
try:
    eredmeny = 10 / 0
except ZeroDivisionError:
    print("Nullával nem lehet osztani!")
except ValueError:
    print("Ez egy másik típusú hiba lenne.")


# ⚠️ FIGYELEM! ⚠️
# Soha ne használj csupasz "except:" (kiírás nélkül)! Ez olyan, mintha
# a biztonsági háló AKKORA lenne, hogy nemcsak a kötéltáncost kapja el,
# hanem véletlenül az egész cirkuszi sátrat is megállítja - vagyis
# elkap olyan dolgokat is, amiket valójában nem szerettél volna
# elkapni (pl. amikor a felhasználó Ctrl+C-vel le akarja állítani a
# programot). Mindig írd ki, MILYEN hibát vársz: except ValueError,
# except ZeroDivisionError, stb.


# ---------------- GYAKORLATOK ----------------

# Feladat 3.1 ⭐
# Próbáld meg elosztani a 10-et 0-val try/except blokkban, és írasd ki
# a "Nullával nem lehet osztani!" üzenetet, ha hiba történik.

# TODO: írd meg a try/except blokkot


# Feladat 3.2 ⭐⭐
# Próbálj meg megnyitni egy NEM létező fájlt (pl. "nincsilyen.txt")
# olvasásra. Kapd el a "FileNotFoundError" hibát, és írj ki egy barátságos
# üzenetet, pl. "A fájl nem található!"

# TODO: írd meg a try/except blokkot
try:
    with open("nincsilyen.txt", "r", encoding="utf-8") as f:
        tartalom = f.read()
        print(tartalom)
except FileNotFoundError:
    print("A fájl nem található")

    


# Feladat 3.3 ⭐⭐⭐
# Az alábbi változóban két, felhasználótól "bekért" szöveg van (ezeket
# most fix értékként adjuk meg, hogy a fájl mindig hiba nélkül fusson -
# az interaktív verziót lásd a megjegyzésben alatta).
#
# Próbáld meg elosztani "szam1"-et "szam2"-vel. Kezeld le mindkét
# lehetséges hibát: ha valamelyik nem szám (ValueError), és ha
# "szam2" nulla (ZeroDivisionError).

szam1_szoveg = "20"
szam2_szoveg = "0"

# Interaktív verzió (csak megjegyzésben, hogy a fájl input() nélkül fusson):
# szam1_szoveg = input("Adj meg egy számot: ")
# szam2_szoveg = input("Adj meg egy másik számot: ")

# TODO: alakítsd át a két szöveget számmá, és próbáld meg elosztani
# őket try/except blokkban, lekezelve mindkét hibalehetőséget


# ==========================================================
# 4. RÉSZ - WHILE CIKLUS: "AMÍG... ADDIG"
# ==========================================================
#
# Gondolj egy biztonsági őrre egy klub bejáratánál:
#
#   "AMÍG van szabad hely a klubban, ADDIG enged be új vendégeket."
#
# Ez pontosan úgy működik, mint a while ciklus: a feltételt (van-e
# szabad hely?) MINDEN körben újra megvizsgálja, és amíg IGAZ, addig
# fut tovább a ciklus törzse.

kapacitas = 5
bent_levok = 0

while bent_levok < kapacitas:
    bent_levok += 1
    print(f"Vendég beengedve. Bent van: {bent_levok}/{kapacitas}")

print("A klub megtelt, a bejárat bezárt!")


# ⚠️ FIGYELEM - VÉGTELEN CIKLUS! ⚠️
# Mi történik, ha az őr elfelejt számolni? Ha a "bent_levok += 1" sor
# hiányzik, a feltétel SOHA nem válik hamissá, és az őr a
# VÉGTELENSÉGIG enged be vendégeket egy klubba, ami már réges-rég
# szétrobbant. A programod ilyenkor lefagy (végtelen ciklusba kerül)!
# Mindig ellenőrizd, hogy a ciklusban VALAMI változik, ami előbb-utóbb
# hamissá teszi a feltételt.


# ---------------- GYAKORLATOK ----------------

# Feladat 4.1 ⭐
# Írj egy while ciklust, ami visszaszámol 5-től 1-ig, és minden számot
# kiír (5, 4, 3, 2, 1).

# TODO: írd meg a while ciklust


# Feladat 4.2 ⭐⭐
# Írj egy while ciklust, ami összeadja az 1-től 10-ig terjedő számokat,
# és a végén kiírja az összeget (55-nek kell lennie).

# TODO: írd meg a while ciklust


# Feladat 4.3 ⭐⭐⭐
# Készíts egy egyszerű "találd ki a számot" játékot! A titkos szám
# legyen 7. Az alábbi lista tartalmazza a "felhasználó" tippjeit
# (fix értékek, hogy a fájl input() nélkül is lefusson).
#
# Használj while ciklust, ami végigmegy a tippeken, és amikor eltalálja
# a titkos számot, a "break" kulcsszóval lépjen ki a ciklusból, és
# írja ki: "Eltaláltad! A szám: 7"

titkos_szam = 7
tippek = [3, 10, 5, 7, 9]  # a "felhasználó" tippjei sorban

# Interaktív verzió (csak megjegyzésben):
# tipp = int(input("Találd ki a titkos számot: "))
# while tipp != titkos_szam:
#     tipp = int(input("Nem jó, próbáld újra: "))

# TODO: írd meg a while ciklust a "tippek" listával és break-kel


# ==========================================================
# GRATULÁLOK, VÉGIGÉRTÉL A LECKÉN! 🎉
# ==========================================================
# Ha elakadtál valahol, nézd át újra a magyarázatokat, vagy kérdezd
# meg a tanárodat. Sok sikert a gyakorlatokhoz!
