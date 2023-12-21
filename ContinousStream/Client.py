from pistream import Client

Client.init("172.17.17.120")

print("Press q to quit")
print("Press k to kill the server")

while True:
    Client.get_image(show_image=True)
