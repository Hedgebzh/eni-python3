print("Cas 1 : Entiers positifs")
nombre1 = input("Saisissez un premier nombre : ")
nombre1 = int(nombre1)
nombre2 = input("Saisissez un second nombre : ")
nombre2 = int(nombre2)

somme = nombre1 + nombre2
comparaison = nombre1 < nombre2

print("La somme des deux nombres rentrées est :", somme)
print(nombre1, "<", nombre2, comparaison)

input("Appuyez sur entrée pour afficher le deuxième cas")

print("Cas 2 : Entiers négatifs")
nombre1 = input("Saisissez un premier nombre négatif :")
nombre1 = int(nombre1)
nombre2 = input("Saisissez un second nombre négatif :")
nombre2 = int(nombre2)

somme = nombre1 + nombre2
comparaison = nombre1 < nombre2

print("La somme des deux nombres rentrées est :", somme)
print(nombre1, "<", nombre2, comparaison)
