# Stores REST API

## Project Description
This is a Store API built with Flask and Python, designed to manage stores and their associated items. The API utilizes a RESTful architecture, allowing clients to easily interact with it using standard HTTP requests. The data is stored in an SQLite database, ensuring a lightweight and efficient system.

With this API, clients can create, update, delete, and retrieve stores and their items. The API is designed to be flexible and easy to use, with comprehensive documentation provided to assist developers in integrating it into their projects. The API is built using best practices, ensuring that it is scalable and maintainable over time.
The application uses predefined Marshmallow schemas which define the structure of the data that can be sent and received by the API endpoints.

### STEPS FOR RUNNING APPLICATION
Application should be run with the docker file included

1. Open the project root folder in your IDE of choice.
2. Install dependencies in the `requirements.txt` in your virtual environment.
3. Ensure IDE is using created virtual environment.
4. Open a terminal or command prompt in the directory and run the following command to build the Docker image
```
docker build -t docker-image-tag .
```
5. use the command below to start a container using the docker image and sync container with development directory.
```
docker run -dp 5005:5000 -w /app -v "%cd%:/app" flask-smorest-api
```
6. Visit [URL](http://127.0.0.1:5005/swagger-ui
) below for UI documentation and test API endpoints

