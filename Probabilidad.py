"""
Autor: Carlos Stiven Ruiz Rojas - 2259629
        Karen Grijalba Ortiz - 2259623
Fecha: 18/10/2023
Descricion: Justificacion de la probabilidad - Frecuencia absoluta

"""

dado1 = 0
dado2 = 0
dado3 = 0
dado4 = 0
acc = 0

for i in range(4,25):
    acc=0
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            for dado3 in range(1, 7):
                for dado4 in range(1, 7):
                    suma = dado1 + dado2 + dado3 + dado4
                    if suma == i:
                        acc = acc + 1
    print(f"Frecuencia absoluta del {i}: ",acc)
                    
             
                

