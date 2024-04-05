import asyncio
import errno

import websockets
import json

PORT = 7890
print(f"Server listening on port {PORT}")

ws_connected_clients = set()


async def echo_broadcast(websocket, path):
    print(f"A client just connected {websocket} ")
    ws_connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message from client {websocket} Message: {message}")
            for ws_client in ws_connected_clients:
                if ws_client != websocket:
                    await ws_client.send(f"The client sent: {message}")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Client {websocket} disconnected")
        print(e)
    finally:
        ws_connected_clients.remove(websocket)


start_server = websockets.serve(echo_broadcast, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
