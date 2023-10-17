"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 17/10/2023
Descricion: Censo de personas

"""

print("Bienvenido al censo de personas")
print("============JEFE DE HOGAR============")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
tipo = input("Ingrese su tipo de documento: ")
numero = (input("Ingrese su numero de documento: "))
fecha = input("Ingrese su fecha de nacimiento con el formato xx/xx/xxxx: ")
departamento = input("Ingrese su departamento de nacimiento: ")
ciudad = input("Ingrese su ciudad de nacimiento: ")
direccion = input("Ingrese su direccion: ")
cantidad_fam = int(input("Ingrese la cantidad de familiares en el hogar: "))

def censo():
    n = 1
    while ( n <= cantidad_fam):
        print(f"============FAMILIAR {n}============")
        nombre1 = input("Ingrese su nombre: ")
        apellido1 = input("Ingrese su apellido: ")
        tipo1 = input("Ingrese su tipo de documento: ")
        numero1 = (input("Ingrese su numero de documento: "))
        fecha1 = input("Ingrese su fecha de nacimiento con el formato xx/xx/xxxx: ")
        parentesco1 = input(f"Ingrese su parentesco con {nombre} : ")
        n = n + 1

censo()