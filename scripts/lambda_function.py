import json
import os
import boto3

def lambda_handler(event, context):
    try:
        # Extract input text and parameters from the Lambda event
        input_text = event['inputs']
        parameters = event['parameters']

        # Call the SageMaker endpoint for inference
        sagemaker_client = boto3.client('sagemaker-runtime')
        endpoint_name = os.environ["SAGEMAKER_ENDPOINT"]  # Replace with your actual SageMaker endpoint name

        # Construct the request payload
        request_payload = {
            'inputs': input_text,
            'parameters': parameters
        }

        response = sagemaker_client.invoke_endpoint(
            EndpointName=endpoint_name,
            Body=json.dumps(request_payload),
            ContentType='application/json',
            Accept='application/json'
        )

        # Parse the SageMaker response
        result = json.loads(response['Body'].read().decode('utf-8'))
        
        # Store captured data in S3 bucket
        capture_data_in_s3(event)

        # Prepare the JSON response for Lambda
        response_payload = {
            'statusCode': 200,
            'body': json.dumps(result),
            'headers': {
                'Content-Type': 'application/json',
            },
        }

    except Exception as e:
        # Handle any errors
        response_payload = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Content-Type': 'application/json',
            },
        }

    return response_payload


def capture_data_in_s3(event):
    #Extract captured data from the event payload
    captured_data = event.get('capture_data')  # Modify this based on the actual structure of the captured data

    # Store captured data in an S3 bucket
    s3_client = boto3.client('s3')
    bucket_name = 's3://sagemaker-ap-south-1-219289179534/models/logs/'  # Replace with your S3 bucket name
    key = 'captured_data.json'  # Replace with the desired key for the S3 object

    s3_client.put_object(
        Body=json.dumps(captured_data),
        Bucket=bucket_name,
        Key=key
    )

    print('Captured data stored in S3 successfully.')