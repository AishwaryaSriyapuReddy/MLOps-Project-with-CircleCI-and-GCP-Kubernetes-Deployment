# Model Deployment on GCP using CircleCI & Kubernetes

## Table of Contents
- 📌 [Project Overview](#project-overview)
- 📊 [Architecture](#architecture)
- ⚙️ [Tech Stack](#tech-stack)
- 📁 Project Structure
- 🔄 [CI/CD Pipeline Stages](#ci/cd-pipeline-stages)
- 📦 Setup Instructions
- 🚀 How to Run
- 📈 MLFlow Tracking
- 🔐 Model Deployment
- 🧪 Testing
- 📝 Future Enhancements


## Project Overview
This project demonstrates an end-to-end MLOps pipeline where a machine learning model is containerized and deployed using:
- Flask (as an API server),
- Docker (for containerization),
- CircleCI (for CI/CD),
- GCP's GCR and GKE (for container hosting and orchestration).
The model is exposed through a public endpoint using a LoadBalancer service in Kubernetes.

## Architecture 
This project follows a modern CI/CD-based MLOps architecture powered by CircleCI, Docker, and Google Kubernetes Engine (GKE).

<img width="7623" height="600" alt="image" src="https://github.com/user-attachments/assets/b8529820-09ba-42fc-be80-df5dfb15f5a2" />

## Tech Stack

| Tool                                | Purpose                                                     |
| ----------------------------------- | ----------------------------------------------------------- |
| **Python**                          | Core programming language for building the model and app    |
| **Jupyter Notebook**                | For initial data analysis, EDA, and prototyping the model   |
| **Flask**                           | Lightweight web framework to serve the model as an API      |
| **Docker**                          | Containerization of the Flask app for consistent deployment |
| **CircleCI**                        | Automates build, test, and deployment steps (CI/CD)         |
| **GitHub**                          | Source code and version control                             |
| **Google Cloud Platform (GCP)**     | Cloud service provider to host and run the infrastructure   |
| **Google Kubernetes Engine (GKE)**  | Manages Kubernetes cluster for deploying containerized apps |
| **Google Container Registry (GCR)** | Stores and manages Docker images used in deployment         |

## CI/CD Pipeline Stages
1. Checkout Code  
Fetch the latest code from GitHub.

2. Install Dependencies  
Install all Python packages from requirements.txt.

3. Run Tests / Linting (optional)  
Perform code quality checks or run test suites.

4. Build Docker Image  
Create an image using the Dockerfile.

5. Push to GCR  
Push the image to Google Container Registry.

6. Deploy to GKE  
Apply Kubernetes manifests to deploy the app to a cluster.

7. Expose via LoadBalancer  
The app is made available at a public IP endpoint.
