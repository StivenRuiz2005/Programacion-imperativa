"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 29 de abril 2022
Descripcion: Asteriscos 3

"""
def m (n):
    if n >=1:
        for i in range(1,n+1): 
            for j in range(1,i+1):
                print(" "*"* *",end=" ")
            print()

n= int(input("Ingrese un numero mayor a cero: "))
m(n)