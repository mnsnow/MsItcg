# import socket
#
# host = '192.168.1.34'
# port = 5555
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# s.connect((host,port))
# print('11')
# message = input(' --> ')
# print('22')
# while message != 'q':
#     print('2.5')
#     s.send(message.encode())
#     print('33')
#     data1 = s.recv(2048)
#     data = data1.decode()
#     print('Received from server: ' + str(data))
#     message = input(' --> ')
#
# s.close()
# print('44')

import socket

host = '192.168.1.34'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))

while 1:
    with open('connection.txt','r') as f:
        f.seek(0)
        for line in f:
            s.send(str(line).encode())
            print('sending:' + str(line))
    data1 = s.recv(1024)
    data = data1.decode()
    if not data:
        print('break while')
        break
    print('Received from server: ' + str(data))

s.close()




#
