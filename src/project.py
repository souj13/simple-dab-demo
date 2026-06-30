# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

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

print("Hello from my first DAB project!")
