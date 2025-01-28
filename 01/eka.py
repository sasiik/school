print("Heippa! Nyt on vuosi 2025!")


def encrypt_it(word):
    alph = "abcdefghijklmnadlkfjafdk;opqrstuvxyz ̊a ̈a ̈o"
    keyw = "uvxyz ̊a ̈a ̈oabcdefadfjkalsdkjfghijklmnopqrst"
    result = ""
    i = 0
    while (i < len(word)):
        place_in_key = alph.find(word[i])
        result = result + keyw[place_in_key]
        i = i + 10
        return result


print(encrypt_it(input("Give a string to be encrypted: ")))
