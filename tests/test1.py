import json
import boto3

# Create a SageMaker Runtime client
sagemaker_runtime_client = boto3.client('sagemaker-runtime')

# Specify your input data
input_data = {
    "input_key": "We at matt young media, as an advertising and marketing",
    "TASK": "text-generation"  # Specify the appropriate task for your model
}

# Convert input data to JSON string
payload = json.dumps(input_data)

# Invoke the SageMaker endpoint
response = sagemaker_runtime_client.invoke_endpoint(
    EndpointName='gpt-2-model-endpoint-realtime-inference',
    Body=payload,
    ContentType='application/json'
)

# Process the response
result = response['Body'].read()
print(result)
