from utilities import class_new_frame as new_frame, datos_generales as dg, funciones as func
import tkinter as tk

ancho_label = 50
ancho_boton = 20

def mis_cotizaciones(root):

    fr_mis_cotizaciones = new_frame.newFrame(root) # Frame AGREGAR EMPRESA
    
    
     # CONTENIDO ----------------------------------------------------------------
    
    fr_mis_cotizaciones.generar_label("MIS COTIZACIONES")
    
    fr_mis_cotizaciones.generar_label("VISUALIZA Y DESCARGA TUS COTIZACIONES CREADAS")

    
    '''INGRESAR DATOS'''
    fr_grid_0 = new_frame.newFrame(fr_mis_cotizaciones.frame) # Frame para crear grid para INGRESAR RUC
    fr_grid_0.aparecer()

    fr_grid_0.generar_label("FECHA", pack_grid_place='grid', row=0, column=0, padx=15)
    fr_grid_0.generar_label("CODIGO", pack_grid_place='grid', row=0, column=1, padx=15)
    fr_grid_0.generar_label("EMISOR", pack_grid_place='grid', row=0, column=2, padx=15)
    fr_grid_0.generar_label("RECEPTOS", pack_grid_place='grid', row=0, column=3, padx=15)

    COTIZACIONES = {
        'COTI_CODIGO': ['COT20240801', 'COT20240802'],
        'COTI_FECHA': ['04/08/2024', '05/09/2024'],
        'COTI_EMISOR': ['MI EMPRESA S.A.C.', 'MI EMPRESA S.A.C.'],
        'COTI_RECEPTOR': ['EMPRESA EXTRAÑA S.A.C.', 'ORA EMPRESA E.I.R.L.']
    }
    
    
    return fr_mis_cotizaciones