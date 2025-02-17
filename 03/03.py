# -----------------------------------------------------------
#  Kotitehtävät 3
#  Nimi: Stupko Stanislav
# -----------------------------------------------------------

def as_spaced(sentence, space):
    """
    Returns a version of 'sentence' in which each character 
    is separated by the string 'space'.
    Example: as_spaced("text", " ") -> "t e x t"
    """
    result = ""
    i = 0
    # We iterate over each character in 'sentence'
    while i < len(sentence):
        symbol = sentence[i]
        result += symbol
        # Add the separator 'space' after each character,
        # except for the last one (to avoid trailing spaces).
        if i < len(sentence) - 1:
            result += space
        i += 1
    return result


# Test for task 1
print("=== Task 1 Test: as_spaced ===")
print(as_spaced("I REALLY NEED MORE SPACE", " "))
# Example output: I   R E A L L Y   N E E D   M O R E   S P A C E


def split_experiments():
    """
    Demonstrates usage of split, indexing, string conversions, etc.
    Includes bullet-point findings as comments.
    """
    # Pari löytynyttä temppua:
    virke = "Sain asian selville. Kokeile vaikka."
    print("\n=== Task 2: Split Experiments ===")
    print("Original string:", virke)
    kaikki_palat = virke.split(".")
    print("Split with '.' ->", kaikki_palat)
    eka_pala = kaikki_palat[0]
    print("eka_pala =", eka_pala)

    # - Huomaa, että split(".") pilkkoo merkkijonon pisteen kohdalta.
    # - kaikki_palat on lista, jonka kukin alkio on osa merkkijonoa ilman sitä erotinta (".")
    # - Jos haluat toisen palan, voit pyytää kaikki_palat[1] jne. Ole kuitenkin varovainen,
    #   jos pisteitä on vähemmän tai enemmän.
    # - Indeksointi [0] antaa listan ensimmäisen (nollannen) alkion, [1] toisen jne.

    # Jotain muuta koodia:
    liukuluku = 7.62
    merkkeina = str(liukuluku)
    print("\nFloat as string:", merkkeina)
    # - Kun teemme str(7.62), saamme "7.62" (tyyppi 'str')
    alkupala = merkkeina.split(".")[0]  # pilkotaan pisteen kohdalta
    print("alkupala =", alkupala)      # "7"

    # - Jos alkupala on '7' (merkkijonona), niin alkupala+alkupala = '77'
    print("alkupala + alkupala =", alkupala + alkupala)
    # - Mutta int(alkupala) + int(alkupala) = 14
    print("int(alkupala) + int(alkupala) =", int(alkupala) + int(alkupala))


# Run Task 2 experiments
split_experiments()


def classify_user_inputs():
    """
    Reads words from user until 'quit'. 
    Classifies each word based on:
      - odd length & same first/last letter -> "It is odd with the same ends!"
      - even length & different first/last letter -> "It is even with different ends!"
      - otherwise -> "Nothing special."
    """
    print("\n=== Task 3: classify_user_inputs ===")
    print("Type words to be classified, or 'quit' to stop.")
    word = input("Input a word: ")

    while word != "quit":
        first_letter = word[0] if len(word) > 0 else ""
        last_letter = word[-1] if len(word) > 0 else ""
        length = len(word)

        # Check conditions
        if (length % 2 == 1) and (first_letter == last_letter) and (length > 0):
            print("It is odd with the same ends!")
        elif (length % 2 == 0) and (first_letter != last_letter) and (length > 0):
            print("It is even with different ends!")
        else:
            print("Nothing special.")

        word = input("Input a word: ")

# Uncomment below to run Task 3 classification interactively:
# classify_user_inputs()


# Kysytään kaksi float-lukua, sitten toistetaan kyselyä
# ja tarkistetaan, onko luku niiden välissä
def range_check():
    """
    Asks the user for two floats (start and end),
    then repeatedly asks for another float and indicates 
    whether it's within that range or not.
    """
    print("\n=== Task 4: range_check ===")
    start = float(input("Give the start of the range (float): "))
    end = float(input("Give the end of the range (float): "))

    # If you'd like, ensure start <= end by swapping if needed:
    if start > end:
        start, end = end, start

    print(f"Range is now [{start}, {end}]. Type 'quit' to stop.")

    while True:
        user_input = input("Give a float to check, or 'quit': ")
        if user_input.lower() == "quit":
            break
        try:
            val = float(user_input)
            if start <= val <= end:
                print(f"{val} is INSIDE the range.")
            else:
                print(f"{val} is OUTSIDE the range.")
        except ValueError:
            print("Please type a valid float, or 'quit' to stop.")

# Uncomment below to run Task 4 interactively:
# range_check()


def substituted_version(sentence):
    """
    Returns a 'substituted' version of 'sentence' according to the rules:
      - 'ä' -> "ae"
      - 'ö' -> "oe"
      - 'å' -> "a"
      - everything else remains the same
    """
    result = ""
    i = 0
    while i < len(sentence):
        a_letter = sentence[i]

        # Replace each letter according to the rules
        if a_letter == "ä":
            result += "ae"
        elif a_letter == "ö":
            result += "oe"
        elif a_letter == "å":
            result += "a"
        else:
            result += a_letter

        i += 1
    return result


# Test for Task 5
print("\n=== Task 5 Test: substituted_version ===")
test_sentence = "Tämä on ö-mappien å-kokoelma."
print("Original:  ", test_sentence)
print("Substituted:", substituted_version(test_sentence))
