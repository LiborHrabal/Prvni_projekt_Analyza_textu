# Prvni projekt analyza textu. Projekt k opakovani cviceni 1-4.
# Zadani

#Zadani textu
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

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

oddelovac = "-" * 40

# Seznam registrovanych uzivatelu
uzivatele = {"bob": "123",
             "ann": "pass123",
             "mike": "password123",
             "liz": "pass123",
             }
# Vyzva uzivatele k prihlaseni
print(oddelovac, f"Please, enter your username and password.", oddelovac, sep="\n")
jmeno = input("username: ").lower()
heslo = input("password: ").lower()

# Podminka pro overeni uzivatele a jeho hesla
while uzivatele.get(jmeno) != heslo:
    if uzivatele.get(jmeno) != heslo:
        print(oddelovac, f"SORRY, UNKNOWN name or password!", "Insert your username and password again.", oddelovac,
          sep="\n")
        jmeno = input("username: ").lower()
        heslo = input("password: ").lower()

# Vyber textu 1, 2 nebo 3.
print(oddelovac, f"Welcome to the app, {jmeno}.", "We have 3 texts to be analyzed.", oddelovac, sep="\n")
text = input("Enter a number btw. 1 and 3 to select: ")

# Kontrola zadani cisla textu
if text.isnumeric() == 0:
    print("Bad input. Only numeric characters are acceptable.")
    quit()
elif int(text)  < 1 or int(text) > 3:
    print("Number is out of range!")
    quit()

# Analyza textu. Promenna text_analyza vybira text dle volby uzivatele a prizpusobuje na indexovani od nuly.
# Promenna slova = obsahuje list stringu (slov) po odstraneni carek a tecek z textu.
text_analyza = TEXTS[int(text)-1]
slova = [slovo.strip(",.") for  slovo in text_analyza.split()]

# Vypis slov a jejich poctu.
vyskyt_slov = {}
delka_slov = {}
for slovo in slova:
    vyskyt_slov[slovo] = vyskyt_slov.get(slovo, 0)+1
    delka_slov[len(slovo)] = delka_slov.get(len(slovo), 0)+1
hodnoty = (delka_slov.values())
nejdelsi = max(hodnoty)
print(hodnoty)
print(nejdelsi)

#Vypis slov zacinajicich velkym pismenem a jejich pocet
slova_prvni_velke = []
for slovo in slova:
    if slovo.istitle():
        slova_prvni_velke.append(slovo)

#Vypis slov psanych jen velkymi pismeny a jejich pocet
slova_velka = []
for slovo in slova:
    if slovo.isupper() and slovo.isalpha():
        slova_velka.append(slovo)

#Vypis slov psanych jen malymi pismeny a jejich pocet
slova_mala = []
for slovo in slova:
    if slovo.islower():
        slova_mala.append(slovo)

#Vypis cisel
cisla = []
for cislo in slova:
    if cislo.isnumeric():
        cisla.append(cislo)

for cislo in range(len(cisla)):
    cisla[cislo] = int(cisla[cislo])

# Souhrn
print(oddelovac)
print(f"There are {len(slova)} words in the selected text.")
print(f"There are {len(slova_prvni_velke)} titlecase words")
print(f"There are {len(slova_velka)} uppercase words")
print(f"There are {len(slova_mala)} lowercase words.")
print(f"There are {len(cisla)} numeric strings.")
print(f"The sum of all numbers is {sum(cisla)}.")

# Tabulka poctu delek slov
print(oddelovac)
print("LEN|  OCCURENCES  |NR. ")
print(oddelovac)
poradi_slov = sorted(delka_slov)
# print(delka_slov)

for poradi, klic in enumerate(poradi_slov):
    #print(klic,"|","*" * delka_slov[int(klic)],"|",delka_slov[klic])
    print("{:>3}".format(klic)+"|"+"*" * delka_slov[int(klic)]+" "*(2+nejdelsi-delka_slov[int(klic)])+"|",delka_slov[klic])

print(oddelovac)
















