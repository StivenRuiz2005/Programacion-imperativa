"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 08 de abril 2022
Descripcion: Promedio notas finales
"""
#for

def promedio1(n):
    materia=0
    ct=0
    for i in range(0,n):
        nf= float(input("Ingrese su nota final: "))
        cc= int(input("ingrse la cantidad de creditos de la asignatura: "))
        ct+=cc
        materia+=nf*cc
    return materia/ct

n=int(input("Ingrese la cantidad de materias a promediar: "))
print(promedio1(n))

#while

def promedio2(n):
    i=1 
    materia=0
    ct=0
    while i<=n:
        nf= float(input("Ingrese su nota final: "))
        cc= int(input("ingrse la cantidad de creditos de la asignatura: "))
        ct= ct + cc
        materia= (materia + (nf*cc))
        i+=1
    return materia/ct

n=int(input("Ingrese la cantidad de materias a promediar: "))
print(promedio2(n))