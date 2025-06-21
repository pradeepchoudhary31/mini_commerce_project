variable "ecr_repo_url" {
  description = "ECR image URL"
  type        = string
}

variable "db_name" {
  description = "db_name"
  type = string
  default = "items"
}

variable "db_username" {
  description = "db_username"
  type = string
  default = "admin"
}

