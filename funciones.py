
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