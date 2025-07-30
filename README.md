# End-to-End MLOps Pipeline with Circle CI and GCP Kubernetes Deployment

## Table of Contents
- 📌 [Project Overview](#project-overview)
- 📊 [Architecture](#architecture)
- ⚙️ [Tech Stack](#tech-stack)
- 📁 Project Structure
- 🔄 Pipeline Stages
- 📦 Setup Instructions
- 🚀 How to Run
- 📈 MLFlow Tracking
- 🔐 Model Deployment
- 🧪 Testing
- 📝 Future Enhancements


## Project Overview
This MLOps project implements an end-to-end machine learning pipeline, from data ingestion to model deployment, using modern MLOps tools. The pipeline includes:
- ✅ Model development and testing in **Jupyter Notebook**
- 🛠️ Modular refactoring into Python classes
- 🌐 Flask-based user-friendly web interface
- 🐳 Docker containerization
- ☁️ Deployment on GCP's **Kubernetes Cluster (GKE)**
- 🔁 CI/CD with **CircleCI**
- 🔒 Versioning via **GitHub**

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


