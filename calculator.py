from tkinter import *


ventana = Tk()
ventana.title("Calculadora")

# Entrrada de texto
e_texto = Entry(ventana, font = ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)

# TODO
# Funciones
def click_boton(value): 
    return

# botones
boton1 = Button(ventana, text = "1", width = 5, height = 2)
boton2 = Button(ventana, text = "2", width = 5, height = 2)
boton3 = Button(ventana, text = "3", width = 5, height = 2)
boton4 = Button(ventana, text = "4", width = 5, height = 2)
boton5 = Button(ventana, text = "5", width = 5, height = 2)
boton6 = Button(ventana, text = "6", width = 5, height = 2)
boton7 = Button(ventana, text = "7", width = 5, height = 2)
boton8 = Button(ventana, text = "8", width = 5, height = 2)
boton9 = Button(ventana, text = "9", width = 5, height = 2)
boton0 = Button(ventana, text = "0", width = 15, height = 2)

boton_ac = Button(ventana, text = "AC", width = 5, height = 2)
boton_parentesis_izq = Button(ventana, text = "(", width = 5, height = 2)
boton_parentesis_der = Button(ventana, text = ")", width = 5, height = 2)
boton_punto = Button(ventana, text = ".", width = 5, height = 2)

boton_suma = Button(ventana, text = "+", width = 5, height = 2)
boton_resta = Button(ventana, text = "-", width = 5, height = 2)
boton_mult = Button(ventana, text = "x", width = 5, height = 2)
boton_division = Button(ventana, text = "/", width = 5, height = 2)
boton_igual = Button(ventana, text = "=", width = 5, height = 2)

boton_ac.grid(row = 1, column = 0, padx=5, pady=5)
boton_parentesis_izq.grid(row = 1, column = 1, padx=5, pady=5)
boton_parentesis_der.grid(row = 1, column = 2, padx=5, pady=5)
boton_division.grid(row = 1, column = 3, padx=5, pady=5)

boton7.grid(row = 2, column = 0, padx=5, pady=5)
boton8.grid(row = 2, column = 1, padx=5, pady=5)
boton9.grid(row = 2, column = 2, padx=5, pady=5)
boton_mult.grid(row = 2, column = 3, padx=5, pady=5)

boton4.grid(row = 3, column = 0, padx=5, pady=5)
boton5.grid(row = 3, column = 1, padx=5, pady=5)
boton6.grid(row = 3, column = 2, padx=5, pady=5)
boton_resta.grid(row = 3, column = 3, padx=5, pady=5)

boton1.grid(row = 4, column = 0, padx=5, pady=5)
boton2.grid(row = 4, column = 1, padx=5, pady=5)
boton3.grid(row = 4, column = 2, padx=5, pady=5)
boton_suma.grid(row = 4, column = 3, padx=5, pady=5)

boton0.grid(row = 5, column = 0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row = 5, column = 2, padx=5, pady=5)
boton_igual.grid(row = 5, column = 3, padx=5, pady=5)

ventana.mainloop()