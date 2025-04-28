from utilities import class_new_frame as new_frame, funciones as func
from gui.mi_empresa import mi_empresa_agregar_empresa, mi_empresa_agregar_contacto
from gui.nueva_cotizacion import nueva_cotizacion_paso_2


ancho_label = 50
ancho_boton = 20

def nueva_cotizacion(root):

    fr_nueva_cotizacion = new_frame.newFrame(root) # Frame AGREGAR EMPRESA
    
    # CONTENIDO ----------------------------------------------------------------
    
    fr_nueva_cotizacion.generar_label("NUEVA COTIZACION")
    
 
    '''INGRESAR DATOS'''
     # Emisor ----------------------------------------------------------------
    fr_nueva_cotizacion.generar_label("VENDEDOR")
    vendedores = ["NOMBRE  CORREO@GMAIL.COM  CELULAR", "NOMBRE2  CORREO@GMAIL.COM  CELULAR"]
    fr_nueva_cotizacion.radioButton(*vendedores)


    # # Grid receptor ---------------------------------------------------------------
    # fr_nueva_cotizacion.generar_label("CLIENTE")

    # fr_cliente = new_frame.newFrame(fr_nueva_cotizacion) # Frame AGREGAR EMPRESA

    # fr_cliente_0 = new_frame.newFrame(fr_cliente)
    # fr_cliente_0.frame.grid(column=0, row=0, padx=10, pady=10) # Creamos un frame que será la columna 0 de un grid de 'fr_nueva_cotizacion'
    # if True: 
    #     fr_cliente_0_empresas = ["RAZON SOCIAL 3", "RAZON SOCIAL 1", "RAZON SOCIAL 2"]
    #     fr_cliente_0.radioButton(*fr_cliente_0_empresas)
    
    
    # fr_cliente_1 = new_frame.newFrame(fr_cliente)
    # fr_cliente_1.frame.grid(column=1, row=0, padx=10, pady=10) # Creamos un frame que será la columna 0 de un grid de 'fr_nueva_cotizacion'
    # if True: 
    #     fr_cliente_1_contactos = ["NOMBRE  CORREO@GMAIL.COM  CELULAR", "NOMBRE2  CORREO@GMAIL.COM  CELULAR"]
    #     fr_cliente_1.radioButton(*fr_cliente_1_contactos)


    # -----------------------------------------------------------------------------

    fr_nueva_cotizacion.generar_boton("SIGUIENTE", funcion= lambda: func.cambio_frame(fr_nueva_cotizacion, nueva_cotizacion_paso_2.nueva_cotizacion_paso_2(root)))#

    return fr_nueva_cotizacion


