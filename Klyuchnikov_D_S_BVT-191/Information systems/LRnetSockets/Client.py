import socket
import can

HEADER = 64
PORT = 29536
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "101.116.99.97"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    canMessage = can.Message(arbitration_id=0xC0FFEE, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=True)
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    client.send(canMessage)
    print(client.recv(2048).decode(FORMAT))

message = input("enter a message: ")
while message != DISCONNECT_MESSAGE:
    send(message)
    message = input("enter a message: ")
    
send(DISCONNECT_MESSAGE)