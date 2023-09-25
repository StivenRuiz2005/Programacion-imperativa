"""
Autor: Carlos Stiven Ruiz Rojas (2259629)
Fecha: 06 de mayo 2022
Descripcion: tercera pregunta del parcial 1

"""
def costo_recibo(kw):
    if 0<kw<=300:
         kw_total= kw*50
    elif 301<=kw<=500:
         kw_total= ((300*50)+((kw-300)*100))
    elif 501<=kw<=1000:
         kw_total= ((300*50)+(200*100)+((kw-500)*150))
    else:
         kw_total= ((300*50)+(200*100)+(500*150)+((kw-1000)*200))
    return kw_total


kw=float(input("Ingrese el numero de KW gastados: "))
print(costo_recibo(kw))