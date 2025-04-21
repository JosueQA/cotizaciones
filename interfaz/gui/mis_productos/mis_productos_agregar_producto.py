from utilities import class_new_frame as new_frame, datos_generales as dg, funciones as func
import tkinter as tk

ancho_label = 50
ancho_boton = 20

def mis_productos_agregar_producto(root):

    mis_productos_agregar_producto = new_frame.newFrame(root) # Frame AGREGAR EMPRESA
    
    
     # CONTENIDO ----------------------------------------------------------------
    
    mis_productos_agregar_producto.generar_label("MIS PRODUCTOS")
    
    
    # Ingresar RUC ----------------------------------------------------------------
    '''REEMPLAZAR DATOS'''
    fr_grid_0 = new_frame.newFrame(mis_productos_agregar_producto.frame) 
    fr_grid_0.aparecer()

    '''REEMPLAZAR DATOS'''
    fr_grid_1 = new_frame.newFrame(mis_productos_agregar_producto.frame) 
    fr_grid_1.aparecer()

    fr_grid_1.generar_label("CODIGO:", pack_grid_place='grid', row=0, column=0)
    fr_grid_1.generar_entry(pack_grid_place='grid', row=0, column=1)
    
    fr_grid_1.generar_label("PRODUCTO:", pack_grid_place='grid', row=1, column=0)
    fr_grid_1.generar_entry(pack_grid_place='grid', row=1, column=1)

    fr_grid_1.generar_label("COSTO UNIT. (INC. IGV.):", pack_grid_place='grid', row=2, column=0)
    fr_grid_1.generar_entry(pack_grid_place='grid', row=2, column=1)

    # ----------------------------------------------------------------

    mis_productos_agregar_producto.generar_boton("AGREGAR CONTACTO")#, funcion= lambda: func.cambio_frame(fr_mi_empresa, mis_productos_agregar_producto))

    
    return mis_productos_agregar_producto