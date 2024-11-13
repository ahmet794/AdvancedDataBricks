# Databricks notebook source
# DBTITLE 0,--i18n-df60a0fa-baf3-48e9-854b-0c49e93bf8b5
# MAGIC %md
# MAGIC
# MAGIC ## Quarantine Silver Updates
# MAGIC In this lab, you will learn to apply validation rules retrieved from the dataset to bronze tables to create quarantine table, views based on the valid and invalid data.
# MAGIC
# MAGIC ## Learning Objectives
# MAGIC By the end of this lesson, you should be able to:
# MAGIC - Read rules from  **`look_up_db`** and store them in the form of a dictionary.
# MAGIC - Create a quarantine table by reading a source table and applying the validation rules obtained for deriving valid and invalid views.
# MAGIC - Create validated views using the **`create_validated_views`** function and write configuration information for different datasets.

# COMMAND ----------

import dlt
import pyspark.sql.functions as F

# COMMAND ----------

# DBTITLE 0,--i18n-dfbcb403-6b85-4444-8b42-808ccd8d14e9
# MAGIC %md
# MAGIC ## Validate Bronze Tables with Portable Expectations <br>
# MAGIC
# MAGIC The steps below include:
# MAGIC - Retrieve rules from a Spark dataset based on a specified topic.
# MAGIC - Use **`spark.conf.get()`** to retrieves the value of the configuration parameter **`"lookup_db"`**.
# MAGIC - Store the rules in python dictionary in form of key value pair 
# MAGIC - Create a quarantined table to mark whether each record should be quarantined or not.
# MAGIC - **Modularize code with views** for valid and invalid data
# MAGIC - Create validated views for that dataset

# COMMAND ----------

# TODO
lookup_db = spark.FILL_IN

def get_rules(topic):
    df = spark.FILL_IN
)

# COMMAND ----------

# DBTITLE 0,--i18n-ff428057-847b-4e79-8519-6428ca7feae0
# MAGIC %md
# MAGIC ### Modularize code with views
# MAGIC
# MAGIC For this we will use:
# MAGIC - Use **`create_validated_views`** function and pass paramater dataset, source_table, valid_view, invalid_view 
# MAGIC - Use **`get_rules`** function defined earlier to fetch a validation rules and store it in variable.
# MAGIC - Create quarantine table for checking whether data is valid or invalid and include **`is_quarantined`** column to mark whether each record should be quarantined or not. 
# MAGIC - Create function with name **`create_valid`** and apply a filter to select records where "is_quarantined" is false
# MAGIC - Create **`invalid_view`** by applying a filter to select records where "is_quarantined" is true

# COMMAND ----------

# TODO

# COMMAND ----------

# DBTITLE 0,--i18n-d1932877-ab3d-49ca-b25b-b410e0708c0a
# MAGIC %md
# MAGIC
# MAGIC ### Configuration based code
# MAGIC
# MAGIC
# MAGIC Use this steps to create configuration:
# MAGIC - Create a dictionary with name **quarantine_tables_config** and include each dataset by a key.
# MAGIC - Use rules_tag, source, valid_view, invalid_view to specify the information of dataset.
# MAGIC - Use **for** loop to iterate through configuration code and each key-value pair in the quarantine_tables_config dictionary.
# MAGIC - Use **`create_validated_views`** function for each dataset by including it inside for loop to separate the data into valid and invalid categories.

# COMMAND ----------

# TODO

quarantine_tables_config = {
    FILL_IN
}

