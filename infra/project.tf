# module to create GCP project
module "project" {
  source            = "terraform-google-modules/project-factory/google"
  version           = "~> 13.0"
  random_project_id = "false"
  name              = var.project_id
  project_id        = var.project_id
  project_sa_name   = var.service_name
  activate_apis     = var.activate_apis

  org_id          = null
  billing_account = var.billing_account
}