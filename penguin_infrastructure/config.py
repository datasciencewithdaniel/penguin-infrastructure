VPC_NAME = "PenguinVPC"
VPC_CIDR = "10.0.0.0/16"

SECURITY_GROUP_NAME = "PenguinSG"

BOT_ROLE_NAME = "Bot_Role"
SSM_POLICY_NAME = "AmazonSSMManagedInstanceCore"
DYNAMODB_POLICY_NAME = "AmazonDynamoDBFullAccess"

INSTANCE_NAME = "PenguinBotDev"
INSTANCE_TYPE = "t2.micro"

DEFAULT_TAGS = {
    "Project": "Penguin",
    "Organisation": "Data Science with Daniel",
    "Environment": "Development",
    "Deployment": "CDK-Python",
    "Author": "Daniel Chegwidden",
}
