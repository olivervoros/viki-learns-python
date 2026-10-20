# ============================================================
#  A DATETIME MODUL – EGYSZERŰEN
#  Dátumok, időpontok és időtartamok kezelése Pythonban
# ============================================================
#
#  Képzeld el, hogy van egy SZERSZÁMOSLÁDÁD AZ IDŐHÖZ. Benne van:
#
#    date       📅  falinaptár            -> csak a nap (év, hónap, nap)
#    time       ⏰  falióra               -> csak az idő (óra, perc, mp)
#    datetime   📱  telefon zárképernyője -> nap ÉS idő együtt
#    timedelta  ⏳  homokóra              -> időtartam ("3 nap múlva")
#
#  Használat előtt ki kell nyitni a ládát:

from datetime import date, time, datetime, timedelta


# ============================================================
#  1. MI A MAI DÁTUM ÉS A PONTOS IDŐ?
# ============================================================
#
#  EMLÉKEZTETŐ:
#  Olyan, mintha ránéznél a naptárra vagy a telefonodra.
#  date.today()   -> a naptár: melyik nap van ma?
#  datetime.now() -> a telefon: melyik nap van, és hány óra?

print("--- 1. Mai dátum és idő ---")

ma = date.today()
most = datetime.now()

print(ma)    # pl. 2026-10-20
print(most)  # pl. 2026-10-20 18:42:15.123456

# Egyes részeket is elkérhetsz, ahogy a naptárról is
# leolvashatod csak a hónapot:
print("Év:   ", most.year)
print("Hónap:", most.month)
print("Nap:  ", most.day)
print("Óra:  ", most.hour)
print("Perc: ", most.minute)

# 💡 A time-ot ritkábban használjuk önmagában, de így néz ki:
ebedido = time(12, 30)
print("Ebédidő:", ebedido)  # 12:30:00


# ============================================================
#  2. SAJÁT DÁTUM LÉTREHOZÁSA
# ============================================================
#
#  EMLÉKEZTETŐ:
#  Itt TE írod be a dátumot a naptárba, tollal.

print("\n--- 2. Saját dátum ---")

szuletesnap = date(1990, 5, 17)
vizsga = datetime(2026, 12, 1, 9, 30)   # 2026. dec. 1., 9:30

print(szuletesnap)  # 1990-05-17
print(vizsga)       # 2026-12-01 09:30:00

# ⚠️ A sorrend mindig: ÉV, HÓNAP, NAP, utána ÓRA, PERC.
# ⚠️ date(2026, 2, 30) hibát ad, mert február 30. nem létezik!


# ============================================================
#  3. SZÉP FORMÁZÁS: strftime()
# ============================================================
#
#  EMLÉKEZTETŐ:
#  A dátum egy tárgy, a strftime pedig egy CÍMKENYOMTATÓ.
#  Te döntöd el, hogyan nézzen ki a címke.
#
#  Jegyezd meg: str-F-time = string FROM time
#               -> DÁTUMBÓL SZÖVEG
#
#  A leggyakoribb kódok:
#    %Y  év (4 jegy)        2026
#    %m  hónap (2 jegy)     10
#    %d  nap (2 jegy)       20
#    %H  óra (24 órás)      18
#    %M  perc               42
#    %S  másodperc          15
#    %A  a hét napja        Tuesday
#    %B  hónap neve         October

print("\n--- 3. strftime ---")

most = datetime.now()

print(most.strftime("%Y.%m.%d."))           # pl. 2026.10.20.
print(most.strftime("%H:%M"))               # pl. 18:42
print(most.strftime("%Y. %m. %d. %H:%M"))   # pl. 2026. 10. 20. 18:42
print(most.strftime("Ma %A van."))          # pl. Ma Tuesday van.

# 💡 A %A és a %B alapból ANGOLUL írja ki a neveket.


