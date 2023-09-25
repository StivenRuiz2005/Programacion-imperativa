"""
autores: Carlos Stiven Ruiz Rojas (2259629)
         Jhames Plaza Luna (2259577)
         Jhonny Fernando Duque Villada (2259398)
         Nicolas Pulgarin Perez (2259346)
Fecha: 5 de abril 2022
Descripcion: Notas finales
"""
def nota_final(name_materia):
    nota1= float(input("Ingrese la nota 1: "))
    nota2= float(input("Ingrese la nota 2: "))
    nota3= float(input("Ingrese la nota 3: "))
    parcial= float(input("Ingrese la nota del parcial: "))

    if name_materia == "matematicas":
        promedio_nota = (nota1 + nota2 + nota3)/3
        total= (parcial*0.9)+(promedio_nota*0.1)
    elif name_materia == "quimica":
        promedio_nota = (nota1 + nota2 + nota3)/3
        total= (parcial*0.85)+(promedio_nota*0.15)
    elif name_materia == "fisica":
        promedio_nota = (nota1 + nota2 + nota3)/3
        total=(parcial*0.8)+(promedio_nota*0.2)
    else:
        total= -1
    return total
    

def materia():
    global name_materia
    name_materia= input("Ingrese el nombre de la materia: ")
    print(name_materia)
    print("===========================================================================")
    final= nota_final(name_materia)
    if 5 >= final >= 3:
        print(f"su nota final en",name_materia,"es: ",final,"\n Usted gano la materia")
    elif 0<= final <=2.9:
        print(f"su nota final en",name_materia,"es: ",final,"\n Usted perdio la materia")
    else:
        print("Nota no valida o materia no existente")
    print("============================================================================")

#Impresion 3 ejemplos a las vez
(materia())
(materia())
(materia())