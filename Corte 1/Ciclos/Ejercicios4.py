"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 22 de abril 2022
Descripcion: Salario

""" 

print("=======================For=========================")
def salario(empleados):
    retefuentes= 0
    for i in range(0,empleados):
         print("===================Empleado",i+1,"================")
         salario_base= int(input("Digite su salario basico:"))
         bonificaciones= int(input("Digite su bonificacion: "))
         IBC= salario_base*0.4
         if IBC < 1000000:
             IBC = 1000000
         eps= IBC * 0.125
         pension= IBC * 0.16
         arl= IBC * 0.005

         if salario_base >= 3000000:
             solidaridad = IBC * 0.1
         else:
             solidaridad= 0

         if salario_base > 4000000:
             retefuentes= salario_base + bonificaciones         
         if 4000000<= salario_base <= 800000:
             retefuentes = retefuentes * 0.089
         elif 8000000 < salario_base < 12000000:
             retefuentes = retefuentes * 0.125
         elif salario_base >= 12000000:
             retefuentes = retefuentes * 0.18
         else:
             retefuentes = 0
    
         total_descuentos = (eps + pension + arl + solidaridad)* 0.4
         print("El salario neto es: ",salario_base+bonificaciones-total_descuentos-retefuentes)
    return "Muchas gracias por usar mi aplicacion"
     
empleados = int(input("Digite la cantidad de empleados: "))

print(salario(empleados))

print("=======================While=====================")
def salario(empleados1):
    retefuentes= 0
    i=0
    while(i < empleados1):
         print("===================Empleado",i+1,"================")
         salario_base= int(input("Digite su salario basico:"))
         bonificaciones= int(input("Digite su bonificacion: "))
         IBC= salario_base*0.4
         if IBC < 1000000:
             IBC = 1000000
         eps= IBC * 0.125
         pension= IBC * 0.16
         arl= IBC * 0.005

         if salario_base >= 3000000:
             solidaridad = IBC * 0.1
         else:
             solidaridad= 0

         if salario_base > 4000000:
             retefuentes= salario_base + bonificaciones         
         if 4000000<= salario_base <= 800000:
             retefuentes = retefuentes * 0.089
         elif 8000000 < salario_base < 12000000:
             retefuentes = retefuentes * 0.125
         elif salario_base >= 12000000:
             retefuentes = retefuentes * 0.18
         else:
             retefuentes = 0
    
         total_descuentos = (eps + pension + arl + solidaridad)* 0.4
         print("El salario neto es: ",salario_base+bonificaciones-total_descuentos-retefuentes)
         i +=1
    return "Muchas gracias por usar mi aplicacion"
     
empleados1 = int(input("Digite la cantidad de empleados: "))

print(salario(empleados1))