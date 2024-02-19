#######################################################################################################################################
### Realtime Inference


# import boto3
# import sagemaker
# from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri
# import time
# import os 

# def setup_cloudtrail(region, trail_name, s3_bucket_name):
#     # Create a CloudTrail client
#     cloudtrail_client = boto3.client('cloudtrail', region_name=region)

#     try:
#         # Attempt to create the trail
#         response = cloudtrail_client.create_trail(
#             Name=trail_name,
#             S3BucketName=s3_bucket_name
#         )
#         print("CloudTrail trail created.")
#     except cloudtrail_client.exceptions.TrailAlreadyExistsException:
#         # If the trail already exists, just print a message
#         print("CloudTrail trail already exists.")
    
#     try:
#         # Specify event selectors to filter the events captured by the trail
#         event_selectors = {
#             'ReadWriteType': 'All',
#             'IncludeManagementEvents': True,
#             'DataResources': [
#                 {
#                     'Type': 'AWS::SageMaker::Endpoint',
#                     'Values': ['*']
#                 }
#             ]
#         }

#         # Update the trail to include event selectors
#         cloudtrail_client.update_trail(
#             Name=trail_name,
#             EventSelectors=[event_selectors]
#         )

#         # Start logging
#         cloudtrail_client.start_logging(Name=trail_name)
#         print("Logging started for CloudTrail trail.")
#     except Exception as e:
#         print(f"Error updating CloudTrail trail: {e}")


# def deploy_to_sagemaker(model_s3_uri, role_arn, instance_type, region, capture_s3_uri):
#     # Set up CloudTrail
#     place = region
#     # setup_cloudtrail(place, "sagemaker-cloudtrail", capture_s3_uri.split('/')[2])

#     # Create a SageMaker client
#     sagemaker_client = boto3.client('sagemaker', region_name=region)
    
#     image_uri = get_huggingface_llm_image_uri(backend="huggingface", region=region)
    
#     model_name = "gpt-2-model"

#     hub = {
#         "HF_MODEL_ID": "gpt2", 
#         "HF_TASK": "text-generation",
#     }

#     huggingface_model = HuggingFaceModel(
#         model_data=model_s3_uri,
#         name=model_name, 
#         env=hub, 
#         role=role_arn, 
#         image_uri=image_uri
#     )
    
#     data_capture_config = sagemaker.model_monitor.DataCaptureConfig(
#         enable_capture=True,
#         sampling_percentage=100,
#         destination_s3_uri=capture_s3_uri
#     )
    
#     # Deploy the model to create a SageMaker endpoint
#     huggingface_model.deploy(
#         initial_instance_count=1,
#         instance_type=instance_type,
#         endpoint_name="gpt-2-model-endpoint-realtime-inference",  # Replace with your desired endpoint 
#         data_capture_config=data_capture_config  # Pass data capture config
#     )  
    
#     # Wait for the endpoint to be in service
#     endpoint_status = None
#     while endpoint_status != 'InService':
#         response = sagemaker_client.describe_endpoint(EndpointName="gpt-2-model-endpoint-realtime-inference")
#         endpoint_status = response["EndpointStatus"]
#         time.sleep(120)  # Wait for 120 seconds before checking again
    
#     print("SageMaker Endpoint is now in service.")
    
#     # # Configure CloudWatch to monitor the endpoint
#     # cloudwatch_client = boto3.client('cloudwatch')
#     # cloudwatch_client.put_metric_alarm(
#     #     AlarmName='YourEndpointHealthAlarm',
#     #     ComparisonOperator='GreaterThanThreshold',
#     #     EvaluationPeriods=1,
#     #     MetricName='CPUUtilization',
#     #     Namespace='AWS/SageMaker',
#     #     Period=60,
#     #     Statistic='Average',
#     #     Threshold=70.0,
#     #     ActionsEnabled=False,
#     #     AlarmDescription='Alarm when CPU utilization exceeds 70%',
#     #     Dimensions=[
#     #         {
#     #             'Name': 'EndpointName',
#     #             'Value': 'gpt-2-model-endpoint-realtime-inference'
#     #         },
#     #     ],
#     #     Unit='Percent'
#     # )
    
