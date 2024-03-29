# GPT-2 SageMaker Deployment

## Overview

This project orchestrates the seamless deployment of a pre-trained GPT-2 model from the Hugging Face model hub onto Amazon SageMaker, enabling real-time inference. By leveraging AWS S3 for model storage and integrating the endpoint with AWS Lambda function and API Gateway, this deployment ensures efficient and scalable model serving.

## Architecture for MLOps Pipeline

<img src="https://github.com/Alpha-131/MLOps-Pipeline/assets/92028472/ac51219f-d2ba-40c3-a2b6-a3fb19cb3e54" width="800">

The MLOps pipeline architecture illustrates the flow of activities involved in deploying and managing machine learning models. This comprehensive workflow encompasses various stages, including data preparation, model training, deployment, monitoring, and maintenance. Each stage plays a crucial role in ensuring the successful and efficient operation of machine learning systems.

## Project Structure

- `data/`: Houses all project-related data.
- `model/`: Stores the GPT-2 model weights.
- `notebooks/`: Contains comprehensive experimentation notebooks.
- `scripts/`: Hosts Python scripts for seamless local and remote execution.
- `src/`: Organizes the model as a package along with associated modules.
- `tests/`: Comprises a suite of tests to ensure model robustness.
- `requirements.txt`: Lists all project dependencies for reproducibility.

## Usage (MLOps Pipeline)

1. **Clone Repository:**
    ```bash
    git clone https://github.com/Alpha-131/MYM-assessment-task.git
    ```

2. **Configure AWS Settings:**
    - Modify AWS configurations in relevant scripts to match project requirements.

3. **Upload Model to S3:**
    ```bash
    python upload_to_s3.py
    ```

4. **Deploy SageMaker Model:**
    ```bash
    python deploy_to_sagemaker.py
    ```

5. **Setup Lambda Function:**
    - Integrate the endpoint with a Lambda function for streamlined processing.

6. **API Gateway Configuration:**
    - Utilize API Gateway to create a production or testing stage, linking it with the Lambda function for seamless API access.

7. **Access API URL:**
    - Access the API URL for making model inference requests:
        ```
        https://<some_random_code>.execute-api.<region>.amazonaws.com/<stage_name>/<resource_name>
        ```

## Remaining Tasks
- [X] Download GPT-2 model weights.
- [X] Create model.tar.gz file for artifacts.
- [X] Upload model.tar.gz to Amazon S3.
- [X] Write deployment script for sagemaker endpoint.
- [X] Establish CI/CD pipeline for automated deployment.
- [X] Define YAML configuration file for CI/CD pipeline.
- [X] Implement monitoring using AWS Cloudwatch for sagemaker endpoint.
- [X] Implement logging using Cloudtrail and store it in S3 bucket for SageMaker endpoints.
- [ ] Configure autoscaling for dynamic traffic-based scaling.
