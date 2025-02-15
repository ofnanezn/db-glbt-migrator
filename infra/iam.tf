resource "google_project_iam_member" "migrator-bq-user" {
  project = var.project_id
  role    = "roles/bigquery.jobUser"
  member  = "serviceAccount:${module.project.service_account_email}"
}