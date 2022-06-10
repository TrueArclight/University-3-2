import socket
import random
import time
import zlib
#from Protocol import check_hash


def can_bit_array():
    can_array = [1, 11, 1, 1, 0, 4]
    iteration = 0
    while iteration < 116:
        can_array.append(random.randint(0, 128))
        iteration += 1
    can_array.append(15)
    can_array.append(1)
    can_array.append(1)
    can_array.append(7)
    can_array.append(7)
    return bytearray(can_array)


def can_sender(client):
    secs = 0.1
    allPackets = 0
    Packets = 0
    while allPackets <= 270:
        allPackets += 1
        Packets += 1
        can_array = can_bit_array()
        client_hash = ""
        for sym in str(zlib.crc32(can_array)):
            if len(client_hash) != 2:
                client_hash += sym
        can_array.append(int(client_hash))
        # can_array = check_hash(can_array, secs)
        client.send(can_array)
        time.sleep(secs)
        print("Задержка ", int(secs * 1000), "мс\n")
        print("Пакетов отправлено: ", allPackets)
        if Packets == 3:
            secs -= 0.001
            Packets = 0


def connection():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.0.100", 51017))
    print("Подключение к серверу произошло успешно")
    can_sender(client)

connection()
