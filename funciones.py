def Listar_Informacion(datos):
    a=datos.xpath('//marcador/competicion/grupos/grupo/clasificacion/team/name/text()')
    return a,type(a)