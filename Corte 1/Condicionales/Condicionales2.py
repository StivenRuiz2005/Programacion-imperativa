"""
--------------------------------------Ejemplo 1--------------------------------------------

ventas = float(input('ingrese su numero de ventas: '))
cat= int(input('ingrese su categoria: '))
comision= 0

if cat == 1:
  comision = ventas * 0.1
elif cat == 2:
  comision = ventas * 0.2
elif cat == 3:
  comision = ventas * 0.35
elif cat == 4:
  comision = ventas * 0.45
elif cat == 5:
  comision = ventas * 0.5
elif cat == 6:
  comision = ventas * 0.6
else:
  print('no existe esa categoria')

print('El valor de su comision es de:',comision)

---------------------------------------Ejercicio 2---------------------------------------

# variables

estrato= int(input('Ingrese el estrao de su vivienda: '))
V_consumo= float(input('ingrese el valor de su consumo: '))
total= 0
#Desarrollo

if estrato == 1:
    total= V_consumo + 500
elif estrato == 2:
    total= V_consumo + 700
elif estrato == 3:
    total= V_consumo + 4800
elif estrato == 4:
    total= V_consumo + 6700
else:
    print('ese estrato no existe')

print('el valor total de su recibo es de: ', total)

edad= int(input('Digite su edad: '))

---------------------------------------Ejercicio 3----------------------------------------------

if edad >= 0 and edad < 10:
    print('Vaya a la niñiteca')
elif edad >= 10 and edad < 15:
    print('Vaya a la chiquiteca')
elif edad >= 15 and edad <=17:
    print('Vaya a la casa')
elif edad >= 18 and edad <25:
    print('Vaya a la seccion de jovenes')
elif edad >= 25 and edad < 35:
    print('Vaya a la seccion de adultos jovenes')
elif edad >= 35 and edad < 65:
    print('Vaya a la seccion de maduros')
elif edad >= 65 and edad <=80:
    print('Vaya a la seccion de viejoteca')
elif edad >= 80:
    print('Vaya cavado la tumba')
else:
    print('Edad incorrecta')


"""


