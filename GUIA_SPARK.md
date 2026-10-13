# Guía completa de Apache Spark con Python (PySpark)

Este documento explica todo lo que hace este proyecto paso a paso, qué archivos existen, cómo se ejecuta y qué conceptos reales de Apache Spark se están usando.

## 1. ¿Qué es Apache Spark?

Apache Spark es un motor de procesamiento distribuido para grandes volúmenes de datos.

Se usa para:
- analizar datos masivos
- limpiar y transformar datos
- hacer ETL
- unir tablas grandes
- calcular métricas y KPIs
- ejecutar consultas SQL sobre datasets distribuidos
- procesar flujos en tiempo real
- entrenar modelos de machine learning

Spark no es una página web ni un sistema de ventas. Spark es un motor de cómputo distribuido para datos masivos.

## 2. ¿Qué hace este proyecto?

Este proyecto demuestra un caso práctico real y educativo de Spark usando Python (PySpark):

- lee un archivo CSV de ventas
- calcula el subtotal por cada fila
- suma el total de ingresos
- calcula el promedio por compra
- agrupa ventas por producto
- agrupa ventas por cliente
- imprime resultados en la consola

Es un ejemplo pequeño, pero usa la misma lógica que un proyecto real de Spark.

## 3. ¿Por qué este proyecto es real?

Porque utiliza:
- `SparkSession` para crear una sesión de Spark
- `DataFrame` para manejar datos tabulares
- `filter`, `groupBy`, `sum`, `avg`, `orderBy` para transformaciones
- ejecución lazy (perezosa) de Spark
- lectura de archivos CSV con PySpark

Esto es exactamente la base de Apache Spark en la práctica.

## 4. Estructura del proyecto

```text
spark/
├── .gitignore
├── GUIA_SPARK.md
├── README.md
├── requirements.txt
├── run.sh
├── server.py
├── spark_sales_analysis.py
├── app.js
├── index.html
├── styles.css
├── data/
│   └── sales.csv
└── .venv/
```

### Archivos y qué hacen

#### `spark_sales_analysis.py`
Es el script principal. Aquí se ejecuta la lógica real de Spark.

Hace lo siguiente:
1. crea la sesión de Spark
2. lee el CSV de ventas
3. calcula el subtotal
4. suma ingresos totales
5. calcula promedio por venta
6. agrupa por producto
7. agrupa por cliente
8. imprime resultados
9. cierra la sesión de Spark

#### `data/sales.csv`
Es el archivo de ejemplo con datos de ventas.

Cada fila representa una venta con columnas como:
- `date`
- `product`
- `quantity`
- `unit_price`
- `client`

#### `requirements.txt`
Contiene las dependencias del proyecto.

Actualmente:
```txt
pyspark==3.5.1
```

#### `run.sh`
Script auxiliar para ejecutar el análisis de forma rápida.

#### `server.py`
Este archivo no pertenece a Spark. Es un servidor HTTP local que se usó antes para una demo web. No es parte del procesamiento real de Spark.

#### `index.html`, `app.js`, `styles.css`
Son archivos de una vista web o interfaz visual. Sirven para mostrar una UI, pero no forman parte del motor Spark en sí.

#### `README.md`
Es la documentación principal del proyecto.

#### `.gitignore`
Evita subir carpetas innecesarias como `.venv` y archivos temporales de Python.

## 5. Cómo funciona `spark_sales_analysis.py`

Veamos el archivo paso a paso.

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
```

Esto importa:
- `SparkSession`: punto de entrada para crear la sesión de Spark
- `functions as F`: módulo con funciones de agregación y transformación

Luego:

```python
def main():
    spark = SparkSession.builder \
        .appName("ApacheSparkSalesAnalysis") \
        .master("local[*]") \
        .getOrCreate()
