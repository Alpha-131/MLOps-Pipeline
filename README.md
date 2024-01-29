# GPT-2 SageMaker Deployment

## Overview

This project involves deploying a pre-trained GPT-2 model from the Hugging Face model hub to Amazon SageMaker for real-time inference. The deployment process includes uploading the model weights to an AWS S3 bucket and integrating the endpoint with AWS Lambda function and API Gateway.

## Project Structure

- `data/`: Contains all the data used in the project.
- `model/`: Contains all the model weights.
- `notebooks/`: Contains all the experiments and work done on the model before deployment.
- `scripts/`: Contains Python scripts which run when a new change is made and committed. These files can be run individually on your local system using a CLI.
- `src/`: Contains the model as a package along with all the modules.
- `tests/`: Contains multiple tests depending on the requirements.
- `requirements.txt`: Lists all dependencies for the project.

## Usage (MLOps Pipeline)

1. Clone the GitHub repo:
    ```bash
    git clone https://github.com/Alpha-131/MYM-assessment-task.git
    ```
2. Change the AWS configurations inside all the scripts according to your needs.
3. Upload the GPT-2 model to an S3 bucket:
    ```bash
    python upload_to_s3.py
    ```
4. Set up the SageMaker model:
    ```bash
    python deploy_to_sagemaker.py
    ```
5. Setup the Lambda function and add the endpoint to it.
6. Use API Gateway to create a stage for production or testing. Add your Lambda function with all necessary execution roles.
7. You are ready to use the API URL now to send requests:
    ```
    https://<some_random_code>.execute-api.<region>.amazonaws.com/<stage_name>/<resource_name>
    ```

## Remaining Tasks
- [X] Downloaded the GPT-2 model
- [X] Created a model.tar.gz file for model artifacts
- [X] Uploaded model.tar.gz to Amazon S3
- [X] Investigate and resolve the error during endpoint inference.
- [ ] Set up a CI/CD pipeline for automated deployment.
- [ ] Write a YAML file for CI/CD pipeline configuration.
- [ ] Implement monitoring and logging for SageMaker endpoints.
- [ ] Configure autoscaling for dynamic scaling based on traffic.
