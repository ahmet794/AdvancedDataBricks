# Databricks notebook source
# MAGIC %run ./Classroom-Setup-06-Common

# COMMAND ----------

LESSON = "using_api"
DA = init_DA(LESSON, reset=False)

db_token, db_instance = DA.get_credentials()
DA.create_credentials_file(db_token, db_instance)

api_script = f"""
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
  print(f"{{cluster['cluster_name']}}, {{cluster['cluster_id']}}")
"""

DA.write_to_file(api_script, "using_the_api.py")
    
None
