import sqlite3


def crear_bd():
    # Nos conectamos y/o creamos la base de datos
    conn = sqlite3.connect("datos.db")
    cursor = conn.cursor()

    # Activamos la restriccion de claves foraneas
    conn.execute("PRAGMA foreign_keys = ON")

    # Retornamos el cursor
    return conn, cursor


# Crear tablas
def conectar_y_crear_tablas():
    # Traemos el cursor el cursor
    conn, cursor = crear_bd()

    # Tabla de COTIZACIONES
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS cotizacion (
            cotizacion INTEGER PRIMARY KEY AUTOINCREMENT,
            razon_social_cliente TEXT NOT NULL,
            ruc_cliente INTEGER NOT NULL,
            FOREIGN KEY (ruc_cliente) REFERENCES clientes(ruc_cliente)
        )
    """
    )
    # Creamos la tabla de EMPRESA (PROPIETARIO)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS empresa (
            ruc INTEGER PRIMARY KEY AUTOINCREMENT,
            razon_social TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono TEXT,
            correo TEXT,
            pagina_web TEXT,
            vendedor TEXT
        )
    """
    )
    # EMPRESA > Vendedor
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS vendedor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vendedor TEXT NOT NULL,        
            ruc_cliente INTEGER NOT NULL,
            FOREIGN KEY (ruc_cliente) REFERENCES clientes(ruc_cliente)
        )
    """
    )

    # Creamos la tabla de CLIENTES
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            ruc_cliente INTEGER PRIMARY KEY,
            razon_social_cliente TEXT NOT NULL,
            contacto_cliente TEXT,        
            correo_cliente TEXT,
            direccion_de_entrega_cliente TEXT
        )
    """
    )
    # CLIENTES > Contactos
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contacto_cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contacto_cliente TEXT NOT NULL,        
            correo_cliente TEXT,
            ruc_cliente INTEGER NOT NULL,
            FOREIGN KEY (ruc_cliente) REFERENCES clientes(ruc_cliente)
        )
    """
    )
    # CLIENTES > Direccion de entrega cliente
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS direccion_de_entrega_cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            direccion_de_entrega_cliente TEXT NOT NULL,        
            ruc_cliente INTEGER NOT NULL,
            FOREIGN KEY (ruc_cliente) REFERENCES clientes(ruc_cliente)
        )
    """
    )
    # Creamos la tabla de PRODUCTOS
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            valor_unit FLOAT NOT NULL
        )
    """
    )

    # Enviamos los cambios a la bd
    conn.commit()
    # Cerramos la conexion
    conn.close()


# Consultar informacion
def consultar_informacion_tablas(nombre_de_tabla=""):
    conn, cursor = crear_bd()

    if nombre_de_tabla != "":
        # Imprimimos las columnas de la tabla
        cursor.execute("PRAGMA table_info(" + nombre_de_tabla + ")")
        print("\nLa tabla '" + nombre_de_tabla + "' tiene las siguientes columnas:\n")

        for fila in cursor.fetchall():
            print(fila)
        print("\n")

        # Seleccionamos la tabla
        cursor.execute("SELECT * FROM " + nombre_de_tabla)

        print("\nLos registros de la tabla '" + nombre_de_tabla + "' son:\n")

        # Imprimimos las filas
        for fila in cursor.fetchall():
            print(fila)
    else:
        # Llamamos el nommbre de todas las tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for fila in cursor.fetchall():
            print(fila)

    conn.close()


# Insertar registros
def insertamos_datos(nombre_de_tabla, **kwargs):
    conn, cursor = crear_bd()

    columnas = ""
    posiciones = ""
    valores = ()

    # Iteramos las claves y valores del parametro
    for clave, valor in kwargs.items():

        if columnas == "":
            columnas += str(clave).lower()
            posiciones += "?"
        else:
            columnas += ", " + str(clave).lower()
            posiciones += ", ?"
        # Agregamos datos a la tuple 'valores' que seran los valores de la fila en cada columna
        valores = valores + (valor,)

    # Insertamos una fila a la tabla
    cursor.execute(
        "INSERT INTO "
        + nombre_de_tabla
        + " ("
        + columnas
        + ") VALUES ("
        + posiciones
        + ")",
        valores,
    )

    # Enviamos los cambios a la bd
    conn.commit()
    # Cerramos la conexion
    conn.close()


# Insertar registros
def insertamos_nueva_cotizacion(nombre_de_tabla, razon_social_cliente="", ruc_cliente=0):
    conn, cursor = crear_bd()

    columnas = "cotizacion, razon_social_cliente, ruc_cliente"
    posiciones = "?, ?, ?"
    valores = ()

    # Traemos el valor maximo de cotizacion y le sumamos 1, y si no tiene ningun valor le asignamos 1. 
        # > Esto es para asignarle la siguiente numeracion a la cotizacion 
    cursor.execute("SELECT COALESCE(MAX(cotizacion), 0) + 1 FROM cotizaciones")
    nueva_cotizacion = cursor.fetchone()[0]

    # Añadimos el nuevo numero de cotizacion
    valores = valores + (nueva_cotizacion,)  
    valores = valores + (razon_social_cliente,)  
    valores = valores + (ruc_cliente,)  

    # Insertamos una fila a la tabla
    cursor.execute(
        "INSERT INTO "
        + nombre_de_tabla
        + " ("
        + columnas
        + ") VALUES ("
        + posiciones
        + ")",
        valores,
    )

    # Enviamos los cambios a la bd
    conn.commit()
    # Cerramos la conexion
    conn.close()


# ELiminar registros
def eliminar_registro(nombre_de_tabla, nombre_primary_key, primary_key):
    conn, cursor = crear_bd()

    # Eliminamos el registro con el primary_key solicitado
    cursor.execute(
        "DELETE FROM "
        + nombre_de_tabla
        + " WHERE "
        + nombre_primary_key
        + " = "
        + str(primary_key)
    )

    # Enviamos los cambios a la bd
    conn.commit()
    # Cerramos la conexion
    conn.close()
