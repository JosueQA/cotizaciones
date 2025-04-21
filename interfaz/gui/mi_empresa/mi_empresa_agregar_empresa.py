from utilities import class_new_frame as new_frame, datos_generales as dg, funciones as func
import tkinter as tk

ancho_label = 50
ancho_boton = 20

def mi_empresa_agregar_empresa(root):

    fr_agregar_empresa = new_frame.newFrame(root) # Frame AGREGAR EMPRESA
    
    
     # CONTENIDO ----------------------------------------------------------------
    
    fr_agregar_empresa.generar_label("MI EMPRESA")
    
    fr_agregar_empresa.generar_label("AGREGAR UNA EMPRESA")

    
    # Ingresar RUC ----------------------------------------------------------------
    '''REEMPLAZAR DATOS'''
    fr_grid_0 = new_frame.newFrame(fr_agregar_empresa.frame) # Frame para crear grid para INGRESAR RUC
    fr_grid_0.aparecer()

    fr_grid_0.generar_label("INGRESAR RUC:", pack_grid_place='grid', row=0, column=0,pady=15)
    fr_grid_0.generar_entry(pack_grid_place='grid', row=0, column=1,pady=15)
    fr_grid_0.generar_boton("BUSCAR", pack_grid_place='grid', row=0, column=3,pady=15)
    

    # Resultados de la busqueda----------------------------------------------------------------

    '''REEMPLAZAR DATOS'''
    fr_grid_1 = new_frame.newFrame(fr_agregar_empresa.frame) # Frame para crear grid para INGRESAR RUC
    fr_grid_1.aparecer()

    fr_grid_1.generar_label("RUC:", pack_grid_place='grid', row=0, column=0)
    fr_grid_1.generar_label("_____________", pack_grid_place='grid', row=0, column=1)
    
    fr_grid_1.generar_label("RAZON SOCIAL:", pack_grid_place='grid', row=1, column=0)
    fr_grid_1.generar_label("_____________", pack_grid_place='grid', row=1, column=1)

    fr_grid_1.generar_label("DIRECCION:", pack_grid_place='grid', row=2, column=0)
    fr_grid_1.generar_label("_____________", pack_grid_place='grid', row=2, column=1)

    # ----------------------------------------------------------------

    fr_agregar_empresa.generar_boton("AGREGAR EMPRESA")#, funcion= lambda: func.cambio_frame(fr_mi_empresa, fr_agregar_empresa))

    
    return fr_agregar_empresa