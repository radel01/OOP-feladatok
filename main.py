import oop1

# eljárások
adatokListaja = []


def beolvasas():
    beFajl = open("fajl/csoport.txt", "r", encoding="utf-8")

    beFajl.readline()
    sorok = beFajl.readlines()

    for sor in sorok:
        tisztitottSor = sor.strip()
        daraboltSor = tisztitottSor.split("/")
        # példányosítás
        csoportTag = oop1.Csoport(daraboltSor[0], daraboltSor[1], daraboltSor[2])
        # belefűzzük az objektumot
        adatokListaja.append(csoportTag)
        beFajl.close()


def kiir():
    for index in range(0, len(adatokListaja), 1):
        print(adatokListaja[index])


def sorokSzama():
    sorSzam = len(adatokListaja)
    print(f"A tanulók száma: {sorSzam}.")


def megszamlalas():
    osszeg = 0
    for index in range(0, len(adatokListaja), 1):
        osszeg += adatokListaja[index].atlag

    if len(adatokListaja) == 0:
        atlag = 0
    else:
        atlag = osszeg / len(adatokListaja)
    print(f"A suli átlag: {atlag}.")


def elsosok():
    osszeg = 0
    for index in range(0, len(adatokListaja), 1):
        if adatokListaja[index].evfolyam == 1:
            osszeg += 1
    print(f"Az elsősök száma: {osszeg}.")


# főprogram
beolvasas()
kiir()
sorokSzama()
megszamlalas()
elsosok()
