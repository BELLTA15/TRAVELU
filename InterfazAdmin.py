import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
window = tk.Tk()
window.title("Interfaz Admin")

# Establecer el tamaño de la ventana
window.geometry("400x400")

# Cambiar el color de fondo de la ventana principal a gris claro
window.configure(bg='#053B50')

# Crear etiqueta de bienvenida
label_saludo = ttk.Label(window, text="Lista de Usuarios", background='#053B51', font=("Franklin Gothic Medium Cond",18, "bold"))
label_saludo.pack(pady=10)

# Crear un marco para el listado de usuarios
frame_usuarios = ttk.Frame(window)
frame_usuarios.pack(pady=10)

# Crear encabezados de la tabla
columns = ("Nombre", "Correo", "ID","Contraseña")
tree = ttk.Treeview(frame_usuarios, columns=columns, show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Correo", text="Correo")
tree.heading("ID", text="ID")
tree.heading("Contraseña", text="Contraseña")

# Configurar el Scrollbar para interactuar con la tabla
vsb = ttk.Scrollbar(frame_usuarios, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

# Ubicar la tabla y el Scrollbar dentro del marco utilizando el método grid
tree.grid(row=0, column=0, sticky="nsew")
vsb.grid(row=0, column=1, sticky="ns")

# Configurar el marco para expandirse con la ventana principal
frame_usuarios.grid_rowconfigure(0, weight=1)
frame_usuarios.grid_columnconfigure(0, weight=1)

# Leer usuarios.txt y mostrar los datos en la tabla
with open("usuarios.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre = datos[0]
        correo = datos[1]
        id_usuario = datos[3]
        contrasena = datos[2]
        tree.insert("", "end", values=(nombre, correo, id_usuario,contrasena))

# Ajustar el ancho de las columnas
tree.column("Nombre", width=200)  # Ancho de la columna Nombre
tree.column("Correo", width=250)  # Ancho de la columna Correo
tree.column("ID", width=100)  # Ancho de la columna ID
tree.column("Contraseña", width=100) #Ancho de la columna Contraseña

# Obtener el ancho y alto requeridos del cuadro de la tabla
window_width = tree.winfo_reqwidth()
window_height = tree.winfo_reqheight()

# Establecer el tamaño de la ventana principal
window.geometry(f"{window_width+50}x{window_height+100}")

# Iniciar la interfaz gráfica
window.mainloop()
