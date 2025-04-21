from gui import navegacion as nav
from utilities import datos_generales as dg, class_new_frame as new_frame

# CAMBIO DE INTERFAZ
def cambio_frame(framePresente, frameNuevo, comportamiento = 'estandar'):
    
    if comportamiento == 'nav':

        framePresente.pack_forget()
        frameNuevo.pack()
   
        dg.frameActual = frameNuevo
    

    elif comportamiento == 'cancelar':

        framePresente.desaparecer()
        frameNuevo.aparecer()

        nav.historial = nav.historial[:1]

        dg.frameActual = nav.historial[0]
        

    else:
        # framePresente es el que estamo ahora
        framePresente.desaparecer()
        frameNuevo.aparecer()


        # Verificamos si el frame se encuentra en el historial. Map crea una lista de booleans, y con 'any', si alguno es True, recibiremos True.
        existencia_frame_en_historial = any(map(lambda historial_frame: historial_frame == framePresente.frame, nav.historial))
        
        # Si el frame actual no es el ultimo del historial (se da si se uso las flechas de nav.), el frame nuevo ocupara el siguiente lugar del frame actual en el historial, y eliminamos el resto. Esto es para el mano de flecha derecha
        if existencia_frame_en_historial and framePresente.frame != nav.historial[len(nav.historial)-1]: # Si framePresente no  es el ultimo elemento..

            indice_frame_presente = nav.historial.index(framePresente.frame) # Obtenemos el indice del framePresente

            nav.historial[indice_frame_presente + 1] = frameNuevo.frame # Reemplazamos el nuevo frame con el que de la siguiente posicion del frame actual en el historial.

            nav.historial = nav.historial[:nav.historial.index(frameNuevo.frame)+1] # Eliminamos el resto de elementos despues del frame nuevo

        else:
            nav.historial.append(frameNuevo.frame)
       
        dg.frameActual = frameNuevo.frame

    

def botones_juntos(fr_padre, str_boton_izq, str_boton_der):
    fr_grid = new_frame.newFrame(fr_padre.frame)
    fr_grid.aparecer()
    
    fr_grid.generar_boton(str_boton_izq, pack_grid_place="grid", row=0, column=0, padx=5)
    fr_grid.generar_boton(str_boton_der, pack_grid_place="grid", row=0, column=1, padx=5)