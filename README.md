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

API provides endpoints to manage users, products and vehicles. It supports basic CRUD (Create, Read, Update, Delete) operations. Detailed API documentation is also provided in openapi.json file.

### Base URL
The base URL in a local development environment is http://127.0.0.1:5000/api.

### Endpoints

#### Users

##### GET /users
- **Description:** Retrieves information about all users.
- **Response:** 
   - **Status 200 (OK):** Returns a JSON array of user objects. Each object contains user information such as `username`, `firstname`, `lastname`.
   - **Status 500 (Internal Server Error):** If an error occurs during the process, returns a JSON object with an error message.

##### **GET /users/{id}**
- **Description:** Retrieves information about a specific user by `id`.
- **Parameters:**
   - **Path parameter:** `id` (integer) - The unique identifier of the user.
- **Response:**
   - **Status 200 (OK):** Returns a JSON object with user details for the specified `id`.
   - **Status 404 (Not Found):** Returns a JSON object with an error message if the user does not exist.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.

##### **POST /users**
- **Description:** Creates a new user.
- **Request Body:**
   - **JSON object:** Contains the following fields:
     - `username` (string): Username for the new user.
     - `firstname` (string): First name of the user.
     - `lastname` (string): Last name of the user.
- **Response:**
   - **Status 200 (OK):** Returns a JSON object of the created user.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an error occurs during the creation process.

##### **PUT /users/{id}**
- **Description:** Updates a user's information by `id`.
- **Parameters:**
   - **Path parameter:** `id` (integer) - The unique identifier of the user to update.
- **Request Body:**
   - **JSON object:** Contains the following fields:
     - `username` (string): Updated username.
     - `firstname` (string): Updated first name.
     - `lastname` (string): Updated last name.
- **Response:**
   - **Status 200 (OK):** Returns a JSON object of the updated user.
   - **Status 404 (Not Found):** Returns a JSON object with an error message if the user does not exist.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.

##### **DELETE /users/{id}**
- **Description:** Deletes a user by `id`.
- **Parameters:**
   - **Path parameter:** `id` (integer) - The unique identifier of the user to delete.
- **Response:**
   - **Status 200 (OK):** Confirms that the user was successfully deleted.
   - **Status 404 (Not Found):** Returns a JSON object with an error message if the user does not exist.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.

#### Products

##### **GET /products**
- **Description:** Retrieves a list of all products.
- **Response:**
   - **Status 200 (OK):** Returns a JSON array of product objects. Each object contains product information such as `name` and `description`.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.

##### **GET /products/{id}**
- **Description:** Retrieves information about a specific product by `id`.
- **Parameters:**
   - **Path parameter:** `id` (integer) - The unique identifier of the product.
- **Response:**
   - **Status 200 (OK):** Returns a JSON object with product details for the specified `id`.
   - **Status 404 (Not Found):** Returns a JSON object with an error message if the product does not exist.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.

##### **POST /products**
- **Description:** Creates a new product.
- **Request Body:**
   - **JSON object:** Contains the following fields:
     - `name` (string): Name of the new product.
     - `description` (string): Description of the new product.
- **Response:**
   - **Status 200 (OK):** Returns a JSON object of the created product.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an error occurs during the creation process.

##### **PUT /products/{id}**
- **Description:** Updates a product's information by `id`.
- **Parameters:**
   - **Path parameter:** `id` (integer) - The unique identifier of the product to update.
- **Request Body:**
   - **JSON object:** Contains the following fields:
     - `name` (string): Updated name.
     - `description` (string): Updated description.
- **Response:**
   - **Status 200 (OK):** Returns a JSON object of the updated product.
   - **Status 404 (Not Found):** Returns a JSON object with an error message if the product does not exist.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.

##### **DELETE /products/{id}**
- **Description:** Deletes a product by `id`.
- **Parameters:**
   - **Path parameter:** `id` (integer) - The unique identifier of the product to delete.
- **Response:**
   - **Status 200 (OK):** Confirms that the product was successfully deleted.
   - **Status 404 (Not Found):** Returns a JSON object with an error message if the product does not exist.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.

#### Vehicles

##### **GET /vehicles**
- **Description:** Retrieves a list of all vehicles.
- **Response:**
   - **Status 200 (OK):** Returns a JSON array of vehicle objects. Each object contains vehicle information such as `make` and `model`.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.

##### **GET /vehicles/{id}**
- **Description:** Retrieves information about a specific vehicle by `id`.
- **Parameters:**
   - **Path parameter:** `id` (integer) - The unique identifier of the vehicle.
- **Response:**
   - **Status 200 (OK):** Returns a JSON object with vehicle details for the specified `id`.
   - **Status 404 (Not Found):** Returns a JSON object with an error message if the vehicle does not exist.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.

##### **POST /vehicles**
- **Description:** Creates a new vehicle.
- **Request Body:**
   - **JSON object:** Contains the following fields:
     - `make` (string): The make of the new vehicle.
     - `model` (string): The model of the new vehicle.
- **Response:**
   - **Status 200 (OK):** Returns a JSON object of the created vehicle.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an error occurs during the creation process.

##### **PUT /vehicles/{id}**
- **Description:** Updates a vehicle's information by `id`.
- **Parameters:**
   - **Path parameter:** `id` (integer) - The unique identifier of the vehicle to update.
- **Request Body:**
   - **JSON object:** Contains the following fields:
     - `make` (string): Updated maker.
     - `model` (string): Updated model.
- **Response:**
   - **Status 200 (OK):** Returns a JSON object of the updated vehicle.
   - **Status 404 (Not Found):** Returns a JSON object with an error message if the vehicle does not exist.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.

##### **DELETE /vehicles/{id}**
- **Description:** Deletes a vehicle by `id`.
- **Parameters:**
   - **Path parameter:** `id` (integer) - The unique identifier of the vehicle to delete.
- **Response:**
   - **Status 200 (OK):** Confirms that the vehicle was successfully deleted.
   - **Status 404 (Not Found):** Returns a JSON object with an error message if the vehicle does not exist.
   - **Status 500 (Internal Server Error):** Returns a JSON object with an error message if an internal error occurs.