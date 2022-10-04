#!/usr/bin/env python3
import os

# from dotenv import load_dotenv

import aws_cdk as cdk

from penguin_infrastructure.penguin_infrastructure_stack import (
    PenguinInfrastructureStack,
)

app = cdk.App()
PenguinInfrastructureStack(
    app,
    "PenguinInfrastructureStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)

app.synth()
