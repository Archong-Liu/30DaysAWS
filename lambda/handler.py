import json
import os

def handler(event, context):
    bucket_name = os.environ.get("BUCKET_NAME", "")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "message": "Hello from Lambda via API Gateway!",
            "bucket": bucket_name,
            "event": event,
        }),
    } 