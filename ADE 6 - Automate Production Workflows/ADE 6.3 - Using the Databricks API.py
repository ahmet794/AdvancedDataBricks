# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# DBTITLE 0,--i18n-633e3a73-aea8-41b4-b743-85b5263bc88e
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC # Using the Databricks API
# MAGIC In this lesson, you will learn how to setup, configure, and use the Databricks API.
# MAGIC
# MAGIC By the end of this lesson, you should be able to:
# MAGIC * Programmatically run pipeline operations using the REST API using `curl` and Python

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-06.3

# COMMAND ----------

# DBTITLE 0,--i18n-268b949f-3081-4b4c-b12f-6d5db11bd0be
# MAGIC %md
# MAGIC
# MAGIC ## Get Credentials
# MAGIC In the next few lessons, we are going to use the Databricks API and the Databricks CLI to run code from a terminal. Since we are in a learning environment, we are going to provide you the credentials here in the workspace. If you'd like to create these yourself, follow the instructions in the previous lesson on generating tokens. In the "real world" we recommend that you follow your organization's security policies for storing credentials.

# COMMAND ----------

db_token, db_instance = DA.get_credentials()

# COMMAND ----------

# DBTITLE 0,--i18n-bba843f8-9e3b-4927-a0a2-031fe9efc8c2
# MAGIC %md
# MAGIC
# MAGIC ## Use ```curl``` to make a call to the Databricks API
# MAGIC Copy the output of the following cell into the terminal window and press Enter

# COMMAND ----------

print("curl -H \"Authorization: Bearer " + db_token + "\" --get " + db_instance + "/api/2.0/pipelines")

# Copy the curl command printed below

# COMMAND ----------

# DBTITLE 0,--i18n-93303b47-dc2b-4f71-8359-c57649d954fb
# MAGIC %md
# MAGIC
# MAGIC ## Make API calls using Python
# MAGIC You can use Python to make API calls as well. The easiest way to do this is to install the `databricks-cli` package and then import the `databricks_cli` library in a Python script.
# MAGIC
# MAGIC Note that for clusters running Databricks Runtime ML, the Databricks CLI is already installed. This is also already installed for you by the setup script above.

# COMMAND ----------

from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.clusters.api import ClusterApi

api_client = ApiClient(
  host  = db_instance,
  token = db_token
)

clusters_api   = ClusterApi(api_client)
clusters_list  = clusters_api.list_clusters()

print("Cluster name, cluster ID")

for cluster in clusters_list['clusters']:
  print(f"{cluster['cluster_name']}, {cluster['cluster_id']}")

# COMMAND ----------

# DBTITLE 0,--i18n-f5ff06d5-f4d5-42f5-b06a-b0b1604bc0bd
# MAGIC %md
# MAGIC ## View a Python script in the web terminal
# MAGIC Enter the following commands into the web terminal:
# MAGIC
# MAGIC ```cat /tmp/python/using_the_api.py```

# COMMAND ----------

# /tmp/python/using_the_api.py
"""
import credentials as my_credentials

from databricks_cli.clusters.api import ClusterApi
from databricks_cli.sdk.api_client import ApiClient

# Set up the entry point with authentication
api_client = ApiClient(
  host  = my_credentials.db_instance,
  token = my_credentials.db_token
)

clusters_api   = ClusterApi(api_client)
clusters_list  = clusters_api.list_clusters()

print("Cluster name, cluster ID")

for cluster in clusters_list['clusters']:
  print(f"{cluster['cluster_name']}, {cluster['cluster_id']}")
"""

# COMMAND ----------

# DBTITLE 0,--i18n-3b04ee89-0046-441c-afbd-ebd5adcd16e4
# MAGIC %md
# MAGIC
# MAGIC ## Run the script
# MAGIC Run the script by entering:
# MAGIC ```python /tmp/python/using_the_api.py```

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
