from pistream import Server

Server.init()

while True:
    Server.wait_for_connection()

    connected = True
    while connected:
        connected = Server.send_image()
