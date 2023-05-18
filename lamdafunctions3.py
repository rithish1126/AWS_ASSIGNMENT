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