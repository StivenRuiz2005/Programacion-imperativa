"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 2/10/2023
Descricion: Tablas de multiplicar Con For o While

"""

##################### FOR #########################

for i in range(7,13): # Ciclo con limites inicial y final
    print (" TABLA DEL",i)
    acc=0
    for j in range(1,10):
        print(i," X ",j," = ",i*j)
        acc += i*j
    print("Suma total de la tabla del",i ," = ",acc)

#################### WHILE ########################

i= 7
while (i < 13): #Ciclo Con condicion
    print (" TABLA DEL",i)
    acc=0
    j=1
    while(j < 10):
        print(i," X ",j," = ",i*j)
        acc += i*j
        j+=1
    print("Suma total de la tabla del",i ," = ",acc)
    i += 1
    



