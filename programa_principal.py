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
        print()
        print("------------CLASIFICACIÓN DE LA LIGA--------------")
        for a in range(len(Listar_Informacion(doc))):
            lista=[]
            lista.append(Listar_Informacion(doc)[a].split(" "))
            for b in range(len(lista)):
                print(tabulate(lista, headers=['Equipo','Puntos','Diferencia de goles'],tablefmt='grid'))
        print()
    elif opcion==2:
        print()
        print("En la liga hay %i equipos" % Contar_Informacion(doc))
        print()
    elif opcion==3:
        e=input("Introduce un equipo: ")
        for a in range(len(Buscar_informacion(e,doc))):
            if e==Buscar_informacion(e,doc)[a]:
                sol=int(Buscar_informacion(e,doc)[a+1])
        print()
        print("%s ha marcado %i goles." %(e,sol))
        print()
print()
print("Fin del programa")
 