```

Esto crea la sesión de Spark.

- `appName`: nombre de la aplicación
- `master("local[*]")`: indica que se ejecutará localmente usando todos los núcleos de la máquina
- `getOrCreate()`: crea la sesión si no existe

### Lectura del CSV

```python
sales_df = spark.read.option("header", True).option("inferSchema", True).csv("data/sales.csv")
```

Hace esto:
- lee el archivo CSV
- toma la primera fila como encabezados
- infiere tipos de datos automáticamente
- lo carga como un DataFrame

### Cálculo del subtotal

```python
sales_df = sales_df.withColumn(
    "subtotal",
    F.col("quantity") * F.col("unit_price")
)
```

Esto agrega la columna `subtotal`:

`subtotal = quantity * unit_price`

Esto es un ejemplo común de ETL con Spark.

### Total de ventas registradas

```python
total_sales = sales_df.count()
```

`count()` es una acción. Dispara la ejecución real de Spark y cuenta cuántas filas existen.

### Ingresos totales

```python
total_revenue = sales_df.agg(F.sum("subtotal").alias("total_revenue")).collect()[0]["total_revenue"]
```

Esto:
- suma todos los subtotales
- los guarda en una columna llamada `total_revenue`
- usa `collect()` para obtener el resultado final

### Promedio por venta

```python
avg_ticket = sales_df.agg(F.avg("subtotal").alias("avg_ticket")).collect()[0]["avg_ticket"]
```

Calcula el promedio de subtotal por venta.

### Ventas por producto

```python
sales_by_product = sales_df.groupBy("product").agg(
    F.sum("subtotal").alias("revenue_by_product")
).orderBy(F.col("revenue_by_product").desc())
```

Esto:
- agrupa por `product`
- suma el subtotal por producto
- ordena de mayor a menor ingreso

### Ventas por cliente

```python
sales_by_client = sales_df.groupBy("client").agg(
    F.sum("subtotal").alias("total_paid")
).orderBy(F.col("total_paid").desc())
```

Agrupa por cliente y calcula el total pagado por cada cliente.

### Impresión final

```python
print("=== Resumen de ventas ===")
print(f"Total de ventas registradas: {total_sales}")
print(f"Ingresos totales: ${total_revenue:,.2f}")
print(f"Promedio por venta: ${avg_ticket:,.2f}\n")
```

Esto imprime los resultados a consola.

### Cierre de la sesión

```python
finally:
    spark.stop()
```

Esto libera recursos de Spark al final del script.

## 6. Qué es la ejecución lazy en Spark

Spark usa evaluación perezosa.

Eso significa que no ejecuta cada operación inmediatamente; en cambio, construye un plan de ejecución.

Ejemplo:
```python
filtered = sales_df.filter(F.col("monto") > 1000)
```

Esto no ejecuta nada todavía. Solo se ejecuta cuando haces:
```python
filtered.show()
```

Esto es una de las ideas más importantes de Spark.

## 7. Cómo correr el proyecto

### Opción 1: entorno virtual + dependencias

```bash
cd /home/cohorte5/Descargas/spark
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 spark_sales_analysis.py
```

### Opción 2: ejecutar el script cargado

```bash
cd /home/cohorte5/Descargas/spark
chmod +x run.sh
./run.sh
```

## 8. Qué mostraría la salida

Cuando ejecutas el script, el resultado será algo así:

```text
=== Resumen de ventas ===
Total de ventas registradas: 6
Ingresos totales: $2,450.00
Promedio por venta: $408.33

=== Ventas por producto ===
+----------------+------------------+
|product         |revenue_by_product|
+----------------+------------------+
|Laptop Pro      |1200              |
|Impresora HP    |540               |
|Monitor 27"     |320               |
|Webcam 4K       |190               |
|Teclado Mecánico|110               |
|Mouse Gamer     |90                |
+----------------+------------------+
```

## 9. Relación con Apache Spark real

Este proyecto no es una caja negra ni un “servidor de ventas”. Es un ejemplo real de PySpark porque usa:

- `SparkSession`
- `DataFrame`
- transformaciones y acciones
- lectura de CSV
- agregaciones
- agrupación por columnas
- ejecución distribuida

Es una instalación simple y local, pero sigue siendo Apache Spark real.

## 10. Diferencia entre este proyecto y el servidor web anterior

El archivo `server.py` pertenece a un ejemplo de servidor HTTP local. No tiene que ver con la parte real de Spark.

La diferencia es esta:

- `server.py` = sirve páginas y endpoints HTTP
- `spark_sales_analysis.py` = analítica distribuida con Spark

Spark no se usa para servir una página web. Spark se usa para procesar y analizar datos.

## 11. Qué aprenderás con este proyecto

Con este ejemplo aprenderás:
- cómo crear una sesión de Spark
- cómo leer un CSV
- cómo crear columnas calculadas
- cómo hacer agregaciones
- cómo agrupar y ordenar resultados
- cómo usar PySpark para análisis real
- cómo hacer un mini ETL con Spark

## 12. Conclusión

Este proyecto es una base real para aprender Apache Spark usando Python.

Lo que se hace aquí no es inventado:
- está usando Spark de verdad
- trabaja con DataFrames
- realiza análisis distribuidos
- procesa datos de ventas
- genera resultados útiles

Si quieres avanzar más, el siguiente paso natural es:
- Spark SQL con consultas SQL directas
- joins entre tablas
- window functions
- streaming con Kafka
- MLlib para modelos predictivos
- Parquet y Delta Lake

## 13. Siguiente paso recomendado

Para profundizar en Apache Spark real, el siguiente nivel sería:
- joins entre múltiples DataFrames
- funciones de ventana
- procesamiento streaming
- almacenamiento en Parquet
- machine learning con MLlib

