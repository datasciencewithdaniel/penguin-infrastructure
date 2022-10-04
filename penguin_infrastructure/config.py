VPC_NAME = "PenguinVPC"
VPC_CIDR = "10.0.0.0/16"

SECURITY_GROUP_NAME = "PenguinSG"

BOT_ROLE_NAME = "Bot-Role"
SSM_POLICY_NAME = "AmazonSSMManagedInstanceCore"
DSWD_ACCESS_ROLE = "penguin-dynamodb-role"

INSTANCE_NAME = "PenguinBot"
INSTANCE_TYPE = "t2.micro"
INSTANCE_AMI = "ami-09a5c873bc79530d9"

SAVE_LOGS_NAME = "PenguinSaveLogs"

DEFAULT_TAGS = {
    "Project": "Penguin",
    "Organisation": "Data Science with Daniel",
    "Environment": "Development",
    "Deployment": "CDK-Python",
    "Author": "Daniel Chegwidden",
}
