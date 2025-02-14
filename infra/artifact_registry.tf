resource "google_artifact_registry_repository" "migration-repo" {
  location      = var.region
  repository_id = "${var.service_name}-images"
  description   = "Repository to store docker images for migration service"
  format        = "DOCKER"
}

resource "google_artifact_registry_repository_iam_member" "default-sa-writer" {
  location   = var.region
  repository = google_artifact_registry_repository.migration-repo.name
  role       = "roles/artifactregistry.writer"
  member     = "serviceAccount:${module.project.service_account_email}"
}