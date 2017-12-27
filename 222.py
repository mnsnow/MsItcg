import socket

host = '192.168.1.34'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))

message = raw_input(' --> ')

while message != 'q':
    s.send(message)
    data = s.recv(1024)
    print('Received from server' + str(data))
    message = raw_input(' --> ')

s.close()







#
