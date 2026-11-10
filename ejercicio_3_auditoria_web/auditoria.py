"""Cálculo de emisiones y resumen de consumo por planta industrial."""


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """Calcula kg de CO2 equivalente y rechaza consumos negativos."""
    consumo = float(consumo_kwh)
    factor = float(factor_emision)
    if consumo < 0:
        raise ValueError("El consumo eléctrico no puede ser negativo.")
    return consumo * factor


def obtener_metricas_consumo(registros):
    """Devuelve emisiones globales y la planta con mayor consumo.

    Cada registro debe contener las claves ``planta`` y ``consumo_kwh``.
    El resultado incluye emisiones por registro para que el panel pueda mostrar
    tanto el total como el detalle.
    """
    consumo_por_planta = {}
    emisiones_detalle = []
    emisiones_totales = 0.0

    for registro in registros:
        planta = registro["planta"]
        consumo = float(registro["consumo_kwh"])
        emisiones = calcular_emisiones_carbono(consumo)

        if planta not in consumo_por_planta:
            consumo_por_planta[planta] = 0.0
        consumo_por_planta[planta] = consumo_por_planta[planta] + consumo
        emisiones_totales += emisiones
        emisiones_detalle.append(
            {
                "planta": planta,
                "consumo_kwh": consumo,
                "emisiones_kg_co2": emisiones,
            }
        )

    planta_mayor_consumo = "Sin datos"
    consumo_maximo = 0.0
    for planta in consumo_por_planta:
        if consumo_por_planta[planta] > consumo_maximo:
            planta_mayor_consumo = planta
            consumo_maximo = consumo_por_planta[planta]

    return {
        "emisiones_totales_kg_co2": round(emisiones_totales, 2),
        "planta_mayor_consumo": planta_mayor_consumo,
        "consumo_maximo_kwh": round(consumo_maximo, 2),
        "consumo_por_planta": consumo_por_planta,
        "detalle": emisiones_detalle,
    }
