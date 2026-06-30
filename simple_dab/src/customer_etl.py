# Databricks notebook source

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

employees = [
    (1, "Alice", "IT"),
    (2, "Bob", "HR"),
    (3, "Charlie", "Finance")
]

df = spark.createDataFrame(
    employees,
    ["emp_id", "name", "department"]
)

display(df)

# COMMAND ----------

silver_df = df.filter(df.department != "HR")

display(silver_df)

print("Customer ETL completed successfully")