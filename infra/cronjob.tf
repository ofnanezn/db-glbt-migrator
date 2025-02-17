# Create a backup cronjob for each table
resource "google_cloud_scheduler_job" "table-backup" {
  for_each         = toset(var.tables)
  name             = "${each.value}-backup-scheduler"
  description      = "Cronjob to backup ${each.value}"
  schedule         = "0 0 * * *"
  time_zone        = "America/New_York"
  attempt_deadline = "300s"

  retry_config {
    retry_count = 1
  }

  http_target {
    http_method = "POST"
    uri         = "https://bq-glbt-migrator-508891629639.us-central1.run.app/${each.value}/backup"
  }
}