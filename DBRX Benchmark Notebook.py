# Databricks notebook source
# MAGIC %md
# MAGIC # DBRXの日本語ベンチマーク　〜JGLEU版〜

# COMMAND ----------

# MAGIC %md
# MAGIC ## ライブラリーインストール

# COMMAND ----------

# MAGIC %pip install -U transformers==4.39.2 tiktoken==0.6.0 torch==2.2.2 accelerate==0.28.0 hf_transfer==0.1.6
# MAGIC %pip install -e ".[ja]"
# MAGIC
# MAGIC dbutils.library.restartPython()
# MAGIC import os
# MAGIC os.environ['HF_HUB_ENABLE_HF_TRANSFER']="1"

# COMMAND ----------

# MAGIC %md
# MAGIC ## HuggingFaceへログイン

# COMMAND ----------

from huggingface_hub import notebook_login
notebook_login()

# COMMAND ----------

# MAGIC %md
# MAGIC ## DBRX-instructのベンチマーク実行

# COMMAND ----------

# MAGIC %sh
# MAGIC sh models/databricks/dbrx-instruct/harness.sh

# COMMAND ----------

# MAGIC %md
# MAGIC ## DBRX-baseのベンチマーク実行

# COMMAND ----------

# MAGIC %sh
# MAGIC sh models/databricks/dbrx-base/harness.sh

# COMMAND ----------


