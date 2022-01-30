# projekt 1, Ladislav Lukavsky

import sys, os


j = input("Zadej své uživatelské jméno: \t")
h = input("Zadej své heslo: \t")

d = {"bob":"pass123","mike":"password123","liz":"pass123"}

if j in d:

    if d[j]!=h or j == "exit":

        sys.exit("Program se ukončuje")
else:
    sys.exit("Program se ukončuje")

print("Uživatelské jmého a helo je správné, vítejte!")


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

os.system("cls")

v = input("Volbou číslic 1 -3 vyberte mezi jednolivými texty: \t ")
v = int(v)
if v not in range(1,4):
    sys.exit("Program se ukončuje, vstup musí být číslo od 1 do tří")

os.system("cls")

print(f"Výborně vybral jste text č. {v}, teď se podíváme na nějaké statistiky:")
vybrText = TEXTS[v-1]
vyprText = vybrText.translate({ord(i): None for i in "()[],.!?/*-+"})
word_list = vybrText.split()
pocetSlov = len(word_list)
pocetSlovZV = 0
pocetSlovV = 0
pocetSlovM = 0
pocetCisel = 0
cisla = []
sum = 0
cetnost = dict()

for i in word_list:
    if i[0].isupper():
        pocetSlovZV +=1
    if i.isupper():
        pocetSlovV += 1
    if i.islower():
        pocetSlovM += 1
    if i.isnumeric():
        pocetCisel += 1
        cisla.append(i)
    a = len(i)
    if a in cetnost:
        cetnost[a] +=1
    else:
        cetnost[a] = 1

for i in cisla:
    i = int(i)
    sum += i

print("-----------------------------------------------------------------------")
print(f"Ve vybraném textu je celkem {pocetSlov} slov.")
print(f"V textu je celkem {pocetSlovV} slov psaných velkými písmeny.")
print(f"V textu je celkem {pocetSlovZV} slov začínajících velkým písmenem.")
print(f"V textu je celkem {pocetSlovM} slov psaných malými písmeny.")
print(f"V textu je celkem {pocetCisel} čísel.")
print(f"Součet všech čísel v textu je {sum}.")
print("-----------------------------------------------------------------------")




sortItem = cetnost.items()
sortCetnost = sorted(sortItem)




DValues = []
for i in sortCetnost:
    DValues.append(i[1])
maxV = max(DValues)
print("-----------------------------------------------------------------------")
print("délka slova: "  + "|  " + "výskyt " + (maxV-7) * " " + " " + "|" + " četnost:")
print("-----------------------------------------------------------------------")
for i in sortCetnost:
    delk = str(i[0])
    cet = str(i[1])
    hvezda = i[1] * "*"
    if len(delk)==1:
        mezera = "  "
    else:
        mezera = " "
    mezera2 = maxV-i[1]
    print("\t  " + mezera + delk + "|  " + hvezda + mezera2 * " " + " " + "|" + " "+ cet)


print("-----------------------------------------------------------------------")







