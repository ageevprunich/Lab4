terraform {
  required_version = ">=0.13.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS provider
provider "aws" {
  region     = "us-east-1"
}

resource "aws_security_group" "my-app" {
  name        = "my-app"
  description = "security group"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

 ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags= {
    Name = "my-app"
  }
}

resource "aws_instance" "myapp_instance" {
  ami           = "ami-0669b163befffbdfc"
  instance_type = "t2.micro"
  security_groups= ["my-app"]
  tags = {
    Name = "myapp_instance"
  }
}

output "instance_public_ip" {
  value     = aws_instance.myapp_instance.public_ip
  sensitive = true
}
