import tkinter as tk
from tkinter import ttk

# Función para guardar datos en un archivo
def guardar_datos():
    nombre = nombre_entry.get()
    email = email_entry.get()
    id = id_entry.get()
    telefono = telefono_entry.get()
    contrasena = contrasena_entry.get()

    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre},{email},{contrasena},{id},{telefono}\n")

    # Limpiar los campos después de guardar los datos
    nombre_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    telefono_entry.delete(0, tk.END)
    contrasena_entry.delete(0, tk.END)

# Crear la ventana principal
window = tk.Tk()
window.title("Registro de Usuarios")

# Cambiar el color de fondo de la ventana principal a un tono de azul claro
window.configure(bg='#053B50')

# Crear etiquetas y campos de entrada
titulo_label = ttk.Label(window, text="Registro de Usuarios", font=("Franklin Gothic Medium Cond", 16), background='#053B50',foreground='white')
nombre_label = ttk.Label(window, text="Nombre:",font=("Corbel",12), background='#053B50',foreground='white')
email_label = ttk.Label(window, text="Email:",font=("Corbel",12), background='#053B50',foreground='white')
id_label = ttk.Label(window, text="ID:",font=("Corbel",12), background='#053B50',foreground='white')
telefono_label = ttk.Label(window, text="Telefono:",font=("Corbel",12), background='#053B50',foreground='white')
contrasena_label = ttk.Label(window, text="Contraseña:",font=("Corbel",12), background='#053B50',foreground='white')

nombre_entry = ttk.Entry(window)
email_entry = ttk.Entry(window)
id_entry = ttk.Entry(window)
telefono_entry = ttk.Entry(window)
contrasena_entry = ttk.Entry(window, show="*")  # Para ocultar la contraseña

# Crear botón de guardar
guardar_button = ttk.Button(window, text="Registrar", command=guardar_datos)

# Organizar los elementos en la ventana usando GridLayout
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)
nombre_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
nombre_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
id_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
id_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
telefono_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
telefono_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
contrasena_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
contrasena_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
guardar_button.grid(row=6, column=0, columnspan=2, pady=10)

# Alinear todos los elementos al centro de la ventana
for child in window.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Ajustar el tamaño de la ventana automáticamente
window.update_idletasks()
window.geometry(f"{window.winfo_reqwidth()}x{window.winfo_reqheight()}")

# Iniciar la interfaz gráfica
window.mainloop()