# ============================================================
#  4. SZÖVEGBŐL DÁTUM: strptime()
# ============================================================
#
#  EMLÉKEZTETŐ:
#  Valaki kézzel felírta egy cetlire: "2026.12.24."
#  Te pedig BEÍROD A NAPTÁRBA. Ehhez meg kell mondanod a
#  Pythonnak, milyen formában van írva a cetli.
#
#  Jegyezd meg: str-P-time = string PARSE time
#               -> SZÖVEGBŐL DÁTUM

print("\n--- 4. strptime ---")

szoveg = "2026.12.24."
karacsony = datetime.strptime(szoveg, "%Y.%m.%d.")

print(karacsony)  # 2026-12-24 00:00:00

# ⚠️ A mintának és a szövegnek PONTOSAN egyeznie kell,
#    még a pontoknak és kötőjeleknek is!
#    datetime.strptime("2026-12-24", "%Y.%m.%d.")  -> ValueError

# 💡 Ha csak a dátum rész kell (az óra nem), használd a .date()-et:
print(karacsony.date())  # 2026-12-24


# ============================================================
#  5. SZÁMOLÁS AZ IDŐVEL: timedelta
# ============================================================
#
#  EMLÉKEZTETŐ:
#  A timedelta egy HOMOKÓRA. Nem egy konkrét napot jelent,
#  hanem egy IDŐTARTAMOT: "10 nap", "2 óra", "3 hét".
#  Egy naphoz hozzáadhatsz egy homokórányi időt.

print("\n--- 5. timedelta ---")

ma = date.today()

egy_het_mulva = ma + timedelta(days=7)
tegnap = ma - timedelta(days=1)

print("Egy hét múlva:", egy_het_mulva)
print("Tegnap:       ", tegnap)

# Két dátumot ki is vonhatsz egymásból.
# Az eredmény egy timedelta lesz (egy homokóra):
karacsony = date(ma.year, 12, 24)
hatra_van = karacsony - ma
print("Karácsonyig még", hatra_van.days, "nap van.")

# 💡 Mértékegységek: weeks, days, hours, minutes, seconds
hosszu_hetvege = timedelta(days=3, hours=5)
print("Hosszú hétvége:", hosszu_hetvege)  # 3 days, 5:00:00

# ⚠️ date-ből csak date-et lehet kivonni, datetime-ból datetime-ot.
#    Ha keverni szeretnéd, a datetime-ot alakítsd át: .date()


# ============================================================
#  6. ÖSSZEHASONLÍTÁS
# ============================================================
#
#  EMLÉKEZTETŐ:
#  A dátumok úgy viselkednek, mint a számok egy számegyenesen.
#  A KORÁBBI dátum a "kisebb", a KÉSŐBBI a "nagyobb".

print("\n--- 6. Összehasonlítás ---")

hatarido = date(2026, 11, 1)

if date.today() > hatarido:
    print("Lejárt a határidő!")
else:
    print("Még van időd.")


# ============================================================
#  FELADATOK
# ============================================================

print("\n========== FELADATOK ==========")

# ------------------------------------------------------------
# 1. feladat ⭐
# Írasd ki a mai dátumot ebben a formában: 2026/10/20
# ------------------------------------------------------------
print("\n1. feladat:")
# TODO: ide írd a megoldást
pass


# ------------------------------------------------------------
# 2. feladat ⭐⭐
# Kérd be a felhasználó születési dátumát ÉÉÉÉ-HH-NN formában,
# és írd ki, hány napos.
# (Most fix értékkel dolgozz, az input() sor maradjon kommentben!)
# ------------------------------------------------------------
print("\n2. feladat:")
# szoveg = input("Születési dátum (ÉÉÉÉ-HH-NN): ")
szoveg = "1990-05-17"
# TODO: ide írd a megoldást
pass


# ------------------------------------------------------------
# 3. feladat ⭐
# Egy könyvtári könyvet ma kölcsönöztél ki, és 21 napod van
# visszavinni. Írd ki a határidőt ÉÉÉÉ.HH.NN. formában.
# ------------------------------------------------------------
print("\n3. feladat:")
# TODO: ide írd a megoldást
pass


