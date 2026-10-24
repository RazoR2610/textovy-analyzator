"""
main.py: prvý projekt do Engeto Online Python Akadémie

author: Roman Nagy
email: romankonagy@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# registrovani pouzivatelia
pouzivatelia = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

ciara = "----------------------------------------"

# prihlasenie
meno = input("meno:")
heslo = input("heslo:")

if meno not in pouzivatelia or pouzivatelia[meno] != heslo:
    print("neregistrovaný používateľ, ukončujem program..")
    exit()

print(ciara)
print("Vitaj v aplikácii,", meno)
print("Máme", len(TEXTS), "texty na analýzu.")
print(ciara)

# vyber textu
volba = input("Zadaj číslo od 1 do " + str(len(TEXTS)) + " pre výber: ")

if not volba.isdigit():
    print("Nezadal si číslo, ukončujem program..")
    exit()

cislo_textu = int(volba)

if cislo_textu < 1 or cislo_textu > len(TEXTS):
    print("Text s takým číslom neexistuje, ukončujem program..")
    exit()

text = TEXTS[cislo_textu - 1]

# rozdelenie na slova a odstranenie interpunkcie
slova = []
for slovo in text.split():
    slovo = slovo.strip(".,:;!?")
    if slovo != "":
        slova.append(slovo)

# pocitanie
s_velkym = 0
velkymi = 0
malymi = 0
pocet_cisel = 0
sucet_cisel = 0

for slovo in slova:
    if slovo.istitle():
        s_velkym = s_velkym + 1
    if slovo.isupper() and slovo.isalpha():
        velkymi = velkymi + 1
    if slovo.islower():
        malymi = malymi + 1
    if slovo.isdigit():
        pocet_cisel = pocet_cisel + 1
        sucet_cisel = sucet_cisel + int(slovo)

print(ciara)
print("Vo vybranom texte je", len(slova), "slov.")
print("Počet slov začínajúcich veľkým písmenom:", s_velkym)
print("Počet slov písaných veľkými písmenami:", velkymi)
print("Počet slov písaných malými písmenami:", malymi)
print("Počet čísel:", pocet_cisel)
print("Súčet všetkých čísel:", sucet_cisel)
print(ciara)

# graf dlzok slov
dlzky = {}
for slovo in slova:
    dlzka = len(slovo)
    if dlzka in dlzky:
        dlzky[dlzka] = dlzky[dlzka] + 1
    else:
        dlzky[dlzka] = 1

# zistim najvacsi pocet, aby graf nebol rozhadzany
najviac = 0
for pocet in dlzky.values():
    if pocet > najviac:
        najviac = pocet

sirka = najviac + 2
if sirka < 15:
    sirka = 15

print("DĹŽKA|" + "VÝSKYT".center(sirka) + "|POČET")
print(ciara)
for dlzka in sorted(dlzky):
    pocet = dlzky[dlzka]
    hviezdy = "*" * pocet
    print(str(dlzka).rjust(5) + "|" + hviezdy.ljust(sirka) + "|" + str(pocet))
