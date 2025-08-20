#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_cdk_project.my_cdk_project_stack import MyCdkProjectStack


app = cdk.App()
MyCdkProjectStack(app, "MyCdkProjectStack",
    env=cdk.Environment(account='390402542308', region='ap-east-2'),
    )

app.synth()
