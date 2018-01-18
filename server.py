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
            if 'USER_HAND_LIST' in line:
                user_hand_list_01 = str(line)
            if 'PLAYER_HAND_LIST' in line:
                player_hand_list_01 = str(line)
            if 'USER_HP' in line:
                user_hp_01 = str(line)
            if 'PLAYER_HP' in line:
                player_hp_01 = str(line)
            if 'USER_LV' in line:
                user_lv_01 = str(line)
            if 'PLAYER_LV' in line:
                player_lv_01 = str(line)
            if 'USER_MONSTER_LIST' in line:
                user_monster_list_01 = str(line)
            if 'PLAYER_MONSTER_LIST' in line:
                player_monster_list_01 = str(line)
            if 'USER_ITEM_LIST' in line:
                user_item_list_01 = str(line)
            if 'PLAYER_ITEM_LIST' in line:
                player_item_list_01 = str(line)
            if 'USER_MONSTER_HP' in line:
                user_monster_hp_01 = str(line)
            if 'PLAYER_MONSTER_HP' in line:
                player_monster_hp_01 = str(line)
            if 'USER_CHARACTER_UNDER' in line:
                user_character_under_01 = str(line)
            if 'PLAYER_CHARACTER_UNDER' in line:
                player_character_under_01 = str(line)
            if 'TURN_INDICATOR' in line:
                turn_indicator_01 = str(line)



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
            if 'USER_HAND_LIST' in line:
                user_hand_list_02 = str(line)
            if 'PLAYER_HAND_LIST' in line:
                player_hand_list_02 = str(line)
            if 'USER_HP' in line:
                user_hp_02 = str(line)
            if 'PLAYER_HP' in line:
                player_hp_02 = str(line)
            if 'USER_LV' in line:
                user_lv_02 = str(line)
            if 'PLAYER_LV' in line:
                player_lv_02 = str(line)
            if 'USER_MONSTER_LIST' in line:
                user_monster_list_02 = str(line)
            if 'PLAYER_MONSTER_LIST' in line:
                player_monster_list_02 = str(line)
            if 'USER_ITEM_LIST' in line:
                user_item_list_02 = str(line)
            if 'PLAYER_ITEM_LIST' in line:
                player_item_list_02 = str(line)
            if 'USER_MONSTER_HP' in line:
                user_monster_hp_02 = str(line)
            if 'PLAYER_MONSTER_HP' in line:
                player_monster_hp_02 = str(line)
            if 'USER_CHARACTER_UNDER' in line:
                user_character_under_02 = str(line)
            if 'PLAYER_CHARACTER_UNDER' in line:
                player_character_under_02 = str(line)
            if 'TURN_INDICATOR' in line:
                turn_indicator_02 = str(line)



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
    if user_hand_list_01 != user_hand_list_02:
        s.send(((str(user_hand_list_02)[:-1]+'||')*10).encode())
    if player_hand_list_01 != player_hand_list_02:
        s.send(((str(player_hand_list_02)[:-1]+'||')*10).encode())
    if user_hp_01 != user_hp_02:
        s.send(((str(user_hp_02)[:-1]+'||')*10).encode())
    if player_hp_01 != player_hp_02:
        s.send(((str(player_hp_02)[:-1]+'||')*10).encode())
    if user_lv_01 != user_lv_02:
        s.send(((str(user_lv_02)[:-1]+'||')*10).encode())
    if player_lv_01 != player_lv_02:
        s.send(((str(player_lv_02)[:-1]+'||')*10).encode())
    if user_monster_list_01 != user_monster_list_02:
        s.send(((str(user_monster_list_02)[:-1]+'||')*10).encode())
    if player_monster_list_01 != player_monster_list_02:
        s.send(((str(player_monster_list_02)[:-1]+'||')*10).encode())
    if user_item_list_01 != user_item_list_02:
        s.send(((str(user_item_list_02)[:-1]+'||')*10).encode())
    if player_item_list_01 != player_item_list_02:
        s.send(((str(player_item_list_02)[:-1]+'||')*10).encode())
    if user_monster_hp_01 != user_monster_hp_02:
        s.send(((str(user_monster_hp_02)[:-1]+'||')*10).encode())
    if player_monster_hp_01 != player_monster_hp_02:
        s.send(((str(player_monster_hp_02)[:-1]+'||')*10).encode())
    if user_character_under_01 != user_character_under_02:
        s.send(((str(user_character_under_02)[:-1]+'||')*10).encode())
    if player_character_under_01 != player_character_under_02:
        s.send(((str(player_character_under_02)[:-1]+'||')*10).encode())
    if turn_indicator_01 != turn_indicator_02:
        s.send(((str(turn_indicator_02)[:-1]+'||')*10).encode())


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
    user_hand_list = ''
    player_hand_list = ''
    user_hp = ''
    player_hp = ''
    user_lv = ''
    player_lv = ''
    user_monster_list = ''
    player_monster_list = ''
    user_item_list = ''
    player_item_list = ''
    user_monster_hp = ''
    player_monster_hp = ''
    user_character_under = ''
    player_character_under = ''
    turn_indicator = ''

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

    if 'USER_HAND_LIST' in data:
        aaa = data[data.find('USER_HAND_LIST'):]
        bbb = aaa[:aaa.find('||')]
        player_hand_list = str(bbb.replace('USER_HAND_LIST = ', ''))
        print('PLAYER_HAND_LIST---------: ' + player_hand_list + '.')

    if 'PLAYER_HAND_LIST' in data:
        aaa = data[data.find('PLAYER_HAND_LIST'):]
        bbb = aaa[:aaa.find('||')]
        user_hand_list = str(bbb.replace('PLAYER_HAND_LIST = ', ''))
        print('USER_HAND_LIST---------: ' + user_hand_list + '.')

    if 'USER_HP' in data:
        aaa = data[data.find('USER_HP'):]
        bbb = aaa[:aaa.find('||')]
        player_hp = str(bbb.replace('USER_HP = ', ''))
        print('PLAYER_HP---------: ' + player_hp + '.')

    if 'PLAYER_HP' in data:
        aaa = data[data.find('PLAYER_HP'):]
        bbb = aaa[:aaa.find('||')]
        user_hp = str(bbb.replace('PLAYER_HP = ', ''))
        print('USER_HP---------: ' + user_hp + '.')

    if 'USER_LV' in data:
        aaa = data[data.find('USER_LV'):]
        bbb = aaa[:aaa.find('||')]
        player_lv = str(bbb.replace('USER_LV = ', ''))
        print('PLAYER_LV---------: ' + player_lv + '.')

    if 'PLAYER_LV' in data:
        aaa = data[data.find('PLAYER_LV'):]
        bbb = aaa[:aaa.find('||')]
        user_lv = str(bbb.replace('PLAYER_LV = ', ''))
        print('USER_LV---------: ' + user_lv + '.')

    if 'USER_MONSTER_LIST' in data:
        aaa = data[data.find('USER_MONSTER_LIST'):]
        bbb = aaa[:aaa.find('||')]
        player_monster_list = str(bbb.replace('USER_MONSTER_LIST = ', ''))
        print('PLAYER_MONSTER_LIST---------: ' + player_monster_list + '.')

    if 'PLAYER_MONSTER_LIST' in data:
        aaa = data[data.find('PLAYER_MONSTER_LIST'):]
        bbb = aaa[:aaa.find('||')]
        user_monster_list = str(bbb.replace('PLAYER_MONSTER_LIST = ', ''))
        print('USER_MONSTER_LIST---------: ' + user_monster_list + '.')

    if 'USER_ITEM_LIST' in data:
        aaa = data[data.find('USER_ITEM_LIST'):]
        bbb = aaa[:aaa.find('||')]
        player_item_list = str(bbb.replace('USER_ITEM_LIST = ', ''))
        print('PLAYER_ITEM_LIST---------: ' + player_item_list + '.')

    if 'PLAYER_ITEM_LIST' in data:
        aaa = data[data.find('PLAYER_ITEM_LIST'):]
        bbb = aaa[:aaa.find('||')]
        user_item_list = str(bbb.replace('PLAYER_ITEM_LIST = ', ''))
        print('USER_ITEM_LIST---------: ' + user_item_list + '.')

    if 'USER_MONSTER_HP' in data:
        aaa = data[data.find('USER_MONSTER_HP'):]
        bbb = aaa[:aaa.find('||')]
        player_monster_hp = str(bbb.replace('USER_MONSTER_HP = ', ''))
        print('PLAYER_MONSTER_HP---------: ' + player_monster_hp + '.')

    if 'PLAYER_MONSTER_HP' in data:
        aaa = data[data.find('PLAYER_MONSTER_HP'):]
        bbb = aaa[:aaa.find('||')]
        user_monster_hp = str(bbb.replace('PLAYER_MONSTER_HP = ', ''))
        print('USER_MONSTER_HP---------: ' + user_monster_hp + '.')

    if 'USER_CHARACTER_UNDER' in data:
        aaa = data[data.find('USER_CHARACTER_UNDER'):]
        bbb = aaa[:aaa.find('||')]
        player_character_under = str(bbb.replace('USER_CHARACTER_UNDER = ', ''))
        print('PLAYER_CHARACTER_UNDER---------: ' + player_character_under + '.')

    if 'PLAYER_CHARACTER_UNDER' in data:
        aaa = data[data.find('PLAYER_CHARACTER_UNDER'):]
        bbb = aaa[:aaa.find('||')]
        user_character_under = str(bbb.replace('PLAYER_CHARACTER_UNDER = ', ''))
        print('USER_CHARACTER_UNDER---------: ' + user_character_under + '.')

    if 'TURN_INDICATOR' in data:
        aaa = data[data.find('TURN_INDICATOR'):]
        bbb = aaa[:aaa.find('||')]
        turn_indicator = str(bbb.replace('TURN_INDICATOR = ', ''))
        print('TURN_INDICATOR---------: ' + turn_indicator + '.')



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

        #write player_name
        if user_hand_list != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_HAND_LIST' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_HAND_LIST = ' + user_hand_list + '\n'

        #write player_name
        if player_hand_list != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_HAND_LIST' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_HAND_LIST = ' + player_hand_list + '\n'

        #write player_name
        if user_hp != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_HP' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_HP = ' + user_hp + '\n'

        #write player_name
        if player_hp != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_HP' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_HP = ' + player_hp+ '\n'

        #write player_name
        if user_lv != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_LV' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_LV = ' + user_lv + '\n'

        #write player_name
        if player_lv != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_LV' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_LV = ' + player_lv+ '\n'

        #write player_name
        if user_monster_list != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_MONSTER_LIST' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_MONSTER_LIST = ' + user_monster_list + '\n'

        #write player_name
        if player_monster_list != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_MONSTER_LIST' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_MONSTER_LIST = ' + player_monster_list + '\n'

        #write player_name
        if user_item_list != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_ITEM_LIST' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_ITEM_LIST = ' + user_item_list + '\n'

        #write player_name
        if player_item_list != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_ITEM_LIST' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_ITEM_LIST = ' + player_item_list + '\n'

        #write player_name
        if user_monster_hp != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_MONSTER_HP' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_MONSTER_HP = ' + user_monster_hp + '\n'

        #write player_name
        if player_monster_hp != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_MONSTER_HP' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_MONSTER_HP = ' + player_monster_hp + '\n'

        #write player_name
        if user_character_under != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_CHARACTER_UNDER' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_CHARACTER_UNDER = ' + user_character_under + '\n'

        #write player_name
        if player_character_under != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_CHARACTER_UNDER' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_CHARACTER_UNDER = ' + player_character_under + '\n'

        #write player_name
        if turn_indicator != '':
            y = 1
            f.seek(0)
            for line in f:
                if 'TURN_INDICATOR' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'TURN_INDICATOR = ' + turn_indicator + '\n'



    with open('connection.txt','w') as f:
        f.writelines(x)




s.close()













# --
