import tkinter as tk
from tkinter import ttk
import subprocess

def abrir_conductor():
    subprocess.Popen(["python3", "InterfazConductor.py"])

def abrir_usuario():
    subprocess.Popen(["python3", "InterfazUsuario.py"])
def abrir_admin():
    subprocess.Popen(["python3", "InterfazAdmin.py"])

# Declarar las variables como globales
usuario = False
conductor = False

def verificar_usuario():
    global usuario, conductor  # Declarar que estamos utilizando las variables globales
    email = email_entry.get()
    contrasena = contrasena_entry.get()
    
    # Verificar en archivos y establecer las variables de usuario y conductor
    if ver_archivo("usuarios.txt", email, contrasena):
        print("Bienvenido usuario")
        usuario = True
        abrir_usuario()  # Abrir la interfaz de usuario
    elif ver_archivo("conductores.txt", email, contrasena):
        print("Bienvenido conductor")
        conductor = True
        abrir_conductor()  # Abrir la interfaz de conductor
    elif ver_archivo("admins.txt", email, contrasena):
        print("Bienvenido admin")
        conductor = True
        abrir_admin()  # Abrir la interfaz de admin
    else:
        print("Usuario no registrado o contraseña incorrecta")

def ver_archivo(nombre: str, email: str, contrasena: str):
    with open(nombre, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[1] == email and datos[2] == contrasena:
                return True
    return False  # Solo devuelve False si no se encuentra una coincidencia

window = tk.Tk()
window.title("Inicio de Sesión")

# Establecer el tamaño de la ventana
window.geometry("300x300")

# Cambiar el color de fondo de la ventana principal a un tono de azul claro
window.configure(bg='#053B50')

# Crear etiquetas y campos de entrada
titulo_label = ttk.Label(window, text="Inicio de Sesión", font=("Franklin Gothic Medium Cond", 18), background='#053B50')
email_label = ttk.Label(window, text="Email:",font=("Corbel",12), background='#053B50')
contrasena_label = ttk.Label(window, text="Contraseña:",font=("Corbel",12), background='#053B50')

email_entry = ttk.Entry(window)
contrasena_entry = ttk.Entry(window, show="*", background='#f0f5f5')  # Para ocultar la contraseña

# Crear botón de ingresar
guardar_button = ttk.Button(window, text="Ingresar", command=verificar_usuario)

# Organizar los elementos en la ventana usando GridLayout
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)
email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
contrasena_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
contrasena_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
guardar_button.grid(row=3, column=0, columnspan=2, pady=10)

# Alinear todos los elementos al centro de la ventana
for child in window.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Ajustar el tamaño de la ventana automáticamente
window.update_idletasks()
window.geometry(f"{window.winfo_reqwidth()}x{window.winfo_reqheight()}")

# Iniciar la interfaz gráfica
window.mainloop()
