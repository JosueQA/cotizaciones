from gui.mi_empresa import mi_empresa_agregar_contacto
from utilities import class_new_frame as new_frame, datos_generales as dg, funciones as func
from gui.mi_empresa import mi_empresa_agregar_empresa


ancho_label = 50
ancho_boton = 20

def mi_empresa(root):

    fr_mi_empresa = new_frame.newFrame(root) # Frame MI EMPRESA
    
     # CONTENIDO ----------------------------------------------------------------
    
    fr_mi_empresa.generar_label("MI EMPRESA")


     # Mis razon social ---------------
    
    '''REEMPLAZAR DATOS'''
    fr_grid_1 = new_frame.newFrame(fr_mi_empresa.frame) 
    fr_grid_1.aparecer()

    fr_grid_1.generar_label("RUC:", pack_grid_place='grid', row=0, column=0)
    fr_grid_1.generar_label("20548798523", pack_grid_place='grid', row=0, column=1)

    fr_grid_1.generar_label("RAZON SOCIAL:", pack_grid_place='grid', row=1, column=0)
    fr_grid_1.generar_label("Siguiente Nivel Peru SAC", pack_grid_place='grid', row=1, column=1)

    fr_grid_1.generar_label("DOMICILIO FISCAL:", pack_grid_place='grid', row=2, column=0)
    fr_grid_1.generar_label("Calle Piedritas 231 Las Casuarinas Lima Lima", pack_grid_place='grid', row=2, column=1)
        
    
        # Cambiar Empresa
    fr_mi_empresa.generar_boton("CAMBIAR EMPRESA", funcion= lambda: func.cambio_frame(fr_mi_empresa, mi_empresa_agregar_empresa.mi_empresa_agregar_empresa(root)))

     # Mis contactos --------------------------

    '''REEMPLAZAR DATOS'''
    fr_grid_2 = new_frame.newFrame(fr_mi_empresa.frame) 
    fr_grid_2.aparecer()

    fr_grid_2.generar_label("Nombre:", pack_grid_place='grid', row=2, column=0)
    fr_grid_2.generar_label("Putin Salsa", pack_grid_place='grid', row=2, column=1)

    fr_grid_2.generar_label("Correo:", pack_grid_place='grid', row=0, column=0)
    fr_grid_2.generar_label("putincumbia@cumbion.com", pack_grid_place='grid', row=0, column=1)

   
        # Agregar contacto
    fr_mi_empresa.generar_boton("AGREGAR CONTACTO", funcion= lambda: func.cambio_frame(fr_mi_empresa, mi_empresa_agregar_contacto.mi_empresa_agregar_contacto(root)))


    return fr_mi_empresa