# Add random suffix to minimize collition in bucket name
resource "random_string" "random-suffix" {
  length  = 2
  numeric = true
  lower   = true
  upper   = false
  special = false
}

resource "google_storage_bucket" "migrator-bucket" {
  name          = "${var.service_name}-${random_string.random-suffix.result}"
  location      = var.region
  force_destroy = true

  uniform_bucket_level_access = true
}

resource "google_storage_bucket_iam_member" "migrator-bucket-writer" {
  bucket = google_storage_bucket.migrator-bucket.name
  role   = "roles/storage.admin"
  member = "serviceAccount:${module.project.service_account_email}"
}