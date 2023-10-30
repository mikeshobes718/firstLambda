#!/usr/bin/env python3

import aws_cdk as cdk

from sqs_lambda_demo.sqs_lambda_demo_stack import SqsLambdaDemoStack


app = cdk.App()
SqsLambdaDemoStack(app, "SqsLambdaDemoStack")

app.synth()
