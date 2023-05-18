import boto3
import datetime
import json

s3 = boto3.resource('s3')
bucket_name = 'rithishbucket'
key_name = 'file{}.json'

def lambda_handler(event, context):
    try:

        body = event['body']
        timestamp = str(datetime.datetime.now())
        body["timestamp"] = timestamp
        

        json_data = json.dumps(body)
        file_name = key_name.format(timestamp.replace(" ", "_"))
        s3.Object(bucket_name, file_name).put(Body=json_data)


        print(f"Object created in S3 bucket {bucket_name}: {file_name}")

        return {
            "file_name": file_name,
            "status": "success"
        }

    except Exception as e:
        print(e)
        return {
            "status": e
        }
