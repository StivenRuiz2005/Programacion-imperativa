import numpy as np
from tkinter import *
from tkinter import ttk

# Programación del Frontend

#Configuración de la ventana
ventana=Tk()
ventana_width=950
ventana_height=600
screen_width=ventana.winfo_screenwidth()
screen_height=ventana.winfo_screenheight()
x=(screen_width/2)-(ventana_width/2)
y=(screen_height/2)-(ventana_height/2)
ventana.geometry(f'{ventana_width}x{ventana_height}+{int(x)}+{int(y)}')
ventana.title("Gestor de Proyectos")
ventana.configure(bg="#9BEDF3")
ventana.resizable (True,True)

#Labels

label1=Label(ventana,text="Luisa es gay",bg="#9BEDF3",font="Helvetica 36 bold")
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
label9=Label(ventana,text="Decisión",bg="#9BEDF3",font="Helvetica 18 bold")
label9.grid(row=9,column=2)

#Entradas

int1=Entry(ventana)
int1.grid(row=2,column=1)
int2=Entry(ventana)
int2.grid(row=3,column=1)
int3=Entry(ventana)
int3.grid(row=5,column=1)
int4=Entry(ventana)
int4.grid(row=7,column=1,ipadx=100,ipady=50)

#Botones

boton1=Button(ventana,text="Establecer datos")
boton1.grid(row=2,column=2,ipadx=30)
boton2=Button(ventana,text="Ingresar periodo")
boton2.grid(row=5,column=2,ipadx=30)
boton3=Button(ventana,text="Calcular VPN")
boton3.grid(row=8,column=1)
ventana.mainloop()

# Programación Backend

