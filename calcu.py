import tkinter as tk

# Funciones de operación
def sumar():
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    resultado.set(num1 + num2)

def restar():
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    resultado.set(num1 - num2)

def multiplicar():
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    resultado.set(num1 * num2)

def dividir():
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    if num2 != 0:
        resultado.set(num1 / num2)
    else:
        resultado.set("Error: No se puede dividir por cero.")

# Ventana
ventana = tk.Tk()  #Llamamos a la ventana.
ventana.title("Calculadora Simple") #Título.
ventana.geometry("170x170") #Tamaño.
ventana.configure(bg="#FF0000") #Color.
# Variables para entrada y resultado
entrada_num1 = tk.Entry(ventana, width=10)   #Asignamos y guardamos las variables que el usuario va a meter.
entrada_num2 = tk.Entry(ventana, width=10)
resultado = tk.StringVar() #Variable del resultado.

# Etiquetas y botones
etiqueta_num1 = tk.Label(ventana, text="Primer número:") #Como en Java en orden ponemos  los labeles y lo que necesitmos .
entrada_num1 = tk.Entry(ventana, width=10)
etiqueta_num2 = tk.Label(ventana, text="Segundo número:")
entrada_num2 = tk.Entry(ventana, width=10)
etiqueta_resultado = tk.Label(ventana, text="Resultado:")

etiqueta_num1.grid(row=0, column=0) #Copiado de la calculadora de Java , asignamos donde irá cada cosa, Fila '0' - Columna '0'.
entrada_num1.grid(row=0, column=1) #Fila '0' - Columna '1'
etiqueta_num2.grid(row=1, column=0) #Fila '1' - Columna '0'
entrada_num2.grid(row=1, column=1) #Fila '1' - Columna '1'
etiqueta_resultado.grid(row=2, column=0) #Fila '2' - Columna '0'

# Etiqueta de resultado que se guardara con la operación.
resultado_etiqueta = tk.Label(ventana, textvariable=resultado)
resultado_etiqueta.grid(row=2, column=1) #Fila '2' - Columna '1'

# Botones y operaciones, agregamos funcionalidad a cada cosa con command podemos darle una accion.
btn_sumar = tk.Button(ventana, text="Sumar", command=sumar)
btn_restar = tk.Button(ventana, text="Restar", command=restar)
btn_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
btn_dividir = tk.Button(ventana, text="Dividir", command=dividir)

btn_sumar.grid(row=3, column=0) #Fila '3' - Columna '0'
btn_restar.grid(row=3, column=1) #Fila '3' - Columna '1'
btn_multiplicar.grid(row=4, column=0) #Fila '4' - Columna '0'
btn_dividir.grid(row=4, column=1) #Fila '4' - Columna '1'

# Ejecutamos
ventana.mainloop()
