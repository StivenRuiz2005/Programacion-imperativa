"""

Autores:  Carlos Stiven Ruiz Rojas (2259629)
          Juan Manuel Ramirez Agudelo (2259482)
          Juan David Rojas Narvaez (2259673)
          Alejandro Sierra betancourt (2259559)
Fecha: 22 de junio del 2022
Descripcion: Proyecto Final - Programacion imperativa

"""

from ast import Global
import numpy as np
from tkinter import *
from tkinter import ttk

#Funciones 
def inversion():
    global inversion_inicial,porcentaje
    inversion_inicial= float(int1.get())
    porcentaje= float(int2.get())
    return inversion_inicial,porcentaje

def flujo_tiempo():     
     global total
     n=1 
     flujo_periodo = int3.get()
     total(n,flujo_periodo)

cantidadarray=np.zeros(10)
flujoarray=np.zeros(10)
m=0
def total(n,flujo_periodo):
    global m    
    m= m+n
    global cantidadarray,flujoarray
    cantidadarray[m] = float(m)
    flujoarray[m] = float(flujo_periodo)
    label10.insert(END,"\n"+str(m)+'\t'+flujo_periodo)


def calculo():
    inver= inversion_inicial
    porcen= porcentaje
    global Vp
    Vf=0
    for i in range(1,m+1):
        Vf = Vf + (flujoarray[i]/(1+(porcen/100))**i)
    Vp = round((-(inver) + Vf),1)
    
    if Vp > 0:
        Vp.astype(str)
        label11["text"]= Vp
        label12["text"]= "Realizar"
    elif Vp < 0:
        Vp.astype(str)
        label11["text"]= Vp
        label12["text"]= "No realizar"  
#Configuración de la ventana
ventana=Tk()
ventana_width=1050
ventana_height=750
screen_width=ventana.winfo_screenwidth()
screen_height=ventana.winfo_screenheight()
x=(screen_width/2)-(ventana_width/2)
y=(screen_height/2)-(ventana_height/2)
ventana.geometry(f'{ventana_width}x{ventana_height}+{int(x)}+{int(y)}')
ventana.title("Gestor de Proyectos")
ventana.configure(bg="#9BEDF3")
ventana.resizable (False,False)

#frame

frame = Frame(ventana)
frame.grid(row=7,column=1)

#Labels

label1=Label(ventana,text="Gestión del proyecto",bg="#9BEDF3",font="Helvetica 36 bold")
label1.grid(row=0,column=1,ipadx=15,ipady=30)
label2=Label(ventana,text="Datos del proyecto",bg="#9BEDF3",font="Helvetica 18 bold")
label2.grid(row=1,column=1)
label3=Label(ventana,text="Inversión inicial",bg="#9BEDF3",font="Helvetica 12")
label3.grid(row=2,column=0)
label4=Label(ventana,text="Porcentaje de rendimiento (%)",bg="#9BEDF3",font="Helvetica 12")
label4.grid(row=3,column=0)
label5=Label(ventana,text="Peridos de tiempo del proyecto",bg="#9BEDF3",font="Helvetica 18 bold")
label5.grid(row=4,column=1)
label6=Label(ventana,text="Flujo del periodo",bg="#9BEDF3",font="Helvetica 12")
label6.grid(row=5,column=0)
label7=Label(ventana,text="Información",bg="#9BEDF3",font="Helvetica 12")
label7.grid(row=6,column=1)
label8=Label(ventana,text="VPN:",bg="#9BEDF3",font="Helvetica 18 bold")
label8.grid(row=9,column=0)
label9=Label(ventana,text="Decisión:",bg="#9BEDF3",font="Helvetica 18 bold")
label9.grid(row=9,column=2)
label10= Text(frame)
label10.insert('1.0',"Periodo\tUtilidad")
label10.grid()

label11=Label(ventana,text="No calculado",bg="#9BEDF3",font="Helvetica 18 bold")
label11.grid(row=10,column= 0)

label12=Label(ventana,text="No calculado",bg="#9BEDF3",font="Helvetica 18 bold")
label12.grid(row=10,column= 2)

#Entradas

int1=Entry(ventana)
int1.grid(row=2,column=1)
int2=Entry(ventana)
int2.grid(row=3,column=1)
int3=Entry(ventana)
int3.grid(row=5,column=1)


#Botones

boton1=Button(ventana,text="Establecer datos", command= inversion)
boton1.grid(row=2,column=2,ipadx=30)
boton2=Button(ventana,text="Ingresar periodo", command= flujo_tiempo)
boton2.grid(row=5,column=2,ipadx=30)
boton3=Button(ventana,text="Calcular VPN", command = calculo)
boton3.grid(row=8,column=1,rowspan=4)
ventana.mainloop()
