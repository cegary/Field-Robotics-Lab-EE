import socket
import setup

server_mac_address = "d8:3a:dd:6d:2f:b8"

client_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
setup.init()
try:
    client_sock.connect((server_mac_address, 1))

    while 1:
        data = client_sock.recv(1024).decode('utf-8') 
        if(data.decode('utf-8') == "KILL"):
            break
        elif data[0:3] == "btn:":
            speed = 0
        else:
            m = int(data[2:])
            if m > 1023:
                speed = 1000
            elif m < 0:
                speed = -1000
            elif m == 512:
                speed = 0
            else:
                if m > 512:
                    speed = max(1000, (m-512)*2)
                else:
                    speed = min(-1000, (m-512)*2)
        setup.move(speed)         

except KeyboardInterrupt as ke:
   client_sock.close()