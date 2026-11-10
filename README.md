# Trabajo Práctico Final Integrador - Programación con Python

**EcoTech Solutions | FESAT 2026**

> Si estás aprendiendo, empezá por `LEEME_PRIMERO.md`. Cada ejercicio también tiene un notebook `.ipynb` con explicaciones y celdas para ejecutar en Google Colab.

Este proyecto está organizado en tres carpetas independientes, una por ejercicio, como pide la consigna. Cada carpeta contiene el código fuente y una demostración ejecutable. El ejercicio 3 incluye las pruebas unitarias solicitadas y una aplicación Django mínima.

## Estructura

```text
TP_Final_Python_FESAT_2026/
├── ejercicio_1_sensores/
│   ├── ejercicio_1_sensores_colab.ipynb
│   ├── sensores.py
│   └── demo.py
├── ejercicio_2_productos/
│   ├── ejercicio_2_productos_colab.ipynb
│   ├── productos.py
│   ├── demo.py
│   └── catalogo_ecotech.json       # se crea al ejecutar demo.py
└── ejercicio_3_auditoria_web/
    ├── ejercicio_3_auditoria_web_colab.ipynb
    ├── auditoria.py
    ├── tests.py
    ├── datos_consumo.json
    ├── manage.py
    └── sustentabilidad/
        ├── settings.py
        ├── urls.py
        ├── views.py
        └── templates/sustentabilidad/panel.html
```

## Abrir los notebooks en Google Colab

1. Descargá el ZIP y descomprimilo.
2. Entrá a [Google Colab](https://colab.research.google.com/).
3. Elegí **Archivo → Subir notebook** y seleccioná el `.ipynb` del ejercicio que quieras estudiar.
4. Ejecutá las celdas de arriba hacia abajo con el botón de reproducir.

Los notebooks explican los conceptos y muestran el resultado. Los archivos `.py` son el código modular que se entrega.

## Ejercicio 1: sensores

Desde la carpeta `ejercicio_1_sensores`, ejecutar:

```bash
python demo.py
```

La demostración limpia lecturas con temperaturas numéricas y de texto, normaliza ubicaciones y muestra alertas y promedio.

## Ejercicio 2: productos

Desde la carpeta `ejercicio_2_productos`, ejecutar:

```bash
python demo.py
```

La demostración imprime la ficha polimórfica, captura el error al intentar asignar stock `-5` y guarda los productos válidos en `catalogo_ecotech.json`.

## Ejercicio 3: auditoría y Django

Requiere Python 3.10 o posterior y Django. Antes de ejecutar, definí la variable de entorno `DJANGO_SECRET_KEY` con una clave local. Desde `ejercicio_3_auditoria_web`:

```bash
python -m pip install -r requirements.txt
python -m unittest tests.py
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` para ver el panel. La prueba unitaria verifica el cálculo normal y el rechazo de consumos negativos.

## Entrega

Se puede entregar esta carpeta comprimida como ZIP o publicarla en un repositorio público de GitHub. En GitHub, creá un repositorio nuevo como público y subí el contenido completo de esta carpeta, incluida la estructura de los tres ejercicios. Antes de enviar, ejecutá las demostraciones y las pruebas desde sus carpetas, y comprobá que el archivo `catalogo_ecotech.json` se haya creado correctamente.