# ------------------------------------------------------------
# 4. feladat ⭐⭐
# Írd ki, hány nap van még szilveszterig (december 31.).
# ------------------------------------------------------------
print("\n4. feladat:")
# TODO: ide írd a megoldást
pass


# ------------------------------------------------------------
# 5. feladat ⭐⭐⭐  (ZÁRÓFELADAT – minden együtt)
# Egy edzőterem-bérlet kezdete szövegként érkezik: "2026.10.01."
# A bérlet 30 napig érvényes.
#   a) Alakítsd a szöveget dátummá (strptime)
#   b) Számold ki a lejárat napját (timedelta)
#   c) Írd ki a lejáratot ÉÉÉÉ.HH.NN. formában (strftime)
#   d) Vizsgáld meg, érvényes-e még ma a bérlet (összehasonlítás)
#   e) Ha érvényes, írd ki, hány nap van még hátra
# ------------------------------------------------------------
print("\n5. feladat:")
berlet_kezdete = "2026.10.01."
# TODO: ide írd a megoldást
pass


# ============================================================
#  MEGOLDÁSOK
#  (Előbb próbáld meg egyedül, csak utána nézz ide! 😉)
# ============================================================

print("\n========== MEGOLDÁSOK ==========")

# --- 1. megoldás ---
print("\n1. megoldás:")
print(date.today().strftime("%Y/%m/%d"))


# --- 2. megoldás ---
print("\n2. megoldás:")
# szoveg = input("Születési dátum (ÉÉÉÉ-HH-NN): ")
szoveg = "1990-05-17"
szuletes = datetime.strptime(szoveg, "%Y-%m-%d").date()
kor_napban = (date.today() - szuletes).days
print(f"Te {kor_napban} napos vagy!")
# 💡 A .date() azért kell, mert date-ből csak date-et lehet kivonni.


# --- 3. megoldás ---
print("\n3. megoldás:")
hatarido = date.today() + timedelta(days=21)
print("Visszaviteli határidő:", hatarido.strftime("%Y.%m.%d."))


# --- 4. megoldás ---
print("\n4. megoldás:")
ma = date.today()
szilveszter = date(ma.year, 12, 31)
print(f"Szilveszterig még {(szilveszter - ma).days} nap van.")
# 💡 A ma.year miatt jövőre is működik a program, nem kell átírni.


# --- 5. megoldás ---
print("\n5. megoldás:")
berlet_kezdete = "2026.10.01."

kezdet = datetime.strptime(berlet_kezdete, "%Y.%m.%d.").date()   # a)
lejarat = kezdet + timedelta(days=30)                            # b)
print("A bérlet lejár:", lejarat.strftime("%Y.%m.%d."))          # c)

ma = date.today()
if ma <= lejarat:                                                # d)
    hatra = (lejarat - ma).days                                  # e)
    print(f"A bérlet érvényes, még {hatra} nap van hátra.")
else:
    print("A bérlet lejárt, ideje megújítani!")


# ============================================================
#  AMIT MA GYAKOROLTUNK
# ============================================================
#
#  📅  date(év, hónap, nap)         -> egy nap a naptárban
#  ⏰  time(óra, perc)              -> egy időpont az órán
#  📱  datetime(...)                -> nap ÉS idő együtt
#  ⏳  timedelta(days=..., ...)     -> időtartam (homokóra)
#
#  date.today()     -> mai dátum
#  datetime.now()   -> most (dátum + idő)
#
#  .strftime("%Y.%m.%d.")           -> DÁTUMBÓL SZÖVEG (címkenyomtató)
#  datetime.strptime(szoveg, minta) -> SZÖVEGBŐL DÁTUM (cetliről a naptárba)
#
#  datum2 - datum1                  -> timedelta, napok: .days
#  datum + timedelta(days=7)        -> egy hét múlva
#  datum1 < datum2                  -> korábbi-e?
#
#  Egy mondatban:
#  date = naptár, time = óra, datetime = mindkettő,
#  timedelta = homokóra. A strftime dátumból szöveget csinál,
#  a strptime szövegből dátumot.
# ============================================================