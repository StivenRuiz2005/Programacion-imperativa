"""
Autor: Carlos Stiven Ruiz Rojas
Fecha: 29 de abril 2022
Descripcion: Partidos

"""
def total(n_partidos):
    puntos=0
    p_g=0
    p_p=0
    p_e=0
    g_a_t=0
    g_c_t=0
    for i in range(0,n_partidos):
        print(f"============================Partido {i+1}===================================")
        G_A= int(input(f"Ingrese los goles a favor del partido: "))
        G_C=int(input(f"Ingrese los goles recibidos en el partido: "))
        if G_A > G_C:
            p_g +=1
            puntos += 3
        elif G_C == G_A:
            p_e += 1
            puntos += 1           
        else:
            p_p += 1
            puntos += 0
        g_a_t += G_A
        g_c_t += G_C
    print(f"=================================================\n El EQUIPO {nombre}\n=====================================================\n puntos totales: {puntos} \n Gano:{p_g}\n Perdio:{p_p}\n empato: {p_e}\n goles a favor: {g_a_t} \n goles en contra: {g_c_t}")

nombre=str(input("Ingrese el nombre del equipo: "))
n_partidos=int(input("ingrese el numeros de partidos jugados: "))
(total(n_partidos))



       