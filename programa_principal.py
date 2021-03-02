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
        for elem in Buscar_informacion(e,doc):
            print(elem)
    elif opcion==4:
        p=input("Introduce una posicion de la tabla: ")
        if int(Buscar_informacion_relacionada(p,doc)[1])>1:
            print("El equipo que se encuentra en la posicion %s es %s y ha participado en %s eventos" % (p,Buscar_informacion_relacionada(p,doc)[0],Buscar_informacion_relacionada(p,doc)[1]))
        else:
            print("El equipo que se encuentra en la posicion %s es %s y ha participado en %s evento" % (p,Buscar_informacion_relacionada(p,doc)[0],Buscar_informacion_relacionada(p,doc)[1]))
    elif opcion==5:
        print()
        e1=input("Equipo local: ")
        e2=input("Equipo visitante: ")
        print()
        for elem in Ejercicio_libre(e1,e2,doc):
            print("Resultado:  ",elem)
        print()
print()
print("Fin del programa")
 