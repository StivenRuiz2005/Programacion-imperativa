"""
autores: Carlos Stiven Ruiz Rojas (2259629)
         Jhames Plaza Luna (2259577)
         Jhonny Fernando Duque Villada (2259398)
         Nicolas Pulgarin Perez (2259346)
Fecha: 5 de abril 2022
Descripcion: Descuento de compra de computadoras
"""

def calculoVenta(val_unit,num_compu):
    global precio
    global descuento
    precio = num_compu*val_unit
    if num_compu<5 and num_compu>=0:
        descuento=precio*0.1
        total = precio - descuento
    elif 10>num_compu>=5:
        descuento=precio*0.2
        total = precio - descuento
    elif num_compu>=10:
        descuento=precio*0.4
        total = precio - descuento
    else:
        total = "Cantidad no correcta"
    return total

def llamar():
    print("============================================================")
    global nombre
    global num_compu
    global val_unit
    nombre=input("Nombre del cliente: ")
    num_compu=int(input("Cantidad de computadoras a comprar :"))
    val_unit=float(input("Valor unitario por computadoras :"))
    print("============================================================")
    calculoVenta(val_unit, num_compu)
    print("El precio de las computadoras: ",precio)
    print("El descuento obtenido es: ",descuento)
    print("El valor total a pagar: ", calculoVenta(val_unit,num_compu,))
    print("============================================================")

#impresion 3 ejemplos a la vez

print("venta n°1")
llamar()

print("venta n°2")
llamar()

print("venta n°3")
llamar()