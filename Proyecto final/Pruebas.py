from pydoc import text
import numpy as np
from tkinter import *
from tkinter import ttk

"""
import numpy as np

inversion_inicial = float(input("Ingrese la inversion inicial: "))
porcentaje_crecimiento = float(input("Ingrese el porcentaje de crecimiento: "))

n = int(input("Ingrese cuantos flujos tuvo : "))
Vf = 0
for i in range(1,n+1):
    flujo_tiempo = float(input("Ingrese el Flujo del periodo: "))
    Vf = Vf + (flujo_tiempo/(1+(porcentaje_crecimiento/100))**i)
Vp = -(inversion_inicial) + Vf
print(Vp)
"""
def inversion():
    vp= float(int1.get())
    r= float(int2.get())

def flujo_tiempo():     
     global cantidadarray,flujoarray
     n=1 
     flujo_periodo = int3.get()

     cantidadarray=np.array([0])
     flujoarray=np.array([])
    
     cantidadarray = np.insert(cantidadarray,cantidadarray.size,float(n))
     flujoarray = np.insert(flujoarray,flujoarray.size,float(flujo_periodo))
     print(flujoarray)

     label10.insert(END,"\n"+str(n)+'\t'+flujo_periodo)

ventana=Tk()

ventana_width=900
ventana_height=550
screen_width=ventana.winfo_screenwidth()
screen_height=ventana.winfo_screenheight()
x=(screen_width/2)-(ventana_width/2)
y=(screen_height/2)-(ventana_height/2)
ventana.geometry(f'{ventana_width}x{ventana_height}+{int(x)}+{int(y)}')
ventana.title("Gestor de Proyectos")
ventana.configure(bg="#9BEDF3")
ventana.resizable (True,True)
ventana
label1=Label(ventana,text="Gestión del proyecto",bg="#9BEDF3",font="Helvetica 36 bold")
label1.grid(row=0,column=1,ipady=15)
label2=Label(ventana,text="Datos del proyecto",bg="#9BEDF3",font="Helvetica 18 bold")
label2.grid(row=1,column=1,ipady=15)
label3=Label(ventana,text="Inversión inicial",bg="#9BEDF3",font="Helvetica 12",anchor=W)
label3.grid(row=2,column=0,ipadx=50)
label4=Label(ventana,text="Porcentaje de rendimiento (%)",bg="#9BEDF3",font="Helvetica 12")
label4.grid(row=3,column=0,ipady=1)
label5=Label(ventana,text="Periodos de tiempo del proyecto",bg="#9BEDF3",font="Helvetica 18 bold")
label5.grid(row=4,column=1,ipady=12.5)
label6=Label(ventana,text="Flujo del periodo",bg="#9BEDF3",font="Helvetica 12",anchor=W)
label6.grid(row=5,column=0,ipadx=45)
label7=Label(ventana,text="Información",bg="#9BEDF3",font="Helvetica 12")
label7.grid(row=6,column=1,ipady=5)
label8=Label(ventana,text="VPN:",bg="#9BEDF3",font="Helvetica 18 bold",anchor=W)
label8.grid(row=9,column=0,ipadx=70)
label9=Label(ventana,text="Decisión: NO CALCULADO",bg="#9BEDF3",font="Helvetica 18 bold",anchor=CENTER)
label9.grid(row=9,column=1,ipadx=50)

label10= Label(ventana,highlightthickness=10,bg='white')
label10.config(highlightbackground="#9BEDF3",highlightcolor="#9BEDF3")
label10.grid(row=7,column=0,ipadx=300,ipady= 50,columnspan=3)

int1=Entry(ventana)
int1.grid(row=2,column=1)
int2=Entry(ventana)
int2.grid(row=3,column=1)
int3=Entry(ventana)
int3.grid(row=5,column=1)


boton1=Button(ventana,text="Establecer datos", command= inversion)
boton1.grid(row=2,column=2,ipadx=50,rowspan=2)
boton2=Button(ventana,text="Ingresar periodo", command= flujo_tiempo)
boton2.grid(row=5,column=2,ipadx=50)
boton3=Button(ventana,text="Calcular VPN",highlightthickness=2)
boton3.grid(row=8,column=1)
ventana.mainloop()