#     # print("CloudWatch monitoring configured.")
    
#     # # Set up a CloudWatch event rule to trigger storing the metrics in S3 periodically
#     # cloudwatch_events_client = boto3.client('events')

#     # response = cloudwatch_events_client.put_rule(
#     #     Name='CaptureDataToS3Rule',
#     #     ScheduleExpression='rate(5 minutes)',  # Adjust the schedule as needed
#     #     State='ENABLED'
#     # )

#     # cloudwatch_events_client.put_targets(
#     #     Rule='CaptureDataToS3Rule',
#     #     Targets=[
#     #         {
#     #             'Id': '1',
#     #             'Arn': 'arn:aws:lambda:ap-south-1:219289179534:function:gpt-2-model-lambda'  # Replace with your Lambda function ARN
#     #         },
#     #     ]
#     # )
    
#     # print("CloudWatch event rule set up.")

#     # Return the endpoint name for reference
#     return "gpt-2-model-endpoint-realtime-inference"

# if __name__ == "__main__":
#     # Set your model S3 URI, SageMaker role, instance type, region, and capture S3 URI
#     model_s3_uri = "s3://sagemaker-ap-south-1-219289179534/models/gpt_2/gpt2_model.tar.gz"
#     role_arn = "arn:aws:iam::219289179534:role/service-role/AmazonSageMaker-ExecutionRole-20240118T015346"
#     instance_type = "ml.m5.xlarge"  
#     region = "ap-south-1"
#     capture_s3_uri = "s3://sagemaker-ap-south-1-219289179534/models/logs/"  # Replace with your capture bucket

#     os.environ["HF_TASK"] = "text-generation"
    
#     # Deploy the GPT-2 model to SageMaker
#     endpoint_name = deploy_to_sagemaker(model_s3_uri, role_arn, instance_type, region, capture_s3_uri)
#     print("SageMaker Endpoint Name:", endpoint_name)



########################################################################################################################################
### Serverless Inference
### This has some error as of right now will fix it later.

# import boto3
# import sagemaker
# from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri
# import time

# def sagemaker_session():
#     sagemaker_session = sagemaker.Session()
#     region = sagemaker_session.boto_region_name
#     # role = sagemaker.get_execution_role()
    
#     return sagemaker_session, region

# # def retrieve_huggingface_image_uri(pytorch_version, transformers_version, py_version):
# #     region = boto3.session.Session().region_name
# #     image_uri = sagemaker.image_uris.retrieve(
# #         framework='huggingface',
# #         base_framework_version=f'pytorch{pytorch_version}',
# #         region=region,
# #         version=transformers_version,
# #         py_version=py_version,
# #         instance_type='ml.m5.xlarge',   # No GPU support on serverless inference
# #         image_scope='inference'
# #     )
# #     return image_uri

# def retrieve_huggingface_image_uri(region, backend = "huggingface"):
#     return get_huggingface_llm_image_uri(backend="huggingface", region=region)

# def create_sagemaker_model(model_name, sagemaker_role, container_image_uri, model_url):
#     client = boto3.client('sagemaker', region_name=boto3.Session().region_name)

#     # Create the model
#     create_model_response = client.create_model(
#         ModelName=model_name,
#         ExecutionRoleArn=sagemaker_role,
#         Containers=[{
#             'Image': container_image_uri,
#             'Mode': 'SingleModel',
#             'ModelDataUrl': model_url,
#         }]
#     )

#     return create_model_response['ModelArn']

# def create_endpoint_config(endpoint_config_name, model_name, serverless_config):
#     client = boto3.client('sagemaker', region_name=boto3.Session().region_name)

