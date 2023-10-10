import tkinter as tk
from tkinter import ttk
import subprocess

def abrir_registro_cond():
    subprocess.Popen(["python3", "registroCond.py"])

def abrir_registro_usu():
    subprocess.Popen(["python3", "registroUsu.py"])
    
def abrir_login():
    subprocess.Popen(["python3", "login.py"])

root = tk.Tk()
root.title("Registro de Usuarios")

# Establecer resolución inicial
root.geometry("600x800")

# Cambiar el color de fondo de la ventana principal a gris claro
root.configure(bg='#053B50')

# Crear un estilo personalizado
style = ttk.Style()
style.configure('TLabel', foreground='white', font=('Arial', 12), background='#053B50')
style.configure('TButton', font=('Arial', 12), background='#EEEEEE', foreground='black')

#Imagen carro logo
img = tk.PhotoImage(file="logo.png")
label_img = tk.Label(root, image=img).pack()

#Anadir comentario
label_saludo = ttk.Label(root, text="¡Hola, ¿cómo estás?")
label_saludo.pack(pady=10)

#Añadir comentario
label_tipo_usuario = ttk.Label(root, text="¿Nuevo por aquí? Elije como quiere registrarte")
label_tipo_usuario.pack(pady=10)

# Cambiar el color de fondo de los botones a gris claro
btn_usuario = ttk.Button(root, text="Usuario", command=abrir_registro_usu, style='TButton')
btn_usuario.pack(fill="both", expand=True, padx=10, pady=10)

#Aladir boton para ingresar al interfaz registro conductor
btn_conductor = ttk.Button(root, text="Conductor", command=abrir_registro_cond, style='TButton')
btn_conductor.pack(fill="both", expand=True, padx=10, pady=10)

#Añadir cometario
label_login = ttk.Label(root, text="¿Ya tienes cuenta?")
label_login.pack(pady=10)

#Aladir boton para ingresar al interfaz admin
btn_login = ttk.Button(root, text="Iniciar sesión", command=abrir_login, style='TButton')
btn_login.pack(fill="both", expand=True, padx=10, pady=10)

def cerrar_todo():
    #Borrar la informacion de info.txt
    with open("info.txt", "w") as archivo:
        archivo.write("")
    root.destroy()

boton_salir = tk.Button(root, text="Salir", command=cerrar_todo,foreground='black', font=('Arial', 12), background='white')
boton_salir.pack(fill="both", expand=True, padx=10, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()