"""
Autor: Carlos Stiven Ruiz Rojas (2259629)
Fecha: 06 de mayo 2022
Descripcion: primera pregunta del parcial 1

"""
def salario_trabajador(tipo_trabajador,num_horas_trabajadas,tiempo_de_trabajo):
    if num_horas_trabajadas <192:
        return "Horas trabajadas minimas no cumplidas"
    else:
        #horas extras
        
        if num_horas_trabajadas == 192:
            h_extras= 0
        elif num_horas_trabajadas > 192:
            h_extras= num_horas_trabajadas - 192
        #tipo de trabajador
        if tipo_trabajador == "ejecutivo":
            salario_base = 3000000
            v_hora= salario_base/192
            p_hora_extra= 1.2*h_extras*v_hora
            s_total= salario_base+p_hora_extra
        elif tipo_trabajador == "administrativo":
            salario_base = 2000000
            v_hora= salario_base/192
            p_hora_extra= (1.2*v_hora)*h_extras
            s_total= salario_base+p_hora_extra
        elif tipo_trabajador == "auxiliar":
            salario_base= 1500000
            v_hora= salario_base/192
            p_hora_extra= 1.2*h_extras*v_hora
            s_total= salario_base + p_hora_extra
        if tiempo_de_trabajo >5:
            salario= (s_total*1.2)
            return salario
        else:
            salario=s_total
            return salario



tipo_trabajador= input("Ingrese el tipo de trabajador (Todo en minusculas) : ")
num_horas_trabajadas= float(input("Ingrese las horas trabajadas: "))
tiempo_de_trabajo=float(input("Ingrese el tiempo trabajado en la empresa: ")) 
print(salario_trabajador(tipo_trabajador,num_horas_trabajadas,tiempo_de_trabajo))