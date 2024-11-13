# Databricks notebook source
# MAGIC %run ./Classroom-Setup-04-Common

# COMMAND ----------

PIPELINE = "performance"
DA = init_DA(PIPELINE)

# COMMAND ----------

DA.conclude_setup()

None

# COMMAND ----------

def print_sql(rows, sql):
    html = f"<textarea style=\"width:100%\" rows={rows}> \n{sql.strip()}</textarea>"
    displayHTML(html)

# COMMAND ----------

def _generate_baseline_query():
  print_sql(2, "SELECT avg(value) as avg FROM dbacademy.iot_data WHERE device_type = 50")

DA.generate_baseline_query = _generate_baseline_query

# COMMAND ----------

def _generate_diskcache_query():
  print_sql(2, "SELECT avg(value) as avg FROM dbacademy.iot_data WHERE device_type = 75")

DA.generate_diskcache_query = _generate_diskcache_query

# COMMAND ----------

def _generate_popcache_query():
  print_sql(2, "CACHE SELECT * FROM dbacademy.iot_data")

DA.generate_popcache_query = _generate_popcache_query
