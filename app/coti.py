import asyncio
from pyppeteer import launch
from datetime import date
import base64
import empresa_receptor


# Cargar HTML
with open("./html/src/index.html", "r", encoding="utf-8") as f:
    html_plantilla = f.read()
# Cargar LOGO
with open("./html/src/assets/cutedog.jpeg", "rb") as img_file:
    logo = base64.b64encode(img_file.read()).decode("utf-8")
# Cargar FECHA
fecha = str(date.today())


# Cargar DATOS DEL CLIENTE
ruc_cliente,razon_social_cliente,contacto_cliente,correo_cliente = empresa_receptor.empresa_receptor()
# --------- AGREGAR ESTAS VARIABLES AL HTML EN LA LINEA 23 ---------------cod

# Reemplazar en plantilla
html_final = html_plantilla.replace("{{cliente}}", cliente)\
                           .replace("{{fecha}}", fecha)\
                           .replace("{{filas}}", filas)\
                           .replace("{{LOGO}}", logo)

# Función async para generar el PDF
async def generar_pdf():
    browser = await launch()
    page = await browser.newPage()
    await page.setContent(html_final)
    await page.pdf({'path': 'cotizacion.pdf', 'format': 'A4', 'printBackground': True})
    await browser.close()

# Ejecutar desde terminal
asyncio.run(generar_pdf())
