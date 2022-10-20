import math
import random


# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_hello_world():
    print("Hello Worldsss")


# si le type est considéré comme int il faut la caster pour le concaténé
nombre = 15
print("Le nombre est " + str(nombre))

# le 004 trop facile voici le 005 :
# Dans cet exercice, nous allons utiliser les nouvelles fonctionnalités de Python 3, afin de printer les 3 variables a, b et c, séparées par un symbole d'addition (+).
# Votre script doit donc afficher : 2 + 6 + 3.


a = 2
b = 6
c = 3

print(str(a) + " + " + str(b) + " + " + str(c))

# liste = range(3)
# list2 = range(5)

# print(liste(list2))
user_type = str
prenom = "Pierre"


def check_type(var, letype):
    if isinstance(var, letype):
        print("is a string")
    else:
        print("is not a string")


check_type(prenom, user_type)

# Votre condition doit vérifier si la variable prenom est bien une chaîne de caractère. Ici c'est le cas,
# votre condition doit donc être vraie et printer la phrase "La variable est une chaîne de caractères".

prenom = 0

check_type(prenom, int)


# INSÉRER VOTRE CONDITION DE NOUVEAU
# Cette fois-ci, la variable n'est pas égale à une chaîne de caractère. Votre condition doit donc être fausse et
# la phrase ne doit pas s'afficher.

def change_phrase(phrase):
    return print(phrase.replace("Bonjour", "salut"))


phrase = "Bonjour les amis"
change_phrase(phrase);
# nouvelle_phrase = ???

cetteliste = ["pomme", "poire", "cerise"]

print(cetteliste)
print(len(cetteliste))

liste1 = ["pomme", "poire", "cerise"]
liste2 = [1, 2, 3]
liste3 = []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hello_world()

liste12 = ["pomme", "poire", "cerise"]

# for x in liste12:
#    print(x)

# for x in range(liste12):
#    print(liste12[x])

lemot = "pomme, poire, cerise, fraise, orange"
lemot_liste = lemot.split(", ")
lemot_liste.sort()
print(lemot_liste)
lemot_en_order = ", ".join(lemot_liste)
print(lemot_en_order)


def calc_volume_shere(rayon):
    return print(4.0 * math.pi * (rayon ** 3) / 3)


calc_volume_shere(4)


def listNumber():
    # number_max = 100
    # number_min = 10
    # numbers = []
    # number_index = 0
    # while number_max <= number_min:
    #     if not numbers:
    #         numbers
    #     if number <= number_max:
    #         number+=1
    #         numbers.append(number)

    liste = list(range(10, 101))
    print(liste)


listNumber()


def generateurDeDes(nb_lance):
    print(random.randint(1, 6))
    tab = []
    i = 0
    while i < nb_lance:
        random_number = random.randint(1, 6);
        print("Dés : " + str(random_number))
        tab.append(random_number)
        i += 1

    print(tab)
    calcMoyenneNbLance(tab, nb_lance)


def calcMoyenneNbLance(array, nb_lance):
    return print(sum(array) / nb_lance)


generateurDeDes(10)


def calcNumberOfCharInSentence(c):
    phrase = "aaaa le teste"
    num = 0
    for e in phrase:
        if e == c:
            num += 1
    print(num)


calcNumberOfCharInSentence("a")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# type texte = str
# Numérique = int, float, complex
# séqeuence = list, tuple, range
# mapping = dict
# type de set = set, frozenset
# booleen = bool
# binaires = bytes, bytearray, memoryview
# type none = NoneType

# example de nombre complex :
# x = 1j

# Bitwise
# & AND
# | OR
# ~ NOT
# ^ XOR
