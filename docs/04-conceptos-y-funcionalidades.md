# 04. Conceptos y funcionalidades de Spark explicados detalladamente

## 1. SparkSession

`SparkSession` es el punto de entrada principal para trabajar con Spark SQL y DataFrames.

Ejemplo:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MiProyecto") \
    .master("local[*]") \
    .getOrCreate()
```

Esto permite:

- iniciar una aplicación Spark
- leer archivos
- construir DataFrames
- ejecutar SQL
- guardar resultados

## 2. DataFrame

Un DataFrame en Spark es una tabla distribuida con filas y columnas.

Ejemplo:

```python
df = spark.read.option("header", True).csv("ventas.csv")
```

Se parece a una tabla en SQL, pero con capacidad para trabajar sobre datos distribuidos.

### ¿Qué hace?

- organiza datos estructurados
- permite columnas con nombres
- aplica transformaciones
- permite agregaciones y filtros

## 3. Transformations

Las transformaciones toman un DataFrame y devuelven otro DataFrame.

Ejemplos:

```python
df2 = df.filter(df.monto > 1000)
df3 = df.select("cliente", "monto")
df4 = df.withColumn("subtotal", df.quantity * df.unit_price)
```

Estas operaciones no ejecutan el cálculo inmediatamente.

### Importante
Spark usa evaluación perezosa, por eso las transformaciones se planifican antes de ejecutarse.

## 4. Actions

Las acciones desencadenan la ejecución real del cálculo.

Ejemplos:

```python
df2.show()
df2.count()
df2.collect()
df2.write.parquet("salida")
```

Cuando se ejecuta una acción, Spark hace el trabajo real sobre los datos.

## 5. Lazy evaluation

La evaluación perezosa es esencial en Spark.

Permite:

- optimizar el plan de ejecución
- evitar operaciones innecesarias
- encadenar varias transformaciones
- reducir trabajo y tiempo

Ejemplo:

```python
resultado = df.filter(df.monto > 1000)
resultado = resultado.groupBy("cliente").sum()
resultado.show()
```

Hasta `show()` no ocurre la ejecución final.

## 6. SQL y Spark SQL

Spark permite trabajar con SQL sobre DataFrames.

Ejemplo:

```python
df.createOrReplaceTempView("ventas")

query = spark.sql("""
SELECT cliente, SUM(monto) AS total
FROM ventas
GROUP BY cliente
ORDER BY total DESC
""")
```

Esto es muy útil porque la lógica SQL es familiar para muchos analistas.

## 7. Catalyst

Catalyst es el optimizador de consultas SQL de Spark.

Su trabajo es:

- analizar consultas
- encontrar optimizaciones
- reorganizar el plan
- reducir trabajo innecesario

Esto hace que Spark sea rápido y eficiente.

## 8. Joins (uniones)

Los joins unen dos DataFrames por una columna o condición.

Ejemplo:

```python
ventas = spark.read.csv("ventas.csv")
clientes = spark.read.csv("clientes.csv")

join_df = ventas.join(clientes, ventas.cliente_id == clientes.id, "left")
```

Tipos más comunes:

- inner
- left
- right
- full
- semi
- anti

### ¿Por qué son importantes?

Porque muchos problemas reales requieren unir información de distintas fuentes.

## 9. Shuffle

Cuando se hace un join grande o una operación de agregación entre nodos, Spark puede necesitar mover datos entre executors.

Esto se llama shuffle.

### ¿Qué implica?

- costo de red
- mayor latencia
- uso de memoria
- posible degradación del rendimiento

## 10. Broadcast Join

Cuando una tabla es pequeña, se puede enviar a todos los nodos para evitar un shuffle pesado.

Ejemplo:

```python
from pyspark.sql.functions import broadcast

join_df = ventas.join(broadcast(clientes), ventas.cliente_id == clientes.id, "left")
```

Esto acelera el trabajo si la tabla pequeña cabe en memoria.

## 11. Window Functions

Las funciones de ventana sirven para calcular métricas sobre grupos de filas relacionadas.

Ejemplo:

```python
from pyspark.sql import Window

w = Window.partitionBy("cliente").orderBy("fecha")

resultado = df.withColumn("monto_acumulado", F.sum("monto").over(w))
```

### ¿Para qué se usan?

- acumulados por cliente
- ranking por venta
- comparación por periodo
- KPIs por tiempo

## 12. Lectura de archivos

Spark puede leer varios tipos de fuentes:

- CSV
- JSON
- Parquet
- ORC
- JDBC
- Kafka
- S3
- HDFS
- Azure Data Lake

### En este proyecto se usa CSV

```python
sales_df = spark.read.option("header", True).option("inferSchema", True).csv("data/sales.csv")
```

## 13. Escritura de archivos

Spark también puede guardar resultados.

```python
df.write.mode("overwrite").parquet("resultado")
```

### ¿Por qué Parquet?

Porque es ideal para Spark:

- formato columnar
- eficiente
- comprimido
- mejor performance
- ideal para ETL y analítica

## 14. Particiones

Los datos se dividen en particiones.

Spark procesa cada partición en paralelo.

### ¿Por qué importa?

Porque el rendimiento depende mucho de cómo están repartidos los datos.

Si hay muchas particiones:
- más paralelismo
- posible overhead

Si hay pocas particiones:
- menos paralelismo
- trabajos más lentos

## 15. Caching

Spark puede guardar datos en memoria para reutilizarlos.

```python
df.cache()
```

### ¿Qué hace?

- evita recalcular el mismo DataFrame varias veces
- ayuda a mejorar rendimiento cuando hay múltiples usos del mismo dataset

## 16. Streaming

Spark Structured Streaming permite procesar flujos de datos en tiempo real.

Ejemplo conceptual:

```python
stream = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
```

### ¿Para qué sirve?

- logs en vivo
- eventos de usuario
- métricas en tiempo real
- sensores y IoT
- dashboards actualizados

## 17. MLlib

Spark tiene bibliotecas para machine learning.

Permite:

- regresión lineal
- clasificación
- clustering
- recomendación

### Ejemplo

```python
from pyspark.ml.regression import LinearRegression
```

## 18. GraphX

GraphX se usa para trabajar con grafos y relaciones.

### Ejemplos:

- redes sociales
- graph de clientes
- gráficas de relaciones entre nodos

## 19. ETL y pipelines reales

En producción, Spark normalmente hace esto:

1. leer datos desde archivos o bases de datos
2. validar y limpiar
3. transformar columnas
4. unir informaciones
5. calcular métricas
6. guardar resultados
7. distribuir a informes o modelos

Esto es una pipeline real de ingeniería de datos.

## 20. Resumen final

Las funcionalidades centrales de Spark son:

- lectura distribuida
- transformaciones sobre DataFrames
- acciones que activan ejecución
- SQL sobre datasets grandes
- joins y shuffles
- window functions
- streaming
- MLlib
- almacenamiento eficiente

Todo esto se relaciona directamente con el proyecto que tenemos aquí, donde se lee un CSV, se calcula el subtotal, se agrupan ventas por producto y cliente, y se muestran resultados útiles.
