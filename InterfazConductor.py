import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring

class ViajeApp:
    def __init__(self, root):
        self.root = root
        root.title("Interfaz Conductor")
        root.geometry("800x600")
        root.configure(bg='#F2F2F2')  # Color de fondo más claro

        self.label_saludo = ttk.Label(root, text="Seleccione donde se encuentra", background='#F2F2F2', font=("Arial", 20), foreground='black')
        self.label_saludo.pack(pady=10, side=tk.TOP)

        self.label_mensaje = ttk.Label(root, text="Seleccione hacia donde va", background='#F2F2F2', font=("Arial", 20), foreground='black')
        self.label_mensaje.pack(pady=10)

        self.opciones_origen = ["Giron", "Floridablanca", "Piedecuesta", "Bucaramanga", "Otra Ciudad"]
        self.opciones_destino = ["Giron", "Floridablanca", "Piedecuesta", "Bucaramanga", "Otra Ciudad"]

        self.botones_origen = self.create_buttons(self.opciones_origen, "origen")
        self.botones_destino = self.create_buttons(self.opciones_destino, "destino")

        self.info_origen = ""
        self.info_destino = ""

        self.button_guardar = ttk.Button(root, text="Guardar Viaje", command=self.guardar_viaje, style="TButton")
        self.button_guardar.pack(pady=10, side=tk.TOP)

        self.button_reset = ttk.Button(root, text="Resetear Selección", command=self.reset_seleccion, style="TButton")
        self.button_reset.pack(pady=5, side=tk.TOP)

        self.button_ver_viajes = ttk.Button(root, text="Ver Viajes Guardados", command=self.ver_viajes, style="TButton")
        self.button_ver_viajes.pack(pady=5, side=tk.TOP)

        self.button_eliminar_viajes = ttk.Button(root, text="Eliminar Viajes", command=self.eliminar_viajes, style="TButton")
        self.button_eliminar_viajes.pack(pady=5, side=tk.TOP)

        self.button_editar_viaje = ttk.Button(root, text="Editar Viaje", command=self.editar_viaje, style="TButton")
        self.button_editar_viaje.pack(pady=5, side=tk.TOP)

        self.label_aviso = None
        self.lista_viajes = []

    def create_buttons(self, opciones, destino_tipo):
        botones = []
        for opcion in opciones:
            boton = ttk.Button(self.root, text=opcion, command=lambda op=opcion, dt=destino_tipo: self.mostrar_mensaje(op, dt))
            boton.pack(pady=5, side=tk.TOP)
            botones.append(boton)
        return botones

    def mostrar_mensaje(self, opcion, destino_tipo):
        if destino_tipo == "origen":
            self.label_saludo.config(text=f"Has seleccionado {opcion} {destino_tipo}")
            self.info_origen = opcion
        else:
            self.label_mensaje.config(text=f"Has seleccionado {opcion} {destino_tipo}")
            self.info_destino = opcion

    def guardar_viaje(self):
        if self.info_origen and self.info_destino:
            viaje_info = f"Origen: {self.info_origen}, Destino: {self.info_destino}"
            with open("viajes.txt", "a") as file:
                file.write(viaje_info + "\n")
            self.mostrar_aviso("Viaje Guardado", "El viaje ha sido guardado exitosamente.")
            self.reset_seleccion()
        else:
            self.mostrar_aviso("Error", "Debe seleccionar un origen y destino antes de guardar el viaje")

    def mostrar_aviso(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def reset_seleccion(self):
        self.info_origen = ""
        self.info_destino = ""
        self.label_saludo.config(text="Seleccione donde se encuentra")
        self.label_mensaje.config(text="Seleccione hacia donde va")

    def ver_viajes(self):
        with open("viajes.txt", "r") as file:
            viajes = file.readlines()
        if viajes:
            self.lista_viajes = viajes
            viajes_str = "\n".join(viajes)
            self.mostrar_aviso("Viajes Guardados", f"Lista de viajes guardados:\n{viajes_str}")
        else:
            self.mostrar_aviso("Sin Viajes", "No hay viajes guardados aún.")

    def eliminar_viajes(self):
        if self.lista_viajes:
            with open("viajes.txt", "w") as file:
                file.write("")
            self.mostrar_aviso("Viajes Eliminados", "Todos los viajes guardados han sido eliminados.")
            self.lista_viajes = []
        else:
             self.mostrar_aviso("Sin Viajes", "No hay viajes para eliminar.")
    
    def editar_viaje(self):
        if self.lista_viajes:
            seleccion = askstring("Editar Viaje", "Ingrese el número de línea del viaje que desea editar:")
            try:
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(self.lista_viajes):
                    nuevo_valor = askstring("Editar Viaje", "Ingrese el nuevo valor para el viaje:")
                    if nuevo_valor:
                        self.lista_viajes[seleccion - 1] = nuevo_valor + "\n"
                        with open("viajes.txt", "w") as file:
                            file.writelines(self.lista_viajes)
                        self.mostrar_aviso("Viaje Editado", "El viaje ha sido editado correctamente.")
                    else:
                        self.mostrar_aviso("Error", "El valor ingresado es inválido.")
                else:
                    self.mostrar_aviso("Error", "El número de línea ingresado está fuera de rango.")
            except ValueError:
                self.mostrar_aviso("Error", "Por favor, ingrese un número válido.")
        else:
            self.mostrar_aviso("Sin Viajes", "No hay viajes para editar.")

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 14), padding=10, background='#F2F2F2', foreground='black')
    app = ViajeApp(root)
    root.update()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.mainloop()