#     # Create an endpoint configuration
#     create_endpoint_config_response = client.create_endpoint_config(
#         EndpointConfigName=endpoint_config_name,
#         ProductionVariants=[{
#             'ModelName': model_name,
#             'VariantName': 'AllTraffic',
#             'ServerlessConfig': serverless_config,
#         }]
#     )

#     return create_endpoint_config_response['EndpointConfigArn']

# def create_sagemaker_endpoint(endpoint_name, endpoint_config_name):
#     client = boto3.client('sagemaker', region_name=boto3.Session().region_name)

#     # Create an endpoint
#     create_endpoint_response = client.create_endpoint(
#         EndpointName=endpoint_name,
#         EndpointConfigName=endpoint_config_name
#     )

#     return create_endpoint_response['EndpointArn']

# if __name__ == "__main__":
#     # Specify your details
#     model_name = 'gpt-2'
#     sagemaker_role = 'arn:aws:iam::219289179534:role/service-role/AmazonSageMaker-ExecutionRole-20240118T015346'
#     model_url = 's3://sagemaker-ap-south-1-219289179534/models/gpt_2/gpt2_model.tar.gz'
#     pytorch_version = '1.7.1'
#     transformers_version = '4.6.1'
#     py_version = 'py36'
#     backend = "huggingface"
#     sagemaker_session, region = sagemaker_session()
#     print("REGION ========", region)
    
#     container_image_uri = retrieve_huggingface_image_uri(region, backend)
    
#     serverless_config = {
#         'MemorySizeInMB': 3072,
#         'MaxConcurrency': 1,
#     }
    
#     endpoint_config_name = 'gpt-2-model-endpoint-config'
#     endpoint_name = 'gpt-2-model-endpoint'

#     # Create SageMaker Model
#     model_arn = create_sagemaker_model(model_name, sagemaker_role, container_image_uri, model_url)

#     # Create SageMaker Endpoint Configuration
#     endpoint_config_arn = create_endpoint_config(endpoint_config_name, model_name, serverless_config)

#     # Create SageMaker Endpoint
#     endpoint_arn = create_sagemaker_endpoint(endpoint_name, endpoint_config_name)

#     print("SageMaker Model ARN:", model_arn)
#     print("SageMaker Endpoint Configuration ARN:", endpoint_config_arn)
#     print("SageMaker Endpoint ARN:", endpoint_arn)


#######################################################################################################################################
#### TEST :

import boto3
import sagemaker
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri
import time
import os 

def setup_cloudtrail(region, trail_name, s3_bucket_name):
    #Create a CloudTrail client
    cloudtrail_client = boto3.client('cloudtrail', region_name=region)

    try:
        # Attempt to create the trail
        response = cloudtrail_client.create_trail(
            Name=trail_name,
            S3BucketName=s3_bucket_name
        )
        print("CloudTrail trail created.")
    except cloudtrail_client.exceptions.TrailAlreadyExistsException:
        # If the trail already exists, just print a message
        print("CloudTrail trail already exists.")
    
    try:
        # Specify event selectors to filter the events captured by the trail
        event_selectors = {
            'ReadWriteType': 'All',
            'IncludeManagementEvents': True,
            'DataResources': [
                {
                    'Type': 'AWS::SageMaker::Endpoint',
                    'Values': ['*']
                }
            ]
        }

        # Update the trail to include event selectors
        cloudtrail_client.put_event_selectors(
            TrailName=trail_name,
            EventSelectors=[event_selectors]
        )

        # Start logging
        cloudtrail_client.start_logging(Name=trail_name)
        print("Logging started for CloudTrail trail.")
    except Exception as e:
        print(f"Error updating CloudTrail trail: {e}")

