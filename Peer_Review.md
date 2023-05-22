# Arin's Approach (https://github.com/aroraarin/AWSAssignment/tree/main)
## Task 1
1)For the first question arin has also used awscli and has used commands to create a role "s3-role", then proceeds to attach s3 policy to this role to create s3 buckets in the subscequent steps,  assumes the role to create and run an ec2 instance and then makes a s3 bucket

## Task 2
2)Arin has also given some basic permissions to a role to run the lamda function, then has attached a cloudwatch trigger with a rule to run the python script thrice and then proceeded to get the cloudwatch logs as three files were being uploaded to the s3 bucket
## Task 3
3)For the third task arin has also used the lamda function and has added api triggers and has made api methods to take input and send requests and has tested it using Postman

# Dhruv's Approach (https://github.com/ds-cr/awsAssgn)
## Task 1
1) For the first question dhruv also, has used awscli to create a role "q1-s3-ec2-role-dhruv" , then proceeds to attach s3 policies to this role then proceeds to create and run an ec2 instance with this role , then makes an s3 bucket called "aws-assgn-q1-dhruv"

## Task 2
2) Dhruv has given some basic permissions(policies) like s3 bucket permissions, cloudwatch permissions etc to role associated to a lamda function that can run python scripts.Then has used the dump functions to dump files in the s3 bucket and has used cloudwatch rules to run the script 3 times and generates cloud watch logs

## Task 3
3)Dhruv has use awsapigateway triggers on his lamda function and has made a rest api to take parametrized inputs from user and return file names,This api was then deployed and the curl command was used by him to get output from the api
