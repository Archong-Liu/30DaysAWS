from aws_cdk import (
    Stack,
    aws_s3 as s3,     # 因為我們想要部署S3，所以需要import aws_s3
)
from constructs import Construct

class MyCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
    
        MyL1Bucket = s3.CfnBucket(
            self,
            "MyL1Bucket",
            bucket_name="my-30daysaws-example-l1bucket",
            versioning_configuration={
                "status": "Enabled"
            }
        )

        MyL2Bucket = s3.Bucket(
            self,
            "MyL2Bucket",
            bucket_name="my-30daysaws-example-l2bucket",
            versioned=True,
        )