# 🚀 AWS Serverless Data Pipeline

This project demonstrates a complete **event-driven serverless architecture** built using AWS services.

---

## 📌 Overview

The system processes data using AWS Lambda, stores it in DynamoDB, and handles failures using SQS (Dead Letter Queue). It also exposes an API using API Gateway.

---

## 🏗️ Architecture

[Architecture]<img width="903" height="514" alt="Screenshot 2026-04-22 at 6 47 08 PM" src="https://github.com/user-attachments/assets/cd61173a-2d72-4998-bb8f-cf6b47520033" />

---

## ⚙️ Services Used

- AWS Lambda (Processing logic)
- Amazon DynamoDB (Database)
- Amazon S3 (Event trigger simulation)
- Amazon SNS (Notifications)
- Amazon SQS (Failure handling / DLQ)
- Amazon API Gateway (REST API)
- Amazon CloudWatch (Monitoring & Logs)

---

## 🔄 Workflow

1. Data is triggered (via event/API)
2. Lambda processes the request
3. Data is stored in DynamoDB
4. If processing fails → message sent to SQS
5. Logs are captured in CloudWatch
6. API Gateway retrieves data via Lambda

---

## 📊 API Example

![API Output](screenshots/api-output.png)

---

## 🗄️ DynamoDB Data

![DynamoDB](screenshots/dynamodb.png)

---

## 📥 SQS Failure Queue

![SQS](screenshots/sqs.png)

---

## 📈 CloudWatch Logs

![CloudWatch](screenshots/cloudwatch.png)

---

## 🧪 Sample Lambda Code

```python
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UsersData')

def lambda_handler(event, context):
    try:
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
```

---

## 💡 Key Learnings

- Event-driven architecture design
- Serverless application development
- Error handling using SQS (DLQ)
- API integration with Lambda
- Monitoring using CloudWatch

---

## 🚀 Future Improvements

- Add authentication (JWT / Cognito)
- Implement CI/CD pipeline
- Add retry mechanisms with Step Functions
- Infrastructure as Code (Terraform / CloudFormation)

---

## 📌 Author

Nithin Rallapalli
