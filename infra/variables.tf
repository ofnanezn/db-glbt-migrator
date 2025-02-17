variable "project_id" {
  type        = string
  description = "GCP project ID"
}

variable "region" {
  type        = string
  description = "Region in which resources will be created"
}

variable "service_name" {
  type        = string
  description = "Name of service that will be created"
}

variable "tables" {
  type        = list(string)
  description = "Challenge tables"
}

variable "activate_apis" {
  type        = list(string)
  description = "APIs that will be enabled in the project"
}

variable "billing_account" {
  type        = string
  description = "GCP billing account"
}