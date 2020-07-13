'''
author = L. Zalcik
'''

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
USERS = {"bob":"123",
         "ann":"pass123",
         "mike":"password123",
         "liz":"pass123"
         }
ODDELOVAC = 30 * "#"
print("TEXT ANALYZER\n",ODDELOVAC)
print("Welcome to the app. Please log in")

user = input("Username: ")
password = input("Password: ")


#username check
if user not in USERS:
    print("Wrong username.Try again.")
    quit()
else:
    pass

#password check
if USERS[user] != password:
    print("Wrong Password.Try again.")
    quit()
else:
    pass

#text choose

choose = int(input("We have 3 texts to be analyzed.\n"
                 "Enter a number (1-3)." ))
text_choose = (1, 2, 3)

if choose not in text_choose:
    print("Wrong entry.Choose 1, 2 or 3")
    quit()

else:
    pass

print(ODDELOVAC)

#counting words
words = TEXTS[choose - 1].split()

total_words = len(words)
capital_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_words = 0
summ = 0
graf = dict()



for word in words:
    if word.istitle():
        capital_words += 1
    elif word.isupper():
        uppercase_words += 1
    elif word.islower():
        lowercase_words +=1
    elif word.isdigit():
        numeric_words += 1
        summ += int(word)



print(f"There are {total_words} words.")
print(f"There are {capital_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {numeric_words} numbers.")
print(ODDELOVAC)

# graf bar
graf = dict()
for word in words:
    strip_word = word.strip(" ,.-<>*!'?")
    if len(strip_word) in graf.keys():
        graf[len(strip_word)] += 1
    else:
        graf[len(strip_word)] = 1

for delka in graf:
    print(f"{delka} {'*' * graf[delka]} {graf[delka]}")

print(ODDELOVAC)
print(f'If we summed all the numbers in text we would get: {summ}')
print(ODDELOVAC)











