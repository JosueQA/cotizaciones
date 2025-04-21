from utilities import class_new_frame as new_frame, funciones as func
from gui.mis_productos import mis_productos_agregar_producto

ancho_label = 50
ancho_boton = 20

def mis_productos(root):

    fr_mis_productos = new_frame.newFrame(root) # Frame AGREGAR EMPRESA
    
    
     # CONTENIDO ----------------------------------------------------------------
    
    fr_mis_productos.generar_label("MIS PRODUCTOS")
    
    fr_mis_productos.generar_label("VISUALIZA Y AGREGA TUS PRODUCTOS")

        
    # Creacion de columnas -------------------------------------------------------
    fr_grid_0 = new_frame.newFrame(fr_mis_productos.frame)
    fr_grid_0.aparecer()

    fr_grid_0.generar_label("FECHA DE CREACION", pack_grid_place='grid', row=0, column=0, padx=15)
    fr_grid_0.generar_label("CODIGO", pack_grid_place='grid', row=0, column=1, padx=15)
    fr_grid_0.generar_label("PRODUCTO", pack_grid_place='grid', row=0, column=2, padx=15)
    fr_grid_0.generar_label("COSTO UNIT.", pack_grid_place='grid', row=0, column=4, padx=15)
    
    '''INGRESAR DATOS'''
    COTIZACIONES = {
        'COTI_CODIGO': ['COT20240801', 'COT20240802'],
        'COTI_FECHA': ['04/08/2024', '05/09/2024'],
        'COTI_EMISOR': ['MI EMPRESA S.A.C.', 'MI EMPRESA S.A.C.'],
        'COTI_RECEPTOR': ['EMPRESA EXTRAÑA S.A.C.', 'ORA EMPRESA E.I.R.L.']
    }
    

    # ----------------------------------------------------------------
    fr_mis_productos.generar_boton("AGREGAR PRODUCTO", funcion= lambda: func.cambio_frame(fr_mis_productos, mis_productos_agregar_producto.mis_productos_agregar_producto(root)))
     
   
    return fr_mis_productos