# Model Deployment on GCP using CircleCI & Kubernetes

## Table of Contents
- 📌 [Project Overview](#project-overview)
- 📊 [Architecture](#architecture)
- ⚙️ [Tech Stack](#tech-stack)
- 📁 Project Structure
- 🔄 [CI/CD Pipeline Stages](#ci-cd-pipeline-stages)
- [Project Workflow](#project-workflow)
- 📦 Setup Instructions
- 🚀 How to Run
- 🔐 Model Deployment
- 🧪 Testing
- 📝 [Future Enhancements](#future-enhancements)


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
1. **Checkout** Code : Fetch the latest code from GitHub.
2. Install Dependencies/Python packages from requirements.txt.
3. Run Tests / Linting (optional):  Perform code quality checks or run test suites.
4. **Build** Docker Image using the Dockerfile.
5. **Push** the image to Google Container Registry.
6. **Deploy** the Docker images/app to Google Kubernetes Engine (GKE) cluster.
7. Expose via LoadBalancer : The app is made available at a public IP endpoint.

Pipelines can be triggered manually or automatically on code pushes.

## Project Workflow

1. **Project Setup**
   - Create virtual environments and install dependencies (e.g., pandas, numpy, matplotlib).
   - Organize project structure with folders like `src`, `pipeline`, and `artifacts`.

2. **Jupyter Notebook Testing**
   - Perform data processing, model training, and model selection interactively in a notebook.

3. **Modular Code Development**
   - Convert notebook steps into modular code using classes and methods for better maintainability.

4. **User Application**
   - Build a simple user interface using Flask and basic HTML (optionally styled with ChatGPT).

5. **Training Pipeline**
   - Combine data processing and model training into a single Python script for streamlined execution.

6. **Versioning**
   - Use GitHub for data and code versioning (suitable for small datasets).
   - Optionally use DVC for large datasets.

7. **Google Cloud Setup**
   - Create a Kubernetes cluster on GCP.
   - Set up artifact repositories and service accounts with necessary permissions.
   - Enable required GCP APIs.

## Future Enhancements
- Add ML model versioning using MLflow or DVC
- Integrate monitoring/logging via Prometheus + Grafana
- Add a frontend interface for predictions
- Support multi-environment (dev/staging/prod) deployments
