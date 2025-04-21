from utilities import class_new_frame as new_frame, funciones as func
from gui.mi_empresa import mi_empresa_agregar_empresa, mi_empresa_agregar_contacto
from gui.nueva_cotizacion import nueva_cotizacion_paso_2


ancho_label = 50
ancho_boton = 20

def nueva_cotizacion(root):

    fr_nueva_cotizacion = new_frame.newFrame(root) # Frame AGREGAR EMPRESA
    
     # CONTENIDO ----------------------------------------------------------------
    
    fr_nueva_cotizacion.generar_label("NUEVA COTIZACION")
    
    # Grid body ----------------------------------------------------------------
    fr_grid_body = new_frame.newFrame(fr_nueva_cotizacion.frame) # Frame para crear grid para INGRESAR RUC
    fr_grid_body.aparecer()


    '''INGRESAR DATOS'''
    # Grid emisor ----------------------------------------------------------------
    emisor_empresas = ["RAZON SOCIAL 1", "RAZON SOCIAL 2", "RAZON SOCIAL 3"]
    emisor_contactos = ["NOMBRE  CORREO@GMAIL.COM  CELULAR", "NOMBRE2  CORREO@GMAIL.COM  CELULAR"]
    nuevo_grid(root, fr_nueva_cotizacion, fr_grid_body, 0, "EMISOR", emisor_empresas, emisor_contactos)
    


    # Grid receptor ---------------------------------------------------------------
    receptor_empresas = ["RAZON SOCIAL 3", "RAZON SOCIAL 1", "RAZON SOCIAL 2"]
    receptor_contactos = ["NOMBRE  CORREO@GMAIL.COM  CELULAR", "NOMBRE2  CORREO@GMAIL.COM  CELULAR"]
    nuevo_grid(root, fr_nueva_cotizacion, fr_grid_body, 1, "RECEPTOR", receptor_empresas, receptor_contactos)

    # -----------------------------------------------------------------------------

    fr_nueva_cotizacion.generar_boton("SIGUIENTE", funcion= lambda: func.cambio_frame(fr_nueva_cotizacion, nueva_cotizacion_paso_2.nueva_cotizacion_paso_2(root)))#

    return fr_nueva_cotizacion



def nuevo_grid(root, fr_actual, frame_padre, int_columna, str_emisor_o_receptor, list_empresa_radiobutton, list_contactos_radiobutton):
    
    # Creamos el grid contenedor
    fr_grid_contenedor = new_frame.newFrame(frame_padre.frame)
    fr_grid_contenedor.frame.grid(row=0, column=int_columna, padx=10, pady=10)
    


    # Empresas ----------------------------------------------------------------
    fr_grid_contenedor.generar_label(str_emisor_o_receptor)

    # Generamos las opciones a elegir de las empresas creadas
    fr_grid_contenedor.radioButton(*list_empresa_radiobutton) # El ' * ' desempaqueta una lista o tupla, para poder pasar los elementos como valores

    # Grid para los botones de la seccion empresas --------------------------------
    fr_grid_contenedor.generar_boton("NUEVA EMPRESA", funcion= lambda: func.cambio_frame(fr_actual, mi_empresa_agregar_empresa.mi_empresa_agregar_empresa(root)))
    


    # Contacto ----------------------------------------------------------------
    fr_grid_contenedor.generar_label("CONTACTO")

    # Generamos las opciones a elegir de los contactos creados
    fr_grid_contenedor.radioButton(*list_contactos_radiobutton)

    # Grid para los botones de la seccion empresas --------------------------------
    fr_grid_contenedor.generar_boton("NUEVO CONTACTO", funcion= lambda: func.cambio_frame(fr_actual, mi_empresa_agregar_contacto.mi_empresa_agregar_contacto(root)))
