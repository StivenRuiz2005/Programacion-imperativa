"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 17/10/2023
Descricion: Censo de personas

"""

print("Bienvenido al censo de personas")
print("============JEFE DE HOGAR============")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
tipo = input("Tipo de documento: ")
numero = (input("Numero de documento: "))
fecha = input("Fecha de nacimiento con el formato xx/xx/xxxx: ")
departamento = input("Departamento de nacimiento: ")
ciudad = input("Ciudad de nacimiento: ")
direccion = input("Direccion: ")
cantidad_fam = int(input("Cantidad de familiares en el hogar: "))

nombre1 = [None]*cantidad_fam
apellido1 = [None]*cantidad_fam
tipo1 = [None]*cantidad_fam
numero1 = [None]*cantidad_fam
fecha1 = [None]*cantidad_fam
parentesco1 = [None]*cantidad_fam

def censo():
    n = 0
    while ( n < cantidad_fam):
        print(f"============FAMILIAR {n+1}============")
        nombre1[n] = input("Nombre: ")
        apellido1[n] = input("Apellido: ")
        tipo1[n] = input("Tipo de documento: ")
        numero1[n] = (input("Numero de documento: "))
        fecha1[n] = input("Fecha de nacimiento con el formato xx/xx/xxxx: ")
        parentesco1[n] = input(f"Parentesco con {nombre} : ")
        n = n + 1
    
    print(f"==========================Familia {apellido}============================")

    print(f"================JEFE DE HOGAR================")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Tipo de documento: {tipo}")
    print(f"Numero de documento: {numero}")
    print(f"Fecha de nacimiento con el formato xx/xx/xxxx: {fecha}")
    print(f"Departamento de nacimiento: {departamento}")
    print(f"Ciudad de nacimiento: {ciudad}")
    print(f"Direccion: {direccion}")
    print(f"Cantidad de familiares en el hogar: {cantidad_fam}")
    
    for i in range(0,cantidad_fam):
        print(f"============FAMILIAR {i+1}============")
        print(f"Nombre: {nombre1[i]}")
        print(f"Apellido: {apellido1[i]}")
        print(f"Tipo de documento: {tipo1[i]}")
        print(f"Numero de documento: {numero1[i]}")
        print(f"Fecha de nacimiento con el formato xx/xx/xxxx: {fecha1[i]}")
        print(f"Parentesco con {nombre} : {parentesco1[i]}")
        
    
censo()