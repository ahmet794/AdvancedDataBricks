# Databricks notebook source
# MAGIC %pip install databricks-cli --quiet

# COMMAND ----------

# MAGIC %run ../../Includes/_common

# COMMAND ----------

# MAGIC %run ../../Includes/_stream_factory

# COMMAND ----------

# MAGIC %run ../../Includes/_pipeline_config

# COMMAND ----------

def init_DA(name, reset=True, pipeline=False):

    lesson_config = LessonConfig(name=name, 
                    create_schema=True,
                    create_catalog = False,
                    requires_uc = False,
                    installing_datasets = True,
                    enable_streaming_support = False,
                    enable_ml_support = False)
    DA = DBAcademyHelper(course_config, lesson_config)
    if reset: DA.reset_lesson()
    DA.init()
    DA.paths.python = "file:/tmp/python"

    if pipeline:
        DA.paths.stream_source = f"{DA.paths.working_dir}/stream_source"
        DA.paths.storage_location = f"{DA.paths.working_dir}/storage_location"
        DA.pipeline_name = f"{DA.unique_name(sep='-')}: ETL Pipeline - {name.upper()}"
        DA.lookup_db = f"{DA.unique_name(sep='_')}_lookup"

        if reset:  # create lookup tables
            import pandas as pd

            spark.sql(f"CREATE SCHEMA IF NOT EXISTS {DA.lookup_db}")
            DA.clone_source_table(f"{DA.lookup_db}.date_lookup", source_name="date-lookup")
            DA.clone_source_table(f"{DA.lookup_db}.user_lookup", source_name="user-lookup")

            df = spark.createDataFrame(pd.DataFrame([
                ("device_id_not_null", "device_id IS NOT NULL", "validity", "bpm"),
                ("device_id_valid_range", "device_id > 110000", "validity", "bpm"),
                ("heartrate_not_null", "heartrate IS NOT NULL", "validity", "bpm"),
                ("user_id_not_null", "user_id IS NOT NULL", "validity", "workout"),
                ("workout_id_not_null", "workout_id IS NOT NULL", "validity", "workout"),
                ("action_not_null","action IS NOT NULL","validity","workout"),
                ("user_id_not_null","user_id IS NOT NULL","validity","user_info"),
                ("update_type_not_null","update_type IS NOT NULL","validity","user_info")
            ], columns=["name", "condition", "tag", "topic"]))
            df.write.mode("overwrite").saveAsTable(f"{DA.lookup_db}.rules")
        
    return DA

None

# COMMAND ----------

@DBAcademyHelper.monkey_patch
def write_to_file(self, text, filename):
    filepath = f"{DA.paths.python}/{filename}"
    dbutils.fs.put(filepath, text, overwrite=True)
    print(f"Created file {filepath}")    

@DBAcademyHelper.monkey_patch
def get_credentials(self):
    db_token = dbgems.get_notebooks_api_token()
    db_instance = dbgems.get_notebooks_api_endpoint()
    return db_token, db_instance    

@DBAcademyHelper.monkey_patch
def create_credentials_file(self, db_token, db_instance):
    contents = f"""
db_token = "{db_token}"
db_instance = "{db_instance}"
    """
    self.write_to_file(contents, "credentials.py")    

@DBAcademyHelper.monkey_patch
def print_cli_configuration_steps(self, db_token, db_instance):
    self.display_config_values([
      ("Install the CLI", "pip install databricks-cli"),
      ("Set up authentication", f"databricks configure --host {db_instance} --token"),
      ("Enter token", db_token),
      ("Verify authentication to CLI", "databricks workspace list")  
    ])    

None
