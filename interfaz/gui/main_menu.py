from gui.mi_empresa import mi_empresa
from gui.mis_cotizaciones import mis_cotizaciones
from gui.mis_productos import mis_productos
from gui.nueva_cotizacion import nueva_cotizacion
from utilities import funciones as func, class_new_frame as new_frame
from gui import navegacion as nav
import inspect

# Inicio --------------
def inicio(root):
    
     # INICIALIZAMOS --------------------------------------------------------------------
    fr_main_menu = new_frame.newFrame(root)
    fr_main_menu.aparecer()

    nav.historial.append(fr_main_menu.frame) # Ingresar frame al array de navegacion

    print(fr_main_menu.frame)

    # CARGAMOS LAS INTERFACES DIRECTAMENTE RELACIONADAS --------------------
    interfaces_archivos = [nueva_cotizacion, mi_empresa, mis_cotizaciones, mis_productos]
    interfaces = {}

    for x in interfaces_archivos:
        nombre = inspect.getmodulename(x.__file__) # Obtenemos el nombre 

        funcion_del_archivo = getattr(x, nombre) # 'getattr' obtiene el valor del atributo de un objeto, AL SER UNA FUNCION LLAMAMOS LA REFERENCIA. El 1er param. es el objeto, y el 2do el nombre del atrib.

        interfaces[f'fr_{nombre}'] = funcion_del_archivo(root) # Asignamos una nueva clave-valor, donde sera "fr_{nombredelarchivo}" como clave, y, con el parametro, ejecutamos la referencia de la funcion del archivo en turno asignando este resultado como valor.
  

    
    # CONTENIDO ----------------------------------------------------------------
    fr_main_menu.generar_label("COTI VERSION 0")  
      
    
    fr_main_menu.generar_boton("NUEVA COTIZACION", funcion= lambda: func.cambio_frame(fr_main_menu, interfaces['fr_nueva_cotizacion']))
    
    fr_main_menu.generar_boton("MI EMPRESA", funcion= lambda: func.cambio_frame(fr_main_menu, interfaces['fr_mi_empresa']))

    fr_main_menu.generar_boton("MIS COTIZACIONES", funcion= lambda: func.cambio_frame(fr_main_menu, interfaces['fr_mis_cotizaciones']))

    fr_main_menu.generar_boton("MIS PRODUCTOS", funcion= lambda: func.cambio_frame(fr_main_menu, interfaces['fr_mis_productos']))

    fr_main_menu.generar_boton("SALIR", funcion=lambda: root.destroy())

    

    #frame.botones_pack(pady=20)
       
   # button.pack(pady=20)
    
    return fr_main_menu