#!/usr/bin/env python3
"""
Tehtävät:
1. Luokka Klapi (puuloki), jolla on:
   - kuvaus (merkkijonona, esim. puulaji)
   - massa (numerona)
   - tieto siitä, onko klapi sytytetty palamaan
   - metodi palaa(), joka vähentää massaa portaittain (esim. 1 yksikkö kerrallaan)
   - __str__()-metodi, joka esittää klapin tiedot

2. Luokka Tulipesä, johon voi laittaa useita klapeja.
   - Sisäisesti klapit voidaan tallentaa listaan.
   - Tulipesässä on metodi, jolla kaikki klapit sytytetään ja samanaikaisesti palaa (kutsuu jokaiselle klapille palaa-metodia).
   - Tulipesällä on metodi, joka palauttaa vielä palamattoman klapimassan.
   - __str__()-metodi esittää tulipesän tilanteen

3. Histogrammi-ohjelma:
   - Ohjelma lukee syötteenä merkkijonon.
   - Se selvittää, mitä merkkejä syötteessä esiintyy, ja laskee niiden esiintymistiheydet.
   - Tuloksena piirretään histogrammi, jossa kullakin rivillä on merkki, kaksoispiste, ja sitten 'o'-merkkejä lukumäärän mukaan.
   - Jos merkkien määrä ylittää ruudulle mahtuvan leveyden, histogrammin pylväät skaalataan.
   - Lisäksi ohjelmaan voi antaa oman aakkoston, jolloin histogrammi lasketaan vain näiden merkkien osalta (mukana myös mahdollisesti nolla-arvoisia pylväitä).

Järjestelmän rakenne:
- Luokat ja funktiot on määritelty erillisinä osioina.
- Lopussa pääohjelmassa käyttäjältä kysytään, haluaako hän testata luokkia vai ajaa histogrammi-ohjelman.
"""

# Task 1: Luokka Klapi


class Klapi:
    def __init__(self, kuvaus, massa):
        """
        Alustaa klapin: määrittää puulajin (kuvaus), massan ja sytytetty-tilan (alkutilana False).
        """
        self.kuvaus = kuvaus
        self.massa = massa
        self.sytytetty = False

    def sytyta(self):
        """
        Asettaa klapin syttyneeksi.
        """
        self.sytytetty = True

    def palaa(self, palamis_aste=1):
        """
        Simuloi palamista pienentämällä massaa annettuna portaittain (oletuksena 1 yksikkö).
        Varmistaa, ettei massa mene negatiiviseksi.
        """
        if self.sytytetty and self.massa > 0:
            self.massa -= palamis_aste
            if self.massa < 0:
                self.massa = 0

    def __str__(self):
        return f"Klapi(kuvaus={self.kuvaus}, massa={self.massa}, sytytetty={self.sytytetty})"


# Task 2: Luokka Tulipesä
class Tulipesa:
    def __init__(self):
        """
        Alustaa tyhjän tulipesän, jossa on lista klapeista.
        """
        self.klapit = []

    def lisaa_klapi(self, klapi):
        """
        Lisää klapin tulipesään.
        """
        self.klapit.append(klapi)

    def sytyta_kaikki(self):
        """
        Sytyttää kaikki tulipesän klapit.
        """
        for klapi in self.klapit:
            klapi.sytyta()

    def palaa_kaikki(self, palamis_aste=1):
        """
        Simuloi palamista kaikille klapeille samalla sivulla.
        """
        for klapi in self.klapit:
            if klapi.sytytetty:
                klapi.palaa(palamis_aste)

    def palamaton_massa(self):
        """
        Palauttaa tulipesässä olevan palamattoman klapimassan.
        """
        return sum(klapi.massa for klapi in self.klapit)

    def __str__(self):
        klapit_tiedot = "\n".join(str(klapi) for klapi in self.klapit)
        return f"Tulipesa tilanne:\n{klapit_tiedot}\nYhteinen palamaton massa: {self.palamaton_massa()}"


