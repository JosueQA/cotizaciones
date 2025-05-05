from utilities import funciones as func, class_new_frame as new_frame, datos_generales as dg

historial = []

# CREACION DEL BOTON
def nav(root):
    fr_nav = new_frame.newFrame(root)
    fr_nav.frame.place(x=0, y=0, width=dg.ancho, height=50)

    fr_nav.generar_boton('<-', 'place', x=10, y = 10, funcion= lambda: volver_frame_anterior(), width='defecto')
    fr_nav.generar_boton('->', 'place', x=40, y = 10, funcion= lambda: volver_frame_posterior(), width='defecto')





# FUNCION    
def volver_frame_anterior():

    if dg.frameActual != historial[0] and len(historial) > 1:
        
        frameAnterior = historial[historial.index(dg.frameActual) - 1]
    
        func.cambio_frame(dg.frameActual, frameAnterior, 'nav')
    
    else:
        pass

    #print('Navegacion ----------------------------------------------------------------')
    #print(f'frameActual: {dg.frameActual}')
    #print(f'historial ahora: {historial}')
    
    
def volver_frame_posterior():

    if len(historial) > 1 and historial[len(historial) - 1] != dg.frameActual:
        
        frame_siguiente = historial[historial.index(dg.frameActual) + 1]
    
        func.cambio_frame(dg.frameActual, frame_siguiente, 'nav')
        
        #print('Navegacion ----------------------------------------------------------------')
        #print(f'frameActual: {dg.frameActual}')
        #print(f'historial ahora: {historial}')
    
    # Agregar la logica que elimina los frame del historial si el siguiente frame a navegar no es el mismo que el siguiente en la posicion de 'historial'