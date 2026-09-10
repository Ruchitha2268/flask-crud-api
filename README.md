# Flask CRUD REST API

A simple and containerized CRUD (Create, Read, Update, Delete) REST API built using **Python Flask**, **Flask-SQLAlchemy**, **PostgreSQL**, **Docker**, and **Docker Compose**.

This project demonstrates how to build a backend API for managing user data and connecting a Flask application to a PostgreSQL database using SQLAlchemy and Docker Compose.

---

## 📌 Project Overview

The Flask CRUD API provides REST API endpoints for managing users.

Each user contains:

* User ID
* Username
* Email

The application uses:

* **Flask** to build the REST API
* **Flask-SQLAlchemy** to interact with the database
* **PostgreSQL** for data storage
* **Docker** to containerize the application
* **Docker Compose** to manage the application and database containers
* **Postman** to test the API endpoints

---

## 🚀 Features

* RESTful API using Flask
* Create new users
* Retrieve all users
* Retrieve a user by ID
* Update existing users
* Delete users
* PostgreSQL database integration
* SQLAlchemy ORM
* Docker containerization
* Docker Compose configuration
* HTTP status code handling
* Postman API testing
* Unique constraints for username and email

---

## 🛠️ Technologies Used

| Technology       | Purpose                                |
| ---------------- | -------------------------------------- |
| Python           | Programming language                   |
| Flask            | Web framework                          |
| Flask-SQLAlchemy | ORM and database integration           |
| PostgreSQL       | Relational database                    |
| Docker           | Containerization                       |
| Docker Compose   | Multi-container application management |
| Postman          | API testing                            |
| Git & GitHub     | Version control                        |

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────┐
                    │     Postman     │
                    │    API Client   │
                    └────────┬────────┘
                             │
                             │ HTTP Requests
                             ▼
                    ┌─────────────────┐
                    │    Flask API    │
                    │    Port 4000    │
                    └────────┬────────┘
                             │
                             │ SQLAlchemy
                             ▼
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    │    Database     │
                    │    Port 5432    │
                    └─────────────────┘

              Both services run using Docker Compose
```

---

## 📂 Project Structure

```text
flask-crud-api/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .gitignore
│
├── postman/
│   └── ...
│
└── .postman/
    └── ...
```

### File Description

| File                 | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| `app.py`             | Contains the Flask application, database model, routes, and CRUD operations |
| `Dockerfile`         | Contains instructions to build the Flask application Docker image           |
| `docker-compose.yml` | Defines the Flask application and PostgreSQL database services              |
| `requirements.txt`   | Contains the Python dependencies required by the project                    |
| `postman/`           | Contains Postman-related files used for API testing                         |
| `.gitignore`         | Specifies files and folders that should not be uploaded to GitHub           |
| `README.md`          | Project documentation                                                       |

---

## ⚙️ API Endpoints

The application runs on:

```text
http://localhost:4000
```

### 1. Test API

**GET** `/test`

Checks whether the Flask API is running successfully.

**Request:**

```text
GET http://localhost:4000/test
```

**Example Response:**

```json
{
    "message": "test route"
}
```

**Status Code:** `200 OK`

---

## 👤 User CRUD Operations

### 2. Create a User

**POST** `/users`

Creates a new user in the PostgreSQL database.

**Request:**

```text
POST http://localhost:4000/users
```

**Headers:**

```text
Content-Type: application/json
```

**Request Body:**

```json
{
    "username": "john_doe",
    "email": "john@example.com"
}
```

**Status Code:** `201 Created`

---

### 3. Get All Users

**GET** `/users`

Returns all users stored in the database.

**Request:**

```text
GET http://localhost:4000/users
```

**Example Response:**

```json
[
    {
        "email": "john@example.com",
        "id": 1,
        "username": "john_doe"
    },
    {
        "email": "ravi@example.com",
        "id": 2,
        "username": "ravi"
    }
]
```

**Status Code:** `200 OK`

---

### 4. Get User by ID

**GET** `/users/<id>`

Retrieves a specific user using the user ID.

**Request:**

```text
GET http://localhost:4000/users/1
```

**Example Response:**

```json
{
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com"
    }
}
```

If the user does not exist:

```json
{
    "message": "user not found"
}
```

**Status Codes:**

* `200 OK`
* `404 Not Found`

---

### 5. Update a User

**PUT** `/users/<id>`

Updates the username and email of an existing user.

**Request:**

```text
PUT http://localhost:4000/users/1
```

**Headers:**

```text
Content-Type: application/json
```

**Request Body:**

```json
{
    "username": "john_updated",
    "email": "john.updated@example.com"
}
```

**Status Code:** `200 OK`

### Important

The `username` and `email` fields have unique constraints in the database.

Therefore, a username or email that already belongs to another user cannot be used for an update.

---

### 6. Delete a User

**DELETE** `/users/<id>`

Deletes a user from the database.

**Request:**

```text
DELETE http://localhost:4000/users/1
```

**Example Response:**

```json
{
    "message": "user deleted"
}
```

**Status Code:** `200 OK`

If the user does not exist:

```json
{
    "message": "user not found"
}
```

**Status Code:** `404 Not Found`

---

## 🗄️ Database

This project uses **PostgreSQL** as the relational database.

The database contains a `users` table with the following columns:

| Column     | Data Type | Constraints      |
| ---------- | --------- | ---------------- |
| `id`       | Integer   | Primary Key      |
| `username` | String    | Unique, Not Null |
| `email`    | String    | Unique, Not Null |

### SQLAlchemy Model

```python
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

