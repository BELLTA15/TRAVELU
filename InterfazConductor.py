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
        info_viaje = contenido.strip() + ", " + origen
        archivo2.write(info_viaje)
        archivo2.truncate()  # Truncate any remaining data

def guardar_destino(destino):
    # Leer el contenido de "info.txt" y obtener la información
    with open("info.txt", "r") as archivo_info:
        info_viaje = archivo_info.readline().strip()
        informacion = info_viaje.split(",")
        id_viaje = informacion[0].strip()
        origen_viaje = informacion[3].strip()
        destino_viaje = informacion[4].strip()

    # Leer todas las líneas del archivo "viajes.txt" y realizar las modificaciones
    with open("viajes.txt", "r") as archivo_viajes:
        lineas = archivo_viajes.readlines()

    nuevas_lineas = []
    encontrado = False

    for linea in lineas:
        partes = linea.strip().split(',')
        if partes[0].strip() == id_viaje:
            if partes[3].strip() == origen_viaje and partes[4].strip() == destino_viaje:
                # Si es el mismo ID y el mismo origen y destino, no se modifica
                mostrar_aviso()
                encontrado = True
                break

        # Si no se encuentra un ID coincidente o un destino diferente, se agrega la línea actual
        nuevas_lineas.append(linea)

    # Si no se encontró una coincidencia, se agrega la información de "info.txt" a "viajes.txt"
    if not encontrado:
        nuevas_lineas.append(info_viaje)

    # Escribir las nuevas líneas en "viajes.txt"
    with open("viajes.txt", "w") as archivo_viajes:
        archivo_viajes.writelines(nuevas_lineas)


def mostrar_aviso():
    aviso = tk.Tk()
    aviso.title("AVISO")
    aviso.geometry("400x400")
    aviso.label_aviso = ttk.Label(aviso, text="Ya existe un viaje con el mismo origen y destino", background='#053B50',font=("Franklin Gothic Medium Cond",18),foreground='white')
            
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