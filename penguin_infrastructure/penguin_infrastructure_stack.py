from aws_cdk import Stack, Tags
from constructs import Construct

import os
from . import config, networking, iam, compute


class PenguinInfrastructureStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.scope = scope

        self.parameters()
        networking.create_vpc(self)
        networking.create_security_group(self)
        iam.create_role(self)
        compute.create_user_data(self)
        compute.create_instance(self)
        self.add_default_tags()

    def parameters(self):
        self.AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
        self.AWS_ACCOUNT_DSWD = os.getenv("AWS_ACCOUNT_DSWD")
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        self.GUILD_NAME = os.getenv("GUILD_NAME")

    def add_default_tags(self):
        for name, value in config.DEFAULT_TAGS.items():
            Tags.of(self.scope).add(name, value)

    # def create_vpc(self):
    #     self.vpc = aws_ec2.Vpc(
    #         self, config.VPC_NAME, cidr=config.VPC_CIDR, vpc_name=config.VPC_NAME
    #     )

    # def create_security_group(self):
    #     self.security_group = aws_ec2.SecurityGroup(
    #         self,
    #         config.SECURITY_GROUP_NAME,
    #         vpc=self.vpc,
    #         allow_all_outbound=True,
    #         security_group_name=config.SECURITY_GROUP_NAME,
    #     )
    #     self.security_group.add_ingress_rule(
    #         peer=aws_ec2.Peer.ipv4("0.0.0.0/0"),
    #         description="inbound SSH",
    #         connection=aws_ec2.Port.tcp(22),
    #     )

    # def create_role(self):
    #     self.bot_role = aws_iam.Role(
    #         self,
    #         config.BOT_ROLE_NAME,
    #         assumed_by=aws_iam.ServicePrincipal("ec2.amazonaws.com"),
    #         role_name=config.BOT_ROLE_NAME,
    #     )
    #     self.bot_role.add_managed_policy(
    #         aws_iam.ManagedPolicy.from_aws_managed_policy_name(config.SSM_POLICY_NAME)
    #     )
    #     self.bot_role.add_managed_policy(
    #         aws_iam.ManagedPolicy.from_aws_managed_policy_name(
    #             config.DYNAMODB_POLICY_NAME
    #         )
    #     )

    # def create_user_data(self):
    #     self.user_data = aws_ec2.UserData.for_linux()
    #     self.user_data.add_commands("apt-get update -y")
    #     self.user_data.add_commands("apt-get upgrade -y")
    #     self.user_data.add_commands("apt install make -y")
    #     self.user_data.add_commands("apt install python3-pip -y")
    #     self.user_data.add_commands(
    #         "git clone -b develop --single-branch https://github.com/datasciencewithdaniel/penguin.git"
    #     )
    #     self.user_data.add_commands(
    #         f"cd penguin && sudo python3 -m pip install -r requirements.txt && sudo python3 -m bot.penguin --bot 1 --discord {self.discord_token} --guild '{self.guild_name}'"
    #     )

    # def create_instance(self):
    #     instance_type = aws_ec2.InstanceType(config.INSTANCE_TYPE)
    #     ami_image = aws_ec2.MachineImage().generic_linux(
    #         {"ap-southeast-2": "ami-09a5c873bc79530d9"}
    #     )  # .latest_amazon_linux()
    #     # with open("./penguin_infrastructure/user-data.sh") as file:
    #     #     user_data = file.read()

    #     self.instance = aws_ec2.Instance(
    #         self,
    #         "ec2-instance",
    #         instance_name=config.INSTANCE_NAME,
    #         instance_type=instance_type,
    #         machine_image=ami_image,
    #         vpc=self.vpc,
    #         security_group=self.security_group,
    #         role=self.bot_role,
    #         user_data=aws_ec2.UserData.custom(self.user_data.render()),
    #     )
