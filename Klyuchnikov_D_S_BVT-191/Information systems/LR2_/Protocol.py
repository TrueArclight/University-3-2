import struct


def send(connection, data):
    # Трансформируем строку в массив байт
    # if data == isinstance(bytes, data):
    #     connection.sendall(struct.pack('>I', len(data)) + data)
    # else:
    #     data = bytes(data, "utf8")
    connection.sendall(struct.pack('>I', len(data)) + data)
    # Отправляем C struct типа unsigned int размером 4 байта, хранящие длину сообщения. Данные содержат 4 байта, хранящие длину сообщения, плюс само сообщение.

# Функция чтения принятых данных
def recv(connection):
    # Читаем участок, содержащий длину пакета
    length_data = recv_packets(connection, 4)
    # Если получить не удалось, то ничего не возвращаем
    if not length_data:
        print("Не удалось принять сообщение!!!")
        return None
    # Переводим в питоновский тип
    data_len = struct.unpack('>I', length_data)[0]
    print("Длинна переданного сообщения ", data_len)
    # Декодируем, используя кодировку UTF-8. Можно использовать аргументы "utf8", "utf-8", "UTF8", "UTF-8", это одно и то же.
    return recv_packets(connection, data_len)

# Вспомогательная функция
def recv_packets(connection, n):
    piece = b''
    iteration = 1
    # Пока не получим кусок данных необходимой длины <b>n</b>
    while len(piece) < n:
        # Читаем участок длиной не более, чем нам недостаёт до длины <b>n</b>
        packet = connection.recv(n - len(piece))
        # Если пакет получить не удалось, то ничего не возвращаем
        if not packet:
            print("Пакет получить не удалось!!!")
            return None
        piece += packet
        print("Передача пакета итерация ", iteration)
        iteration += 1
    return piece

