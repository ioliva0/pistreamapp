from pistream import Client

Client.init()

print("Press q to quit")
print("Press k to kill the server")

while True:
    Client.get_image(show_image=True)
