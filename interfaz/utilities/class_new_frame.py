import tkinter as tk
from tkinter import ttk 
from utilities import datos_generales as dg

class newFrame(tk.Frame):
    
    def __init__(self, root, **kwargs):
        
        # root es el contenedor padre del frame
        self.root = root
                
        # Creamos el frame
        self.frame = tk.Frame(root, **kwargs)
        self.widgets = {
            'label': [],
            'button': [],
            'entry': []
        }
    def __repr__(self):
        return f"<NewFrame(id={id(self)})>"

    def aparecer(self, **kwargs):
        self.frame.pack(kwargs)

    def desaparecer(self):
        self.frame.pack_forget()
    


    def generar_entry(self, pack_grid_place = 'pack', espacio_entre_widget = dg.secciones, **kwargs):
        entry = tk.Entry(self.frame)

        if pack_grid_place == 'pack':
            entry.pack(pady=espacio_entre_widget, **kwargs)
        elif pack_grid_place == 'grid':
            entry.grid(kwargs)

        self.widgets['entry'].append(entry)

        return entry


    def generar_boton(self, texto, pack_grid_place = 'pack', espacio_entre_widget = dg.secciones, funcion=None, **kwargs):
        if funcion is None:
            funcion = lambda: print("hello world")
            
            # Creamos el boton
        button = tk.Button(self.frame, text=texto, command= funcion)
        
            # Definimos la geometria de uso 
        if pack_grid_place == 'pack':
            button.pack(pady=espacio_entre_widget)
        elif pack_grid_place == 'grid':
            button.grid(kwargs)
        elif pack_grid_place == 'place':
            button.place(kwargs)


            # Añadimos el button al array para usar un config general
        self.widgets['button'].append(button)
        
        return button
             
 
    def generar_label(self, texto, pack_grid_place = 'pack', espacio_entre_widget = dg.secciones, **kwargs):
        
        label = tk.Label(self.frame, text=texto)
        
        if pack_grid_place == 'pack':
            label.pack(pady=espacio_entre_widget, **kwargs)
        elif pack_grid_place == 'grid':
            label.grid(kwargs)

        self.widgets['label'].append(label)

        return label


    def widget_config(self, boton_entry_label, **kwargs):

        for i in self.widgets[boton_entry_label]:
            i.config(kwargs)


    def generar_combobox(self, pack_grid_place = 'pack', espacio_entre_widget = dg.secciones, opciones = ["", "Opción 1", "Opción 2", "Opción 3"],**kwargs):
      
        # Widget que permite escribir o seleccionar entre opciones
        combobox = ttk.Combobox(self.frame, values=opciones)
        combobox.current(0)

        if pack_grid_place == 'pack':
            combobox.pack(pady=espacio_entre_widget, **kwargs)
        elif pack_grid_place == 'grid':
            combobox.grid(kwargs)

        return combobox

    
    def radioButton(self, *args):
        opciones = [*args]

        # Variable para almacenar la opción seleccionada
        opcion_seleccionada = tk.IntVar(value=opciones[1])

        for x in opciones:
            tk.Radiobutton(self.frame, text=x, variable=opcion_seleccionada, value=x, indicatoron=True).pack(anchor='w')

        ''' Explicacion de Radiobutton'''
        '''
        1. tk.Radiobutton
        Este es el constructor del widget Radiobutton de Tkinter. Se usa para crear un botón de opción que permite seleccionar una opción de un grupo de opciones mutuamente exclusivas.

        2. frame_opciones
        Es el contenedor en el que se colocará el Radiobutton. Los widgets se colocan en un contenedor usando el método pack, grid, o place.

        3. text="Opción 1"
        Este argumento especifica el texto que se mostrará junto al Radiobutton.

        4. variable=opcion_seleccionada
        Este argumento asocia el Radiobutton con una variable (de tipo StringVar, IntVar, etc.). La variable almacena el valor de la opción seleccionada. Todos los Radiobuttons en un grupo deben compartir la misma variable.

        5. value="Opción 1"
        Este argumento define el valor que se almacenará en opcion_seleccionada cuando este Radiobutton sea seleccionado. Los valores deben ser únicos dentro del grupo de Radiobuttons.

        6. indicatoron=True
        Este argumento especifica si el Radiobutton debe mostrar un círculo (cuando es True) o un cuadrado (cuando es False) al lado del texto. Especificando True, se crea el estilo de botón de opción tradicional con un círculo.

        7. .pack(anchor='w')
        Este es el método de geometría pack que coloca el Radiobutton dentro de su contenedor (frame_opciones).

        anchor='w': Alinea el Radiobutton a la izquierda del contenedor (o del lado oeste).'''


# Este grid esta echo ESPECIFICAMNTE PARA USAR RADIOBUTTON
def nuevo_grid(root, fr_actual, frame_padre, int_columna, str_emisor_o_receptor, list_empresa_radiobutton, list_contactos_radiobutton):
    
    # Creamos el grid contenedor
    fr_grid_contenedor = new_frame.newFrame(frame_padre.frame)

    # Si 'int_columna' es un numero, lo definimos como el numero de la columna en un grid, sino no sera grid
    if type(int_columna) == int:
        fr_grid_contenedor.frame.grid(row=0, column=int_columna, padx=10, pady=10)
    else:
        fr_grid_contenedor.frame.pack()


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
