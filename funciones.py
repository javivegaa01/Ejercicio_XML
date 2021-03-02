
def Listar_Informacion(datos):
    nombres=datos.xpath('//clasificacion/team/name/text()')
    puntos=datos.xpath('//clasificacion/team/points/text()')
    goles_marcados=datos.xpath('//clasificacion/team/goals_scored/text()')
    goles_encajados=datos.xpath('//clasificacion/team/goals_conceded/text()')
    equipos=[]
    for elem1,elem2,elem3,elem4 in zip(nombres,puntos,goles_marcados,goles_encajados):
        diferencia=int(elem3)-int(elem4)
        equipos.append(elem1+" "+elem2+" "+str(diferencia))
    return equipos

def Contar_Informacion(datos):
    nombres=datos.xpath('//clasificacion/team/name/text()')
    num_equipos=len(nombres)
    return num_equipos

def Buscar_informacion(equipo,datos):
    nombres=datos.xpath('//clasificacion/team/name/text()')
    goles_marcados=datos.xpath('//clasificacion/team/goals_scored/text()')
    equipos=[]
    for elem1,elem2 in zip(nombres,goles_marcados):
        equipos.append(elem1)
        equipos.append(elem2)
    return equipos