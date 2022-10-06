print(" ")
print("Bienvenue dans ce mini-jeu consistant à deviner le nombre que vous aurez choisi compris entre deux bornes que vous aurez défini.")
print(" ")

while True:
    borne_min = input("Dans un premier temps, saisissez la borne minimale de l'intervalle dans lequel le nombre devra être deviné : ")
    try:
        int(borne_min)
    except:
        pass
    else:
        print("Super, la borne minimale a été définie.")
        print(" ")
        break

while True:
    borne_max = input("Désormais, saisissez la borne maximale de l'intervalle dans lequel le nombre devra être deviné : ")
    try:
        int(borne_max)
    except:
        pass
    else:
        print("Très bien ! Nos deux bornes ont été définies.")
        print(" ")
        break


while True:
    nombre = input("Désormais, saisissez le nombre que vous souhaitez faire deviner et qui sera compris entre les deux bornes définies précédemment : ")
    try:
        int(nombre)
    except:
        pass
    else:
        print('Parfait ! Tous les éléments ont été rentrés et votre mini-jeu "Devine mon nombre" est créé' )
        print(" ")
    break

nb_essai = 0

while True:

    essai = input("Devinez le nombre du maitre du jeu compris entre {} et {} : ".format(borne_min, borne_max))
    print(" ")

    try:
        essai = int(essai)
        nombre = int(nombre)
    except:
        pass
    else:
        if essai < nombre:
            nb_essai += 1
            print("Trop petit, vous êtes à votre essai numéro {}.".format(nb_essai))
            print(" ")
        elif essai > nombre:
            nb_essai += 1
            print("Trop grand, vous êtes à votre essai numéro {}.".format(nb_essai))
            print(" ")
        else:
            nb_essai += 1
            if nb_essai == 1:
                print("Gagné ! Incroyable, vous avez eu besoin d'un seul essai seulement pour gagner !")
                print(" ")
            else:
                print("Gagné ! Bien joué ! Vous avez eu besoin de {} essais pour gagner.".format(nb_essai))
            break

    if essai < nombre:
        borne_min = essai
    elif essai > nombre:
        borne_max = essai
