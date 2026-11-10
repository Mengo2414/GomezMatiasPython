"""Demostración cooperativa del flujo completo del ejercicio 1."""

from sensores import generar_resumen_sensores, limpiar_registro_sensor


registros_crudos = [
    {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": " Planta Norte "},
    {"sensor_id": "SENSOR-002", "temperatura": "35.0 C", "ubicacion": ""},
    {"sensor_id": " SENSOR-003 ", "temperatura": 29, "ubicacion": "Sala de Calderas"},
    {"sensor_id": "SENSOR-004", "temperatura": "dato corrupto", "ubicacion": None},
]

sensores_limpios = [limpiar_registro_sensor(registro) for registro in registros_crudos]
alertas, promedio = generar_resumen_sensores(sensores_limpios, 30.0)

print("Registros normalizados:")
for sensor in sensores_limpios:
    print(sensor)

print(f"\nSensores que superan 30.0 °C: {alertas}")
print(f"Promedio térmico de la planta: {promedio:.2f} °C")

alertas_vacias, promedio_vacio = generar_resumen_sensores([], 30.0)
print(f"Lista vacía: alertas={alertas_vacias}, promedio={promedio_vacio}")
