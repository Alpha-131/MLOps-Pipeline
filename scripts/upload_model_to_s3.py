# from transformers import GPT2LMHeadModel, GPT2Tokenizer
# import os
# import tarfile
# import boto3
# from botocore.exceptions import NoCredentialsError


# def upload_model_to_s3(model_path, s3_bucket, s3_key):
#     # Load the GPT-2 model and tokenizer
#     model = GPT2LMHeadModel.from_pretrained(model_path)
#     tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    
#     # Save the model locally
#     local_model_path = "../model/artifacts/gpt_2"  # Updated path based on your file structure
#     model.save_pretrained(local_model_path)
#     tokenizer.save_pretrained(local_model_path)

#     # Compress the saved model directory
#     with tarfile.open("gpt2_model.tar.gz", "w:gz") as tar:
#         tar.add(local_model_path, arcname=os.path.basename(local_model_path))
        
#     # Set your AWS credentials explicitly
#     aws_access_key_id = 'aws_access_key_id'
#     aws_secret_access_key = 'aws_secret_access_key'
#     aws_session_token = None  

#     # Create an S3 client and upload the compressed model
#     s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)
#     with open("gpt2_model.tar.gz", "rb") as data:
#         s3.upload_fileobj(data, s3_bucket, s3_key)

# if __name__ == "__main__":
#     # Set your S3 bucket and key
#     s3_bucket = "sagemaker-ap-south-1-219289179534"
#     s3_key = "models/gpt_2/gpt2_model.tar.gz"

#     # Set the relative path to your GPT-2 model
#     model_path = "model/gpt_2"

#     # Upload the GPT-2 model to S3
#     upload_model_to_s3(model_path, s3_bucket, s3_key)




import os
import tarfile
import boto3
from botocore.exceptions import NoCredentialsError

def upload_model_to_s3(model_dir, s3_bucket, s3_key):
    # Create a tarball of the gpt_2 directory
    with tarfile.open("gpt2_model.tar.gz", "w:gz") as tar:
        tar.add(model_dir, arcname=os.path.basename(model_dir))

    # Get AWS credentials from environment variables
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    aws_session_token = os.environ.get('AWS_SESSION_TOKEN')
    print(aws_access_key_id)

    # AWS credentials should be handled securely
    # Make sure to configure your credentials properly, e.g. using boto3 session or environment variables
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)
    with open("gpt2_model.tar.gz", "rb") as data:
        s3.upload_fileobj(data, s3_bucket, s3_key)

if __name__ == "__main__":
    # Define the local directory and S3 location
    model_dir = "model/gpt_2"  # Directory containing your model and code
    s3_bucket = "sagemaker-ap-south-1-219289179534"  # Your S3 bucket
    s3_key = "models/gpt_2/gpt2_model.tar.gz"  # S3 key for the tarball

    # Upload the model directory to S3
    upload_model_to_s3(model_dir, s3_bucket, s3_key)

