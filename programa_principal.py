from lxml import etree
from funciones import *
from tabulate import tabulate
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
        print("--------------CLASIFICACIÓN DE LA LIGA--------------")
        print("      Equipo           Puntos       Diferencia de goles")
        for a in range(len(Listar_Informacion(doc))):
            lista_mostrar=[]
            lista_mostrar=(Listar_Informacion(doc)[a].split(" "))
            for b in range(len(lista_mostrar)):
                print(lista_mostrar[b].center(20," "),lista_mostrar[b+1].center(10," "),lista_mostrar[b+2].center(18," "))
            print(lista_mostrar)
print()
print("Fin del programa")