def deploy_to_sagemaker(model_s3_uri, role_arn, instance_type, region, capture_s3_uri):
    # Set up CloudTrail
    place = region
    setup_cloudtrail(place, "sagemaker-cloudtrail", capture_s3_uri.split('/')[2])

    # Create a SageMaker client
    sagemaker_client = boto3.client('sagemaker', region_name=region)
    
    image_uri = get_huggingface_llm_image_uri(backend="huggingface", region=region)
    
    model_name = "gpt-2-model"

    hub = {
        "HF_MODEL_ID": "gpt2", 
        "HF_TASK": "text-generation",
    }

    huggingface_model = HuggingFaceModel(
        model_data=model_s3_uri,
        name=model_name, 
        env=hub, 
        role=role_arn, 
        image_uri=image_uri
    )
    
    data_capture_config = sagemaker.model_monitor.DataCaptureConfig(
        enable_capture=True,
        sampling_percentage=100,
        destination_s3_uri=capture_s3_uri
    )
    
    # Deploy the model to create a SageMaker endpoint
    huggingface_model.deploy(
        initial_instance_count=1,
        instance_type=instance_type,
        endpoint_name="gpt-2-model-endpoint-realtime-inference",  # Replace with your desired endpoint 
        data_capture_config=data_capture_config  # Pass data capture config
    )  
    
    # Wait for the endpoint to be in service
    endpoint_status = None
    while endpoint_status != 'InService':
        response = sagemaker_client.describe_endpoint(EndpointName="gpt-2-model-endpoint-realtime-inference")
        endpoint_status = response["EndpointStatus"]
        time.sleep(120)  # Wait for 120 seconds before checking again
    
    print("SageMaker Endpoint is now in service.")
    
    # Configure CloudWatch to monitor the endpoint
    cloudwatch_client = boto3.client('cloudwatch')
    response = cloudwatch_client.put_metric_alarm(
        AlarmName='YourEndpointHealthAlarm',
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        MetricName='CPUUtilization',
        Namespace='/aws/sagemaker/Endpoints',
        Period=300,  # Period should match the evaluation period (5 minutes)
        Statistic='Maximum',
        Threshold=70.0,
        ActionsEnabled=False,
        AlarmDescription='Alarm when CPU utilization exceeds 70%',
        Dimensions=[
            {
                'Name': 'EndpointName',
                'Value': 'gpt-2-model-endpoint-realtime-inference'
            },
            {
                'Name': 'VariantName',
                'Value': 'AllTraffic'
            }
        ],
        Unit='Percent'
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("CloudWatch alarm created:", response['ResponseMetadata']['HTTPStatusCode'])
    else: 
        print("Error creating CloudWatch alarm. Response from AWS was: ", response)
    
    # Set up a CloudWatch event rule to trigger storing the metrics in S3 periodically
    cloudwatch_events_client = boto3.client('events')

    response = cloudwatch_events_client.put_rule(
        Name='CaptureDataToS3Rule',
        ScheduleExpression='rate(5 minutes)',  # Adjust the schedule as needed
        State='ENABLED'
    )

    cloudwatch_events_client.put_targets(
        Rule='CaptureDataToS3Rule',
        Targets=[
            {
                'Id': '1',
                'Arn': 'arn:aws:lambda:ap-south-1:219289179534:function:gpt-2-model-lambda'  # Replace with your Lambda function ARN
            },
        ]
    )
    
    print("CloudWatch event rule set up.")

    # Return the endpoint name for reference
    return "gpt-2-model-endpoint-realtime-inference"

if __name__ == "__main__":
    # Set your model S3 URI, SageMaker role, instance type, region, and capture S3 URI
    model_s3_uri = "s3://sagemaker-ap-south-1-219289179534/models/gpt_2/gpt2_model.tar.gz"
    role_arn = "arn:aws:iam::219289179534:role/service-role/AmazonSageMaker-ExecutionRole-20240118T015346"
    instance_type = "ml.m5.xlarge"  
    region = "ap-south-1"
    capture_s3_uri = "s3://sagemaker-ap-south-1-219289179534/models/logs/"  # Replace with your capture bucket

    os.environ["HF_TASK"] = "text-generation"
    
    # Deploy the GPT-2 model to SageMaker
    endpoint_name = deploy_to_sagemaker(model_s3_uri, role_arn, instance_type, region, capture_s3_uri)
    print("SageMaker Endpoint Name:", endpoint_name)

