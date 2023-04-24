# Stores REST API

## Project Description
A RESTful API built with Flask and Flask-Smorest, which provides endpoints for managing stores and their respective items. The API allows users to create, retrieve, update, and delete items and stores.

The data is stored in a relational database managed by SQLAlchemy. There are two models defined in this project, ItemModel and StoreModel, which represent the items and stores respectively. ItemModel has a foreign key to StoreModel, allowing a store to have multiple items.
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

