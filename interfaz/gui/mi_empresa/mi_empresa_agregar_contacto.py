from utilities import class_new_frame as new_frame, datos_generales as dg, funciones as func
import tkinter as tk

ancho_label = 50
ancho_boton = 20

def mi_empresa_agregar_contacto(root):

    fr_agregar_empresa = new_frame.newFrame(root) # Frame AGREGAR EMPRESA
    
    
     # CONTENIDO ----------------------------------------------------------------
    
    fr_agregar_empresa.generar_label("MI EMPRESA")
    
    fr_agregar_empresa.generar_label("AGREGAR UN CONTACTO")

    
    # Ingresar RUC ----------------------------------------------------------------
    '''REEMPLAZAR DATOS'''
    fr_grid_0 = new_frame.newFrame(fr_agregar_empresa.frame) # Frame para crear grid para INGRESAR RUC
    fr_grid_0.aparecer()

    '''REEMPLAZAR DATOS'''
    fr_grid_1 = new_frame.newFrame(fr_agregar_empresa.frame) # Frame para crear grid para INGRESAR RUC
    fr_grid_1.aparecer()

    fr_grid_1.generar_label("NOMBRE:", pack_grid_place='grid', row=0, column=0)
    fr_grid_1.generar_entry(pack_grid_place='grid', row=0, column=1)
    
    fr_grid_1.generar_label("CELULAR:", pack_grid_place='grid', row=1, column=0)
    fr_grid_1.generar_entry(pack_grid_place='grid', row=1, column=1)

    fr_grid_1.generar_label("CORREO:", pack_grid_place='grid', row=2, column=0)
    fr_grid_1.generar_entry(pack_grid_place='grid', row=2, column=1)

    # ----------------------------------------------------------------

    fr_agregar_empresa.generar_boton("AGREGAR CONTACTO")#, funcion= lambda: func.cambio_frame(fr_mi_empresa, fr_agregar_empresa))

    
    return fr_agregar_empresa