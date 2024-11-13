# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# DBTITLE 0,--i18n-1628b1a7-a52d-407f-a7ec-b457a9ecf7f7
# MAGIC %md
# MAGIC
# MAGIC
# MAGIC # Generate Tokens
# MAGIC In this lesson, you will generate a token and, which you will use throughout this module.
# MAGIC
# MAGIC By the end of this lesson, you should be able to:
# MAGIC * Generate credentials for working with the lessons in this module

# COMMAND ----------

# DBTITLE 0,--i18n-59694b00-5741-4284-986c-dbb5de1e9563
# MAGIC %md
# MAGIC ### Introduction
# MAGIC In the next few lessons, we are going to use the Databricks API and the Databricks CLI to run code from a terminal. Since we are in a learning environment, we are going to save a credentials file right here in the workspace. In the "real world" we recommend that you follow your organization's security policies for storing credentials.
# MAGIC * Run the classroom setup script in the next cell to configure the classroom
# MAGIC * Complete the steps below to generate credentials and save the credentials file.

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-06.1

# COMMAND ----------

# DBTITLE 0,--i18n-817102c0-1b8a-41c8-a24e-23fe66053a77
# MAGIC %md
# MAGIC ## Verify that Personal Access Token are enabled in the workspace
# MAGIC Steps:
# MAGIC 1. Click on your username in the top bar and select **Admin Settings** from the drop down menu.
# MAGIC 1. Click **Workspace Settings**.
# MAGIC 1. Enable **Personal Access Tokens** if it is not already enabled  
# MAGIC **NOTE:** If you are unable to access the Admin Settings, you may not be able to generate a PAT and complete the lessons in this module.

# COMMAND ----------

# DBTITLE 0,--i18n-1b6670fa-91ec-43a4-813c-b860ebc27b00
# MAGIC %md
# MAGIC ## Generate a token
# MAGIC Steps:
# MAGIC 1. Click on your username in the top bar and select **User Settings** from the drop down menu.
# MAGIC 1. Navigate to the **Access tokens** tab, click **Generate new token**, and configure your token as specified below.
# MAGIC
# MAGIC | Setting | Instructions |
# MAGIC |--|--|
# MAGIC | Comment | Enter "API/CLI Demo" |
# MAGIC | Lifetime | Optionally change the default lifetime for 90 days |
# MAGIC
# MAGIC <br>
# MAGIC
# MAGIC 3. Click the **Generate** button.
# MAGIC 4. Copy the displayed token (you will not be able to view the token again) and click **Done**.
# MAGIC
# MAGIC **NOTE:** If you lose the copied token, you cannot regenerate that exact same token. Instead, you must repeat this procedure to create a new token. 
# MAGIC
# MAGIC If you lose the copied token, Databricks recommends that you immediately delete that token from your workspace by clicking the **X** next to the token on the Access tokens tab. This token is just like a username and password. Treat it with the same security as other credentials.

# COMMAND ----------

# DBTITLE 0,--i18n-23f58b17-b0f7-4b75-a644-89561286a802
# MAGIC %md
# MAGIC
# MAGIC ## Save credentials
# MAGIC When you use the token in your own environment, you will want to follow the security practices of your organization. For the purpose of this demo, we are going to create a file that stores the token in the same directory as this notebook. 
# MAGIC
# MAGIC Steps:
# MAGIC 1. Copy and paste your **Personal Access Token** below and assign it to the variable `db_token`
# MAGIC 2. Copy and paste your workspace **Instance URL** below and assign it to the variable `db_instance`
# MAGIC    - In your browser's address bar, select just the portion of the address from "https:" to ".com"
# MAGIC    - Example `https://cust-success.cloud.databricks.com/`

# COMMAND ----------

# TODO
db_token = "FILL-IN"
db_instance = "FILL-IN"

# COMMAND ----------

# DBTITLE 0,--i18n-1bf1a2b7-432d-4501-a19e-8a7ab41f2815
# MAGIC %md
# MAGIC
# MAGIC Run the cell below to write your credentials to a file called `credentials.py`.

# COMMAND ----------

DA.create_credentials_file(db_token, db_instance)

# COMMAND ----------

# DBTITLE 0,--i18n-17b7606d-d121-4225-b737-60863dd436bc
# MAGIC %md
# MAGIC ### Conclusion
# MAGIC We will use the credential file in later lessons of this module.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
