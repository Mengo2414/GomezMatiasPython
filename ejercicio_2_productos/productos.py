"""Modelo de productos ecológicos, validación de stock y persistencia JSON."""

import json
from pathlib import Path


class StockInvalidoError(Exception):
    """Excepción de negocio para valores de stock negativos."""

    def __init__(self, mensaje="El stock no puede ser un valor negativo."):
        super().__init__(mensaje)


class DispositivoEcologico:
    """Clase base para los productos del catálogo ecológico."""

    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = float(precio)
        self._stock = 0
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(
                f"Stock inválido para '{self.nombre}': se intentó asignar {valor}."
            )
        self._stock = valor

    def generar_ficha_tecnica(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": f"${self.precio:.2f}",
            "stock": self.stock,
        }


class PanelSolar(DispositivoEcologico):
    """Producto solar que amplía la ficha base con datos de ingeniería."""

    def __init__(self, id_producto, nombre, precio, stock, eficiencia, potencia_w):
        super().__init__(id_producto, nombre, precio, stock)
        self.eficiencia = float(eficiencia)
        self.potencia_w = float(potencia_w)

    def generar_ficha_tecnica(self):
        ficha = super().generar_ficha_tecnica()
        ficha.update(
            {
                "tipo": "Panel Solar Fotovoltaico",
                "potencia_nominal_w": self.potencia_w,
                "eficiencia": f"{self.eficiencia:.1f}%",
            }
        )
        return ficha


class GestorInventario:
    """Serializa las fichas comerciales del catálogo en formato JSON."""

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        ruta = Path(ruta_archivo)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        catalogo = [
            dispositivo.generar_ficha_tecnica()
            for dispositivo in lista_dispositivos
        ]
        with ruta.open("w", encoding="utf-8") as archivo:
            json.dump(catalogo, archivo, ensure_ascii=False, indent=4)
        return ruta
