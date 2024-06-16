import pytest
import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def websocket_connection():
    """
    Fixture to establish a WebSocket connection for the tests.
    Closes the WebSocket connection after the test.
    """
    with client.websocket_connect("/ws") as websocket:
        yield websocket
        websocket.close()

def test_websocket_connection_establishment_and_closure():
    """
    Test that a WebSocket connection can be established and closed properly.
    """
    with client.websocket_connect("/ws") as websocket:
        assert websocket  # Ensure connection is established
        websocket.send_text("test connection")
        response = websocket.receive_text()
        assert response == "Echo: test connection"

def test_websocket_echo_single_message(websocket_connection):
    """
    Test that a single message sent to the WebSocket is echoed back correctly.
    """
    message = "Hello, WebSocket!"
    websocket_connection.send_text(message)
    response = websocket_connection.receive_text()
    assert response == f"Echo: {message}"

def test_websocket_echo_multiple_messages(websocket_connection):
    """
    Test that multiple messages sent to the WebSocket are echoed back correctly.
    """
    messages = ["First message", "Second message", "Third message"]
    for message in messages:
        websocket_connection.send_text(message)
        response = websocket_connection.receive_text()
        assert response == f"Echo: {message}"

def test_websocket_unexpected_disconnection():
    """
    Test how the WebSocket server handles unexpected disconnections.
    """
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("This should work")
        response = websocket.receive_text()
        assert response == "Echo: This should work"

        websocket.close()

        # Verify server-side disconnection
        try:
            websocket.send_text("This should fail")
            # Attempt to receive the disconnection message or confirm failure
            response = websocket.receive_text()
            assert response == "Connection closed"
        except Exception as e:
            # Ensure the exception is related to WebSocket closure
            assert "WebSocket connection is closed" in str(e) or "Cannot send" in str(e)

def test_websocket_broadcast():
    """
    Test that a message sent to one WebSocket is broadcasted to all connected clients.
    """
    with client.websocket_connect("/ws") as websocket1, client.websocket_connect("/ws") as websocket2:
        websocket1.send_text("Broadcast message")
        response1 = websocket1.receive_text()
        response2 = websocket2.receive_text()
        assert response1 == f"Echo: Broadcast message"
        assert response2 == f"Echo: Broadcast message"

def test_websocket_json_message():
    """
    Test sending and receiving JSON messages through the WebSocket.
    """
    with client.websocket_connect("/ws") as websocket:
        json_message = {"type": "greeting", "content": "Hello, JSON!"}
        websocket.send_json(json_message)
        response = websocket.receive_text()  # Receive as text first
        
        # Extract the JSON part of the response and compare objects
        received_message = response.replace('Echo: ', '', 1)
        received_json = json.loads(received_message)

        assert received_json == json_message
