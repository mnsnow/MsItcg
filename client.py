import socket

host = '192.168.1.34'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))

message = input(' --> ')

while message != 'q':
    pass
    s.send(message.encode())
    data1 = s.recv(2048)
    data = data1.decode()
    print('Received from server: ' + str(data))
    message = input(' --> ')

s.close()







#
