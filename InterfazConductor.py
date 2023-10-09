import tkinter as tk
from tkinter import ttk

# Mostrar ventana que dice "Bienvenido conductor"
window = tk.Tk()
window.title("Interfaz Conductor")

#establecer el tamaño de la ventana
window.geometry("300x300")


# Cambiar el color de fondo de la ventana principal a gris claro
window.configure(bg='#053B50')

# Crear etiqueta de bienvenida
label_saludo = ttk.Label(window, text="Hola conductor, ¿cómo estás?", background='#053B51', font=("Franklin Gothic Medium Cond",18))
label_saludo.pack(pady=10)

# Iniciar la interfaz gráfica
window.update()  # Forzar una actualización para calcular el tamaño correcto
window.geometry(f"{window.winfo_reqwidth()}x{window.winfo_reqheight()}")  # Ajustar tamaño automáticamente

# Iniciar la interfaz gráfica
window.mainloop()
