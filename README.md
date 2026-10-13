# Apache Spark - Proyecto real de análisis con PySpark

Este repositorio contiene un proyecto real y educativo de Apache Spark usando Python.

## ¿Qué es este proyecto?

Es un ejemplo mínimo pero real de Spark en local para analizar un archivo CSV de ventas.

Hace lo siguiente:
- lee datos desde `data/sales.csv`
- calcula el subtotal por venta
- suma el total de ingresos
- calcula el promedio por venta
- agrupa ventas por producto
- agrupa ventas por cliente
- imprime resultados en la consola

## ¿Qué no es?

Esto no es:
- una app web completa
- un backend HTTP real de producción
- una base de datos
- un servidor de ventas

Esto sí es un ejemplo real de Apache Spark con Python (PySpark).

## Estructura del repositorio

```text
spark/
├── README.md
├── requirements.txt
├── run.sh
├── spark_sales_analysis.py
├── data/
│   └── sales.csv
├── docs/
│   ├── 01-introduccion-apache-spark.md
│   ├── 02-instalacion-y-ejecucion.md
│   ├── 03-explicacion-del-proyecto.md
│   ├── 04-conceptos-y-funcionalidades.md
│   └── 05-relacion-con-airflow.md
├── app.js
├── index.html
├── styles.css
├── server.py
├── .gitignore
└── .venv/
```

## Documentación separada

1. [Introducción a Apache Spark](docs/01-introduccion-apache-spark.md)
2. [Instalación y ejecución](docs/02-instalacion-y-ejecucion.md)
3. [Explicación del proyecto](docs/03-explicacion-del-proyecto.md)
4. [Conceptos y funcionalidades](docs/04-conceptos-y-funcionalidades.md)
5. [Relación con Airflow](docs/05-relacion-con-airflow.md)

## Instalación y ejecución

### Opción recomendada: setup + run

```bash
cd /home/cohorte5/Descargas/spark
chmod +x setup.sh run.sh
./setup.sh
./run.sh
```

### Opción manual

```bash
cd /home/cohorte5/Descargas/spark
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 spark_sales_analysis.py
```

## Requisitos necesarios

- Python 3
- Java instalado en el sistema
- Dependencias listadas en `requirements.txt`

Archivo de requisitos:

```txt
pyspark==3.5.1
```

## Archivo principal

```text
spark_sales_analysis.py
```

Este archivo es el núcleo del proyecto. Aquí se crea la sesión de Spark, se leen los datos, se transforman y se muestran los resultados.

## Requisitos

- Python 3
- Java (requisito para Spark)
- PySpark

## En resumen

Este proyecto demuestra cómo Apache Spark se usa realmente para analizar datos con Python. Es una versión educativa, pequeña y ejecutable, pero mantiene la lógica real del framework.

## Repositorio GitHub

https://github.com/andreswhite2026/spark
