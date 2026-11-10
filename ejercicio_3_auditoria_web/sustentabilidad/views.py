"""Vista web que procesa el historial de consumo y lo envía a la plantilla."""

import json
from pathlib import Path

from django.shortcuts import render

from auditoria import obtener_metricas_consumo


BASE_DIR = Path(__file__).resolve().parents[1]


def vista_panel_sustentabilidad(request):
    ruta_datos = BASE_DIR / "datos_consumo.json"
    with ruta_datos.open("r", encoding="utf-8") as archivo:
        registros = json.load(archivo)

    metricas = obtener_metricas_consumo(registros)
    contexto = {"metricas": metricas}
    return render(request, "sustentabilidad/panel.html", contexto)
