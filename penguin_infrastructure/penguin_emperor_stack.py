from aws_cdk import Stack, Tags, aws_apigateway, aws_lambda, Duration
from constructs import Construct

import os
from . import config


class PenguinEmperorStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.scope = scope

        self.emperor_lambda()
        self.emperor_api()

    def parameters(self):
        self.AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
        self.AWS_ACCOUNT_DSWD = os.getenv("AWS_ACCOUNT_DSWD")
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        self.DISCORD_PENGUIN_PUBLIC_KEY = os.getenv("DISCORD_PENGUIN_PUBLIC_KEY")
        self.GUILD_NAME = os.getenv("GUILD_NAME")

        self.BOT = os.getenv("BOT")
        self.COMMAND = "run" if self.BOT == "0" else "run-baby"

    def add_default_tags(self):
        for name, value in config.DEFAULT_TAGS.items():
            Tags.of(self.scope).add(name, value)

    def emperor_api(self):
        api = aws_apigateway.LambdaRestApi(
            self,
            "emperor-api",
            handler=self._emperor_lambda,
            default_cors_preflight_options=aws_apigateway.CorsOptions(
                allow_origins=aws_apigateway.Cors.ALL_ORIGINS,
                allow_methods=aws_apigateway.Cors.ALL_METHODS,
            ),
        )
        event = api.root.add_resource("event")
        event.add_method("POST")

    def emperor_lambda(self):
        self.pynacl_layer()
        self._emperor_lambda = aws_lambda.Function(
            self,
            "Emperor-Lambda",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            handler="emperor_lambda.lambda_handler",
            code=aws_lambda.Code.from_asset(
                os.path.join(os.path.dirname(__file__), "lambda_functions")
            ),
            function_name="Emperor-Lambda",
            description="Lambda function process Discord commands",
            # role=save_logs_role, # FIX
            layers=[self.layer],
            timeout=Duration.seconds(120),
        )

    def pynacl_layer(self):
        self.layer = aws_lambda.LayerVersion(
            self,
            "PyNaCl-Layer",
            code=aws_lambda.Code.from_asset(
                os.path.join(os.path.dirname(__file__), "lambda_functions/pynacl/")
            ),
            compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_9],
            description="PyNaCl Layer for Discord signature verification",
        )
