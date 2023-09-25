"""
Grupo: Nicolle López Colonia (2259630)
       Carlos Stiven Ruiz Rojas (2259629)
       Jhonny Fernando Duque (2259398)
Fecha: 19 de marzo 2022

"""
import math
#Variables

n_profe= str(input('Por favor ingrese su nombre: '))
hard_disk= float(input('Ingrese la capacidad de almacenamiento de su disco duro en GB: '))
val_disk= float(input('Ingrese el precio de los CD por unidad: '))

#Proceso

cant_disk= (hard_disk*1024)/700
iva= (cant_disk* val_disk)*0.19
precio= iva + (cant_disk* val_disk)

#salida

print(f'para almacenar {hard_disk} GB se requieren {math.ceil(cant_disk)} CDs que cuestan {round(precio)}')
