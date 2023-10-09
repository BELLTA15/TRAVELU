import tkinter as tk
from tkinter import ttk

def mostrar_mensaje(mensaje):
    label_saludo.config(text=mensaje)

# Crear una función para cada botón que cambie el mensaje de bienvenida
def mostrar_giron():
    mostrar_mensaje("Has seleccionado Giron")

def mostrar_floridablanca():
    mostrar_mensaje("Has seleccionado Floridablanca")

def mostrar_piedecuesta():
    mostrar_mensaje("Has seleccionado Piedecuesta")

def mostrar_bucaramanga():
    mostrar_mensaje("Has seleccionado Bucaramanga")

# Crear la ventana principal
window = tk.Tk()
window.title("Interfaz Usuario")
window.geometry("300x300")
window.configure(bg='#053B50')

# Crear etiqueta de bienvenida
label_saludo = ttk.Label(window, text="Seleccione la ruta que desea tomar", background='#053B50',font=("Franklin Gothic Medium Cond",18))
label_saludo.pack(pady=10)
# Crear botones
button_giron = ttk.Button(window, text="Giron", command=mostrar_giron)
button_floridablanca = ttk.Button(window, text="Floridablanca", command=mostrar_floridablanca)
button_piedecuesta = ttk.Button(window, text="Piedecuesta", command=mostrar_piedecuesta)
button_bucaramanga = ttk.Button(window, text="Bucaramanga", command=mostrar_bucaramanga)

# Empaquetar los botones en la ventana
button_giron.pack(pady=5)
button_floridablanca.pack(pady=5)
button_piedecuesta.pack(pady=5)
button_bucaramanga.pack(pady=5)

# Iniciar la interfaz gráfica
window.update()
window.geometry(f"{window.winfo_reqwidth()}x{window.winfo_reqheight()}")
window.mainloop()