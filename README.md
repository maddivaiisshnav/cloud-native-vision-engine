Cloud-Native Vision Engine

A fully serverless, event-driven AI pipeline that performs automated image analysis, object detection, and quality assessment using AWS.

Technologies Used :

-> Compute: AWS Lambda (Python 3.12) — Serverless execution of backend logic.

-> AI/ML: Amazon Rekognition — Deep-learning-based computer vision for object detection and image quality.

-> Storage: Amazon S3 — Scalable object storage for raw image files.

-> Database: Amazon DynamoDB — NoSQL database for high-speed metadata storage and auditing.

-> API Layer: Amazon API Gateway — RESTful endpoints for frontend-to-backend communication.

-> Security: IAM Roles & S3 Pre-signed URLs — Secure, temporary access for direct-to-cloud uploads.

Lambda Functions used in this project :

1. GetPresignedURL : 
Purpose: To eliminate the risk of exposing AWS credentials in the frontend.

Logic: Generates a temporary, cryptographically signed URL that allows the user to upload a specific file directly to an S3 bucket.

2. ImageAIAnalyzer : 
Purpose: The core processing unit triggered automatically by S3 "ObjectCreated" events.

Logic: Sends the image to Amazon Rekognition to detect labels (objects) and technical properties (Brightness/Sharpness).

Data Persistence: Maps the analysis results to the image ID and saves the record into DynamoDB.


3. GetAIResults :
Purpose: Provides the frontend with a way to retrieve analysis metadata.

Logic: Queries the DynamoDB table using the ImageId as a partition key to return the AI summary.

WORKFLOW : 

-> Request Access: User selects an image; frontend requests a Pre-signed URL via API Gateway.

-> Direct Upload: The browser uploads the image directly to Amazon S3.

-> Automated Trigger: S3 detects the new file and immediately triggers the Analyzer Lambda.

-> AI Analysis: The Lambda coordinates with Amazon Rekognition to identify objects and assess quality.

-> Audit Trail: Results are stored permanently in DynamoDB.

-> Polling & Display: The frontend polls the Results API until the analysis is ready and displays it to the user.
