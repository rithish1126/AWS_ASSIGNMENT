# AWS_ASSIGNMENT

## Question 1:

# 1) Create S3 bucket from AWS CLI
Downloaded "awscli" from https://aws.amazon.com/cli/
  ## a) Create an IAM role with s3 full access
  ```
  aws iam create-role --role-name rithishassignmentrole --assume-role-policy-document file://trust-policy.json
  ```
  ### Trust-policy.json
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
   }
  ```
  <img width="1010" alt="Screenshot 2023-05-17 at 11 52 19 PM" src="https://github.com/rithish1126/AWS_ASSIGNMENT/assets/122535424/b5692c70-5f77-459b-855e-756f219ab220">

  ## b) Create an EC2 instance with above role
  ### Attach role policy to the role created
  ```
  aws iam attach-role-policy --role-name rithishassignmentrole --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
  ```
  ###  Create an Instance
  ```
  aws iam create-instance-profile --instance-profile-name rithish_profile
  ```
  <img width="752" alt="Screenshot 2023-05-18 at 11 43 14 AM" src="https://github.com/rithish1126/AWS_ASSIGNMENT/assets/122535424/c4eb2c37-6ef2-4fe1-ad1f-d1dd3c213b69">

  ### Add role to instance
  ```
  aws iam add-role-to-instance-profile --instance-profile-name rithish_profile --role-name rithishassignmentrole
  ```
  ### run the instance
  ```
  aws ec2 run-instances --image-id ami-0a79730daaf45078a --instance-type t3.micro --key-name rithishkeypair --iam-instance-profile Name="rithish_profile" 
  ```
  <img width="1122" alt="Screenshot 2023-05-18 at 11 44 45 AM" src="https://github.com/rithish1126/AWS_ASSIGNMENT/assets/122535424/7942a2ae-4024-4e44-9667-4172dbe2a98e">
<img width="521" alt="Screenshot 2023-05-18 at 11 45 25 AM" src="https://github.com/rithish1126/AWS_ASSIGNMENT/assets/122535424/1648a689-da02-4d96-a175-677e8a3a3c28">

  ## c) Create a bucket from AWS CLI
  ```
  aws s3api create-bucket --bucket rithishbucket --region eu-north-1 --create-bucket-configuration LocationConstraint=eu-north-1 
  ```
  <img width="1126" alt="Screenshot 2023-05-18 at 11 46 23 AM" src="https://github.com/rithish1126/AWS_ASSIGNMENT/assets/122535424/f07bf1b8-43e1-4395-844d-9d60cecfc845">
  <img width="1036" alt="Screenshot 2023-05-18 at 11 46 53 AM" src="https://github.com/rithish1126/AWS_ASSIGNMENT/assets/122535424/eec0057b-59b2-4ad9-a86a-243bbb0b420f">
# 2) Put files from lamda to s3
  ## Create role to allow lamda function to create s3 buckets and enable cloudwatch to generate logs
  <img width="1102" alt="Screenshot 2023-05-18 at 12 08 26 PM" src="https://github.com/rithish1126/AWS_ASSIGNMENT/assets/122535424/1992acc2-e1cc-430b-b7fd-e3a8ff5afabf">
  ## Create rules to run every minute
<img width="1440" alt="Screenshot 2023-05-18 at 12 18 55 PM" src="https://github.com/rithish1126/AWS_ASSIGNMENT/assets/122535424/1156866a-097a-44e9-a616-4b45ebfbf1a7">

  ## Create a lamda function that accepts python code with the above role
  ```
  import boto3
import datetime, time
import json

s3 = boto3.resource('s3')

bucket_name = 'rithishbucket'
key_name = 'transaction{}.json'

cw_logs = boto3.client('logs')

counter=0
def set_concurrency_limit(function_name):
    lambda_client = boto3.client('lambda')
    response = lambda_client.put_function_concurrency(
        FunctionName=function_name,
        ReservedConcurrentExecutions=0
    )
    print(response)
def lambda_handler(event, context):
    global counter
    counter+=1
    try:

        transaction_id = 12345
        payment_mode = "card/netbanking/upi"
        Amount = 200.0
        customer_id = 101
        Timestamp = str(datetime.datetime.now())
        transaction_data = {
            "transaction_id": transaction_id,
            "payment_mode": payment_mode,
            "Amount": Amount,
            "customer_id": customer_id,
            "Timestamp": Timestamp
        }
        

        json_data = json.dumps(transaction_data)
        file_name = key_name.format(Timestamp.replace(" ", "_"))
        s3.Bucket(bucket_name).Object(file_name).put(Body=json_data)
        
        

        print(context)
        if counter==1:
            print('First execution')
        elif counter==2:
            print('Second execution')
        elif counter==3:
            print('Third execution')
            print('Stopping execution')
            set_concurrency_limit('rithishlamdafunction')
    except Exception as e:
        print(e)
  ```
  <img width="1071" alt="Screenshot 2023-05-18 at 12 16 09 PM" src="https://github.com/rithish1126/AWS_ASSIGNMENT/assets/122535424/8abd5a6b-2754-4286-8edc-ecc4ae168908">
  ## Creating Cloudwatch logs
  



  
 

   
