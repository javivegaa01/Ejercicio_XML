
def Listar_Informacion(datos):
    nombres=datos.xpath("//clasificacion/team/name/text()")
    puntos=datos.xpath("//clasificacion/team/points/text()")
    goles_marcados=datos.xpath("//clasificacion/team/goals_scored/text()")
    goles_encajados=datos.xpath("//clasificacion/team/goals_conceded/text()")
    equipos=[]
    for elem1,elem2,elem3,elem4 in zip(nombres,puntos,goles_marcados,goles_encajados):
        diferencia=int(elem3)-int(elem4)
        equipos.append(elem1+" "+elem2+" "+str(diferencia))
    return equipos

def Contar_Informacion(datos):
    nombres=datos.xpath("//clasificacion/team/name/text()")
    num_equipos=len(nombres)
    return num_equipos

def Buscar_informacion(equipo,datos):
    goles_marcados=datos.xpath("//clasificacion/team[name/text()='%s']/goals_scored/text()"%equipo)
    return goles_marcados

def Buscar_informacion_relacionada(posicion,datos):
    lista_nombre=datos.xpath("//clasificacion/team[rank/text()='%s']/name/text()"%posicion)
    local=datos.xpath("//eventos/evento/equipolocal/text()")
    visitante=datos.xpath("//eventos/evento/equipovisitante/text()")
    for elem in lista_nombre:
        nombre=elem
    apariaciones=0
    apariaciones=local.count(nombre)+visitante.count(nombre)
    return nombre,apariaciones

def Ejercicio_libre(equipo1,equipo2,datos):
    res_loc=datos.xpath("//eventos/evento[equipolocal/text()='%s' and equipovisitante/text()='%s']/resultadolocal/text()"%(equipo1,equipo2))
    res_vis=datos.xpath("//eventos/evento[equipolocal/text()='%s' and equipovisitante/text()='%s']/resultadovisitante/text()"%(equipo1,equipo2))
    resultado=[]
    posesion_local=datos.xpath("//eventos/evento[equipolocal/text()='%s' and equipovisitante/text()='%s']/estadisticas/equipoLocal/estadistica[nombre/text()='Posesión']/valor/text()"%(equipo1,equipo2))
    posesion_visitante=datos.xpath("//eventos/evento[equipolocal/text()='%s' and equipovisitante/text()='%s']/estadisticas/equipoVisitante/estadistica[nombre/text()='Posesión']/valor/text()"%(equipo1,equipo2))
    remates_local=datos.xpath("//eventos/evento[equipolocal/text()='%s' and equipovisitante/text()='%s']/estadisticas/equipoLocal/estadistica[nombre/text()='Remates']/valor/text()"%(equipo1,equipo2))
    remates_visitante=datos.xpath("//eventos/evento[equipolocal/text()='%s' and equipovisitante/text()='%s']/estadisticas/equipoVisitante/estadistica[nombre/text()='Remates']/valor/text()"%(equipo1,equipo2))
    remates_a_puerta_local=datos.xpath("//eventos/evento[equipolocal/text()='%s' and equipovisitante/text()='%s']/estadisticas/equipoLocal/estadistica[nombre/text()='Remates a Puerta']/valor/text()"%(equipo1,equipo2))
    remates_a_puerta_visitante=datos.xpath("//eventos/evento[equipolocal/text()='%s' and equipovisitante/text()='%s']/estadisticas/equipoVisitante/estadistica[nombre/text()='Remates a Puerta']/valor/text()"%(equipo1,equipo2))
    faltas_cometidas_local=datos.xpath("//eventos/evento[equipolocal/text()='%s' and equipovisitante/text()='%s']/estadisticas/equipoLocal/estadistica[nombre/text()='Faltas Cometidas']/valor/text()"%(equipo1,equipo2))
    faltas_cometidas_visitante=datos.xpath("//eventos/evento[equipolocal/text()='%s' and equipovisitante/text()='%s']/estadisticas/equipoVisitante/estadistica[nombre/text()='Faltas Cometidas']/valor/text()"%(equipo1,equipo2))
    for elem1,elem2 in zip(res_loc,res_vis):
        resultado.append(elem1+" - "+elem2)
        if elem1>elem2:
            ind_resultado=True
    posesion={}
    remates={}
    faltas={}
    for elem1,elem2,elem3,elem4,elem5,elem6,elem7,elem8 in zip(posesion_local,posesion_visitante,remates_local,remates_visitante,remates_a_puerta_local,remates_a_puerta_visitante,faltas_cometidas_local,faltas_cometidas_visitante):
        posesion["Local"]=elem1
        posesion["Visitante"]=elem2
        remates["Local"]=elem3
        remates["Local a puerta"]=elem5
        remates["Visitante"]=elem4
        remates["Visitante a puerta"]=elem6
        remates["Local"]=elem7
        remates["Visitante"]=elem8
    return resultado,posesion,remates,faltas



#Funciones para validar datos de entrada