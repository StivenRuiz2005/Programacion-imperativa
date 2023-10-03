"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 3/10/2023
Descricion: Cantidad numero pares y suma de pares Con For o While

"""
def parFor():
    suma = 0
    contador = 0
    for i in range(0,5):
        n = int(input("Ingrese un numero: "))
        if (n % 2 == 0):
            print(i,"El numero ", n ," es par")
            suma += n
            contador += 1
    return print("La suma es: ",suma, "Y el numero de pares son:", contador)


def parWhile():
    suma = 0
    contador = 0
    i=1
    while (i < 6):
        i+=1
        n = int(input("Ingrese un numero: "))
        if (n % 2 == 0):
            print(i,"El numero ", n ," es par")
            suma += n
            contador += 1
    return print("La suma es: ",suma, "Y el numero de pares son:", contador)

# Llamamos las funciones

parFor()
print ("==============================")
parWhile()



