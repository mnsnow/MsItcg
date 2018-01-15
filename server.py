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
            if 'LOBBY_PREPARE_TO_GO' in line:
                lobby_prepare_to_go_01 = str(line)
            if 'LOBBY_MY_READY_TO_GO' in line:
                lobby_my_ready_to_go_01 = str(line)
            if 'LOBBY_OTHER_READY_TO_GO' in line:
                lobby_other_ready_to_go_01 = str(line)
            if 'LOBBY_GAME_START' in line:
                lobby_game_start_01 = str(line)
            if 'USER_DECK_LIST' in line:
                user_deck_list_01 = str(line)
            if 'PLAYER_DECK_LIST' in line:
                player_deck_list_01 = str(line)
            if 'USER_CHARACTER_CARD' in line:
                user_character_card_01 = str(line)
            if 'PLAYER_CHARACTER_CARD' in line:
                player_character_card_01 = str(line)

    time.sleep(0.5)

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
            if 'LOBBY_PREPARE_TO_GO' in line:
                lobby_prepare_to_go_02 = str(line)
            if 'LOBBY_MY_READY_TO_GO' in line:
                lobby_my_ready_to_go_02 = str(line)
            if 'LOBBY_OTHER_READY_TO_GO' in line:
                lobby_other_ready_to_go_02 = str(line)
            if 'LOBBY_GAME_START' in line:
                lobby_game_start_02 = str(line)
            if 'USER_DECK_LIST' in line:
                user_deck_list_02 = str(line)
            if 'PLAYER_DECK_LIST' in line:
                player_deck_list_02 = str(line)
            if 'USER_CHARACTER_CARD' in line:
                user_character_card_02 = str(line)
            if 'PLAYER_CHARACTER_CARD' in line:
                player_character_card_02 = str(line)


    if user_name_01 != user_name_02:
        s.send(((str(user_name_02)[:-1]+'||')*10).encode())
    if player_name_01 != player_name_02:
        s.send(((str(player_name_02)[:-1]+'||')*10).encode())
    if exist_room_01 != exist_room_02:
        s.send(((str(exist_room_02)[:-1]+'||')*10).encode())
    if room_people_number_01 != room_people_number_02:
        s.send(((str(room_people_number_02)[:-1]+'||')*10).encode())
    if lobby_prepare_to_go_01 != lobby_prepare_to_go_02:
        s.send(((str(lobby_prepare_to_go_02)[:-1]+'||')*10).encode())
    if lobby_my_ready_to_go_01 != lobby_my_ready_to_go_02:
        s.send(((str(lobby_my_ready_to_go_02)[:-1]+'||')*10).encode())
    if lobby_other_ready_to_go_01 != lobby_other_ready_to_go_02:
        s.send(((str(lobby_other_ready_to_go_02)[:-1]+'||')*10).encode())
    if lobby_game_start_01 != lobby_game_start_02:
        s.send(((str(lobby_game_start_02)[:-1]+'||')*10).encode())
    if user_deck_list_01 != user_deck_list_02:
        s.send(((str(user_deck_list_02)[:-1]+'||')*10).encode())
    if player_deck_list_01 != player_deck_list_02:
        s.send(((str(player_deck_list_02)[:-1]+'||')*10).encode())
    if user_character_card_01 != user_character_card_02:
        s.send(((str(user_character_card_02)[:-1]+'||')*10).encode())
    if player_character_card_01 != player_character_card_02:
        s.send(((str(player_character_card_02)[:-1]+'||')*10).encode())


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
    lobby_prepare_to_go = ''
    lobby_my_ready_to_go = ''
    lobby_other_ready_to_go = ''
    lobby_game_start = ''
    user_deck_list = ''
    player_deck_list = ''
    user_character_card = ''
    player_character_card = ''

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

    if 'LOBBY_PREPARE_TO_GO' in data:
        aaa = data[data.find('LOBBY_PREPARE_TO_GO'):]
        bbb = aaa[:aaa.find('||')]
        lobby_prepare_to_go = str(bbb.replace('LOBBY_PREPARE_TO_GO = ', ''))
        print('LOBBY_PREPARE_TO_GO---------: ' + lobby_prepare_to_go + '.')

    if 'LOBBY_MY_READY_TO_GO' in data:
        aaa = data[data.find('LOBBY_MY_READY_TO_GO'):]
        bbb = aaa[:aaa.find('||')]
        lobby_my_ready_to_go = str(bbb.replace('LOBBY_MY_READY_TO_GO = ', ''))
        print('LOBBY_MY_READY_TO_GO---------: ' + lobby_my_ready_to_go + '.')

    if 'LOBBY_OTHER_READY_TO_GO' in data:
        aaa = data[data.find('LOBBY_OTHER_READY_TO_GO'):]
        bbb = aaa[:aaa.find('||')]
        lobby_other_ready_to_go = str(bbb.replace('LOBBY_OTHER_READY_TO_GO = ', ''))
        print('LOBBY_OTHER_READY_TO_GO---------: ' + lobby_other_ready_to_go + '.')

    if 'LOBBY_GAME_START' in data:
        aaa = data[data.find('LOBBY_GAME_START'):]
        bbb = aaa[:aaa.find('||')]
        lobby_game_start = str(bbb.replace('LOBBY_GAME_START = ', ''))
        print('LOBBY_GAME_START---------: ' + lobby_game_start + '.')

    if 'USER_DECK_LIST' in data:
        aaa = data[data.find('USER_DECK_LIST'):]
        bbb = aaa[:aaa.find('||')]
        player_deck_list = str(bbb.replace('USER_DECK_LIST = ', ''))
        print('PLAYER_DECK_LIST---------: ' + player_deck_list + '.')

    if 'PLAYER_DECK_LIST' in data:
        aaa = data[data.find('PLAYER_DECK_LIST'):]
        bbb = aaa[:aaa.find('||')]
        user_deck_list = str(bbb.replace('PLAYER_DECK_LIST = ', ''))
        print('USER_DECK_LIST---------: ' + user_deck_list + '.')

    if 'USER_CHARACTER_CARD' in data:
        aaa = data[data.find('USER_CHARACTER_CARD'):]
        bbb = aaa[:aaa.find('||')]
        player_character_card = str(bbb.replace('USER_CHARACTER_CARD = ', ''))
        print('PLAYER_CHARACTER_CARD---------: ' + player_character_card + '.')

    if 'PLAYER_DECK_LIST' in data:
        aaa = data[data.find('PLAYER_DECK_LIST'):]
        bbb = aaa[:aaa.find('||')]
        user_character_card = str(bbb.replace('PLAYER_DECK_LIST = ', ''))
        print('USER_DECK_LIST---------: ' + user_character_card + '.')



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

        #write player_name
        if lobby_prepare_to_go != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'LOBBY_PREPARE_TO_GO' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'LOBBY_PREPARE_TO_GO = ' + lobby_prepare_to_go + '\n'

        #write player_name
        if lobby_my_ready_to_go != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'LOBBY_MY_READY_TO_GO' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'LOBBY_MY_READY_TO_GO = ' + lobby_my_ready_to_go + '\n'

        #write player_name
        if lobby_other_ready_to_go != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'LOBBY_OTHER_READY_TO_GO' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'LOBBY_OTHER_READY_TO_GO = ' + lobby_other_ready_to_go + '\n'

        #write player_name
        if lobby_game_start != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'LOBBY_GAME_START' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'LOBBY_GAME_START = ' + lobby_game_start + '\n'

        #write player_name
        if user_deck_list != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_DECK_LIST' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_DECK_LIST = ' + user_deck_list + '\n'

        #write player_name
        if player_deck_list != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_DECK_LIST' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_DECK_LIST = ' + player_deck_list + '\n'

        #write player_name
        if user_character_card != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_CHARACTER_CARD' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_CHARACTER_CARD = ' + user_character_card + '\n'

        #write player_name
        if player_character_card != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_CHARACTER_CARD' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_CHARACTER_CARD = ' + player_character_card + '\n'



    with open('connection.txt','w') as f:
        f.writelines(x)




s.close()













# --
