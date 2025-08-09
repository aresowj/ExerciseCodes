import websocket
# import rel

def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")


def long_lived_connection():
    websocket.enableTrace(True)
    wsapp = websocket.WebSocketApp(
        "ws://localhost:8080/echo",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open,
    )
    wsapp.run_forever()


def short_lived_connection():
    # short-lived connection
    ws = websocket.create_connection("ws://localhost:8080/echo")
    # print(ws.recv())
    print("Sending 'Hello, World'...")
    ws.send("Hello, World")
    print("Sent")
    print("Receiving...")
    print(ws.recv())
    ws.close()


if __name__ == "__main__":
    # long_lived_connection()
    short_lived_connection()
