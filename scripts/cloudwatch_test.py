import boto3

def create_cloudwatch_alarm():
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

    print("CloudWatch alarm created:", response['ResponseMetadata']['HTTPStatusCode'])

if __name__ == "__main__":
    create_cloudwatch_alarm()
