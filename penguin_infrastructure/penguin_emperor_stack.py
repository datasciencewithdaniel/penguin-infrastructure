from aws_cdk import Stack, Tags, aws_apigateway, aws_lambda, Duration
from constructs import Construct

import os
from . import config


class PenguinEmperorStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.scope = scope

        self.parameters()
        self.emperor_lambda()
        self.emperor_api()

        self.add_default_tags()

    def parameters(self):
        self.AWS_ACCOUNT = os.getenv("CDK_DEFAULT_ACCOUNT")
        self.AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
        self.AWS_ACCOUNT_DSWD = os.getenv("AWS_ACCOUNT_DSWD")
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        self.DISCORD_PENGUIN_PUBLIC_KEY = os.getenv("DISCORD_PENGUIN_PUBLIC_KEY")
        self.GUILD_NAME = os.getenv("GUILD_NAME")

        # self.BOT = os.getenv("BOT")
        # self.COMMAND = "run" if self.BOT == "0" else "run-baby"

    def add_default_tags(self):
        for name, value in config.DEFAULT_TAGS.items():
            Tags.of(self.scope).add(name, value)

    def emperor_api(self):
        api = aws_apigateway.LambdaRestApi(
            self,
            "emperor-api",
            handler=self.emperor_lambda_function,
            default_cors_preflight_options=aws_apigateway.CorsOptions(
                allow_origins=aws_apigateway.Cors.ALL_ORIGINS,
                allow_methods=aws_apigateway.Cors.ALL_METHODS,
            ),
        )

        method_response_200 = aws_apigateway.MethodResponse(status_code="200")
        method_response_401 = aws_apigateway.MethodResponse(status_code="401")

        event = api.root.add_resource("event")
        event.add_method(
            "POST",
            method_responses=[method_response_200, method_response_401],
            # request_models=
        )

        # response_model = api.add_model("ResponseModel",
        #     content_type="application/json",
        #     model_name="ResponseModel",
        #     schema=aws_apigateway.JsonSchema(
        #         schema=aws_apigateway.JsonSchemaVersion.DRAFT4,
        #         title="pollResponse",
        #         type=aws_apigateway.JsonSchemaType.OBJECT,
        #         properties={
        #             "state": aws_apigateway.JsonSchema(type=aws_apigateway.JsonSchemaType.STRING),
        #             "greeting": aws_apigateway.JsonSchema(type=aws_apigateway.JsonSchemaType.STRING)
        #         }
        #     )
        # )

        integration_response_401 = aws_apigateway.IntegrationResponse(
            status_code="401", selection_pattern="*[UNAUTHORIZED]*"
        )

    def emperor_lambda(self):
        self.pynacl_layer()
        self.emperor_lambda_function = aws_lambda.Function(
            self,
            "Emperor-Lambda",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            handler="emperor_lambda.lambda_handler",
            code=aws_lambda.Code.from_asset(
                os.path.join(
                    os.path.dirname(__file__), "lambda_functions/emperor_lambda"
                )
            ),
            function_name="Emperor-Lambda",
            description="Lambda function to process Discord commands",
            # role=save_logs_role, # FIX
            layers=[self.layer],
            # timeout=Duration.seconds(120),
        )

    def pynacl_layer(self, layer_name="Emperor-Layer-EC2", layer_version=1):
        self.layer = aws_lambda.LayerVersion.from_layer_version_arn(
            self,
            "PyNaCl-Layer",
            layer_version_arn=f"arn:aws:lambda:ap-southeast-2:{self.AWS_ACCOUNT}:layer:{layer_name}:{layer_version}",
        )
