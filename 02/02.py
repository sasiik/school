# Generoi kolme satunnaista kokonaislukua v ̈alilt ̈a 1-6luku1 = random.randint(1, 6)luku2 = random.randint(1, 6)luku3 = random.randint(1, 6)# Tulosta luvutprint("Ensimm ̈ainen luku:", luku1)print("Toinen luku:", luku2)print("Kolmas luku:", luku3)
import random


def kokeillaan_if_elsea_ver1(sana):
    """Kokeillaan, miten if-lause yksityiskohtineen toimii"""
    sanan_pituus = len(sana)
    sanallinen_arvio = ""

    if sanan_pituus % 2 == 0:
        sanallinen_arvio = "pariton sana"
    else:
        sanallinen_arvio = "parillinen sana"

    print(sanallinen_arvio)


def kokeillaan_if_elsea_ver2(sana):
    """Kokeillaan, miten if-lause yksityiskohtineen toimii"""

    sanan_pituus = len(sana)
    sanallinen_arvio = ""

    if sanan_pituus % 2 == 0:
        sanallinen_arvio = "pariton sana"
    elif sanan_pituus % 2 == 1:
        sanallinen_arvio = "parillinen sana"
    elif sanan_pituus % 2 == 2:
        sanallinen_arvio = "parillinen sana"

    print(sanallinen_arvio)


kokeillaan_if_elsea_ver1("jokinmerkkijono")
kokeillaan_if_elsea_ver1("jokin merkkijono")
kokeillaan_if_elsea_ver2("jokinmerkkijono")
kokeillaan_if_elsea_ver2("jokin merkkijono")


def anna_pallokasa(luku):
    """Palauttaa parillista pallojoukoista koostuvan kasan, jos parametrina saatu luku on parillinen. Muutoin palauttaa parittomista pallojoukoista koostuvan kasan."""
    jakojaannos = luku % 2
    pallokasa = ""
    if jakojaannos == 0:
        pallokasa = " oo \n oooo \n oooooo \n oooooooo \n"
    else:
        pallokasa = " o \n ooo \n ooooo \n ooooooo \n"

    return pallokasa


print()
kokeilu1 = anna_pallokasa(25)
print(kokeilu1)
kokeilu2 = anna_pallokasa(112)
print(kokeilu2)


def tulosta_sanoja(a, b, c, d):
    """Tulostaa argumenttien a, b, c ja d sisällöt kaikissa mahdollisissa eri järjestyksissä allekkain."""
    print(a, b, c, d)
    print(a, b, d, c)
    print(a, c, b, d)
    print(a, c, d, b)
    print(a, d, b, c)
    print(a, d, c, b)
    print(b, a, c, d)
    print(b, a, d, c)
    print(b, c, a, d)
    print(b, c, d, a)
    print(b, d, a, c)
    print(b, d, c, a)
    print(c, a, b, d)
    print(c, a, d, b)
    print(c, b, a, d)
    print(c, b, d, a)
    print(c, d, a, b)
    print(c, d, b, a)
    print(d, a, b, c)
    print(d, a, c, b)
    print(d, b, a, c)
    print(d, b, c, a)
    print(d, c, a, b)
    print(d, c, b, a)


tulosta_sanoja("to", "her", "ne", "keit")


def anna_arvosanana(pisteet):
    """Palauttaa parametrina saatuja pisteit ̈a vastaavankurssiarvosanan."""
    palautettava = 0
    if (pisteet >= 50.0):
        palautettava = '1'
    if (pisteet >= 60.0):
        palautettava = '2'
    if (pisteet >= 70.0):
        palautettava = '3'
    if (pisteet >= 80.0):
        palautettava = '4'
    if (pisteet >= 90.0):
        palautettava = '5'

    return palautettava


merkkijonona = input("Syotä arvosanaksi muunnettavat pisteet: ")
pisteita = float(merkkijonona)
arvosana = anna_arvosanana(pisteita)
print("Arvosana:", arvosana)


# Generoi kolme satunnaista kokonaislukua väliltä 1-6
luku1 = random.randint(1, 6)
luku2 = random.randint(1, 6)
luku3 = random.randint(1, 6)

# Tulosta luvut
print("Ensimmäinen luku:", luku1)
print("Toinen luku:", luku2)
print("Kolmas luku:", luku3)

# Tulosta summan
print("Summa: ", luku1 + luku2 + luku3)

# Tulosta tulon
print("Tulo: ", luku1 * luku2 * luku3)


luku1 = random.random()
luku2 = random.random()
luku3 = random.random()


# Tulosta luvut
print("Ensimmäinen luku:", luku1)
print("Toinen luku:", luku2)
print("Kolmas luku:", luku3)

# Tulosta summan
print("Summa: ", luku1 + luku2 + luku3)

# Tulosta tulon
print("Tulo: ", luku1 * luku2 * luku3)
