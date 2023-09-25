"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 08 de abril 2022
Descripcion: Suma de numeros enteros 

"""
# For

def suma(cantidad):
    global total
    total= 0
    for i in range(0,cantidad+1):
        total= total + i
    return total

Cantidad= int(input("Ingrese el numero hasta donde se quiere sumar: "))

print("la suma de los numeros hasta",Cantidad, "es: ",suma(Cantidad))

#While

def suma(Cantidad):
    i =1
    salida=0
    while i <= Cantidad:
        salida+=i
        i+=1
    return salida

Cantidad= int(input("Ingrese el numero hasta donde se quiere sumar: ")) 

print("la suma de los numero hasta", Cantidad,"es: ",suma(Cantidad))