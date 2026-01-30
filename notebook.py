# Databricks notebook source

GIT_PATH = "/Workspace/databricks-kata"

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS bronze")
spark.sql("USE bronze")

# COMMAND ----------

users_df = spark.read.option("header", "true").option("inferSchema", "true").csv(f"{GIT_PATH}/raw_users.csv")
users_df.write.format("delta").mode("overwrite").saveAsTable("bronze.raw_users")

# COMMAND ----------

subscriptions_df = spark.read.option("header", "true").option("inferSchema", "true").csv(f"{GIT_PATH}/raw_subscriptions.csv")
subscriptions_df.write.format("delta").mode("overwrite").saveAsTable("bronze.raw_subscriptions")

# COMMAND ----------

payments_df = spark.read.option("header", "true").option("inferSchema", "true").csv(f"{GIT_PATH}/raw_payments.csv")
payments_df.write.format("delta").mode("overwrite").saveAsTable("bronze.raw_payments")

# COMMAND ----------

spark.sql("""
SELECT 'raw_users' as table_name, COUNT(*) as records FROM bronze.raw_users
UNION ALL
SELECT 'raw_subscriptions', COUNT(*) FROM bronze.raw_subscriptions
UNION ALL
SELECT 'raw_payments', COUNT(*) FROM bronze.raw_payments
""").show()
