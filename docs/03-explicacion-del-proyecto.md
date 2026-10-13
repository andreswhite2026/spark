# 03. Explicación del proyecto y de cada archivo

## ¿De qué trata este repositorio?

Este repositorio contiene un pequeño proyecto real y educativo de Apache Spark utilizando Python.

Su objetivo es demostrar cómo Spark funciona en la práctica con un caso simple de análisis de ventas.

No se trata de una app web como un sistema de ventas completo. La parte importante aquí es el análisis de datos con Spark.

## Estructura del proyecto

```text
spark/
├── README.md
├── GUIA_SPARK.md
├── requirements.txt
├── run.sh
├── spark_sales_analysis.py
├── data/
│   └── sales.csv
├── app.js
├── index.html
├── styles.css
├── server.py
├── .gitignore
└── .venv/
```

## Qué hace cada archivo

### `README.md`
Es la introducción general del proyecto.

Aquí se explica:
- qué es Spark
- cómo se instala
- cómo se ejecuta
- qué hace el proyecto
- cómo se relaciona con el mundo real

### `GUIA_SPARK.md`
Es la guía completa del proyecto.

Aquí se explica en detalle:
- Apache Spark
- conceptos clave
- preparación local
- funcionamiento de Spark
- flujo del código
- uso correcto del framework

### `requirements.txt`
Contiene las dependencias del proyecto.

Actualmente:

```txt
pyspark==3.5.1
```

### `run.sh`
Es un script para ejecutar el flujo del proyecto más rápido.

### `spark_sales_analysis.py`
Es el archivo más importante del proyecto.

Aquí ocurre la lógica real de Spark.

### `data/sales.csv`
Archivo de datos de prueba con ventas.

### `app.js` / `index.html` / `styles.css`
Estos archivos pertenecen a una interfaz visual o front-end de ejemplo. No son parte del motor Spark en sí.

### `server.py`
Este archivo no forma parte del análisis real de Spark.

Sirve como servidor HTTP local de demostración, pero no es el verdadero flujo de Spark.

### `.gitignore`
Especifica qué archivos no deben subirse al repositorio, por ejemplo la carpeta `.venv`.

## Qué hace exactamente `spark_sales_analysis.py`

Vamos a revisarlo pieza por pieza.

### Importaciones

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
```

Esto importa:

- `SparkSession`: permite crear la sesión de Spark
- `functions as F`: facilita el uso de funciones tipo `sum`, `avg`, `count`, `col`, etc.

### Creación de la sesión

```python
spark = SparkSession.builder \
    .appName("ApacheSparkSalesAnalysis") \
    .master("local[*]") \
    .getOrCreate()
```

Esto crea la aplicación Spark y la ejecuta en modo local.

Significado:

- `appName`: nombre de la app
- `master("local[*]")`: usa la máquina local con todos los núcleos disponibles
- `getOrCreate()`: crea la sesión o reutiliza una existente

### Lectura del CSV

```python
sales_df = spark.read.option("header", True).option("inferSchema", True).csv("data/sales.csv")
```

Hace esto:

- lee el archivo CSV
- interpreta la primera fila como encabezados
- infiere automáticamente tipos de datos
- carga el contenido en un DataFrame

### Cálculo de subtotal

```python
sales_df = sales_df.withColumn(
    "subtotal",
    F.col("quantity") * F.col("unit_price")
)
```

Se crea una nueva columna llamada `subtotal`.

La lógica es:

```text
subtotal = quantity * unit_price
```

Esto es un ejemplo común de ETL: transformar columnas para crear una métrica útil.

### Conteo total de ventas

```python
total_sales = sales_df.count()
```

`count()` es una acción que dispara la ejecución real en Spark.

Resultado:

- cuenta cuántas filas hay en el DataFrame

### Total de ingresos

```python
total_revenue = sales_df.agg(F.sum("subtotal").alias("total_revenue")).collect()[0]["total_revenue"]
```

Esto hace:
- suma la columna `subtotal`
- guarda el resultado en `total_revenue`
- recoge el valor final con `collect()`

### Promedio por venta

```python
avg_ticket = sales_df.agg(F.avg("subtotal").alias("avg_ticket")).collect()[0]["avg_ticket"]
```

Esto:
- calcula el promedio del subtotal
- lo guarda en `avg_ticket`

### Ventas por producto

```python
sales_by_product = sales_df.groupBy("product").agg(
    F.sum("subtotal").alias("revenue_by_product")
).orderBy(F.col("revenue_by_product").desc())
```

Esto hace:

- agrupa por producto
- suma los ingresos por cada producto
- ordena los resultados de mayor a menor ingreso

### Ventas por cliente

```python
sales_by_client = sales_df.groupBy("client").agg(
    F.sum("subtotal").alias("total_paid")
).orderBy(F.col("total_paid").desc())
```

Esto hace:

- agrupa por cliente
- suma el total pagado por cada cliente
- ordena el resultado

### Impresión de resultados

```python
print("=== Resumen de ventas ===")
print(f"Total de ventas registradas: {total_sales}")
print(f"Ingresos totales: ${total_revenue:,.2f}")
print(f"Promedio por venta: ${avg_ticket:,.2f}\n")
```

Esto imprime los resultados en la consola.

### Finalización

```python
finally:
    spark.stop()
```

Esto limpia la sesión y cierra Spark para liberar recursos.

## Gran flujo del proyecto

El flujo del proyecto es este:

```text
CSV de ventas
   ↓
SparkSession
   ↓
DataFrame
   ↓
withColumn(subtotal)
   ↓
count / sum / avg
   ↓
groupBy(product)
   ↓
groupBy(client)
   ↓
show() / consola
```

## ¿Qué hace este flujo en la práctica?

Representa un proceso real de analítica de datos:

- ingestion: lectura del archivo
- transformation: cálculo de subtotal
- aggregation: total, suma, promedio, agrupación
- reporting: resultados finales en consola

Esto es exactamente lo que se hace en ETL con analítica.

## Cómo se relaciona esto con Spark real

Aunque es un ejemplo pequeño, es real por estas razones:

- usa SparkSession
- usa DataFrame
- usa funciones de agregación
- usa evaluación lazy
- procesa datos de forma distribuida
- usa `local[*]` para correr localmente

## Conclusión

Este proyecto demuestra de forma sencilla pero real cómo un pipeline de Spark puede:

- leer datos
- transformarlos
- analizar tendencias
- calcular métricas
- generar resultados útiles

Esto es la base de proyectos reales de ingeniería de datos y analítica con Apache Spark.
