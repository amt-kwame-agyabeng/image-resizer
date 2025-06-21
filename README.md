## Image Resizer
A serverless web app that allows users to upload images, which are automatically resized and stored in Amazon S3. The frontend is a static website hosted via AWS Amplify, and the backend runs on AWS Lambda via API Gateway.

## Live Demo

Application is live here - https://main.d1xklw3gl9yz97.amplifyapp.com


## Features
- Upload images via browser

- Automatic resizing using AWS Lambda

- RESTful and HTTPS API powered by API Gateway

- Serverless and highly scalable architecture


## Project Structure
image-resizer/
├── backend/        # Lambda function code (image processing)
├── frontend/       # Static HTML, CSS, and JS files
├── screenshots/    # screenshots
└── README.md

## Technologies Used
Frontend: HTML, CSS, JavaScript

Backend: AWS Lambda (Python), Pillow, boto3

API Layer: Amazon API Gateway

Storage: Amazon S3

Deployment: Manual or Serverless Framework

### Getting Started

# Frontend (Amplify)
1. Push your project to a GitHub repo.
2. Go to AWS Amplify Console → **Connect App**.
3. Select your repo and branch.
4. Set root directory as `frontend/`.
5. Amplify will build and host your static website.

## Backend (Lambda + API Gateway)

1. Zip your Lambda function:

```bash
cd backend
zip -r function.zip .
```

In AWS Console:

- Create a new Lambda function (Python)

- Upload function.zip

- Create an API Gateway to trigger it

- Allow the functions access to S3 (IAM permissions)

- In your frontend/index.html, update the API URL in 
JavaScript to your deployed API Gateway endpoint

- Update the API endpoint URL in your frontend JavaScript.


