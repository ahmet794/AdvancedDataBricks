# Databricks notebook source
# MAGIC %run ./Classroom-Setup-04-Common

# COMMAND ----------

PIPELINE = "performance"
DA = init_DA(PIPELINE)

# COMMAND ----------

notebooks = [
    "ADE 4.2 - ZOrder Table"
]

DA.configure_pipeline(configuration={"source": DA.paths.stream_source}, notebooks=notebooks, photon=True)
DA.conclude_setup()

None

# COMMAND ----------

def print_sql(rows, sql):
    html = f"<textarea style=\"width:100%\" rows={rows}> \n{sql.strip()}</textarea>"
    displayHTML(html)

# COMMAND ----------

def _generate_nonzorder_query():
  print_sql(2, "SELECT avg(value) as avg FROM dbacademy.iot_data WHERE device_type = 50")

DA.generate_nonzorder_query = _generate_nonzorder_query

# COMMAND ----------

def _generate_zorder_query():
  print_sql(3, f"""
USE SCHEMA {DA.schema_name};
SELECT avg(value) as avg FROM iot_zordered WHERE device_type = 50
            """)

DA.generate_zorder_query = _generate_zorder_query

# COMMAND ----------

def _generate_optimize_query():
  print_sql(3, f"""
USE SCHEMA {DA.schema_name};
OPTIMIZE iot_zordered ZORDER BY (device_type)
            """)

DA.generate_optimize_query = _generate_optimize_query

# COMMAND ----------

def _generate_another_zorder_query():
  print_sql(3, f"""
USE SCHEMA {DA.schema_name};
SELECT avg(value) as avg FROM iot_zordered WHERE device_type = 73
            """)

DA.generate_another_zorder_query = _generate_another_zorder_query
