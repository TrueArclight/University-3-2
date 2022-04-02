import can

bus = can.Bus(channel='vcan0', interface='socketcan')
message = bus.recv()
print(message)