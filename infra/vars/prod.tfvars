project_id = "glbt-challenge-migrations"
service_name = "bq-glbt-migrator"
region = "us-central1"

activate_apis = [
    "bigquery.googleapis.com",
    "compute.googleapis.com",
    "artifactregistry.googleapis.com",
    "run.googleapis.com",
    "cloudscheduler.googleapis.com",
]