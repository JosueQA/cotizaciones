from utilities import class_new_frame as new_frame, funciones as func
from gui import main_menu

ancho_label = 50
ancho_boton = 20

def nueva_cotizacion_paso_2(root):

    fr_nueva_cotizacion_paso_2 = new_frame.newFrame(root) # Frame AGREGAR EMPRESA
    
    
     # CONTENIDO ----------------------------------------------------------------
    
    fr_nueva_cotizacion_paso_2.generar_label("NUEVA COTIZACION")
    
    fr_nueva_cotizacion_paso_2.generar_label("INGRESAR PRODUCTOS")

    
    # Creacion de columnas -------------------------------------------------------
    fr_grid_0 = new_frame.newFrame(fr_nueva_cotizacion_paso_2.frame)
    fr_grid_0.aparecer()

    '''INGRESAR DATOS'''
    fr_grid_0.generar_label("ITEM", pack_grid_place='grid', bd=3, relief="groove", row=0, column=0, padx=0)
    fr_grid_0.generar_label("CANTIDAD", pack_grid_place='grid', bd=3, relief="groove", row=0, column=1, padx=0)
    fr_grid_0.generar_label("DESCRIPCION", pack_grid_place='grid', bd=3, relief="groove", row=0, column=2, ipadx=30, padx=0)
    fr_grid_0.generar_label("VALOR UNIT.", pack_grid_place='grid', bd=3, relief="groove", row=0, column=3, padx=0)
    fr_grid_0.generar_label("IMPORTE", pack_grid_place='grid', bd=3, relief="groove", row=0, column=4, ipadx=10, padx=0)
    

    

    # ----------------------------------------------------------------
    fr_nueva_cotizacion_paso_2.generar_boton("AGREGAR PRODUCTO")

    fr_nueva_cotizacion_paso_2.generar_boton("CANCELAR", funcion=lambda: func.cambio_frame(fr_nueva_cotizacion_paso_2, main_menu.inicio(root), comportamiento='cancelar'))
    
    
    return fr_nueva_cotizacion_paso_2