import asyncio
import websockets
import websocket
import uuid

URL = "ws://127.0.0.1:7890"
ID = uuid.uuid4()


def on_message(websocket, message):
    print(f"Client: {ID}: Received message: {message}")


def on_error(websocket, error):
    print(f"Client: {ID}: Encountered error: {error}")


def on_close(websocket, close_status_code, close_msg):
    print(f"Client: {ID}: Connection closed: {close_status_code}")


def on_open(ws):
    print(f"Connection opened by {ID}")
    ws.send(f"Client: {ID}: Hello, Server!")


if __name__ == "__main__":
    websocket = websocket.WebSocketApp(URL,
                                       on_message=on_message,
                                       on_error=on_error,
                                       on_close=on_close)
    websocket.on_open = on_open
    websocket.run_forever()

# Implementation using websockets library.
# async def listen_server():
#
#     client_num = randrange(10)
#
#     async with websockets.connect(URL) as websocket:
#         await websocket.send(f"I'm the client {client_num}")
#         while True:
#             response = await websocket.recv()
#             print(response)
#
# # Start the connection to the server
# asyncio.get_event_loop().run_until_complete(listen_server())
