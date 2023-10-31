"""
Autor: Carlos Stiven Ruiz Rojas (2259629)
Fecha: 06 de mayo 2022
Descripcion: segunda pregunta del parcial 1

"""
def precio_total(cantidad_producto):
    v_postres=0
    v_panes=0
    v_bebidas=0
    for i in range(0,cantidad_producto):
        try:
            tipo_producto= input("Ingrese el tipo de producto \n postres \n panes \n bebidas \n :").lower()
            precio_producto= int(input("Ingrese el precio del producto: "))
        except(ValueError):
            print("Error, ingrese valores numericos")
            precio_total(cantidad_producto)
        if tipo_producto == "postres":
            v_postres+=precio_producto
        elif tipo_producto == "panes":
            v_panes+=precio_producto
        elif tipo_producto == "bebidas":
            v_bebidas+=precio_producto
        else:
            print("El tipo de producto no existe")
            precio_total(cantidad_producto)
    v_final= v_postres + v_panes + v_bebidas
    return f"Los postres tienen un valor de {v_postres}, los panes de {v_panes}, las bebidas un valor de {v_bebidas}. El total del inventario es por: {v_final}"

def datos():
    try:
        cantidad_producto= int(input("Ingrese la cantidad de productos: "))
    except(ValueError):
        print("El valor ingresado no es un numero entero")
        datos()
    else:
        print(precio_total(cantidad_producto))

if __name__ == "__main__":
    datos()