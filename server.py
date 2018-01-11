import socket
import select
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 5555

s.bind((host, port))
s.listen(5)

c, addr = s.accept()

while 1:

    # Sending data
    with open('connection.txt','r') as f:
        f.seek(0)
        for line in f:
            if 'USER_NAME' in line:
                user_name_01 = str(line)
            if 'PLAYER_NAME' in line:
                player_name_01 = str(line)
            if 'USER_CHARACTER_HP' in line:
                user_character_hp_01 = str(line)

    time.sleep(0.3)

    with open('connection.txt','r') as f:
        f.seek(0)
        for line in f:
            if 'USER_NAME' in line:
                user_name_02 = str(line)
            if 'PLAYER_NAME' in line:
                player_name_02 = str(line)
            if 'USER_CHARACTER_HP' in line:
                user_character_hp_02 = str(line)

    if user_name_01 != user_name_02:
        c.send(((str(user_name_02)[:-1]+'||')*10).encode())
    if player_name_01 != player_name_02:
        c.send(((str(player_name_02)[:-1]+'||')*10).encode())
    if user_character_hp_01 != user_character_hp_02:
        c.send(((str(user_character_hp_02)[:-1]+'||')*10).encode())

    c.send(('lalala'*10).encode())
    # Reciving data
    data1 = c.recv(1024)
    data = data1.decode()
    if not data:
        print('break while')
        break

    user_name = ''
    player_name = ''
    user_character_hp = ''
    # get variables from data
    if 'USER_NAME' in data:
        aaa = data[data.find('USER_NAME'):]
        bbb = aaa[:aaa.find('||')]
        user_name = str(bbb.replace('USER_NAME = ', ''))
        print('USER_NAME---------: ' + user_name + '.')

    if 'PLAYER_NAME' in data:
        aaa = data[data.find('PLAYER_NAME'):]
        bbb = aaa[:aaa.find('||')]
        player_name = str(bbb.replace('PLAYER_NAME = ', ''))
        print('PLAYER_NAME---------: ' + player_name + '.')

    if 'USER_CHARACTER_HP' in data:
        aaa = data[data.find('USER_CHARACTER_HP'):]
        bbb = aaa[:aaa.find('||')]
        user_character_hp = str(bbb.replace('USER_CHARACTER_HP = ', ''))
        print('USER_CHARACTER_HP---------: ' + user_character_hp + '.')



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

        #write user.character_card.health
        if user_character_hp != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_CHARACTER_HP' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_CHARACTER_HP = ' + user_character_hp + '\n'


    with open('connection.txt','w') as f:
        f.writelines(x)




c.close()













# --
