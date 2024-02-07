#######################################################################################################################################
### Realtime Inference

# import sagemaker
# from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri
# import time
# import os 

# def deploy_to_sagemaker(model_s3_uri, role_arn, instance_type):
#     # Create a SageMaker session
#     region = os.getenv('AWS_REGION')
#     sagemaker_session = sagemaker.Session()
#     # region = sagemaker_session.boto_region_name

#     image_uri = get_huggingface_llm_image_uri(backend="huggingface", region=region)
    
#     model_name = "gpt-2-model"

#     hub = {
#         "HF_MODEL_ID": "gpt2", 
#         "HF_TASK": "text-generation",
#     #     "SM_NUM_GPUS": "1",
#     }

#     huggingface_model = HuggingFaceModel(
#         model_data=model_s3_uri,
#         name=model_name, 
#         env=hub, 
#         role=role_arn, 
#         image_uri=image_uri
#     )
    
#     # # Create Hugging Face Model Class
#     # huggingface_model = HuggingFaceModel(
#     #     model_data=model_s3_uri,  # S3 path to your model
#     #     role=role_arn,  # IAM role with permissions to create an endpoint
#     #     sagemaker_session=sagemaker_session,
#     #     transformers_version="4.6",  # Transformers version used
#     #     pytorch_version="1.7",  # PyTorch version used
#     #     py_version='py36',  # Python version used
#     #     env={'HF_TASK': 'text-generation'}
#     # )

#     # Deploy the model to create a SageMaker endpoint
#     predictor = huggingface_model.deploy(
#         initial_instance_count=1,
#         instance_type=instance_type,
#         endpoint_name="gpt-2-model-endpoint-realtime-inference"  # Replace with your desired endpoint 
#     )  
    
#     pred = predictor.predict(
#         {
#         "inputs": "We at MYM as a advertising and marketing agency, ",
#         "parameters": {
#             "do_sample": True,
#             "max_new_tokens": 100,
#             "temperature": 0.7,
#             "num_beams": 5,
#         },
#     })
#     print(pred)
    
#     # Return the endpoint name for reference
#     return huggingface_model.endpoint_name

# if __name__ == "__main__":
#     # Set your model S3 URI, SageMaker role, and instance type
#     model_s3_uri = "s3://sagemaker-ap-south-1-219289179534/models/gpt_2/gpt2_model.tar.gz"
#     # model_s3_uri = "s3://sagemaker-ap-south-1-219289179534/models/model.tar.gz"
#     role_arn = "arn:aws:iam::219289179534:role/service-role/AmazonSageMaker-ExecutionRole-20240118T015346"
#     instance_type = "ml.m5.xlarge"  # Eligible for the AWS Free Tier

#     os.environ["HF_TASK"] = "text-generation"
#     # Deploy the GPT-2 model to SageMaker
#     endpoint_name = deploy_to_sagemaker(model_s3_uri, role_arn, instance_type)
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
##### TEST :

import boto3
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri
import time
import os 

def deploy_to_sagemaker(model_s3_uri, role_arn, instance_type, region):
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
    
    # Deploy the model to create a SageMaker endpoint
    huggingface_model.deploy(
        initial_instance_count=1,
        instance_type=instance_type,
        endpoint_name="gpt-2-model-endpoint-realtime-inference"  # Replace with your desired endpoint 
    )  
    
    # Wait for the endpoint to be in service
    endpoint_status = None
    while endpoint_status != 'InService':
        response = sagemaker_client.describe_endpoint(EndpointName="gpt-2-model-endpoint-realtime-inference")
        endpoint_status = response["EndpointStatus"]
        time.sleep(10)  # Wait for 10 seconds before checking again
    
    print("SageMaker Endpoint is now in service.")
    
    # Return the endpoint name for reference
    return "gpt-2-model-endpoint-realtime-inference"

if __name__ == "__main__":
    # Set your model S3 URI, SageMaker role, instance type, and region
    model_s3_uri = "s3://sagemaker-ap-south-1-219289179534/models/gpt_2/gpt2_model.tar.gz"
    role_arn = "arn:aws:iam::219289179534:role/service-role/AmazonSageMaker-ExecutionRole-20240118T015346"
    instance_type = "ml.m5.xlarge"  # Eligible for the AWS Free Tier
    region = "ap-south-1"

    os.environ["HF_TASK"] = "text-generation"
    
    # Deploy the GPT-2 model to SageMaker
    endpoint_name = deploy_to_sagemaker(model_s3_uri, role_arn, instance_type, region)
    print("SageMaker Endpoint Name:", endpoint_name)














