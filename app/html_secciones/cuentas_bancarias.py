def cuentas_bancarias():
    cuenta_bancaria = [
        {
            "banco": "bcp",
            "cuenta_corriente_soles": "1923818298",
            "cuenta_corriente_dolares": "1923818298",
            "codigo_interbancario_cci_soles": "2319238182981",
            "codigo_interbancario_cci_dolares": "2319238182981",
        }
    ]

    cuentas_bancarias = ""
    for x in cuenta_bancaria:
        cuentas_bancarias = f"""
        <div class="border-1px flex items-center text-center">
                <p class="w-full">{x['banco']}</p>
        </div>
        <div class="border-1px flex items-center text-center">
                <p>SOLES DOLARES</p>
        </div>
        <div class="border-1px flex items-center text-center">
                <p>{x['cuenta_corriente_soles']} {x['cuenta_corriente_dolares']}</p>
        </div>
        <div class="border-1px flex items-center text-center">
                <p>{x['codigo_interbancario_cci_soles']} {x['codigo_interbancario_cci_dolares']}</p>
        </div>
        """

    return {"cuentas_bancarias": cuentas_bancarias}