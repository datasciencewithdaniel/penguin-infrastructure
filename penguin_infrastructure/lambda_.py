from aws_cdk import aws_lambda, aws_iam, aws_s3
from . import config
import os


def create_role(self):
    save_logs_role = aws_iam.Role(
        self,
        f"{config.SAVE_LOGS_NAME}-Role",
        assumed_by=aws_iam.ServicePrincipal("lambda.amazonaws.com"),
        role_name=f"{config.SAVE_LOGS_NAME}-Role",
    )
    save_logs_role.add_managed_policy(
        aws_iam.ManagedPolicy.from_aws_managed_policy_name(
            "service-role/AWSLambdaBasicExecutionRole"
        )
    )
    save_logs_role.add_managed_policy(
        aws_iam.ManagedPolicy.from_aws_managed_policy_name(
            "service-role/AWSLambdaVPCAccessExecutionRole"
        )
    )
    save_logs_role.add_managed_policy(
        aws_iam.ManagedPolicy.from_aws_managed_policy_name(config.SAVE_LOGS_S3_POLICY)
    )
    save_logs_role.attach_inline_policy(
        aws_iam.Policy(
            self,
            "penguin-ec2-access-policy",
            policy_name="penguin-ec2-access-policy",
            statements=[
                aws_iam.PolicyStatement(
                    actions=["ec2:*"],
                    resources=[f"arn:aws:ec2:*"],
                    effect=aws_iam.Effect.ALLOW,
                )
            ],
        )
    )
    return save_logs_role


def save_logs(self):
    save_logs_role = create_role(self)
    self.save_logs = aws_lambda.Function(
        self,
        config.SAVE_LOGS_NAME,
        runtime=aws_lambda.Runtime.PYTHON_3_9,
        handler="lambda_function.lambda_handler",
        code=aws_lambda.Code.from_asset(
            os.path.join(os.path.dirname(__file__), "lambda_save_logs")
        ),
        function_name=config.SAVE_LOGS_NAME,
        description="Lambda function to save Penguin Bot logs",
        role=save_logs_role,
    )


def create_logs_bucket(self):
    self.logs_bucket = aws_s3.Bucket(
        self,
        config.SAVE_LOGS_BUCKET,
        bucket_name=config.SAVE_LOGS_BUCKET,
        encryption=aws_s3.BucketEncryption.S3_MANAGED,
        versioned=True,
    )


def create_schedule_trigger(self):
    pass
