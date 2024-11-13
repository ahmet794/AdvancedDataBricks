# Databricks notebook source
# DBTITLE 0,--i18n-7eb161cc-c6cf-41ce-991a-7b2418a11352
# MAGIC %md
# MAGIC
# MAGIC ## Workouts BPM Silver Updates
# MAGIC In this lab, you will learn to defines a data processing pipeline for streaming data related to **BPM** (heart rate) measurements and workout sessions and create derived tables like "bpm_silver", "workouts_silver", "workouts_completed", and "workout_bpm".
# MAGIC
# MAGIC ## Learning Objectives
# MAGIC By the end of this lesson, you should be able to:
# MAGIC - Retrieve rules from a Spark dataset based on a specified topic.
# MAGIC - Process heart rate data by categorizing it.
# MAGIC - Process workout session data, casting timestamps, and ensuring data completeness.
# MAGIC - Determine completed workout sessions by matching "start" and "stop" actions.
# MAGIC - Calculate heart rate data within completed workout sessions, filtering out problematic records.

# COMMAND ----------

import dlt
import pyspark.sql.functions as F

# COMMAND ----------

# DBTITLE 0,--i18n-509a3465-f68e-4dbe-a109-7f44def26de8
# MAGIC %md
# MAGIC ## Read rules from Dataset
# MAGIC
# MAGIC To read rules from table:
# MAGIC - Define function with name **get_rules** and pass **topic** in parameters.
# MAGIC - Use **`spark.conf.get()`** to retrieves the value of the configuration parameter **`"lookup_db"`**.
# MAGIC - Store the rules in python dictionary in form of key value pair

# COMMAND ----------

# TODO

lookup_db = spark.FILL_IN

def get_rules(topic):
    df = spark.FILL_IN


# COMMAND ----------

# DBTITLE 0,--i18n-dbcd6a09-8d40-4c52-a672-ad990cd31f79
# MAGIC %md
# MAGIC
# MAGIC ## Maintaining quality checks in table
# MAGIC Represent the process of processing streaming data for both **heartrate** and **workout-related** data and store it in **"silver"** tables.
# MAGIC
# MAGIC Follow these steps to maintain quality check in table:
# MAGIC - Read a stream named **"valid_bpm"** select columns: "device_id", "time", "heartrate".
# MAGIC - Add a new column **"bpm_check"** based on the **"heartrate"** value and add watermark with 30 sec
# MAGIC - Drop duplicate records based on "device_id" and "time
# MAGIC - Same for **"valid_workouts"** select columns: "user_id", "workout_id", "timestamp" (casted as "time"), "action", "session_id" apply watermarking on time column and drop duplicates
# MAGIC - Create a SQL query that performs a left join between **"workouts_silver"** for "start" actions and **"workouts_silver"** for "stop" actions 
# MAGIC - Select columns from "a" and "b", calculating the "in_progress" status.
# MAGIC - Similarly, create a SQL query that joins **"bpm_silver"** with **"workouts_completed"** and **"user_lookup"**.
# MAGIC - Select appropriate columns from the joined data.
# MAGIC - Apply a filter to select only records where **"bpm_check"** is 'OK

# COMMAND ----------

# TODO

@dlt.table(table_properties={"quality": "silver"})
def bpm_silver():
   return (
       FILL_IN
)

@dlt.table(table_properties={"quality": "silver"})
def workouts_silver():
    return (
       FILL_IN
)

@dlt.table
def workouts_completed():
    return spark.sql(
        FILL_IN
)

@dlt.table
def workout_bpm():
    return spark.sql(
        FILL_IN
)

