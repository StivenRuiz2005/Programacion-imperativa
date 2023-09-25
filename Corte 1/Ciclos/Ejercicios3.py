"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 08 de abril 2022
Descripcion: Tienda
"""
print("==========================FOR==========================")
def compras(n):
    cod=0
    precio=0
    total1=0
    total=0
    for i in range(0,n):
        cod=int(input("Ingrese el codigo del producto: "))
        precio=float(input("Ingrese el precio por unidad del producto:"))
        uni= int(input("Ingrese las unidades a comprar:"))
        if cod == 1:
            total1= ((precio*uni)*0.05)+(precio*uni)
            print(total1)
        elif cod==2:
            total1=((precio*uni)*0.1)+(precio*uni)
            print(total1)
        elif cod==3:
            total1=((precio*uni)*0.08)+(precio*uni)
            print(total1)
        elif cod==4:
            total1=((precio*uni)*0.19)+(precio*uni)
            print(total1)
        else:
            print("Codigo no valido")
        total= total + total1
    return total

n=int(input("Ingrese el numero de las ventas a realizar: "))
print("el valor total de la venta es: ",compras(n))
print("========================While==============================")
def compras1(n):
    cod=0
    precio=0
    total1=0
    i=0
    total=0
    while(i<n):
        cod=int(input("Ingrese el codigo del producto: "))
        precio=float(input("Ingrese el precio por unidad del producto:"))
        uni= int(input("Ingrese las unidades a comprar:"))
        if cod == 1:
            total1= ((precio*uni)*0.05)+(precio*uni)
            print(total1)
        elif cod==2:
            total1=((precio*uni)*0.1)+(precio*uni)
            print(total1)
        elif cod==3:
            total1=((precio*uni)*0.08)+(precio*uni)
            print(total1)
        elif cod==4:
            total1=((precio*uni)*0.19)+(precio*uni)
            print(total1)
        else:
            print("Codigo no valido")
        total= total + total1
        i+=1
    return total
n=int(input("Ingrese el numero de las ventas a realizar: "))
print("el valor total de la venta es: ",compras(n))    
    
    


