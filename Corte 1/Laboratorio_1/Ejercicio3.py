"""
Grupo: Nicolle López Colonia (2259630)
       Carlos Stiven Ruiz Rojas (2259629)
       Jhonny Fernando Duque (2259398)
Fecha: 19 de marzo 2022

"""

#variables

base= float(input('Ingrese la base de su lote en Metros: '))
altura= float(input('Ingrese la altura de su lote en Metros: '))
p_metros2= int(input('Ingrese el precio de cada metro cuadrado: '))

#proceso

hectarea= (base*altura)/10000
v_lote= (base*altura)*p_metros2
imp= v_lote * 0.013
#Salida

print(f'El numero de hectares es {hectarea}, el lote tiene un valor de {v_lote} y un impuesto de {imp}')