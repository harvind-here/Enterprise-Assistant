# Enterprise-Assistant
 A chat based assistant for efficient administration and IT support for clients, admins and employees of a company/enterprise.

# Enterprise Chatbot

This project implements a chat-based assistant designed to provide efficient administration and IT support for clients, administrators, and employees within a company or enterprise environment. It aims to streamline communication and problem-solving through a conversational interface.

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
├── index.ts         # TypeScript entry point
├── rag.py          # Retrieval Augmented Generation implementation
├── security.py     # Security implementations
└── various configuration files
```

## Preliminary Setup Guide

Follow these instructions to get a development environment set up:

**1. Clone the Repository**
```bash
git clone https://github.com/your-username/enterprise-chatbot.git
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
