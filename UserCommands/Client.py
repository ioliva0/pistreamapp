import cv2

from pistream import Client

Client.init("172.17.17.120")

Client.request_disable_timeout()


def bad_command():
    print("Invalid Command, please use one of the commands in parentheses")


def list_commands():
    print("Commands:")
    print("get one frame (1)")
    print("start stream  (2)")
    print("quit          (3)")
    print("kill server   (4)")


list_commands()

while True:
    command = input("Input a command: ").lower()

    if command == "help" or command == "h" or command == "?":
        list_commands()
        continue

    try:
        command = int(command)
    except ValueError:
        bad_command()
        continue

    match command:
        case 1:
            Client.request_frame()
            image = Client.get_image()
            cv2.imshow("image", image)
            print("Press any key to continue...")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        case 2:
            print("Press q to quit...")
            Client.request_stream_start()
            while cv2.waitKey(1) & 0xFF != ord("q"):
                image = Client.get_image()
                cv2.imshow("stream", image)
            Client.request_stream_stop()
            cv2.destroyAllWindows()
        case 3:
            Client.close()
            exit()
        case 4:
            Client.kill_server()
            exit()
