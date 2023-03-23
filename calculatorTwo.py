from tkinter import *


root = Tk()

root.title("Calculator Two")

# Entrada de texto
texto = Entry(root, width=36)
texto.grid(row=0, column=0, columnspan=20, pady=5, padx=5)

indice = 0

def get_numbers(n):
    global indice
    texto.insert(indice, n)
    indice += 1

def get_operation(operator):
    global indice
    operator_longitud = len(operator)
    texto.insert(1, operator)
    indice += operator_longitud
    
def calculate():
    texto_state = texto.get()
    try:
        result = eval(texto_state)
        reset()
        texto.insert(0, result)
    except Exception:
        reset()
        texto.insert(0, "Error")
        
def reset():
    texto.delete(0, END)
    i = 0

# Botones
Button(root, text="0", width=15, height=2, command=lambda:get_numbers(0)).grid(row=5, column = 0, columnspan=2, padx=5, pady=5)
Button(root, text=".", width=4, height=2, command=lambda:get_numbers(".")).grid(row=5, column=2, padx=5, pady=5)
Button(root, text="=", width=4, height=2, command=lambda:calculate()).grid(row=5, column=3, padx=5, pady=5)

Button(root, text="1", width=4, height=2, command=lambda:get_numbers(1)).grid(row=4, column=0, padx=5, pady=5)
Button(root, text="2", width=4, height=2, command=lambda:get_numbers(2)).grid(row=4, column=1, padx=5, pady=5)
Button(root, text="3", width=4, height=2, command=lambda:get_numbers(3)).grid(row=4, column=2, padx=5, pady=5)
Button(root, text="+", width=4, height=2, command=lambda:get_operation("+")).grid(row=4, column=3, padx=5, pady=5)

Button(root, text="4", width=4, height=2, command=lambda:get_numbers(4)).grid(row=3, column=0, padx=5, pady=5)
Button(root, text="5", width=4, height=2, command=lambda:get_numbers(5)).grid(row=3, column=1, padx=5, pady=5)
Button(root, text="6", width=4, height=2, command=lambda:get_numbers(6)).grid(row=3, column=2, padx=5, pady=5)
Button(root, text="-", width=4, height=2, command=lambda:get_operation("-")).grid(row=3, column=3, padx=5, pady=5)

Button(root, text="7", width=4, height=2, command=lambda:get_numbers(7)).grid(row=2, column=0, padx=5, pady=5)
Button(root, text="8", width=4, height=2, command=lambda:get_numbers(8)).grid(row=2, column=1, padx=5, pady=5)
Button(root, text="9", width=4, height=2, command=lambda:get_numbers(9)).grid(row=2, column=2, padx=5, pady=5)
Button(root, text="X", width=4, height=2, command=lambda:get_operation("*")).grid(row=2, column=3, padx=5, pady=5)

Button(root, text="AC", width=4, height=2, command=lambda:reset()).grid(row=1, column=0, padx=5, pady=5)
Button(root, text="+/-", width=4, height=2, command=lambda:get_operation("/")).grid(row=1, column=1, padx=5, pady=5)
Button(root, text="%", width=4, height=2, command=lambda:get_operation("%")).grid(row=1, column=2, padx=5, pady=5)
Button(root, text="/", width=4, height=2, command=lambda:get_operation("/")).grid(row=1, column=3, padx=5, pady=5)

root.mainloop()