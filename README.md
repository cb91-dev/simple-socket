# FastAPI WebSocket Application

### Overview
This project is a FastAPI-based WebSocket application that supports real-time communication between clients. It allows clients to connect to a WebSocket endpoint, send messages, and receive responses from the server. The server can broadcast messages to all connected clients. This application is containerized using Docker for both development and production environments.

### Features

- Real-time communication using WebSockets.
- Echo server functionality for testing.
- Broadcast messages to all connected clients.
- JSON message handling.
- Dockerized for easy deployment and development.

### Table of Contents

- Overview
- Features
- Architecture
- Setup and Installation
  - Prerequisites
  - Installation
  - Running the Application
  - Running Tests
- Usage
  - WebSocket Endpoint
- Development
 - Project Structure
 - Testing
- Contributing
- License

### Architecture
The application is built using FastAPI for the WebSocket server and managed by Docker for containerization. The key components include:

- FastAPI: Framework for building the WebSocket server.
- Uvicorn: ASGI server to run the FastAPI application.
- Docker: Containerization for development and deployment.
- pytest: Testing framework for unit tests.
------------
### Setup and Installation
#### Prerequisites
- Docker: Ensure Docker is installed. [Docker Installation Guide](https://docs.docker.com/engine/install/)
- Docker Compose: Ensure Docker Compose is installed. [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

#### Installation
###### Clone the repository:
````
git clone https://github.com/yourusername/simple-socket.git
cd simple-socket
````

######  Build the Docker image:
```` 
docker-compose build
````

#### Running the Application
###### Start the application using Docker Compose:
```
docker-compose up
```
##### Access the application at http://localhost:8000.


#### Running Tests
##### Run tests using Docker Compose:
````
docker-compose exec web sh -c "PYTHONPATH=/workspace pytest -vs /workspace/app/test_main.py"

````
###### Or access the container and run tests manually:

````
docker exec -it fastapi-websocket_web_1 /bin/sh
export PYTHONPATH=/workspace
pytest /workspace/app/test_main.py -vs
````
------------------------------------------
### Usage
#### WebSocket Endpoint:
 The WebSocket endpoint /ws allows clients to connect and communicate with the server. Here’s how to use it:

##### Connect to the WebSocket:
```
const socket = new WebSocket('ws://localhost:8000/ws');
```
##### Send a Message:
```
socket.send('Hello, WebSocket!');
```
##### Receive a Message:
```
socket.onmessage = (event) => {
    console.log('Message from server:', event.data);
};
```


### Development
#### Project Structure
```
simple-socket/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── manager.py
│   └── test_main.py
├── Dockerfile
└── docker-compose.yml
```

- app/main.py: FastAPI application with WebSocket endpoint.
- app/manager.py: Manages WebSocket connections and message broadcasting.
- app/test_main.py: Unit tests for the WebSocket application.
- Dockerfile: Docker configuration for the application.
- docker-compose.yml: Docker Compose configuration for multi-container setup.

### Testing
Tests are written using pytest and are located in app/test_main.py. They include:

- Connection Establishment and Closure: Verify WebSocket connections.
- Echo Single Message: Test echo functionality.
- Echo Multiple Messages: Test multiple message handling.
- Unexpected Disconnection: Test server handling of unexpected disconnections.
- Broadcast: Verify message broadcasting to all clients.
- JSON Message Handling: Test sending and receiving JSON messages.

#### To run tests
```
docker-compose exec web sh -c "PYTHONPATH=/workspace pytest -vs /workspace/app/test_main.py"

```

### Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss new features or bug fixes. Make sure to follow the project's coding standards and write tests for new features.