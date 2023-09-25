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
        tipo_producto= input("Ingrese el tipo de producto \n postres \n panes \n bebidas \n :")
        precio_producto= int(input("Ingrese el precio del producto: "))
        if tipo_producto == "postres":
            v_postres+=precio_producto
        elif tipo_producto == "panes":
            v_panes+=precio_producto
        elif tipo_producto == "bebidas":
            v_bebidas+=precio_producto
    v_final= v_postres + v_panes + v_bebidas
    return f"Los postres tienen un valor de {v_postres}, los panes de {v_panes}, las bebidas un valor de {v_bebidas}. El total del inventario es por: {v_final}"


cantidad_producto= int(input("Ingrese la cantidad de productos: "))
print(precio_total(cantidad_producto))
