"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 3/10/2023
Descricion: usando try and catch

"""
def division():
    try:
        try:
            num1 = int(input("Ingrese un numero: "))
            num2 = int(input("Ingrese un numero: "))
        except(ValueError):
            print("Error, ingrese valores numericos")
            division()
        else:
            print("La division es: ",num1/num2)
    except (ZeroDivisionError):
        print("No se puede dividir por cero")
        division()
        
division()