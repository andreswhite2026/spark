# 02. Instalación y ejecución del proyecto

## Objetivo

En este documento se explica exactamente cómo se instaló Spark en el computador local y cómo se ejecuta este proyecto paso a paso.

## Qué usé para correrlo localmente

Para ejecutar Spark localmente en este equipo usé:

- Ubuntu/Linux
- Python 3
- virtual environment (`.venv`)
- PySpark
- Java (requisito de Spark)

La forma más fácil y reproducible es usar los scripts del proyecto:

```bash
cd /home/cohorte5/Descargas/spark
chmod +x setup.sh run.sh
./setup.sh
./run.sh
```

También se puede hacer de forma manual:

```bash
cd /home/cohorte5/Descargas/spark
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 spark_sales_analysis.py
```

## Requisitos reales

Spark requiere que el sistema tenga Java disponible.

En muchos entornos Linux, esto se comprueba con:

```bash
java -version
python3 --version
```

Si Java no está instalado, se necesita instalarlo primero.

## Archivo de dependencias

El proyecto tiene este archivo:

```txt
requirements.txt
```

Contenido:

```txt
pyspark==3.5.1
```

Esto significa que la dependencia principal es PySpark en la versión 3.5.1.

## Instalación paso a paso

### Paso 1: entrar a la carpeta del proyecto

```bash
cd /home/cohorte5/Descargas/spark
```

### Paso 2: crear entorno virtual

```bash
python3 -m venv .venv
```

### Paso 3: activar el entorno virtual

```bash
source .venv/bin/activate
```

### Paso 4: instalar las dependencias

```bash
pip install -r requirements.txt
```

Esto instalará PySpark y sus dependencias necesarias para correr Spark localmente.

## Cómo ejecutar el proyecto

### Opción 1: ejecutar el script principal

```bash
cd /home/cohorte5/Descargas/spark
source .venv/bin/activate
python3 spark_sales_analysis.py
```

### Opción 2: usar el script `run.sh`

```bash
cd /home/cohorte5/Descargas/spark
chmod +x run.sh
./run.sh
```

## Qué hace `run.sh`

El script `run.sh` normalmente ejecuta el flujo de Spark del proyecto de la misma manera:

```bash
#!/bin/bash
source .venv/bin/activate
python3 spark_sales_analysis.py
```

Este archivo sirve para hacer que la ejecución sea más rápida y reproducible.

## Qué ocurre al correrlo

Cuando ejecutas el script, Spark hace lo siguiente:

1. crea la sesión
2. lee el CSV de ventas
3. calcula subtotal
4. suma ingresos totales
5. calcula promedio por venta
6. agrupa por producto y cliente
7. muestra resultados por consola
8. cierra la sesión

## Salida esperada

La salida en consola se parece a esto:

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

## Importante sobre el entorno local

Este proyecto se ejecutó en local usando:

```python
.master("local[*]")
```

Eso significa que Spark va a usar la máquina local como clúster de prueba y aprovechar todos los núcleos disponibles.

Esto es ideal para aprender, practicar y desarrollar sin iniciar un clúster real.

## Diferencia entre correr local y en clúster real

### Local
- buena para aprender
- funciona desde nuestra computadora
- útil para pruebas y demos
- no requiere infraestructura grande

### Cluster real
- usado en producción
- requiere varios nodos
- más escalable
- aplica para proyectos grandes de Big Data

## Conclusión

La instalación y ejecución de este proyecto en local fue muy simple y real:

- crear entorno virtual
- instalar PySpark
- lanzar la sesión de Spark
- leer un CSV
- procesar datos y mostrar resultados

Esto es exactamente la base para trabajar con Spark localmente y luego escalar a entornos más grandes cuando el problema crece.
