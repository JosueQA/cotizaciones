from gui.mi_empresa import mi_empresa_agregar_contacto
from utilities import class_new_frame as new_frame, datos_generales as dg, funciones as func
from gui.mi_empresa import mi_empresa_agregar_empresa


ancho_label = 50
ancho_boton = 20

def mi_empresa(root):

    fr_mi_empresa = new_frame.newFrame(root) # Frame MI EMPRESA
    
     # CONTENIDO ----------------------------------------------------------------
    
    fr_mi_empresa.generar_label("MI EMPRESA")
    
    fr_mi_empresa.generar_label(f"VISUALIZA TU(S) RAZON(ES) SOCIAL(ES)\nRECUERDA QUE ELEGIRAS LA RAZON SOCIAL A USAR AL MOMENTO DE CREAR UNA COTIZACION")


     # Mis razon(es) social(es) ---------------
    
    '''REEMPLAZAR DATOS'''
    fr_mi_empresa.generar_label("RAZON SOCIAL")

    fr_mi_empresa.generar_label("RAZON SOCIAL 1", espacio_entre_widget=dg.listas)
    fr_mi_empresa.generar_label("RAZON SOCIAL 2", espacio_entre_widget=dg.listas)
    fr_mi_empresa.generar_label("RAZON SOCIAL 3", espacio_entre_widget=dg.listas)

    fr_mi_empresa.generar_boton("AGREGAR EMPRESA", funcion= lambda: func.cambio_frame(fr_mi_empresa, mi_empresa_agregar_empresa.mi_empresa_agregar_empresa(root)))

     # Mis contactos --------------------------

    '''REEMPLAZAR DATOS'''
    fr_mi_empresa.generar_label("CONTACTO")

    fr_mi_empresa.generar_label("CONTACTO CORREO TELEFONO 1", espacio_entre_widget=dg.listas)
    fr_mi_empresa.generar_label("CONTACTO CORREO TELEFONO 2", espacio_entre_widget=dg.listas)
    fr_mi_empresa.generar_label("CONTACTO CORREO TELEFONO 3", espacio_entre_widget=dg.listas)

    fr_mi_empresa.generar_boton("AGREGAR CONTACTO", funcion= lambda: func.cambio_frame(fr_mi_empresa, mi_empresa_agregar_contacto.mi_empresa_agregar_contacto(root)))


    return fr_mi_empresa