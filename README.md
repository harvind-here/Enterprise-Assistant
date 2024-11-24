# Enterprise-Assistant
 A chat based assistant for efficient administration and IT support for clients, admins and employees of a company/enterprise.

## Skills:
<img src="https://img.shields.io/badge/LLMs-3776AB?style=flat-square&logo=ML&logoColor=white" alt="LLMs"> <img src="https://img.shields.io/badge/RAG-3776AB?style=flat-square&logo=finetuning&logoColor=white" alt="RAG"> <img src="https://img.shields.io/badge/Flask-3776AB?style=flat-square&logo=Data&logoColor=white" alt="Flask">

## Features

*   **Chat-Based Interface:**  Provides a user-friendly way to interact and get support.
*   **Targeted Support:** Designed to assist clients, administrators, and employees.
*   **Multi-Platform Compatibility (planned):**  Will be accessible via web, mobile, or other platforms.
*   **Efficient IT Support:** Offers solutions and guidance for common IT issues.
*   **Admin Assistance:** Facilitates administrative tasks and provides helpful information.
*   **Client Interaction:** Improves client support experience.

## Repository Structure

The repository contains the following files and directories:
```
├── dataset/           # Training and configuration data
├── static/           # Static assets and resources
├── templates/        # HTML/template files
├── app.py           # Main application file
├── chatbot.py       # Core chatbot logic
├── document_processor.py  # Document handling functionality
├── rag.py          # Retrieval Augmented Generation implementation
└── security.py     # Security implementations
```

## Preliminary Setup Guide

Follow these instructions to get started:

**1. Clone the Repository**
```bash
git clone https://github.com/harvind-here/enterprise-chatbot.git
cd enterprise-chatbot
```
2. Install Python Dependencies

Make sure you have Python 3.7 or higher installed. Then install the necessary packages using pip:
```bash
pip install -r sih_requirements.txt
```
3. Configuration (if any)

Certain environment variables or configuration files might need to be updated with the correct credentials, API keys, etc.

4. Run the application
```bash
python app.py
```
