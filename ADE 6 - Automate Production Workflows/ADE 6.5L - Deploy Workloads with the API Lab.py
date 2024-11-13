# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# DBTITLE 0,--i18n-ec8041ff-7d13-4f98-b940-3803c89bb6d1
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC # Lab: Working with the Databricks API
# MAGIC In this lab, you will use the Databricks CLI to work with DLT pipelines
# MAGIC
# MAGIC By the end of this lab, you should be able to:
# MAGIC * Programmatically deploy a workload using the Databricks CLI

# COMMAND ----------

# DBTITLE 0,--i18n-cacb5a78-ef75-48af-b3d1-9de4921e7b74
# MAGIC %md
# MAGIC
# MAGIC Run the setup script for this lab by running the cell below.

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-06.5L

# COMMAND ----------

db_token, db_instance = DA.get_credentials()

# COMMAND ----------

# DBTITLE 0,--i18n-344f74ae-b469-4fca-9f1b-f08f57d61cef
# MAGIC %md
# MAGIC ## Run your pipeline using the CLI
# MAGIC The pipeline you will be working with was generated when you ran the classroom setup script at the top of this notebook. The output from that cell shows, among other things, your pipeline's name. Use the pipeline name to get your pipeline id from the list of pipelines [here](#joblist/pipelines)
# MAGIC  
# MAGIC Open the driver's terminal by clicking View -> Open web terminal in the menu at the top of the page, and run the proper CLI command to start your pipeline.
# MAGIC
# MAGIC ## Check your work
# MAGIC To check your work, execute the following Python code. This uses the Pipelines API to check whether you've successfully triggered an update for your pipeline.
# MAGIC
# MAGIC Note: if this fails and states that the pipeline's state is "COMPLETED", you may not have run the script quickly enough after starting the pipeline. Try running the pipeline again, and immediately run the Python code.

# COMMAND ----------

# TODO
# Get your pipeline ID from the list of pipelines, 
# Open the driver's web terminal, 
# Use the proper CLI command to start the pipeline,
# Run the cell below to check your work

# COMMAND ----------

import time

from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.pipelines.api import PipelinesApi

# Set up the entry point with authentication
api_client = ApiClient(
  host  = db_instance,
  token = db_token
)

# Instantiate a PipelinesApi object
pipelines_api = PipelinesApi(api_client)

pipeline = pipelines_api.get(f"{DA.pipeline_id}")
try:
  state = pipeline.get("latest_updates")[0]["state"]
  # Check if running
  not_done = ["WAITING_FOR_RESOURCES", "INITIALIZING", "SETTING_UP_TABLES", "RUNNING"]
  done = ["COMPLETED", "FAILED", "CANCELED"]
  # state = pipelines_api.get(f"{DA.pipeline_id}").get("latest_updates")[0]["state"]

  if state in not_done:
      print(f"Pipeline is running (State: {state})")
      print("Excellent work!!")
  elif state in done:
      print(f"Pipeline is done (State: {state})")
      print("Excellent work!!")
  else:
      print("Something must be wrong. Double-check that you started the pipeline")
except:
  print("Something must be wrong. Double-check that you started the pipeline")





# COMMAND ----------

# DBTITLE 0,--i18n-bc221a52-dc14-4f0d-8389-9203e52edc8d
# MAGIC %md
# MAGIC
# MAGIC ## Run Python script
# MAGIC
# MAGIC You can also run this check within the Web Terminal by running the `check_pipeline.py` script created for you by the setup script above.
# MAGIC
# MAGIC Run the script by entering:
# MAGIC ```python /tmp/python/check_pipeline.py```

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
