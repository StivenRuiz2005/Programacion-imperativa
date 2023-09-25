"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 29 de abril 2022
Descripcion: Asteriscos 2

"""
def m (n):
    if n >=1:        
        for i in range(n,0,-1): 
            for j in range(0,-i,-1):
                print("*",end=" ")
            print()
        for i in range(2,n+1): 
            for j in range(1,i+1):
                print("*",end=" ")
            print()

    else:
        print("Error")

n= int(input("Ingrese un numero mayor a cero: "))
m(n)