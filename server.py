import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 5555

s.bind((host, port))

s.listen(1)

c, addr = s.accept()
print('Connection from: '+ str(addr))

while 1:
    data1 = c.recv(1024)
    data = data1.decode()
    if not data:
        break
    print('from connected user:' + str(data))
    data = str(data).upper()
    print('sending:' + str(data))
    c.send(data.encode())

c.close()


#
