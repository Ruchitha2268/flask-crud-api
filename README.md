\# Flask CRUD REST API



A simple CRUD (Create, Read, Update, Delete) REST API built using \*\*Python Flask\*\*, \*\*SQLAlchemy\*\*, and \*\*PostgreSQL\*\*, with \*\*Docker\*\* and \*\*Docker Compose\*\* for containerized development.



\## 📌 Project Overview



This project demonstrates a basic REST API for managing user information. It allows users to be created, retrieved, updated, and deleted using HTTP requests.



The API is tested using \*\*Postman\*\* and uses \*\*PostgreSQL\*\* as the database.



\## 🚀 Features



\* Create a new user

\* Get all users

\* Get a user by ID

\* Update user details

\* Delete a user

\* PostgreSQL database integration

\* SQLAlchemy ORM

\* Docker containerization

\* API testing using Postman



\## 🛠️ Technologies Used



\* Python

\* Flask

\* Flask-SQLAlchemy

\* PostgreSQL

\* Docker

\* Docker Compose

\* Postman

\* Git \& GitHub



\## 📁 Project Structure



```text

flask-crud-api/

│

├── app.py

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── .gitignore

├── postman/

└── README.md

```



\## 🔗 API Endpoints



| Method | Endpoint      | Description       |

| ------ | ------------- | ----------------- |

| POST   | `/users`      | Create a new user |

| GET    | `/users`      | Get all users     |

| GET    | `/users/<id>` | Get a user by ID  |

| PUT    | `/users/<id>` | Update a user     |

| DELETE | `/users/<id>` | Delete a user     |



\## 📝 Example Request



\### Create User



\*\*POST\*\*



```text

http://localhost:4000/users

```



Request body:



```json

{

&#x20; "username": "Ruchi",

&#x20; "email": "ruchi@example.com"

}

```



\## ▶️ How to Run



\### 1. Clone the repository



```bash

git clone https://github.com/Ruchitha2268/flask-crud-api.git

cd flask-crud-api

```



\### 2. Start the Docker containers



```bash

docker compose up -d

```



\### 3. Check running containers



```bash

docker ps

```



\### 4. Test the API



The API runs at:



```text

http://localhost:4000

```



You can use \*\*Postman\*\* to test the API endpoints.



\## 🎯 What I Learned



Through this project, I learned how to:



\* Build REST APIs using Flask

\* Perform CRUD operations

\* Connect Flask applications with PostgreSQL

\* Use SQLAlchemy for database operations

\* Containerize applications using Docker

\* Test REST APIs using Postman

\* Manage projects using Git and GitHub



\## 👩‍💻 Author



\*\*Ruchitha Bathini\*\*



GitHub: https://github.com/Ruchitha2268



