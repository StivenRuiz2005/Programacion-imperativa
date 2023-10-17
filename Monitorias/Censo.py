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

def censo():
    n = 1
    while ( n <= cantidad_fam):
        print(f"============FAMILIAR {n}============")
        nombre1 = input("Nombre: ")
        apellido1 = input("Apellido: ")
        tipo1 = input("Tipo de documento: ")
        numero1 = (input("Numero de documento: "))
        fecha1 = input("Fecha de nacimiento con el formato xx/xx/xxxx: ")
        parentesco1 = input(f"Parentesco con {nombre} : ")
        n = n + 1

censo()