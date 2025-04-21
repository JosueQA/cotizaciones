def datos_complementarios(
    tiempo_de_entrega="2 dias habiles",
    observaciones="Aqui van las observaciones",
    dinero_escrito="Son 99 soles y 94 centimos",
    sub_total="S/ 100",
    igv="S/ 18",
    total="S/ 118",
    forma_de_pago="CONTADO",
):

    return {
        "tiempo_de_entrega": tiempo_de_entrega,
        "observaciones": observaciones,
        "dinero_escrito": dinero_escrito,
        "sub_total": sub_total,
        "igv": igv,
        "total": total,
        "forma_de_pago": forma_de_pago,
    }
