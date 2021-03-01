from lxml import etree
from funciones import *

doc=etree.parse("fut.xml")

print("Bienvenido al programa")
print()

while True:
    menu=''' MENÚ:
    1.Listar información
    2.Contar información
    3.Buscar información
    4.Buscar información relacionada
    5.Ejercicio libre
    6.Salir
    '''
    print(menu)
    opcion=int(input("Eliga una opción: "))
    while opcion<1 or opcion>6:
        print("Imposible")
        opcion=int(input("Vuelve a introducir una opción: "))
    if opcion==6:
        break
    elif opcion==1:
        print(Listar_Informacion(doc))

print()
print("Fin del programa")