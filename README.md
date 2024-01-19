# GPT-2 SageMaker Deployment Pipeline

This repository contains scripts and configurations for deploying a GPT-2 model on Amazon SageMaker. The pipeline involves creating a SageMaker model, packaging it, and deploying it to an endpoint.

## Architecture Overview

The pipeline consists of the following steps:

1. **Download and Prepare the GPT-2 Model:**
   - Clone the GPT-2 model from the Hugging Face Hub.
   - Create a tar file containing the model artifacts.

2. **Upload Model to S3:**
   - Upload the tar file containing the GPT-2 model to an S3 bucket.
   - Check if the model already exists in S3 before uploading.

3. **Create SageMaker Model:**
   - Use SageMaker Hugging Face SDK to create a SageMaker model.
   - Specify the S3 location of the GPT-2 model.

4. **Deploy Model to SageMaker Endpoint:**
   - Deploy the created SageMaker model to a SageMaker endpoint.
   - Configure the environment and specify instance type.

5. **Testing the Deployed Model:**
   - Send a sample input to the deployed endpoint and receive predictions.

## Scripts

- `scripts/download_model.py`: Downloads the GPT-2 model from the Hugging Face Hub.
- `scripts/upload_to_s3.py`: Uploads the model to an S3 bucket.
- `scripts/deploy_to_sagemaker.py`: Creates a SageMaker model and deploys it to an endpoint.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