---

## 🐳 Docker Configuration

The project uses Docker Compose to run the application and PostgreSQL database.

### Flask Application

```text
Container: flask_app
Port: 4000
```

### PostgreSQL Database

```text
Container: flask_db
Port: 5432
```

Docker Compose creates a network that allows the Flask application to communicate with PostgreSQL using the database service name.

---

## 💻 Running the Project Locally

### Prerequisites

Install:

* Git
* Docker Desktop
* Postman (optional)

Make sure **Docker Desktop is running** before starting the application.

### Step 1: Clone the Repository

```bash
git clone https://github.com/Ruchitha2268/flask-crud-api.git
cd flask-crud-api
```

### Step 2: Build the Docker Image

```bash
docker compose build
```

### Step 3: Start the Containers

```bash
docker compose up -d
```

The `-d` option runs the containers in detached mode.

### Step 4: Check Container Status

```bash
docker compose ps
```

You should see the application and PostgreSQL containers running.

### Step 5: Test the Application

Open:

```text
http://localhost:4000/test
```

Expected response:

```json
{
    "message": "test route"
}
```

---

## 🧪 Testing with Postman

The API can be tested using Postman.

| Operation      | Method | Endpoint   |
| -------------- | ------ | ---------- |
| Create User    | POST   | `/users`   |
| Get All Users  | GET    | `/users`   |
| Get User by ID | GET    | `/users/1` |
| Update User    | PUT    | `/users/1` |
| Delete User    | DELETE | `/users/1` |

---

## 🔄 CRUD Flow

```text
                    CRUD API
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
      CREATE          READ          UPDATE
       POST            GET            PUT
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
                     DELETE
                      DELETE
```

The application performs:

```text
CREATE → Add a new user
READ   → Retrieve users
UPDATE → Modify an existing user
DELETE → Remove a user
```

---

## 🛑 Stopping the Application

To stop the containers:

```bash
docker compose down
```

This stops and removes the application and database containers.

---

## 🔍 Viewing Application Logs

### Flask Application Logs

```bash
docker compose logs flask_app
```

### PostgreSQL Logs

```bash
docker compose logs flask_db
```

### Follow Flask Logs

```bash
docker compose logs -f flask_app
```

---

## 🔄 Restarting the Application

If you make changes to the Flask application:

```bash
docker compose down
docker compose build
docker compose up -d
```

---

## 🧹 Removing Containers and Volumes

### Remove Containers

```bash
docker compose down
```

### Remove Containers and Database Volume

```bash
docker compose down -v
```

> ⚠️ **Warning:** Removing the volume deletes the PostgreSQL data stored in that Docker volume.

---

## 📌 Error Handling

The API handles application and database errors and returns appropriate HTTP status codes.

Common status codes include:

* `200 OK`
* `201 Created`
* `404 Not Found`
* `500 Internal Server Error`

For example:

```json
{
    "message": "error creating user",
    "error": "..."
}
```

---

## 🔐 Data Validation and Constraints

The PostgreSQL database enforces unique values for:

* `username`
* `email`

Therefore, attempting to create or update a user with an existing username or email can result in a database constraint error.

---

## 📚 What I Learned

Through this project, I gained practical experience with:

* Flask REST API development
* CRUD operations
* HTTP methods and status codes
* SQLAlchemy ORM
* PostgreSQL database integration
* Docker containerization
* Docker Compose
* Container-to-container communication
* API testing using Postman
* Git and GitHub version control

---

## 🚀 Future Improvements

Possible future enhancements include:

* User authentication and authorization
* JWT-based authentication
* Password hashing
* Input validation
* Pagination
* Search and filtering
* Swagger/OpenAPI documentation
* Automated testing
* Database migrations using Flask-Migrate
* Production deployment
* CI/CD using GitHub Actions
* API rate limiting

---

## 👩‍💻 Author

**Ruchitha Bathini**

GitHub: [Ruchitha2268](https://github.com/Ruchitha2268)

Project Repository: [flask-crud-api](https://github.com/Ruchitha2268/flask-crud-api)

---

## ⭐ Project Highlights

```text
Flask REST API
       +
SQLAlchemy
       +
PostgreSQL
       +
Docker
       +
Docker Compose
       +
Postman
       =
Containerized CRUD Backend
```

If you found this project useful, consider giving the repository a ⭐ on GitHub.

