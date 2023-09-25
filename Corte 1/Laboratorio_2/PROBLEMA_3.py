"""
autores: Carlos Stiven Ruiz Rojas (2259629)
         Jhames Plaza Luna (2259577)
         Jhonny Fernando Duque Villada (2259398)
         Nicolas Pulgarin Perez (2259346)
Fecha: 5 de abril 2022
Descripcion: Indice de Masa Corporal
"""
def imc(altura,peso):
    global IMC
    IMC= peso/(altura**2)
    return IMC

def estado(imc):
    if imc < 18.5:
        a="Su estado es: Bajo peso"
    elif 18.5 < imc > 24.9:
        a="su estado es: Peso normal"
    elif 25 <= imc >= 29.9:
        a="su estado es: sobrepeso"
    else:
        a="su estado es: Obesidad tipo I"
    return a


def llamar():
    global nombre,altura,peso
    nombre=input("Ingrese su nombre: ")
    altura= float(input("ingrese su altura en metros: "))
    peso= float(input("Ingrese su peso en kilos: "))
    print("======================================================")
    print("Su nombre es: ",nombre)
    print("su altura es: ",altura)
    print("su peso es: ",peso)
    print("Su Indice de MAsa Corporal es: ",imc(altura,peso))
    print(estado(IMC))
    print("=======================================================")

#impresion de los 3 ejemplos a la vez

llamar()
llamar()
llamar()