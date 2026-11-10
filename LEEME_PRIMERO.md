# Antes de empezar: entendamos el trabajo

No hace falta aprender todo el código de memoria. El objetivo es reconocer qué tema del curso se usa en cada parte y poder explicar con tus palabras qué hace.

## Los tres ejercicios, en palabras simples

### 1. Sensores: limpiar y resumir datos

Los sensores envían datos desordenados, por ejemplo una temperatura escrita como `"35.0 C"` y una ubicación con espacios. Una función limpia cada registro y otra función calcula qué sensores superan el umbral y cuál es el promedio.

**Temas del curso:** cadenas, diccionarios, funciones, `if`, `try/except`, listas, bucle `for`, comprensión de listas y tupla.

### 2. Productos: controlar el stock

Se define un producto general y luego un panel solar más específico. La propiedad `stock` permite revisar el valor cada vez que se cambia. Si alguien intenta asignar un número negativo, se lanza una excepción propia. Por último, la ficha se guarda en un archivo JSON.

**Temas del curso:** clases y objetos, `__init__`, atributos, encapsulamiento con `@property`, herencia, `super()`, sobrescritura de métodos, excepciones y archivos JSON.

### 3. Emisiones: calcular y mostrar métricas

Una función multiplica los kWh consumidos por el factor de emisión. Otra recorre los registros, suma las emisiones y busca qué planta consumió más. Las pruebas verifican el cálculo y el caso de consumo negativo. Django usa esos resultados para mostrar un panel web.

**Temas del curso:** funciones, listas y diccionarios, bucles, excepciones, `unittest`, JSON, vistas de Django y plantillas HTML.

## Qué archivo usar

- Para **aprender y ejecutar paso a paso en Colab**, abrí el notebook `.ipynb` de cada ejercicio.
- Para **la entrega modular**, están los archivos `.py` distribuidos en sus carpetas.
- Para **la página del ejercicio 3**, están incluidos los archivos de Django, la plantilla HTML y los datos JSON.

## ZIP o GitHub

Las dos alternativas contienen el mismo proyecto:

1. **ZIP:** entregar el archivo comprimido completo.
2. **GitHub público:** crear un repositorio nuevo, elegir visibilidad **Public** y subir todo el contenido de esta carpeta. No subas solamente los notebooks: también deben estar las carpetas de código y Django.

## Qué mirar para explicar el trabajo

- Ejercicio 1: qué entra a `limpiar_registro_sensor`, qué devuelve y cómo `generar_resumen_sensores` detecta una alerta.
- Ejercicio 2: cómo el setter evita stock negativo y cómo `PanelSolar` agrega datos a la ficha base.
- Ejercicio 3: por qué `consumo_kwh * factor_emision` calcula emisiones y qué comprueba cada prueba.
