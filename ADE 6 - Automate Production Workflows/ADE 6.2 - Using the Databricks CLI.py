# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# DBTITLE 0,--i18n-74269711-cd43-4b9c-8908-f06d215ca27d
# MAGIC %md
# MAGIC # Using the Databricks CLI
# MAGIC In this lesson, you will execute commands using the Databricks CLI. We will use the cluster web terminal for this demo.
# MAGIC
# MAGIC By the end of this lab, you should be able to:
# MAGIC * Launch the driver's web terminal to run shell commands on the driver node
# MAGIC * Install the Databricks CLI and configure authentication to a Databricks workspace
# MAGIC * List files or clusters in your workspace to verify successful authentication
# MAGIC * Configure Databricks Secrets

# COMMAND ----------

# DBTITLE 0,--i18n-bccc5e28-657f-4d43-a064-12f310a9b7e0
# MAGIC %md
# MAGIC ## Setup
# MAGIC Run the classroom setup script in the next cell to configure the classroom.

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-06.2

# COMMAND ----------

# DBTITLE 0,--i18n-17875401-9beb-4811-9864-f7f66142f5c2
# MAGIC %md
# MAGIC
# MAGIC ## Get Credentials
# MAGIC In the next few lessons, we are going to use the Databricks API and the Databricks CLI to run code from a terminal. Since we are in a learning environment, we are going to provide you the credentials here in the workspace. If you'd like to create these yourself, follow the instructions in the previous lesson on generating tokens. In the "real world" we recommend that you follow your organization's security policies for storing credentials.

# COMMAND ----------

db_token, db_instance = DA.get_credentials()

# COMMAND ----------

# DBTITLE 0,--i18n-99bcb96f-b69e-4f51-b7d0-3e4f2bd561c2
# MAGIC %md
# MAGIC
# MAGIC ## Setup CLI in Cluster Web Terminal
# MAGIC | Step | Command |
# MAGIC | --- | --- |
# MAGIC | Install the CLI | `pip install databricks-cli` |
# MAGIC | Set up authentication info and host to connect to | `databricks configure --host {db_instance} --token` |
# MAGIC | This issues a prompt (`Token:`) to enter your personal access token  | `{db_token}` |
# MAGIC | Verify authentication to CLI | databricks workspace list |

# COMMAND ----------

DA.print_cli_configuration_steps(db_token, db_instance)

# COMMAND ----------

# DBTITLE 0,--i18n-967f7df1-d1ed-4236-bf8a-bb154bf422cb
# MAGIC %md
# MAGIC ## Verify Correct Config
# MAGIC Paste the output of the following cell into the terminal, press "Enter/Return", and verify that you receive output.

# COMMAND ----------

print(f"databricks workspace ls /Users/{DA.username}")

# COMMAND ----------

# DBTITLE 0,--i18n-f044424f-6685-4966-a84d-6f98b4b4dcf0
# MAGIC %md
# MAGIC ## Create secrets
# MAGIC Optionally, store your secrets in a secret scope using the Databricks CLI.
# MAGIC ```
# MAGIC databricks secrets create-scope --scope <scope-name>
# MAGIC databricks secrets put --scope <scope-name> --key db_instance
# MAGIC databricks secrets put --scope <scope-name> --key db_token
# MAGIC ```
# MAGIC Then, you can read the secrets stored in the secret scope in a notebook.
# MAGIC ```
# MAGIC db_instance = dbutils.secrets.get(scope="<your-scope>", key=db_instance)
# MAGIC db_token = dbutils.secrets.get(scope="<your-scope>", key=db_token)
# MAGIC ```
# MAGIC The values fetched from the scope are never displayed in the notebook (see [Secret redaction](https://docs.databricks.com/security/secrets/redaction.html)).

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
