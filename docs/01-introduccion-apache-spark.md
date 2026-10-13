# 01. Introducción a Apache Spark

## ¿De qué se trata todo esto?

Este proyecto está enfocado en Apache Spark, que es un motor de procesamiento distribuido para manejar grandes cantidades de datos.

La idea central es esta:

- Spark toma datos grandes
- los divide en partes llamadas particiones
- ejecuta cálculos en paralelo
- optimiza el flujo de trabajo
- devuelve resultados finales que pueden usarse para análisis, reportes, ETL o modelos de aprendizaje automático

Es importante aclarar una cosa real:

- Apache Spark no es una página web
- no es un backend HTTP como Flask o FastAPI
- no es una base de datos
- no es un navegador ni una UI
- no es un servidor de ventas

Apache Spark es un motor de cómputo distribuido para procesar datos masivos.

## ¿Para qué sirve Spark?

Spark sirve para cosas como:

- transformación de datos
- limpieza y validación de datos
- ETL (Extract, Transform, Load)
- consultas SQL sobre datasets enormes
- análisis de ventas, finanzas, telecom, logística
- procesamiento de eventos en tiempo real
- machine learning con MLlib
- análisis de flujos de datos

## ¿Por qué es importante?

Porque en la vida real los datos ya no caben en una sola máquina.

Cuando una empresa o negocio tiene:

- millones de filas
- muchas fuentes de datos
- tráfico en tiempo real
- registros de ventas, usuarios, clics, logs, sensores

entonces una sola computadora ya no es suficiente.

Spark resuelve eso distribuyendo la carga de procesamiento entre varios nodos o ejecutores.

## Diferencia entre Spark y Python normal

Python normal puede procesar datos pequeños o medianos en una sola máquina.

Spark puede ir más lejos porque:

- divide los datos en particiones
- procesa varias partes al mismo tiempo
- usa memoria y paralelización
- puede correr sobre un clúster

Esto significa que Spark es ideal cuando el volumen de datos es grande o cuando necesitás escalabilidad.

## Conceptos clave de Spark

### 1. Driver
Es el proceso principal que coordina la ejecución.

Se encarga de:
- crear el plan de trabajo
- organizar tareas
- distribuir la carga
- recopilar resultados finales

### 2. Cluster Manager
Es quien administra los recursos del clúster.

Puede ser:
- YARN
- Kubernetes
- Standalone
- Mesos

### 3. Executors
Son procesos que ejecutan las tareas reales sobre las particiones de datos.

### 4. Partitions
Son las divisiones del dataset.

Cada partición puede procesarse de manera independiente, lo que permite paralelismo.

### 5. DataFrame
Es la estructura tabular principal de Spark.

Se parece a una tabla de SQL, pero funciona sobre datos distribuídos.

### 6. SparkSession
Es la puerta de entrada para crear una aplicación Spark con Python.

### 7. Lazy evaluation
Spark usa evaluación perezosa.

Es decir:
- no ejecuta todo de inmediato
- primero crea el plan
- ejecuta cuando llega a una acción final como `show()`, `count()` o `write()`

## ¿Qué hace este proyecto exactamente?

Este proyecto usa PySpark para analizar un archivo CSV de ventas.

El flujo es este:

1. leer archivo `data/sales.csv`
2. crear una sesión de Spark
3. detectar la estructura del CSV
4. crear una columna `subtotal`
5. calcular total de ingresos
6. calcular promedio por venta
7. agrupar ventas por producto
8. agrupar ventas por cliente
9. mostrar resultados en consola

## Qué representa cada una de esas operaciones

- `read.csv()` = lectura de datos
- `withColumn()` = creación de nueva columna
- `count()` = conteo de filas
- `sum()` = suma agregada
- `avg()` = promedio
- `groupBy()` = agrupación por columna
- `orderBy()` = ordenamiento
- `show()` = acción que activa ejecución y muestra resultados

## Relación con Big Data

Spark es un ecosistema central del Big Data porque permite:

- procesar datos rápidos y distribuidos
- ejecutar SQL sobre grandes datasets
- manejar ETL industrial
- integrar pipeline con herramientas de análisis y almacenamiento

## Conclusión del tema

Apache Spark es importante porque permite procesar datos grandes en paralelo, con mejor rendimiento que muchas soluciones tradicionales. Es una pieza clave en ciencia de datos, ingeniería de datos, analítica, ETL y machine learning.

Este proyecto es una versión educativa real y pequeña de cómo se usa Spark de verdad con Python.
