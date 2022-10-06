import random


print("Bienvenue dans ce mini-jeu consistant à deviner le nombre compris entre 0 et 100 (exclus) tiré au sort par le programme")
print(" ")
nombre = random.randint(0, 100)
print("Le nombre vient d'être tiré au sort par le programme")
print(" ")
nb_essai = 0

while True:

    essai = input("Saississez un nombre : ")

    try:
        essai = int(essai)
    except:
        pass
    else:
        if essai < nombre:
            nb_essai += 1
            print("Trop petit, vous êtes à votre essai numéro {}.".format(nb_essai))
        elif essai > nombre:
            nb_essai += 1
            print("Trop grand, vous êtes à votre essai numéro {}.".format(nb_essai))
        else:
            nb_essai += 1
            if nb_essai == 1:
                print("Gagné ! Incroyable, vous avez eu besoin d'un seul essai seulement pour gagner !")
            else:
                print("Gagné ! Bien joué ! Vous avez eu besoin de {} essais pour gagner.".format(nb_essai))
            break





