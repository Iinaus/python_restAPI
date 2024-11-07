# Python/Flask REST API

## Table of contents
- [About](#about)
- [Getting started](#getting-started)
  - [Dependencies](#dependencies)
  - [Dev setup step-by-step](#dev-setup-step-by-step)
- [API documentation](#api-documentation)
  - [Base URL](#base-url)
  - [Endpoints](#endpoints)


## About

This project is a RESTful API built with Python and Flask to manage user, product, and vehicle data. It serves as a practical exercise in developing web APIs and understanding core backend development concepts. Additionally, the project aimed to provide hands-on experience with architectural patterns and their applications, such as MVC, repository pattern, factory pattern, and dependency injection. The project was developed as part of the Web Development and Frameworks course at Lapland University of Applied Sciences.

With this exercise we practiced:
- Setting up a Python backend using Flask.
- Applying different architectural patterns, including MVC, repository pattern, factory pattern, service pattern, and dependency injection.
- Implementing CRUD operations (Create, Read, Update, Delete).
- Handling HTTP requests and responses to interact with the frontend or other services.
- Working with various databases (MySQL, PostgreSQL, MongoDB) for data storage and retrieval.

## Getting started

Instructions on how to set up and run the backend.

### Dependencies

This project relies on the following dependencies:

- **Flask**: A lightweight Python web framework for handling HTTP requests, routing, and response management.
- **mysql-connector-python**: A library to interact with MySQL databases.
- **psycopg2-binary**: A PostgreSQL adapter for Python, enabling seamless interaction with PostgreSQL databases.
- **python-dotenv**: Manages environment variables securely by loading them from a `.env` file.
- **pymongo**: A MongoDB driver for Python, used to interact with MongoDB databases.

Make sure to install these dependencies before running the project to ensure smooth execution.

### Dev Setup Step-by-Step

1. Clone the project
2. Create a `.env` file in the project root. Refer to `.env.example` for required environment variables.
3. Create and activate a virtual environment:
   `python -m venv venv`
   `.\venv\Scripts\activate` *Windows
   `source venv/bin/activate` *macOS/Linux
   python -m venv venv
4. Install dependencies: `pip install -r requirements.txt`
5. Run the project `python app.py`

## API documentation

API provides endpoints to manage users, products and vehicles. It supports basic CRUD (Create, Read, Update, Delete) operations.

### Base URL
The base URL in a local development environment depends on the database being used.

### Endpoints

#### GET /users
- **Description:** Retrieves information about all users.
- **Response:** 
   - **Status 200 (OK):** Returns a JSON array of user objects. Each object contains user information such as name, email, etc.
   - **Status 500 (Internal Server Error):** If an error occurs during the process, returns a JSON object with an error message. 

### Note
As the project evolves, API documentation and README will be updated.