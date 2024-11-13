# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# DBTITLE 0,--i18n-012c67db-0e47-49e4-98e0-33503cc54915
# MAGIC %md
# MAGIC # Deploy a Pipeline with the Databricks CLI
# MAGIC * Trigger a pipeline run with the CLI.
# MAGIC * Clone a pipeline using the CLI.

# COMMAND ----------

# DBTITLE 0,--i18n-6f54a73b-5dc8-4f9d-91c2-3165f3faa4cd
# MAGIC %md
# MAGIC ## Run the setup script
# MAGIC Run the setup script for this lesson by running the cell below.

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-06.4

# COMMAND ----------

db_token, db_instance = DA.get_credentials()

# COMMAND ----------

# DBTITLE 0,--i18n-382764d1-d0b9-4b7d-9920-ed5225135a5f
# MAGIC %md
# MAGIC ## Trigger a pipeline run with the CLI

# COMMAND ----------

# DBTITLE 0,--i18n-5a287243-2bbb-4b97-9409-2d173673c854
# MAGIC %md
# MAGIC - Paste the output of the following cell into the terminal, and press "Enter/Return".
# MAGIC - To view the current status of the pipeline run, paste the second command into the terminal, and press "Enter/Return" (repeat, as needed).

# COMMAND ----------

print(f"databricks pipelines start --pipeline-id {DA.pipeline_id} --full-refresh")
print(f"databricks pipelines get --pipeline-id {DA.pipeline_id}")

# COMMAND ----------

# DBTITLE 0,--i18n-7a19523f-d060-441d-964b-3f1149a29fdf
# MAGIC %md
# MAGIC ## Clone a pipeline
# MAGIC Cloning a pipeline using the CLI involves getting the settings for a pipeline, removing elements of the settings that are not needed, changing the name of the pipeline, and creating a new pipeline with the changed settings. The command below performs all of these actions in a single line.\
# MAGIC \
# MAGIC Note the following elements of the command:
# MAGIC * We use the same "get" command to get the json output of the existing pipeline.
# MAGIC * This output is piped into a python script that performs the following actions:
# MAGIC     - Keeps only the "spec" portion of the json
# MAGIC     - Deletes the existing id (a new id will be created when the new pipeline is created)
# MAGIC     - Cleans up single quotes and the true and false values
# MAGIC * The output of the python script is then saved to `settings.json`
# MAGIC * We follow that with a second terminal command to create a new pipeline with the settings we just saved.

# COMMAND ----------

# DBTITLE 0,--i18n-1bb5727a-67f3-4a92-83be-c59cf3be714c
# MAGIC %md
# MAGIC ## Get pipeline settings
# MAGIC Paste the entire command (all lines), and press "Enter/Return".

# COMMAND ----------

print(f"databricks pipelines get --pipeline-id {DA.pipeline_id} | python -c \"import sys, json; settings = json.load(sys.stdin)['spec']; del settings['id']; settings['name'] = settings['name'] + '_copy'; settings['target'] = settings['target'] + '_copy'; print(str(settings).replace(\\\"'\\\", '\\\"').replace('True', 'true').replace('False', 'false'))\" > settings.json && databricks pipelines create --settings settings.json")

# COMMAND ----------

# DBTITLE 0,--i18n-53ad8f42-c860-443e-95f4-6c65755030b3
# MAGIC %md
# MAGIC ## View `settings.json`
# MAGIC In the terminal window enter `cat settings.json`. This will display the contents of `settings.json`.
# MAGIC  
# MAGIC The `settings.json` file contains information needed to create a pipeline. This file can be added to version control and can be changed as needed for future pipeline creation.

# COMMAND ----------

# DBTITLE 0,--i18n-41bedf56-eacd-4a9c-956b-46f11098b67c
# MAGIC %md
# MAGIC
# MAGIC ## Push your `settings.json` file to a Databricks repo for version control

# COMMAND ----------

# DBTITLE 0,--i18n-de1bacd2-8ac5-46c7-9ed4-699ac802c2a3
# MAGIC %md
# MAGIC ## Run the new pipeline
# MAGIC In order to run the new pipeline:
# MAGIC - Copy the ID of the new pipeline into the cell below, making sure to exclude the period (full stop) at the end of the ID, and run the cell.
# MAGIC - Paste the first command in the output of the cell into the terminal, and press "Enter/Return".
# MAGIC - We use the same "get" command to get the status of the pipeline run. Paste the second command from the output of the next cell into the terminal, and press "Enter/Return".

# COMMAND ----------

new_id = "PASTE_NEW_ID_HERE"
print(f"databricks pipelines start --pipeline-id {new_id} --full-refresh")
print(f"databricks pipelines get --pipeline-id {new_id}")

# COMMAND ----------

# DBTITLE 0,--i18n-5b03ae1c-b3f0-404c-9ee6-60036dfd3efa
# MAGIC %md
# MAGIC ### Delete the pipeline
# MAGIC Paste the command below into the terminal, change the ID, and press "Enter/Return" to delete the pipeline.

# COMMAND ----------

print(f"databricks pipelines delete --pipeline-id {new_id}")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
