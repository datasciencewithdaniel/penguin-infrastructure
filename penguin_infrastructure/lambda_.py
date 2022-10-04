from aws_cdk import aws_lambda
from . import config
import os


def save_logs(self):
    self.save_logs = aws_lambda.Function(
        self,
        config.SAVE_LOGS_NAME,
        runtime=aws_lambda.Runtime.PYTHON_3_9,
        handler="lambda_function.lambda_handler",
        code=aws_lambda.Code.from_asset(
            os.path.join(os.path.dirname(__file__), "lambda_save_logs")
        ),
    )
