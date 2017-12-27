import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.1.34'
port = 5555

s.bind((host, port))

s.listen(1)

c, addr = sock.accept()
print('Connection from: '+ str(addr))

while 1:
    data = c.recv(1024)
    if not data:
        break
    print('from connected user:' + str(data))
    data = str(data).upper()
    print('sending:' + str(data))
    c.send(data)

c.close()


#
