# db-glbt-migrator

## Introduction
This repository contains the solution to the code challenge related to building an API that executes some data related processes.

### Project structure
The repository is divided into this set of folders:

* **config/** All config files are placed into this folder (in this case, only environment variables file is placed here).
* **infra/** Terraform files are placed in this folder. These files are used to create the underlying infrastructure, such as the GCS Bucket, BigQuery Dataset, GCP project, etc.
* **migrations/** SQL files to create tables and load historic data into them.
* **scripts/** Shell scripts to run some utilitary processes, such as push to Artifactory, deploy new version into Cloud Run, et
* **src/** Source code related to the API

## Installation
In order to replicate the project, it is required to follow some steps:

* Set some required environment variables
```
export BILLING_ACCOUNT="<YOUR_GCP_BILLING_ACCOUNT>"
export PROJECT_ID="glbt-challenge-migrations"
export DATASET_ID="bq_glbt_migrator"
export TAG_NAME="<TAG_VERSION>"   # e.g. v0.0.1
```
* Run Terraform commands to create resources:
```
terraform init
terraform plan -var-file vars/prod.tfvars -var billing_account=$BILLING_ACCOUNT
terraform apply -var-file vars/prod.tfvars -var billing_account=$BILLING_ACCOUNT
```
* Set environment variable with the bucket created by Terraform:
```
export BUCKET_NAME="<YOUR_BUCKET_NAME>"
```
* Run script to upload csv files to GCS (scripts/upload_table_files.sh).
* Run migration scripts. These scripts can be run from the BigQuery console in GCP.
* Upload first Docker image version into GCP Artifactory (scripts/push_docker_version.sh).
* Deploy first version from the API in Cloud Run (scripts/deploy_cloud_run.sh).

**NOTE:**  Project ID and Dataset ID variable can be changed, but they also need to be modified into Terraform variables file.

## API endpoints
* /<table_name>/insert
* /<table_name>/backup
* /<table_name>/restore
* /metrics/report1
* /metrics/report2
   
