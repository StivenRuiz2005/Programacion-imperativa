"""
Autor: Carlos Stiven Ruiz Rojas (2259629)
Fecha: 03 de junio 2022
Descripcion: Mi primera interface

"""
from tkinter import *
from tkinter import ttk


def mensaje():
    bb="Te quiero y adoro mushisimooooo <3"
    shi="Muchos bejoos para ti :)"
    etiqueta1["text"] = bb
    etiqueta2["text"] = shi
inf  = Tk() #Declaramos interfaz
inf.geometry("300x300") #Tamaño
inf.title("Mi primera interface")

# Frame
frame = ttk.Frame(inf,padding=10) #Creo un frame
frame.grid()#Acomodar los elementos en un matriz

#crear la matriz
etiqueta1= Label(frame,text="Hola mivida")
etiqueta1.grid(row=0,column=1)

etiqueta2= Label(frame,text="")
etiqueta2.grid(row=1,column=0)
#Crear boton 
ttk.Button(frame,text="Presioname", command=mensaje).grid(row=2,column=0)

#Imagen 

inf.mainloop() #Esto hace que la interfaz quede cargada