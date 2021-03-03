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
        if existe_el_equipo(e,doc)==False:
            print("Ese equipo no es de la liga")
        else:
            for elem in Buscar_informacion(e,doc):
                g=elem
            print("Goles marcados: %s " % g )
    elif opcion==4:
        p=input("Introduce una posicion de la tabla: ")
        if exite_la_posicion(Contar_Informacion(doc),doc)==False:
            print("La posicion es erronea o está fuera del rango")
        else:
            if int(Buscar_informacion_relacionada(p,doc)[1])>1:
                print("El equipo que se encuentra en la posicion %s es %s y ha participado en %s eventos" % (p,Buscar_informacion_relacionada(p,doc)[0],Buscar_informacion_relacionada(p,doc)[1]))
            else:
                print("El equipo que se encuentra en la posicion %s es %s y ha participado en %s evento" % (p,Buscar_informacion_relacionada(p,doc)[0],Buscar_informacion_relacionada(p,doc)[1]))
    elif opcion==5:
        print()
        e1=input("Equipo local: ")
        e2=input("Equipo visitante: ")
        if (existe_el_equipo(e1,doc)==False and existe_el_equipo(e2,doc)==False) or (existe_el_equipo(e1,doc)==False and existe_el_equipo(e2,doc)==True) or (existe_el_equipo(e1,doc)==True and existe_el_equipo(e2,doc)==False):
            print("Algún equipo (o los dos) no es de la liga.")
        else:
            if len(Ejercicio_libre(e1,e2,doc)[0])<1:
                print("Ese partido aún no se ha jugado")
            else:
                for elem in Ejercicio_libre(e1,e2,doc)[0]:
                    res=elem
                print("RESULTADO: %s" % res)
                print()
                print("-----------ESTADISTICAS-----------")
                print("%s                         %s" % (e1,e2))
                print("%s         Posesion             %s" % (Ejercicio_libre(e1,e2,doc)[1]["Local"],Ejercicio_libre(e1,e2,doc)[1]["Visitante"]))
                print("%s         Remates              %s" % (Ejercicio_libre(e1,e2,doc)[2]["Local"],Ejercicio_libre(e1,e2,doc)[2]["Visitante"]))
                print("%s         A puerta             %s" % (Ejercicio_libre(e1,e2,doc)[2]["Local a puerta"],Ejercicio_libre(e1,e2,doc)[2]["Visitante a puerta"]))
                print("%s          Faltas              %s" % (Ejercicio_libre(e1,e2,doc)[3]["Local"],Ejercicio_libre(e1,e2,doc)[3]["Visitante"]))
                print("----------------------------------")
                ind_posesion=False
                ind_tiros=False
                print()
                print("Observaciones:")
                if Ejercicio_libre(e1,e2,doc)[1]["Local"]>Ejercicio_libre(e1,e2,doc)[1]["Visitante"]:
                    if (int(Ejercicio_libre(e1,e2,doc)[1]["Local"])-int(Ejercicio_libre(e1,e2,doc)[1]["Visitante"]))>=20:
                        print("%s ha dado una lección de futbol y ha dominado completamente el partido." % e1)
                    else:
                        print("La posesión ha estado repartida entre los dos equipos.")
                else:
                    if (int(Ejercicio_libre(e1,e2,doc)[1]["Visitante"])-int(Ejercicio_libre(e1,e2,doc)[1]["Local"]))>=20:
                        print("%s ha dado una lección de futbol y ha dominado completamente el partido." % e2)
                        ind_posesion=True
                    else:
                        print("La posesión ha estado repartida entre los dos equipos.")
                if int(Ejercicio_libre(e1,e2,doc)[2]["Local a puerta"])>int(Ejercicio_libre(e1,e2,doc)[2]["Visitante a puerta"]):
                    print("%s ha tenido más efectividad que %s." % (e1,e2))
                else:
                    print("%s ha tenido más efectividad que %s." % (e2,e1))
                    ind_tiros=True
                print()
                print("Conclusión")
                if ind_posesion==True and ind_tiros==False and (int(Ejercicio_libre(e1,e2,doc)[0][0][0:1])>int(Ejercicio_libre(e1,e2,doc)[0][0][4])):
                    print("El partido tiene un justo resultado ya que %s ha aprovechado sus oportunidades a pesar del domino de juego del %s." % (e1,e2))
                elif ind_posesion==False and ind_tiros==True and (int(Ejercicio_libre(e1,e2,doc)[0][0][0:1])<int(Ejercicio_libre(e1,e2,doc)[0][0][4])):
                    print("El partido tiene un justo resultado ya que %s ha aprovechado sus oportunidades a pesar del domino de juego del %s." % (e2,e1))
                elif ind_posesion==False and ind_tiros==False and (int(Ejercicio_libre(e1,e2,doc)[0][0][0:1])>int(Ejercicio_libre(e1,e2,doc)[0][0][4])):
                    print("%s claro y justo ganador del partido ha controlado perfectamente los tiempos y ha dado un repaso futbolistico a %s" %(e1,e2))
                elif ind_posesion==True and ind_tiros==True and (int(Ejercicio_libre(e1,e2,doc)[0][0][0:1])<int(Ejercicio_libre(e1,e2,doc)[0][0][4])):
                    print("%s claro y justo ganador del partido ha controlado perfectamente los tiempos y ha dado un repaso futbolistico a %s" %(e2,e1))
                elif ind_posesion==True and ind_tiros==True and (Ejercicio_libre(e1,e2,doc)[0][0][0:1]==Ejercicio_libre(e1,e2,doc)[0][0][4]):
                    print("El partido es injusto ya que el %s deberia haber ganado el partido, ya que ha tenido completo dominio de posesión y han tirado más que el rival a puerta. %s tendrá que afinar su punteria para la siguiente jornada. " % (e2,e2))
                elif ind_posesion==False and ind_tiros==False and (Ejercicio_libre(e1,e2,doc)[0][0][0:1]==Ejercicio_libre(e1,e2,doc)[0][0][4]):
                    print("El partido es injusto ya que el %s deberia haber ganado el partido, ya que ha tenido completo dominio de posesión y han tirado más que el rival a puerta. %s tendrá que afinar su punteria para la siguiente jornada. " % (e1,e1))
                print()     
print()
print("Fin del programa")
 