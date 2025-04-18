import asyncio
from pyppeteer import launch
from datetime import date
from html_secciones import productos, cliente, empresa, datos_complementarios, cuentas_bancarias

# Cargar HTML
with open("../html/src/index.html", "r", encoding="utf-8") as f:
    html_plantilla = f.read()
# Cargar FECHA
fecha = str(date.today())

# Cargar datos
valores_html = empresa.empresa() | cliente.cliente() | datos_complementarios.datos_complementarios() | productos.productos() | cuentas_bancarias.cuentas_bancarias()

# Cargar datos al HTML
for clave, valor in valores_html.items():
    html_plantilla = html_plantilla.replace("{{" + clave.upper() + "}}", valor)
    # Cargar otros datos
html_final = html_plantilla.replace("{{FECHA_DE_EM}}", fecha)\
                           .replace("{{FECHA_DE_VCTO}}", fecha)


# Función async para generar el PDF
async def generar_pdf():
    browser = await launch()
    page = await browser.newPage()
    await page.setContent(html_final)
    await page.pdf({'path': 'cotizacion.pdf', 'format': 'A4', 'printBackground': True})
    await browser.close()

# Ejecutar desde terminal
asyncio.run(generar_pdf())
