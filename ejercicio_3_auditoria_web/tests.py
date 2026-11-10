"""Pruebas unitarias requeridas para el algoritmo de emisiones."""

import unittest

from auditoria import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):
    def test_calculo_con_factor_predeterminado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_calculo_con_factor_personalizado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(50, 0.2), 10.0)

    def test_consumo_negativo_eleva_value_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-1)


if __name__ == "__main__":
    unittest.main()
