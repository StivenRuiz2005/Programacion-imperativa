"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 25 de marzo 2022
Descripcion: Cambio de divisas

"""

def cantidad_arboles(a):
    n_metros_2 = n_hectareas * 10000

    if n_metros_2 > 1000000:
        pt= n_metros_2 * 0.7
        ot= n_metros_2 * 0.2
        ct= n_metros_2 * 0.1

    elif n_metros_2 <= 1000000:
        pt= n_metros_2 * 0.5
        ot= n_metros_2 * 0.3
        ct= n_metros_2 * 0.2
    else:
        print('Cantidad de hectareas incorrecta :(')

    p= (pt/10)*8
    o= (ot/15)*15
    c= (ct/7)*12

    return p,o,c


n_hectareas= float(input('Ingrese el numero de hectareas: '))
print(cantidad_arboles(n_hectareas))