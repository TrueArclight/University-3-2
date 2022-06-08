import socket, Protocol


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.19.98.76", 51017))
print("Подключение к серверу произошло успешно")
file = open("Image.jpg", mode="rb")
data = file.read()
Protocol.send(client, data)
file.close()
client.close()