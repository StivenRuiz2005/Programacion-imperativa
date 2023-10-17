
import random as rd

"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 17/10/2023
Descripcion: Tests multiplicacion
"""
nombre = input("Ingrese su nombre: ")
acertar = 0
fallar = 0


print("Bienvenido al test de multiplicacion ", nombre)

def test():
    global acertar, fallar
    try:
        num1 = rd.randint(-5,15)
        num2 = rd.randint(-5,15)
        resultado = num1*num2
        resul = int(input(f"Cuanto es {num1} * {num2} = "))
    except ValueError:
        print("No se puede ingresar letras, decimales u otros caracteres")
        test()
    else:
        if resul == resultado:
            acertar = acertar + 1
        else:
            fallar = fallar + 1
            print("El resultado es: ", resultado)

for i in range(12):
    test()

print("=========El test ha finalizado============")
print("Nombre : ",nombre)
print("El numero de aciertos es: ", acertar)
print("El numero de fallos es: ", fallar)