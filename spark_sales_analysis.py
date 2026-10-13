from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main():
    spark = SparkSession.builder \
        .appName("ApacheSparkSalesAnalysis") \
        .master("local[*]") \
        .getOrCreate()

    try:
        sales_df = spark.read.option("header", True).option("inferSchema", True).csv("data/sales.csv")

        sales_df = sales_df.withColumn(
            "subtotal",
            F.col("quantity") * F.col("unit_price")
        )

        total_sales = sales_df.count()
        total_revenue = sales_df.agg(F.sum("subtotal").alias("total_revenue")).collect()[0]["total_revenue"]
        avg_ticket = sales_df.agg(F.avg("subtotal").alias("avg_ticket")).collect()[0]["avg_ticket"]

        print("\n=== Resumen de ventas ===")
        print(f"Total de ventas registradas: {total_sales}")
        print(f"Ingresos totales: ${total_revenue:,.2f}")
        print(f"Promedio por venta: ${avg_ticket:,.2f}\n")

        print("=== Ventas por producto ===")
        sales_by_product = sales_df.groupBy("product").agg(
            F.sum("subtotal").alias("revenue_by_product")
        ).orderBy(F.col("revenue_by_product").desc())
        sales_by_product.show(truncate=False)

        print("=== Ventas por cliente ===")
        sales_by_client = sales_df.groupBy("client").agg(
            F.sum("subtotal").alias("total_paid")
        ).orderBy(F.col("total_paid").desc())
        sales_by_client.show(truncate=False)

    finally:
        spark.stop()


if __name__ == "__main__":
    main()
