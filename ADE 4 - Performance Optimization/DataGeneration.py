# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists dbacademy;
# MAGIC drop table if exists dbacademy.iot_data

# COMMAND ----------

from pyspark.sql.functions import *

numFiles = 125
numRowsPerFile = 10000000

(spark
 .range(0,numRowsPerFile * numFiles, numPartitions = numFiles)
#  .repartition(numFiles)
 .selectExpr('*', 'RAND() as value', 'id % 100 as device_type')
 .write
 .mode('overwrite')
 .saveAsTable('dbacademy.iot_data')
)

# COMMAND ----------

# MAGIC %sql select * from dbacademy.iot_data

# COMMAND ----------

# MAGIC %sql SELECT device_type, avg(value) FROM dbacademy.iot_data GROUP BY device_type

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
