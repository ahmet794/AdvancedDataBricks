# Databricks notebook source
# MAGIC %run ./Classroom-Setup-06-Common

# COMMAND ----------

LESSON = "deploy-workload"
DA = init_DA(LESSON, pipeline=True)

try:
    notebooks=[
        "bronze/prod/ingest",
        "silver/quarantine",
        "silver/workouts_bpm",
        "silver/users"    
    ]
    DA.configure_pipeline(configuration={"source": DA.paths.stream_source, "lookup_db": DA.lookup_db}, notebooks=notebooks)
    DA.pipeline_id = DA.generate_pipeline()
except:
    DA.pipeline_id = "<pipeline_id>"

DA.daily_stream = StreamFactory(
    source_dir=DA.paths.datasets, 
    target_dir=DA.paths.stream_source,
    load_batch=load_daily_batch,
    max_batch=16
)
DA.daily_stream.load()

db_token, db_instance = DA.get_credentials()
DA.create_credentials_file(db_token, db_instance)

api_script = f"""
import credentials as my_credentials
import time

from databricks_cli.pipelines.api import PipelinesApi
from databricks_cli.sdk.api_client import ApiClient

# Set up the entry point with authentication
api_client = ApiClient(
  host  = my_credentials.db_instance,
  token = my_credentials.db_token
)

# Instantiate a PipelinesApi object
pipelines_api = PipelinesApi(api_client)

# Make a pipeline start request using the library
resp  = pipelines_api.start_update(f"{DA.pipeline_id}")
state = pipelines_api.get(f"{DA.pipeline_id}").get("latest_updates")[0]["state"]
print(state)

# Check if finished
done = ["COMPLETED", "FAILED", "CANCELED"]
while state not in done:
    duration = 15
    time.sleep(duration)
    state = pipelines_api.get(f"{DA.pipeline_id}").get("latest_updates")[0]["state"]
    print(state)

"""

DA.write_to_file(api_script, "check_pipeline.py")

None
