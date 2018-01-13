import socket
import select
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 5555

sock.bind((host, port))
sock.listen(5)

s, addr = sock.accept()

while 1:

    # Sending data
    with open('connection.txt','r') as f:
        f.seek(0)
        for line in f:
            if 'USER_NAME' in line:
                user_name_01 = str(line)
            if 'PLAYER_NAME' in line:
                player_name_01 = str(line)
            if 'EXIST_ROOM' in line:
                exist_room_01 = str(line)
            if 'ROOM_PEOPLE_NUMBER' in line:
                room_people_number_01 = str(line)

    time.sleep(0.3)

    with open('connection.txt','r') as f:
        f.seek(0)
        for line in f:
            if 'USER_NAME' in line:
                user_name_02 = str(line)
            if 'PLAYER_NAME' in line:
                player_name_02 = str(line)
            if 'EXIST_ROOM' in line:
                exist_room_02 = str(line)
            if 'ROOM_PEOPLE_NUMBER' in line:
                room_people_number_02 = str(line)

    if user_name_01 != user_name_02:
        s.send(((str(user_name_02)[:-1]+'||')*10).encode())
    if player_name_01 != player_name_02:
        s.send(((str(player_name_02)[:-1]+'||')*10).encode())
    if exist_room_01 != exist_room_02:
        s.send(((str(exist_room_02)[:-1]+'||')*10).encode())
    if room_people_number_01 != room_people_number_02:
        s.send(((str(room_people_number_02)[:-1]+'||')*10).encode())


    s.send(('lalala'*10).encode())
    # Reciving data
    data1 = s.recv(1024)
    data = data1.decode()
    if not data:
        print('break while')
        break

    user_name = ''
    player_name = ''
    user_character_hp = ''
    exist_room = ''
    room_people_number = ''
    # get variables from data
    if 'USER_NAME' in data:
        aaa = data[data.find('USER_NAME'):]
        bbb = aaa[:aaa.find('||')]
        player_name = str(bbb.replace('USER_NAME = ', ''))
        print('PLAYER_NAME---------: ' + player_name + '.')

    if 'PLAYER_NAME' in data:
        aaa = data[data.find('PLAYER_NAME'):]
        bbb = aaa[:aaa.find('||')]
        user_name = str(bbb.replace('PLAYER_NAME = ', ''))
        print('USER_NAME---------: ' + user_name + '.')

    if 'EXIST_ROOM' in data:
        aaa = data[data.find('EXIST_ROOM'):]
        bbb = aaa[:aaa.find('||')]
        player_name = str(bbb.replace('EXIST_ROOM = ', ''))
        exist_room = str(bbb.replace('EXIST_ROOM = ', ''))
        print('EXIST_ROOM---------: ' + exist_room + '.')

    if 'ROOM_PEOPLE_NUMBER' in data:
        aaa = data[data.find('ROOM_PEOPLE_NUMBER'):]
        bbb = aaa[:aaa.find('||')]
        room_people_number = str(bbb.replace('ROOM_PEOPLE_NUMBER = ', ''))
        print('ROOM_PEOPLE_NUMBER---------: ' + room_people_number + '.')

    # Writing into the file
    with open('connection.txt','a+') as f:
        f.seek(0)
        x = f.readlines()

        #write user_name
        if user_name != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_NAME' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_NAME = ' + user_name + '\n'


        #write player_name
        if player_name != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_NAME' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_NAME = ' + player_name + '\n'

        #write exist room
        if exist_room != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'EXIST_ROOM' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'EXIST_ROOM = ' + exist_room + '\n'

        #write player_name
        if room_people_number != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'ROOM_PEOPLE_NUMBER' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'ROOM_PEOPLE_NUMBER = ' + room_people_number + '\n'


    with open('connection.txt','w') as f:
        f.writelines(x)




s.close()













# --
