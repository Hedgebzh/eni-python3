import sys

nombre1 = input("Saisissez un premier nombre : ")
nombre2 = input("Saisissez un second nombre : ")

try:
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)
except ValueError as error:
    print("La conversion des nombres ne s'est pas réalisée.", file=sys.stderr)
    sys.exit()

if nombre1 < nombre2:
    print ("{} < {}".format(nombre1, nombre2))
elif nombre1 > nombre2:
    print("{} > {}".format(nombre1, nombre2))
else:
    print("{} = {}".format(nombre1, nombre2))
