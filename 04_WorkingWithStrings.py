# Working with strings
phrase = "Sabuesito Academy"

# Notes
## Si utilizas index con un caracter que no se encuentra en el String, entonces dará error

print(phrase)
print(phrase.upper())
print(phrase.lower())
print(phrase.upper().isupper())
print(phrase.upper().islower())
print(phrase.lower().islower())
print(phrase.index("esito"))
print(phrase[0])
print(phrase[0:5])
print(phrase[0:phrase.index(" ")])
print(len(phrase))
print(phrase[0:-1])
print(phrase.replace("Sabuesito", "Cat"))