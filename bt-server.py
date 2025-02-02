import socket
import serial
import time




server_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

server_sock.bind(("", 1))
print("Server is waiting for a connection...")


server_sock.listen(1)
sock, addr = server_sock.accept()

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

start = input()
if start != "n":
    while 1:
        if ser.in_waiting > 0:
            sock.send(ser.readline())
            #line = ser.readline().decode('utf-8').rstrip()
            #sock.send(line.encode('utf-8'))
        
        


sock.close()
server_sock.close()