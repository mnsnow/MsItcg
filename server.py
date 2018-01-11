# import socket
# import select
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# host = ''
# port = 5555
#
# s.bind((host, port))
#
# s.listen(5)
#
# c, addr = s.accept()
#
# print('Connection from: '+ str(addr))
#
# while 1:
#     data1 = c.recv(1024)
#     data = data1.decode()
#     if not data:
#         print('break while')
#         break
#     print('from connected user:' + str(data))
#     data = str(data).upper()
#     print('sending:' + str(data))
#     c.send(data.encode())
#
# c.close()
# print('55')

# # Use this to find local ip address
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# print(s.getsockname()[0])
# s.close()



import socket
import select
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 5555

s.bind((host, port))
s.listen(5)

c, addr = s.accept()

print('Connection from: '+ str(addr))

while 1:
    with open('connection.txt','r') as f:
        f.seek(0)
        for line in f:
            c.send(str(line).encode())
            print('sending:' + str(line))
    data1 = c.recv(1024)
    data = data1.decode()
    if not data:
        print('break while')
        break
    print('from connected user:' + str(data))



c.close()
print('55')