# Task 3: Histogrammi-ohjelma
def count_frequencies(s, custom_alphabet=None):
    """
    Laskee merkkijonon s merkkien esiintymistiheydet.
    Jos custom_alphabet annetaan, alustaa laskennan vain niillä merkeillä.
    """
    freq = {}
    if custom_alphabet is None or custom_alphabet == "":
        # Käytä kaikkia syötteen merkkejä
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
    else:
        # Alusta aakkosilla ja lisää myös puuttuvat merkit nolla-arvoina
        for ch in custom_alphabet:
            freq[ch] = 0
        for ch in s:
            if ch in freq:
                freq[ch] += 1
    return freq


def draw_histogram(freq, max_width=50):
    """
    Piirtää histogrammin annetuista merkkien esiintymistiheyksistä.
    Jos suurin lukumäärä ylittää max_width:n, pylväät skaalataan.
    """
    if not freq:
        return
    max_count = max(freq.values())
    scale = 1
    if max_count > max_width:
        scale = max_width / max_count

    # Käydään läpi merkit aakkosjärjestyksessä
    for ch in sorted(freq.keys()):
        count = freq[ch]
        # Skaalaa tarvittaessa
        if scale < 1:
            num_symbols = int(round(count * scale))
        else:
            num_symbols = count
        # Jos merkille kuuluu vähintään yksi mutta pyöristyksessä tulee 0, piirretään ainakin 1 symboli
        if count > 0 and num_symbols == 0:
            num_symbols = 1
        print(f"{ch}:{'o' * num_symbols}")


def run_histogram_program():
    """
    Kysyy käyttäjältä syötteen ja mahdollisen omat aakkoset, sekä piirtää histogrammin.
    """
    input_string = input("Anna merkkijono: ")
    custom_alphabet = input(
        "Anna oma aakkosto (tai paina Enter ottaaksesi kaikki merkit): ")
    frequencies = count_frequencies(input_string, custom_alphabet)
    print("\nHistogrammi:")
    draw_histogram(frequencies)


# Testausfunktiot Klapi ja Tulipesä -luokkien toiminnan havainnollistamiseksi
def test_klapi_and_tulipesa():
    print("Testataan Klapi ja Tulipesa -luokkia\n")

    # Luodaan pari klapia
    klapi1 = Klapi("Koivu", 10)
    klapi2 = Klapi("Mänty", 15)
    print("Alkuperäiset klapit:")
    print(klapi1)
    print(klapi2)
    print("\nSytytetään klapi1 ja poltetaan sitä muutaman kerran:")

    # Sytytetään ensimmäinen klapi ja simuloidaan palamista
    klapi1.sytyta()
    for i in range(3):
        klapi1.palaa()
        print(f"Vaihe {i+1}: {klapi1}")

    # Luodaan tulipesä, lisätään siihen klapit ja sytytetään ne
    tulipesa = Tulipesa()
    tulipesa.lisaa_klapi(klapi1)
    tulipesa.lisaa_klapi(klapi2)
    tulipesa.sytyta_kaikki()

    print("\nTulipesä ennen lisäpolttoja:")
    print(tulipesa)

    # Simuloidaan tulipesässä palamista usealla askeleella
    for i in range(5):
        tulipesa.palaa_kaikki()
        print(f"\nTulipesä palamisen jälkeen vaihe {i+1}:")
        print(tulipesa)


# Pääohjelma, joka antaa käyttäjän valita testauksen tai histogrammi-toiminnon
if __name__ == "__main__":
    print("Valitse toiminto:")
    print("1. Testaa Klapi ja Tulipesa -luokkia")
    print("2. Suorita histogrammi-ohjelma")
    choice = input("Valintasi (1 tai 2): ").strip()
    if choice == "1":
        test_klapi_and_tulipesa()
    elif choice == "2":
        run_histogram_program()
    else:
        print("Virheellinen valinta!")
