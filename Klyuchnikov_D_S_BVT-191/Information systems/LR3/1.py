import socket
import random


def can_packet():
    can_array = [1, 11, 1, 4]
    iteration = 0
    while iteration < 116:
        can_array.append(random.randint(0, 128))
        iteration += 1
    can_array.append(15)
    can_array.append(1)
    can_array.append(1)
    can_array.append(7)
    can_array.append(192)
    can_array.append(168)
    can_array.append(0)
    can_array.append(107)
    return bytearray(can_array)


def connection(ip, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        print("connected")
        return client
    except:
        print("wrong ip", ip, "sad‚!!!")


def broadcast(client, packet):
    try:
        client.send(packet)
        print("sended")
    except:
        print("exeption")


if __name__ == "__main__":
    _ip = 'localhost'
    _port = 51017
    _client = connection(_ip, _port)
    _packet = can_packet()
    broadcast(_client, _packet)
    input()