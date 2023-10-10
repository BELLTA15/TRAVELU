import tkinter as tk

def guardar_informacion():
    nombre = nombre_entry.get()
    numero = numero_entry.get()
    correo = correo_entry.get()
    num_documento = num_documento_entry.get()

    # Guardar la información en un archivo
    with open('usuario.txt', 'w') as file:
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Número: {numero}\n")
        file.write(f"Correo: {correo}\n")
        file.write(f"Número de documento: {num_documento}\n")

    # Actualizar la etiqueta de información
    info_usuario.config(text=f"Información guardada:\nNombre: {nombre}\nNúmero: {numero}\nCorreo: {correo}\nNúmero de documento: {num_documento}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Información del Usuario")

# Etiquetas y campos de entrada
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(ventana)
nombre_entry.pack()

numero_label = tk.Label(ventana, text="Número:")
numero_label.pack()
numero_entry = tk.Entry(ventana)
numero_entry.pack()

correo_label = tk.Label(ventana, text="Correo:")
correo_label.pack()
correo_entry = tk.Entry(ventana)
correo_entry.pack()

num_documento_label = tk.Label(ventana, text="Número de documento:")
num_documento_label.pack()
num_documento_entry = tk.Entry(ventana)
num_documento_entry.pack()

# Botón para guardar la información
boton_guardar = tk.Button(ventana, text="Guardar Información", command=guardar_informacion)
boton_guardar.pack()

# Etiqueta para mostrar la información
info_usuario = tk.Label(ventana, text="", wraplength=300)
info_usuario.pack()

# Ejecutar la aplicación
ventana.mainloop()
