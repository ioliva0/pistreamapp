from pistream import Server

Server.init("172.17.17.120", 9999)

while True:
    Server.wait_for_connection()

    connected = True
    while connected:
        connected = Server.send_image()
