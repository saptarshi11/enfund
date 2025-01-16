# AWS Lambda Functions

This repository contains two AWS Lambda functions:
1. **Add Two Numbers**: A Lambda function to add two numbers and return the result.
2. **Store Document in S3**: A Lambda function to store a document or PDF file in an S3 bucket.

## Prerequisites
- An AWS account.
- AWS CLI installed and configured.
- Python installed locally for development.
- An S3 bucket created for storing files.

---

## 1. Add Two Numbers Lambda Function

### Description
This function takes two numbers (`num1` and `num2`) as input from the event and returns their sum.

### File: `lambda_function.py`

### Steps to Deploy and Test
1. **Create a Deployment Package**:
   ```bash
   zip function.zip lambda_function.py
   ```
2. **Create a Lambda Function in AWS**:
   - Go to the AWS Lambda Console.
   - Click **Create function**.
   - Choose **Author from scratch**.
   - Enter the function name (e.g., `AddTwoNumbers`).
   - Choose the runtime as Python.
   - Upload the `function.zip` file in the function code section.
   - Configure a test event with the following JSON:
     ```json
     {
       "num1": 5,
       "num2": 10
     }
     ```
3. **Test the Function**:
   - Click **Test** and verify the response:
     ```json
     {
       "statusCode": 200,
       "body": {
         "result": 15
       }
     }
     ```

---
## 2. Store Document in S3 Lambda Function

### Description
This function accepts a document or PDF file (passed as a base64-encoded string) and uploads it to a specified S3 bucket.

### File: `lambda_store.py`

### Steps to Deploy and Test
1. **Install Dependencies**:
   If using any dependencies (e.g., `boto3`), install them locally and package them:
   ```bash
   pip install boto3 -t .
   zip -r function.zip *
   ```
2. **Create a Lambda Function in AWS**:
   - Go to the AWS Lambda Console.
   - Click **Create function**.
   - Choose **Author from scratch**.
   - Enter the function name (e.g., `StoreDocumentInS3`).
   - Choose the runtime as Python.
   - Upload the `function.zip` file in the function code section.
3. **Set Up Environment Variables**:
   - Add an environment variable for the S3 bucket name (`BUCKET_NAME`).
4. **Configure IAM Permissions**:
   - Attach an IAM role with `s3:PutObject` permission for the S3 bucket.
5. **Configure a Test Event**:
   Use the following JSON structure for testing:
   ```json
   {
       "file": {
           "name": "example.pdf",
           "content": "base64-encoded-content"
       }
   }
   ```
6. **Test the Function**:
   - Click **Test** and verify the response:
     ```json
     {
       "statusCode": 200,
       "body": {
         "message": "example.pdf uploaded successfully!"
       }
     }
     ```

---

## Repository Structure
```plaintext
.
├── lambda_function.py        # Add Two Numbers Lambda function
├── lambda_store.py           # Store Document in S3 Lambda function
├── README.md                    # Documentation
```

---

## Notes
- Ensure the S3 bucket exists before running the `Store Document in S3` function.
- For the `Store Document in S3` function, use `base64` encoding for file content in the event payload.

---

### **Running the Code Locally**
1. **Ensure File Organization:**
   - Create a folder, e.g., `ResponsiveWebProject`.
   - Place the files you uploaded (`project.html`, `script.js`) and any other associated files like `styles.css` in this folder.

2. **Preview the Project:**
   - Open the `project.html` file in a browser by double-clicking it or dragging it into a browser window.

---
