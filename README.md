# GPT-2 SageMaker Deployment

## Overview

This project demonstrates the deployment of a GPT-2 model on Amazon SageMaker using the Hugging Face Transformers library.

In this project, I utilized the Hugging Face Transformers library to directly download a pretrained GPT-2 model and tokenizer from the HF model hub. Rather than training and preprocessing, I leveraged the pretrained model directly.

The deployment process involves uploading the model artifacts to an S3 bucket and then deploying the model on Amazon SageMaker using the Hugging Face SageMaker SDK.

**Note:** While deploying, I encountered an error during the inference/prediction phase. Further investigation is needed to resolve this issue.

## Project Structure

- `upload_to_s3.py`: Script to upload GPT-2 model artifacts to an S3 bucket.
- `deploy_to_sagemaker.py`: Script to create a SageMaker model and deploy it using the Hugging Face SageMaker SDK.

## Usage

1. Run the `upload_to_s3.py` script to upload the GPT-2 model to an S3 bucket.
   ```bash
   python upload_to_s3.py
   ```

2. Set up your SageMaker model by running the `deploy_to_sagemaker.py` script.
   ```bash
   python deploy_to_sagemaker.py
   ```

## Remaining Tasks
- [X] Downloaded the GPT-2 model
- [X] Created a model.tar.gz file for model artifacts
- [X] Uploaded model.tar.gz to Amazon S3
- [ ] Investigate and resolve the error during endpoint inference.
- [ ] Set up a CI/CD pipeline for automated deployment.
- [ ] Write a YAML file for CI/CD pipeline configuration.
- [ ] Implement monitoring and logging for SageMaker endpoints.
- [ ] Configure autoscaling for dynamic scaling based on traffic.

