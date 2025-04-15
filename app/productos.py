def productos(cliente, productos):
    # Datos
    cliente = "Juan Pérez"
    productos = [
        {"item": "Agua 20L", "cantidad": 2, "descripcion": "Agua 20L", "valor_unit": 10, "importe": 400},
        {"item": "Agua 20L", "cantidad": 2, "descripcion": "Agua 20L", "valor_unit": 10, "importe": 400},
        {"item": "Agua 20L", "cantidad": 2, "descripcion": "Agua 20L", "valor_unit": 10, "importe": 400},
    ]
    # Armar las filas
    filas = ""
    for p in productos:
        filas += f"""
            <div class='text-center flex items-center justify-center border-1px'><p>{p['item']}</p></div>
            <div class='text-center flex items-center justify-center border-1px'><p>{p['cantidad']}</p></div>
            <div class='text-center flex items-center justify-center border-1px'><p>{p['descripcion']}</p></div>
            <div class='text-center flex items-center justify-center border-1px'><p>{p['valor_unit']}</p></div>
            <div class='text-center flex items-center justify-center border-1px'><p>{p['importe']:.2f}</p></div>
        """