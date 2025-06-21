terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    bucket         = "mini-commerce-tf-state"     
    key            = "terraform/state.tfstate"    # Path inside the bucket
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"            # Optional but recommended
  }
}

provider "aws" {
  region = "us-east-1"
}
