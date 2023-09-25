"""Calculadora del porcentaje de ganancias"""

from tkinter import *
from tkinter import ttk

interface = Tk()
interface.geometry("800x500")
interface.title("Porcentaje de Ganancias")

frame = ttk.Frame(interface,padding=10)

etiqueta1= Label(frame,text="Hola mundo")
etiqueta1.grid(row=0,column=0)

interface.mainloop()

"""
bases

c_total=int(input("Ingrese la cantidad de productos"))
p_producto= int(input("Ingrese el precio de el paquete total"))

#Calculo unidad

p_unidad= p_producto/ c_total
"""


