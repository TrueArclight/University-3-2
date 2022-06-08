import socket, Protocol

PORT = 51017
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print(f'Server ip {SERVER}')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(True)
print("Сервер ожидает подключение клиента")
client_data, client_address = server.accept()
print("Клиент подключен ", client_address)
file = open("Klyuchnikov_D_S_BVT-191/Information systems/LR2_/Image_Server.jpg", mode="wb")
data = Protocol.recv(client_data)
file.write(data)
file.close()


