"""
Grupo: Nicolle López Colonia (2259630)
       Carlos Stiven Ruiz Rojas (2259629)
       Jhonny Fernando Duque (2259398)
Fecha: 19 de marzo 2022

"""
#Variables de entrada
name_Team = str(input('Ingrese el nombre del equipo: '))
p_ganados = int(input('Ingrese el numero de partidos ganados: '))
p_perdidos = int(input('Ingrese el numero de partidos perdidos: '))
p_empatados = int(input('ingrese el numero de partidos empatados: '))
g_en_contra = int(input('Ingrese los goles en contra: '))
g_a_favor = int(input('Ingrese los goles a favor: ')) 

#procesos

Partidos_totales= p_ganados + p_perdidos + p_empatados
puntos = (p_ganados * 3) + (p_empatados * 1 )
dif_goles = g_a_favor - g_en_contra

#Salida

print(f'Su equipo {name_Team} jugo {Partidos_totales} partidos, gano {p_ganados}, perdio {p_perdidos}, empato {p_empatados}, consiguiendo {puntos} puntos,')
print(f'Recibio {g_en_contra} goles en contra y marco {g_a_favor}, dando una diferencia de goles de {dif_goles}')
