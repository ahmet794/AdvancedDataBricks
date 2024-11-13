# Databricks notebook source
# MAGIC %run ./Classroom-Setup-04-Common

# COMMAND ----------

PIPELINE = "performance"
DA_photon = init_DA(PIPELINE)

# COMMAND ----------

PIPELINE = "performance_2"
DA_nonphoton = init_DA(PIPELINE)

# COMMAND ----------

notebooks = [
    "ADE 4.1 - Photon"
]
# DA.set_dlt_policy("DBAcademy DLT Photon")
DA_photon.configure_pipeline(configuration={"source": DA_photon.paths.stream_source}, notebooks=notebooks, photon=True)
DA_photon.conclude_setup()

None

# COMMAND ----------

notebooks = [
    "ADE 4.1 - NonPhoton"
]
# DA.set_dlt_policy("DBAcademy DLT Photon")
DA_nonphoton.configure_pipeline(configuration={"source": DA_nonphoton.paths.stream_source}, notebooks=notebooks, photon=False)
DA_nonphoton.conclude_setup()

None

