"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 01 abril 2022
Descripcion: Dia sin IVA
"""

def total(precio,tipo):
  if precio >= 1500000:
    if tipo == 'alimentos':
      iva = (precio*0.05)
    elif tipo == 'tecnologia':
      iva = (precio*0.08)
    elif tipo =='ropa':
      iva = (precio*0.19)
    elif tipo == 'medicamentos':
      iva = (precio*0.12)
    else:
      print('ese tipo de producto no esta disponible')
    if iva > 200000:
      final= iva - (20000+iva*0.02)
      return  precio + final
    else:
      return iva + precio
  elif precio < 1500000:
    return precio
  else:
    print('el valor ingresado fue incorrecto')
    
precio=float(input('Digite el precio del producto: '))
tipo= str(input('Ingrese el tipo de producto: '))

print('El precio final es',total(precio,tipo))