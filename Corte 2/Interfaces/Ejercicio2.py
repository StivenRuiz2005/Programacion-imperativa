"""
Autor: Carlos Stiven Ruiz Rojas (2259629)
Fecha: 03 de junio 2022
Descripcion: Calculadora

"""

from cProfile import label
from tkinter import *
from tkinter import ttk

interface = Tk()
interface.geometry("400x400")
interface.title("Calculadora Epicaaaaa")

frame = ttk.Frame(interface,padding=10)

etiqueta1= Label(frame,text="Hola mundo")
etiqueta1.grid(row=0,column=0)

interface.mainloop()

# Manejar los elementos