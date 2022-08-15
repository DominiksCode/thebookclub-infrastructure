import sys
import os
from aws_cdk import (
    Stack,
    Environment
)

from .lib.cdn_stack import Hosting

from constructs import Construct

class TheBookClubStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        env = Environment(
            account=os.environ.get(
                "CDK_DEPLOY_ACCOUNT", os.environ.get("CDK_DEFAULT_ACCOUNT")
            ),
            region="eu-central-1"
        )
        hosting = Hosting(
            scope=self,
            construct_id=f"thebookclubinfrastructure-stack",
            env=env,
            description="Hosting to host static http files",
        )