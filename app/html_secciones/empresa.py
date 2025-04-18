import base64

# Cargar LOGO
with open("../html/src/assets/cutedog.jpeg", "rb") as img_file:
    logo = base64.b64encode(img_file.read()).decode("utf-8")

def empresa(
        telefono = "923847562",
        correo = "josuelml28@hotmail.com",
        direccion = "domicilio fiscal",
        pagina_web = "www.tuempresa.com",
        ruc = str(20550178169), 
        razon_social = "Juan Pérez", 
        vendedor = "Socrates",
        ):

    # Datos

    return {
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "pagina_web": pagina_web,
        "ruc": ruc, 
        "razon_social": razon_social, 
        "vendedor": vendedor,
        "logo": logo
    }