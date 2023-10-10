import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

# Ruta de la imagen seleccionada
imagen_seleccionada = None

# Función para mostrar mensaje
def mostrar_mensaje(mensaje):
    label_saludo.config(text=mensaje)

# Función para mostrar imagen
def mostrar_imagen(ruta):
    if ruta:
        imagen_window = tk.Toplevel(window)  # Crea una ventana secundaria
        imagen_window.title("Imagen")

        imagen = PhotoImage(file=ruta)

        label_imagen = ttk.Label(imagen_window, image=imagen, background='#053B50')
        label_imagen.image = imagen
        label_imagen.pack()

# Función para llenar el Treeview
def llenar_treeview(destino):
    tree.delete(*tree.get_children())  # Limpiar el Treeview

    with open("viajes.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[5] == destino:
                id = datos[0]
                nombre = datos[1]
                placas = datos[3]
                modelo = datos[2]
                origen = datos[4]
                paonde = datos[5]
                tree.insert("", "end", values=(id, nombre, modelo, placas, origen, paonde))

# Funciones para mostrar información y llenar el Treeview
def mostrar_giron():
    global imagen_seleccionada
    mostrar_mensaje("Has seleccionado Giron")
    imagen_seleccionada = 'Giron.png'
    mostrar_imagen(imagen_seleccionada)
    llenar_treeview("Giron")

def mostrar_floridablanca():
    global imagen_seleccionada
    mostrar_mensaje("Has seleccionado Floridablanca")
    imagen_seleccionada = 'Floridablanca.png'
    mostrar_imagen(imagen_seleccionada)
    llenar_treeview("Floridablanca")

def mostrar_piedecuesta():
    global imagen_seleccionada
    mostrar_mensaje("Has seleccionado Piedecuesta")
    imagen_seleccionada = 'Piedecuesta.png'
    mostrar_imagen(imagen_seleccionada)
    llenar_treeview("Piedecuesta")

def mostrar_bucaramanga():
    global imagen_seleccionada
    mostrar_mensaje("Has seleccionado Bucaramanga")
    imagen_seleccionada = 'Bucaramanga.png'
    mostrar_imagen(imagen_seleccionada)
    llenar_treeview("Bucaramanga")

# Crear ventana principal
window = tk.Tk()
window.title("Interfaz Usuario")
window.geometry("700x300")
window.configure(bg='#053B50')

# Crear etiqueta de saludo
label_saludo = ttk.Label(window, text="Seleccione la ruta que desea tomar", background='#053B50', font=("Franklin Gothic Medium Cond", 18), foreground='white')
label_saludo.pack(pady=10)

# Crear botones
button_giron = ttk.Button(window, text="Giron", command=mostrar_giron)
button_floridablanca = ttk.Button(window, text="Floridablanca", command=mostrar_floridablanca)
button_piedecuesta = ttk.Button(window, text="Piedecuesta", command=mostrar_piedecuesta)
button_bucaramanga = ttk.Button(window, text="Bucaramanga", command=mostrar_bucaramanga)

button_giron.pack(pady=5, anchor='e', fill='x')
button_floridablanca.pack(pady=5, anchor='e', fill='x')
button_piedecuesta.pack(pady=5, anchor='e', fill='x')
button_bucaramanga.pack(pady=5, anchor='e', fill='x')

# Crear Treeview fuera de la función
columns = ("ID", "Nombre", "Modelo", "Placas", "Origen", "Destino")
tree = ttk.Treeview(window, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Modelo", text="Modelo")
tree.heading("Placas", text="Placas")
tree.heading("Origen", text="Origen")
tree.heading("Destino", text="Destino")

# Ajustar el ancho de las columnas
tree.column("ID", width=100)  # Ancho de la columna Nombre
tree.column("Nombre", width=100)  # Ancho de la columna Correo
tree.column("Modelo", width=100)  # Ancho de la columna ID
tree.column("Placas", width=100)  # Ancho de la columna Contraseña
tree.column("Origen", width=100)  # Ancho de la columna Contraseña
tree.column("Destino", width=100)  # Ancho de la columna Contraseña
tree.pack(padx=10, pady=10)

# Iniciar la ventana principal
window.mainloop()