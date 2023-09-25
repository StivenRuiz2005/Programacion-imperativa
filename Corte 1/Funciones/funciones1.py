"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 25 de marzo 2022
Descripcion: Cambio de divisas
"""
def mostrar_precio_divisa(divisa):
    if divisa== 'dolar':
        return 3080
    elif divisa== 'euro':
        return 3469
    elif divisa== 'libra':
        return 4748
    else:
        print('La divisa no existe')
def precio_a_convertir(divisa,valor_a_convertir):
    if divisa == 'dolar':
        return valor_a_convertir/3080
    elif divisa == 'euro':
        return valor_a_convertir/3469
    elif divisa == 'libra':
        return valor_a_convertir/4748

# General

divisa= input('Ingrese la divisa \n1.dolar \n2.euro \n3.libra \nIngrese su respuesta: ')
valor_a_convertir= float(input('Ingrese el valor a convertir: '))
opcion= int(input('ingrese la opcion a escoger: \n1 Saber valor divisas \n2 Convertir pesos a divisas \n Escoga la opcion en numeros: '))

if opcion == 1:
    print(mostrar_precio_divisa(divisa))
elif opcion == 2:
    print(precio_a_convertir(divisa,valor_a_convertir))
else:
    print('Opcion no valida')

    