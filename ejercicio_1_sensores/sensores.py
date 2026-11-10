"""Normalización de registros y resumen estadístico de sensores térmicos."""


def limpiar_registro_sensor(registro_raw):
    """Devuelve una copia estandarizada de un registro de sensor crudo."""
    registro_limpio = {}

    identificador = registro_raw.get("sensor_id", "")
    registro_limpio["sensor_id"] = str(identificador).strip()

    temperatura_raw = registro_raw.get("temperatura", 0.0)
    if isinstance(temperatura_raw, (int, float)):
        temperatura = float(temperatura_raw)
    else:
        temperatura_texto = str(temperatura_raw)
        temperatura_texto = (
            temperatura_texto.replace("°", "")
            .replace("C", "")
            .replace("c", "")
            .replace("F", "")
            .replace("f", "")
            .replace(" ", "")
        )
        try:
            temperatura = float(temperatura_texto)
        except ValueError:
            temperatura = 0.0
    registro_limpio["temperatura"] = temperatura

    ubicacion_raw = registro_raw.get("ubicacion")
    if isinstance(ubicacion_raw, str) and ubicacion_raw.strip():
        registro_limpio["ubicacion"] = ubicacion_raw.strip()
    else:
        registro_limpio["ubicacion"] = "Área No Asignada"

    return registro_limpio


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """Retorna (IDs en alerta, promedio térmico redondeado a dos decimales)."""
    if not lista_sensores_limpios:
        return [], 0.0

    suma_temperaturas = 0.0
    sensores_en_alerta = []

    for sensor in lista_sensores_limpios:
        temperatura = sensor["temperatura"]
        suma_temperaturas += temperatura
        if temperatura > umbral_temperatura:
            sensores_en_alerta.append(sensor["sensor_id"])

    promedio = round(suma_temperaturas / len(lista_sensores_limpios), 2)
    return sensores_en_alerta, promedio
