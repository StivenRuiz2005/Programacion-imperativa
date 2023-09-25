from tkinter import *
from tkinter import ttk

ima = Tk()

ima.geometry("500x500")

logo= PhotoImage(file="Dia2.png")

etiqueta= Label(ima,image=logo).pack()

ima.mainloop()
