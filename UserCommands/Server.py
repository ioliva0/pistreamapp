from pistream import Server

Server.set_resolution((1280, 720))
Server.set_quality(70)

Server.init()

while True:
    Server.wait_for_connection()

    connected = True
    while connected:
        connected = Server.serve()
