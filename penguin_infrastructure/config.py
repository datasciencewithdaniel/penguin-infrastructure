VPC_NAME = "PenguinVPC"
VPC_CIDR = "10.0.0.0/16"

SECURITY_GROUP_NAME = "PenguinSG"

SSM_ROLE_NAME = "SSM_Role"
SSM_POLICY_NAME = "AmazonSSMManagedInstanceCore"

INSTANCE_NAME = "PenguinBotDev"
INSTANCE_TYPE = "t2.micro"

DEFAULT_TAGS = {
    "Project": "Penguin",
    "Organisation": "Data Science with Daniel",
    "Environment": "Dev",
    "Deployment": "CDK-Python",
    "Author": "Daniel Chegwidden",
}
