# Flask App Readme

## Introduction

This is a Python Flask application that requires Python 3.11. This document provides a step-by-step guide to set up the application, including creating a Python virtual environment, installing dependencies, and running the application. Additionally, there is a Postman collection named `ML APIs.postman_collection` that can be used to test the APIs.

## Prerequisites

- Python 3.11
- Flask
- Postman (for testing APIs)

## Setup Instructions

### Step 1: Install Python 3.11

Ensure that Python 3.11 is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Create a Python Virtual Environment

Open a terminal and navigate to your project directory. Run the following commands to create and activate a virtual environment:

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### Step 3: Install Requirements

With the virtual environment activated, install the necessary dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Rename the `sample.env` file to `.env` file in the root directory of the project and add following values required values:

```
DB_HOST=your_db_host
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

These environment variables will be used in your application to configure the database connection.

### Step 5: Run the Application

Run the Flask application using the following command:

```bash
python run.py
```

The application will be up and running on `http://localhost:5000`.

### Step 6: Use Postman Collection

To test the APIs, you can use the provided Postman collection. Import the `ML APIs.postman_collection` file into Postman and use the pre-configured requests to interact with the API.

## Additional Information

- Ensure that the virtual environment is activated whenever you work on the project.
- You can deactivate the virtual environment using the command `deactivate`.

## Contact

For any issues or questions:
- Elbert Ehsan
- elbert.ehsan@epikafleet.com