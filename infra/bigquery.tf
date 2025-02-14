resource "google_bigquery_dataset" "migrator-dataset-stg" {
  dataset_id                  = "${replace(var.service_name, "-", "_")}_stg"
  description                 = "Staging migration dataset"
  location                    = var.region
  default_table_expiration_ms = 86400000 # 1 day

  access {
    role          = "OWNER"
    user_by_email = module.project.service_account_email
  }
}

resource "google_bigquery_dataset" "migrator-dataset-tgt" {
  dataset_id  = "${replace(var.service_name, "-", "_")}_tgt"
  description = "Target migration dataset"
  location    = var.region

  access {
    role          = "OWNER"
    user_by_email = module.project.service_account_email
  }
}