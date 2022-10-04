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
