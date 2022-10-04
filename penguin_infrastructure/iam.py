from aws_cdk import aws_iam
from . import config


def create_role(self):
    self.bot_role = aws_iam.Role(
        self,
        config.BOT_ROLE_NAME,
        assumed_by=aws_iam.ServicePrincipal("ec2.amazonaws.com"),
        role_name=config.BOT_ROLE_NAME,
    )
    self.bot_role.add_managed_policy(
        aws_iam.ManagedPolicy.from_aws_managed_policy_name(config.SSM_POLICY_NAME)
    )
    self.bot_role.attach_inline_policy(
        aws_iam.Policy(
            self,
            "dswd-dynamodb-access-policy",
            policy_name="dswd-dynamodb-access-policy",
            statements=[
                aws_iam.PolicyStatement(
                    actions=["sts:AssumeRole"],
                    resources=[
                        f"arn:aws:iam::{self.AWS_ACCOUNT_DSWD}:role/{config.DSWD_ACCESS_ROLE}"
                    ],
                    effect=aws_iam.Effect.ALLOW,
                )
            ],
        )
    )
