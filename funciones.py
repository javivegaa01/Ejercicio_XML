
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