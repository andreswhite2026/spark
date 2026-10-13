# Apache Spark - Proyecto de análisis real con PySpark

Este proyecto demuestra un ejemplo real de Apache Spark usando Python.

## ¿Qué hace?

El script principal lee un archivo CSV de ventas, calcula subtotales, suma ingresos totales, calcula el promedio por venta y agrupa resultados por producto y cliente.

## Estructura

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
└── .gitignore
```

## Requisitos

- Python 3
- Java (Spark lo necesita)
- PySpark

## Instalación

```bash
cd /home/cohorte5/Descargas/spark
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecución

```bash
cd /home/cohorte5/Descargas/spark
source .venv/bin/activate
python3 spark_sales_analysis.py
```

O con:

```bash
cd /home/cohorte5/Descargas/spark
chmod +x run.sh
./run.sh
```

## Explicación rápida

- `SparkSession` crea la sesión de Spark
- `read.csv()` lee los datos
- `withColumn()` crea la columna subtotal
- `count()` cuenta filas
- `sum()` y `avg()` calculan métricas
- `groupBy()` agrega por producto o cliente
- `show()` imprime resultados

## Documentación completa

Consulta `GUIA_SPARK.md` para una explicación detallada paso a paso.

## Diferencia con un proyecto web

Este proyecto no es un servidor web. Es un ejemplo real de Apache Spark usando PySpark para análisis de datos.
