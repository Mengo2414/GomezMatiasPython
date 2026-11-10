"""Demostración de herencia, polimorfismo, excepción y guardado JSON."""

from productos import GestorInventario, PanelSolar, StockInvalidoError


panel = PanelSolar(
    id_producto="SOL-001",
    nombre="Panel Solar EcoTech 450 W",
    precio=285000.00,
    stock=12,
    eficiencia=21.5,
    potencia_w=450,
)

print("Ficha técnica del producto:")
print(panel.generar_ficha_tecnica())

try:
    panel.stock = -5
except StockInvalidoError as error:
    print(f"\nAdvertencia controlada: {error}")

catalogo = [panel]
gestor = GestorInventario()
ruta_guardada = gestor.guardar_catalogo_json(catalogo, "catalogo_ecotech.json")
print(f"Catálogo guardado correctamente en: {ruta_guardada}")
