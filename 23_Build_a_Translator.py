# Build a Translator (2:52:41)


def translate(phrase):
    translation = ""

    for letter in phrase:
        if letter in "AEIOU":
            letter = "G"
        elif letter in "aeiou":
            letter = "g"

        translation = translation + letter

    return translation


result = translate("Aama de bu")
print(result)
