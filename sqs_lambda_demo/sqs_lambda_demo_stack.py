from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_sources
)

class SqsLambdaDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create our Queue
        queue = sqs.Queue(
            self, "SqsLambdaDemoQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # Create our Lambda Function
        sqs_lambda = _lambda.Function(
            self, "SQSLambda",
            handler="lambda_handler.handler",
            runtime=_lambda.Runtime.PYTHON_3_10,
            code=_lambda.Code.asset("lambda"),
        )

        # Create our event source
        sqs_event_source = lambda_event_sources.SqsEventSource(queue)

        # Add SQS event source to our Lambda Function
        sqs_lambda.add_event_source(sqs_event_source)