import json
import boto3

def lambda_handler(event, context):
    try:
        # Extract input text from the Lambda event
        input_text = event['inputText']

        # Call the SageMaker endpoint for inference
        sagemaker_client = boto3.client('sagemaker-runtime')
        endpoint_name = "gpt-2-model-endpoint-realtime-inference"  # Replace with your actual SageMaker endpoint name

        response = sagemaker_client.invoke_endpoint(
            EndpointName=endpoint_name,
            Body=json.dumps({"text": input_text}),
            ContentType='application/json',
            Accept='application/json'
        )

        # Parse the SageMaker response
        result = json.loads(response['Body'].read().decode('utf-8'))

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
