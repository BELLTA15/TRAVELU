import tkinter as tk
from tkinter import ttk

def mostrar_origen(mensaje):
    label_saludo.config(text=mensaje)

def mostrar_destino(mensaje):   
    label_mensaje.config(text=mensaje)    

#Metodo para guardar la informacion seleccionada con el boton
def guardar_origen(origen):
    with open("info.txt", "r+") as archivo2:  # Open in read and write mode
        contenido = archivo2.read()
        archivo2.seek(0)  # Move the file pointer to the beginning
        info_viaje = contenido.strip() + "," + origen
        archivo2.write(info_viaje)
        archivo2.truncate()  # Truncate any remaining data

def guardar_destino(destino):
    # Leer el contenido de "info.txt" y obtener la información
    with open("info.txt", "r+") as archivo2:  # Open in read and write mode
        contenido = archivo2.read()
        archivo2.seek(0)  # Move the file pointer to the beginning
        info_viaje = contenido.strip() + "," + destino
        archivo2.write(info_viaje)
        archivo2.truncate()  # Truncate any remaining data
    with open("info.txt", "r") as archivo_info:
        info_viaje = archivo_info.readline().strip()
        informacion = info_viaje.split(",")
        id_viaje = informacion[0].strip()
        verificar_viaje(id_viaje, informacion)
        
def verificar_viaje(id_viaje, informacion):
    lista_viajes = []
    sentinela = False
    with open("viajes.txt", "r") as archivo_viajes:
        for linea in archivo_viajes:
            elementos = linea.strip().split(",")
            lista_viajes.append(elementos)
    for i in range(len(lista_viajes)):
        if lista_viajes[i][0] == id_viaje:
            lista_viajes[i] = informacion
            sentinela = True
    if sentinela == False:
        lista_viajes.append(informacion)
    with open("viajes.txt", "w") as archivo_viajes:
        for i in range(len(lista_viajes)):
            archivo_viajes.write(",".join(lista_viajes[i]) + "\n")
                       
# Crear una función para cada botón que cambie el mensaje de bienvenida
def mostrar_giron():
    mostrar_origen("Has seleccionado Giron")
    origen = "Giron"
    guardar_origen(origen)

def mostrar_floridablanca():
    mostrar_origen("Has seleccionado Floridablanca")
    origen = "Floridablanca"
    guardar_origen(origen)

def mostrar_piedecuesta():
    mostrar_origen("Has seleccionado Piedecuesta")
    origen = "Piedecuesta"
    guardar_origen(origen)

def mostrar_bucaramanga():
    mostrar_origen("Has seleccionado Bucaramanga")
    origen = "Bucaramanga"
    guardar_origen(origen)

def mostrar_giron2():
    mostrar_destino("Has seleccionado Giron")
    destino = "Giron"
    guardar_destino(destino)

def mostrar_floridablanca2():
    mostrar_destino("Has seleccionado Floridablanca")
    destino = "Floridablanca"
    guardar_destino(destino)

def mostrar_piedecuesta2():
    mostrar_destino("Has seleccionado Piedecuesta")
    destino = "Piedecuesta"
    guardar_destino(destino)

def mostrar_bucaramanga2():
    mostrar_destino("Has seleccionado Bucaramanga")
    destino = "Bucaramanga"
    guardar_destino(destino)


# Crear la ventana principal
window = tk.Tk()
window.title("Interfaz Conductor")
window.geometry("300x300")
window.configure(bg='#053B50')

# Crear etiqueta de bienvenida
label_saludo = ttk.Label(window, text="Seleccione donde se encuentra", background='#053B50',font=("Franklin Gothic Medium Cond",18),foreground='white')
label_saludo.pack(pady=10,side=tk.TOP)
# Crear botones
button_giron = ttk.Button(window, text="Giron", command=mostrar_giron)
button_giron.pack(pady=5,side=tk.TOP)
button_floridablanca = ttk.Button(window, text="Floridablanca", command=mostrar_floridablanca)
button_floridablanca.pack(pady=5,side=tk.TOP)
button_piedecuesta = ttk.Button(window, text="Piedecuesta", command=mostrar_piedecuesta)
button_piedecuesta.pack(pady=5,side=tk.TOP)
button_bucaramanga = ttk.Button(window, text="Bucaramanga", command=mostrar_bucaramanga)
button_bucaramanga.pack(pady=5,side=tk.TOP)

#Crear etiqueda de mensaje en medio de los botones
label_mensaje = ttk.Label(window, text="Seleccione hacia donde va", background='#053B50',font=("Franklin Gothic Medium Cond",18),foreground='white')
label_mensaje.pack(pady=10,)

# Crear botones
button_giron2 = ttk.Button(window, text="Giron", command=mostrar_giron2)
button_giron2.pack(pady=5)
button_floridablanca2 = ttk.Button(window, text="Floridablanca", command=mostrar_floridablanca2)
button_floridablanca2.pack(pady=5)
button_piedecuesta2 = ttk.Button(window, text="Piedecuesta", command=mostrar_piedecuesta2)
button_piedecuesta2.pack(pady=5)
button_bucaramanga2 = ttk.Button(window, text="Bucaramanga", command=mostrar_bucaramanga2)
button_bucaramanga2.pack(pady=5)

# Iniciar la interfaz gráfica
window.update()
window.geometry(f"{window.winfo_reqwidth()}x{window.winfo_reqheight()}")
window.mainloop()