import tkinter as tk
from utilities import datos_generales as dg
from gui import main_menu, navegacion as nav

# Crear la ventana principal ---------
root = tk.Tk()
root.title("Cotizacion")

root.geometry(f"{dg.ancho}x{dg.alto}")

# Navegacion ----------
navegacion = nav.nav(root)


# Inicio --------------
frameInicio = main_menu.inicio(root)


root.mainloop()