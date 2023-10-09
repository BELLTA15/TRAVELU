import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
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
style.configure('TLabel', foreground='white', font=('Corbel', 18), background='#053B50')
style.configure('TButton', font=('Corbel', 18), background='#EEEEEE', foreground='black')

#Imagen carro logo
image = Image.open("logo.png")
image = image.resize((200,200), Image.Resampling.BOX)

img = ImageTk.PhotoImage(image)
lbl_img = Label(image=img)
lbl_img.pack()



label_saludo = ttk.Label(root, text="¡Hola, ¿cómo estás?")
label_saludo.pack(pady=10)

label_tipo_usuario = ttk.Label(root, text="¿Nuevo por aquí? Elije como quiere registrarte")
label_tipo_usuario.pack(pady=10)

# Cambiar el color de fondo de los botones a gris claro
btn_usuario = ttk.Button(root, text="Usuario", command=abrir_registro_usu, style='TButton')
btn_usuario.pack(fill="both", expand=True, padx=10, pady=10)

btn_conductor = ttk.Button(root, text="Conductor", command=abrir_registro_cond, style='TButton')
btn_conductor.pack(fill="both", expand=True, padx=10, pady=10)

label_login = ttk.Label(root, text="¿Ya tienes cuenta?")
label_login.pack(pady=10)

btn_login = ttk.Button(root, text="Iniciar sesión", command=abrir_login, style='TButton')
btn_login.pack(fill="both", expand=True, padx=10, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()
