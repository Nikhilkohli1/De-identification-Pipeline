# De-identification-Pipeline

## Task 1 - Anonymization/Deindentification using AWS 


We’ll demonstrate how you can use a combination of Amazon Comprehend Medical, AWS Step Functions, and Amazon DynamoDB to identify sensitive health data and help support your compliance objectives

The architecture
This architecture uses the following services:

1. Amazon Comprehend Medical to identify entities within a body of text
2. AWS Step Functions and AWS Lambda to coordinate and execute the workflow
3. Amazon DynamoDB to store the de-identified mapping

![arch](https://github.com/Nikhilkohli1/De-identification-Pipeline/blob/main/Task%201%20-%20aws/identify-sensitive-data-1.gif)

Output Flow for Anonymization and Deidentification

![anonymize](https://github.com/Nikhilkohli1/De-identification-Pipeline/blob/main/Task%201%20-%20aws/anonymize.png)

![deiden](https://github.com/Nikhilkohli1/De-identification-Pipeline/blob/main/Task%201%20-%20aws/deidentify.png)


## Task 3 - Deidentification using GCP 

 This is a reference implementation of an end to end data tokenization solution designed to migrate sensitive data in BigQuery.

![pipe](https://github.com/Nikhilkohli1/De-identification-Pipeline/blob/main/Task%203%20-%20gcp/edp%202.png)

![pipe2](https://github.com/Nikhilkohli1/De-identification-Pipeline/blob/main/Task%203%20-%20gcp/edp%203.png)
