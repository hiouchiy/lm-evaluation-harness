# Databricks notebook source
# MAGIC %md
# MAGIC # DBRXの日本語ベンチマーク　〜JGLEU版〜
# MAGIC
# MAGIC 環境
# MAGIC - Databricks Runtime: 14.3 LTS ML GPU
# MAGIC - ノートサイズ: Standard_NC96ads_A100_v4 (A100_80GB × 4)以上　（※RAMが270GBほど必要なため）

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
# MAGIC
# MAGIC 【**重要**】事前に下記のサイトにて利用申請フォームを提出いただく必要があります。
# MAGIC - DBRX-instruct: https://huggingface.co/databricks/dbrx-instruct
# MAGIC - DBRX-base: https://huggingface.co/databricks/dbrx-base
# MAGIC
# MAGIC その後にHuggigFaceのアカウント設定よりアクセストークンを発行し、下記コマンドにて表示されるログインフォームに入力ください。

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


