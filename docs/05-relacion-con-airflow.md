# 05. Relación entre Apache Spark y Apache Airflow

## ¿Qué es Apache Airflow?

Apache Airflow es una herramienta para programar y orquestar flujos de trabajo.

Su función principal no es procesar datos por sí mismo, sino organizar tareas y programarlas.

Airflow se usa para definir DAGs (Directed Acyclic Graphs), que son secuencias de tareas que se ejecutan en orden según dependencias.

## ¿Qué hace Airflow?

Airflow puede programar tareas como:

- ejecutar scripts de Python
- lanzar ETL
- mover archivos
- ejecutar jobs de Spark
- cargar datos a una base de datos
- enviar alertas si falla un proceso

## ¿Cómo se relaciona con Spark?

Spark procesa los datos.
Airflow organiza cuándo y en qué orden se ejecutan los jobs.

Es decir:

- Spark hace el cálculo pesado
- Airflow decide cuándo correrlo y cómo orquestarlo

## Un ejemplo real de relación

Imagina este flujo:

1. Airflow ejecuta un job diario a las 2:00 AM
2. descarga archivos de ventas
3. prepara la carpeta de trabajo
4. lanza un comando `spark-submit`
5. Spark lee el CSV
6. Spark calcula métricas
7. Spark guarda resultados en parquet
8. Airflow notifica que el proceso terminó bien o falló

## ¿Por qué se usan juntos?

Porque cada herramienta hace una cosa distinta:

- Spark = procesamiento distribuido de datos
- Airflow = orquestación, programación y coordinación

### Si solo usaras Spark
- podrías ejecutar un trabajo, pero no tendrías una agenda ni dependencias definidas

### Si solo usaras Airflow
- podrías programar tareas, pero no procesar grandes datos masivos por sí mismo

### Juntos
- Airflow coordina y Spark procesa

## ¿Se parece a esto?

Sí, se relaciona con un flujo industrial de datos:

```text
Airflow DAG
   ↓
trigger / schedule
   ↓
Spark job
   ↓
transformaciones y agregaciones
   ↓
resultados / almacenamiento
```

## ¿Cuándo es útil esta combinación?

Cuando hay:

- ETL diario
- pipelines de datos
- cargas de archivos periódicas
- necesidades de scheduling
- trabajos con alta dependencia entre tareas
- sistemas productivos de analítica

## Diferencia importante

Spark no es Airflow y Airflow no es Spark.

### Spark
- procesa datos
- transforma datasets
- hace análisis y ML

### Airflow
- orquesta tareas
- ejecuta jobs programados
- gestiona dependencias

## ¿Qué comando usa Airflow para lanzar Spark?

En un entorno real suele usarse:

```bash
spark-submit mi_script.py
```

Airflow podría ejecutar ese comando a través de un operador.

## ¿Por qué esto es importante en el proyecto?

Porque el proyecto actual es un ejemplo básico de Spark, pero el mundo real normalmente agrega:

- programación con Airflow
- automatización de tareas
- orquestación de jobs
- monitoreo y alertas
- almacenamiento en lake o warehouse

## Conclusión

La relación real es:

- Spark ejecuta el procesamiento de datos
- Airflow ejecuta, programa y coordina ese procesamiento

La razón por la que son importantes juntas es que una empresa necesita tanto poder de procesamiento como capacidad de automatización y coordinación.

En resumen: Spark hace el trabajo pesado, Airflow organiza el trabajo para que ocurra en el momento correcto y con dependencias bien definidas.
