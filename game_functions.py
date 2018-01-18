import sys
import random
import pygame
import socket
from pygame.locals import *
from card_database import *
from card import Character, Monster, Tactic, Item
from settings import Settings
from button import Button
from display import Screen_status, Button_status
from grid import Grid
import card_database_filter as cdf
from action import Action
from builtins import any
import time


#------------------------------Networking------------------------------------------------------

def read_network_variables(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ read variables for multiplayer form text file"""
    with open('connection.txt','r') as f:
        f.seek(0)
        for line in f:
            if 'PLAYER_NAME' in line:
                player2.name = str(line.replace('PLAYER_NAME = ', ''))[:-1]
                player2.name_copy = str(line.replace('PLAYER_NAME = ', ''))[:-1]
            if 'USER_NAME' in line:
                user.name = str(line.replace('USER_NAME = ', ''))[:-1]
                user.name_copy = str(line.replace('USER_NAME = ', ''))[:-1]
            if 'EXIST_ROOM' in line:
                if 'N/A' not in line:
                    button_status.lobby_screen_room_list_display = str(line.replace('EXIST_ROOM = ', ''))[:-1]
                    button_status.lobby_screen_room_list_display_copy = str(line.replace('EXIST_ROOM = ', ''))[:-1]
                else:
                    button_status.lobby_screen_room_list_display = 'N/A'
                    button_status.lobby_screen_room_list_display_copy = 'N/A'
            if 'ROOM_PEOPLE_NUMBER' in line:
                if str(line.replace('ROOM_PEOPLE_NUMBER = ', ''))[:-1] == '0':
                    button_status.lobby_screen_room_status = '0/2'
                    button_status.lobby_screen_room_status_copy = '0/2'
                elif str(line.replace('ROOM_PEOPLE_NUMBER = ', ''))[:-1] == '1':
                    button_status.lobby_screen_room_status = '1/2'
                    button_status.lobby_screen_room_status_copy = '1/2'
                elif str(line.replace('ROOM_PEOPLE_NUMBER = ', ''))[:-1] == '2':
                    button_status.lobby_screen_room_status = '2/2'
                    button_status.lobby_screen_room_status_copy = '2/2'
            if 'LOBBY_PREPARE_TO_GO' in line:
                if 'False' in line:
                    button_status.lobby_screen_prepare_to_go_display = False
                    button_status.lobby_screen_prepare_to_go_display_copy = False
                elif 'True' in line:
                    button_status.lobby_screen_prepare_to_go_display = True
                    button_status.lobby_screen_prepare_to_go_display_copy = True
            if 'LOBBY_MY_READY_TO_GO' in line:
                if 'False' in line:
                    button_status.lobby_screen_my_ready_to_go = False
                    button_status.lobby_screen_my_ready_to_go_copy = False
                elif 'True' in line:
                    button_status.lobby_screen_my_ready_to_go = True
                    button_status.lobby_screen_my_ready_to_go_copy = True
            if 'LOBBY_OTHER_READY_TO_GO' in line:
                if 'False' in line:
                    button_status.lobby_screen_other_ready_to_go = False
                    button_status.lobby_screen_other_ready_to_go_copy = False
                elif 'True' in line:
                    button_status.lobby_screen_other_ready_to_go = True
                    button_status.lobby_screen_other_ready_to_go_copy = True
            if 'LOBBY_GAME_START' in line:
                if 'False' in line:
                    button_status.lobby_screen_game_start = False
                    button_status.lobby_screen_game_start_copy = False
                elif 'True' in line:
                    button_status.lobby_screen_game_start = True
                    button_status.lobby_screen_game_start_copy = True
            # if 'USER_DECK_LIST' in line:
            #     user.deck_list = make_deck_from_string(line.replace('USER_DECK_LIST = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            #     user.deck_list_copy = make_deck_from_string(line.replace('USER_DECK_LIST = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            if 'PLAYER_DECK_LIST' in line:
                player2.deck_list = make_deck_from_string(line.replace('PLAYER_DECK_LIST = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                player2.deck_list_copy = make_deck_from_string(line.replace('PLAYER_DECK_LIST = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            # if 'USER_CHARACTER_CARD' in line:
            #     if line.replace('USER_CHARACTER_CARD = ', '')[:-1] == '[]':
            #         user.character_card = []
            #         user.character_card_copy = []
            #     else:
            #         user.character_card = make_deck_from_string(line.replace('USER_CHARACTER_CARD = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
            #         user.character_card_copy = make_deck_from_string(line.replace('USER_CHARACTER_CARD = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
            if 'PLAYER_CHARACTER_CARD' in line:
                if line.replace('PLAYER_CHARACTER_CARD = ', '')[:-1] == '[]':
                    player2.character_card = []
                    player2.character_card_copy = []
                else:
                    try:
                        player2.character_card = make_deck_from_string(str(line.replace('PLAYER_CHARACTER_CARD = ', ''))[:-1], ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
                        player2.character_card_copy = make_deck_from_string(line.replace('PLAYER_CHARACTER_CARD = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
                    except IndexError:
                        pass
            # if 'USER_HAND_LIST' in line:
            #     user.hand_list = make_deck_from_string(line.replace('USER_HAND_LIST = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            #     user.hand_list_copy = make_deck_from_string(line.replace('USER_HAND_LIST = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            if 'PLAYER_HAND_LIST' in line:
                player2.hand_list = make_deck_from_string(line.replace('PLAYER_HAND_LIST = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                player2.hand_list_copy = make_deck_from_string(line.replace('PLAYER_HAND_LIST = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            if 'USER_HP' in line:
                try:
                    user.character_card.health = str(line.replace('USER_HP = ', ''))[:-1]
                    user.character_card_health_copy = str(line.replace('USER_HP = ', ''))[:-1]
                except:
                    pass
            if 'PLAYER_HP' in line:
                try:
                    player2.character_card.health = str(line.replace('PLAYER_HP = ', ''))[:-1]
                    player2.character_card_health_copy = str(line.replace('PLAYER_HP = ', ''))[:-1]
                except:
                    pass
            if 'USER_LV' in line:
                try:
                    user.character_card.level = str(line.replace('USER_LV = ', ''))[:-1]
                    user.character_card_level_copy = str(line.replace('USER_LV = ', ''))[:-1]
                except:
                    pass
            if 'PLAYER_LV' in line:
                try:
                    player2.character_card.level = str(line.replace('PLAYER_LV = ', ''))[:-1]
                    player2.character_card_level_copy = str(line.replace('PLAYER_LV = ', ''))[:-1]
                except:
                    pass

            if 'USER_MONSTER_LIST' in line:
                ls = eval(str(line.replace('USER_MONSTER_LIST = ', ''))[:-1])
                for i in range(6):
                    if ls[i] != '':
                        user.monster_in_play_dict[str(i+1)] = eval(ls[i])
                        user.monster_in_play_dict_copy[str(i+1)] = eval(ls[i])
            if 'PLAYER_MONSTER_LIST' in line:
                ls = eval(str(line.replace('PLAYER_MONSTER_LIST = ', ''))[:-1])
                for i in range(6):
                    if ls[i] != '':
                        player2.monster_in_play_dict[str(i+1)] = eval(ls[i])
                        player2.monster_in_play_dict_copy[str(i+1)] = eval(ls[i])
            if 'USER_ITEM_LIST' in line:
                ls = eval(str(line.replace('USER_ITEM_LIST = ', ''))[:-1])
                for i in range(6):
                    if ls[i] != '':
                        user.item_in_play_dict[str(i+1)] = eval(ls[i])
                        user.item_in_play_dict_copy[str(i+1)] = eval(ls[i])
            if 'PLAYER_ITEM_LIST' in line:
                ls = eval(str(line.replace('PLAYER_ITEM_LIST = ', ''))[:-1])
                for i in range(6):
                    if ls[i] != '':
                        player2.item_in_play_dict[str(i+1)] = eval(ls[i])
                        player2.item_in_play_dict_copy[str(i+1)] = eval(ls[i])
            if 'USER_MONSTER_HP' in line:
                ls = eval(str(line.replace('USER_MONSTER_HP = ', ''))[:-1])
                for i in range(6):
                    if ls[i] != '':
                        user.monster_in_play_dict[str(i+1)].health = ls[i]
                        user.monster_in_play_dict_copy[str(i+1)].health = ls[i]
            if 'PLAYER_MONSTER_HP' in line:
                ls = eval(str(line.replace('PLAYER_MONSTER_HP = ', ''))[:-1])
                for i in range(6):
                    if ls[i] != '':
                        player2.monster_in_play_dict[str(i+1)].health = ls[i]
                        player2.monster_in_play_dict_copy[str(i+1)].health = ls[i]
            if 'USER_CHARACTER_UNDER' in line:
                ls = eval(str(line.replace('USER_CHARACTER_UNDER = ', ''))[:-1])
                for i in range(15):
                    if ls[i] != '':
                        user.character_under_card_by_level[str(10*(i+1))] = eval(ls[i])
                        user.character_under_card_by_level_copy[str(10*i+1)] = eval(ls[i])
            if 'PLAYER_CHARACTER_UNDER' in line:
                ls = eval(str(line.replace('PLAYER_CHARACTER_UNDER = ', ''))[:-1])
                for i in range(15):
                    if ls[i] != '':
                        player2.character_under_card_by_level[str(10*(i+1))] = eval(ls[i])
                        player2.character_under_card_by_level_copy[str(10*i+1)] = eval(ls[i])
            if 'TURN_INDICATOR' in line:
                if 'my' in line:
                    button_status.battle_screen_pvp_turn_indicator = 'my'
                    button_status.battle_screen_pvp_turn_indicator_copy = 'my'
                elif 'other' in line:
                    button_status.battle_screen_pvp_turn_indicator = 'other'
                    button_status.battle_screen_pvp_turn_indicator_copy = 'other'

def write_network_variables(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ Write variables for multiplyaer from text file"""
    with open('connection.txt','a+') as f:
        f.seek(0)
        x = f.readlines()

        #write user_name
        if user.name != user.name_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_NAME' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_NAME = ' + user.name + '\n'

        #write player_name
        if player2.name != player2.name_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_NAME' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'PLAYER_NAME = ' + player2.name + '\n'


        #write esist room
        if button_status.lobby_screen_room_list_display != button_status.lobby_screen_room_list_display_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'EXIST_ROOM' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'EXIST_ROOM = ' + button_status.lobby_screen_room_list_display + '\n'

        #write number of people in room
        if button_status.lobby_screen_room_status != button_status.lobby_screen_room_status_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'ROOM_PEOPLE_NUMBER' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'ROOM_PEOPLE_NUMBER = ' + str(button_status.lobby_screen_room_status[0]) + '\n'

        #write number of people in room
        if button_status.lobby_screen_prepare_to_go_display != button_status.lobby_screen_prepare_to_go_display_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'LOBBY_PREPARE_TO_GO' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'LOBBY_PREPARE_TO_GO = ' + str(button_status.lobby_screen_prepare_to_go_display) + '\n'

        #write number of people in room
        if button_status.lobby_screen_my_ready_to_go != button_status.lobby_screen_my_ready_to_go_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'LOBBY_MY_READY_TO_GO' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'LOBBY_MY_READY_TO_GO = ' + str(button_status.lobby_screen_my_ready_to_go) + '\n'

        #write number of people in room
        if button_status.lobby_screen_other_ready_to_go != button_status.lobby_screen_other_ready_to_go_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'LOBBY_OTHER_READY_TO_GO' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'LOBBY_OTHER_READY_TO_GO = ' + str(button_status.lobby_screen_other_ready_to_go) + '\n'

        #write number of people in room
        if button_status.lobby_screen_game_start != button_status.lobby_screen_game_start_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'LOBBY_GAME_START' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'LOBBY_GAME_START = ' + str(button_status.lobby_screen_game_start) + '\n'

        #write number of people in room
        if len(user.deck_list) != len(user.deck_list_copy):
            y = 1
            f.seek(0)
            deck_list_string = []
            for card in user.deck_list:
                deck_list_string.append('CARD_' + card.set_number + '_' + card.card_number)
            for line in f:
                if 'USER_DECK_LIST' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'USER_DECK_LIST = ' + str(deck_list_string) + '\n'

        #write number of people in room
        if type(user.character_card) != type(user.character_card_copy):
            y = 1
            f.seek(0)
            character_string = ['CARD_' + user.character_card.set_number + '_' + user.character_card.card_number]
            for line in f:
                if 'USER_CHARACTER_CARD' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'USER_CHARACTER_CARD = ' + str(character_string) + '\n'

        #write number of people in room
        if len(player2.deck_list) != len(player2.deck_list_copy):
            y = 1
            f.seek(0)
            deck_list_string = []
            for card in player2.deck_list:
                deck_list_string.append('CARD_' + card.set_number + '_' + card.card_number)
            for line in f:
                if 'PLAYER_DECK_LIST' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'PLAYER_DECK_LIST = ' + str(deck_list_string) + '\n'

        #write number of people in room
        if type(player2.character_card) != type(player2.character_card_copy):
            y = 1
            f.seek(0)
            character_string = ['CARD_' + player2.character_card.set_number + '_' + player2.character_card.card_number]
            for line in f:
                if 'PLAYER_CHARACTER_CARD' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'PLAYER_CHARACTER_CARD = ' + str(character_string) + '\n'

        #write number of people in room
        if len(user.hand_list) != len(user.hand_list_copy):
            y = 1
            f.seek(0)
            deck_list_string = []
            for card in user.hand_list:
                deck_list_string.append('CARD_' + card.set_number + '_' + card.card_number)
            for line in f:
                if 'USER_HAND_LIST' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'USER_HAND_LIST = ' + str(deck_list_string) + '\n'

        #write number of people in room
        if len(player2.hand_list) != len(player2.hand_list_copy):
            y = 1
            f.seek(0)
            deck_list_string = []
            for card in player2.hand_list:
                deck_list_string.append('CARD_' + card.set_number + '_' + card.card_number)
            for line in f:
                if 'PLAYER_HAND_LIST' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'PLAYER_HAND_LIST = ' + str(deck_list_string) + '\n'

        #write number of people in room
        if user.character_card != [] and user.character_card.health != user.character_card_health_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_HP' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'USER_HP = ' + str(user.character_card.health) + '\n'

        #write number of people in room
        if player2.character_card != [] and player2.character_card.health != player2.character_card_health_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_HP' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'PLAYER_HP = ' + str(player2.character_card.health) + '\n'

        #write number of people in room
        if user.character_card != [] and user.character_card.level != user.character_card_level_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_LV' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'USER_LV = ' + str(user.character_card.level) + '\n'

        #write number of people in room
        if player2.character_card != [] and player2.character_card.level != player2.character_card_level_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'PLAYER_LV' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'PLAYER_LV = ' + str(player2.character_card.level) + '\n'

        #write number of people in room
        for i in range(6):
            if user.monster_in_play_dict[str(i+1)] != user.monster_in_play_dict_copy[str(i+1)]:
                y = 1
                f.seek(0)
                deck_list_string = []
                for i in range(6):
                    card = user.monster_in_play_dict[str(i+1)]
                    if card != '':
                        deck_list_string.append('card_' + card.set_number + '_' + card.card_number)
                    else:
                        deck_list_string.append('')
                for line in f:
                    if 'USER_MONSTER_LIST' not in line:
                        y += 1
                    else:
                        break

                x[y-1] = 'USER_MONSTER_LIST = ' + str(deck_list_string) + '\n'
                break

        #write number of people in room
        for i in range(6):
            if player2.monster_in_play_dict[str(i+1)] != player2.monster_in_play_dict_copy[str(i+1)]:
                y = 1
                f.seek(0)
                deck_list_string = []
                for i in range(6):
                    card = player2.monster_in_play_dict[str(i+1)]
                    if card != '':
                        deck_list_string.append('card_' + card.set_number + '_' + card.card_number)
                    else:
                        deck_list_string.append('')
                for line in f:
                    if 'PLAYER_MONSTER_LIST' not in line:
                        y += 1
                    else:
                        break

                x[y-1] = 'PLAYER_MONSTER_LIST = ' + str(deck_list_string) + '\n'
                break

        #write number of people in room
        for i in range(6):
            if user.item_in_play_dict[str(i+1)] != user.item_in_play_dict_copy[str(i+1)]:
                y = 1
                f.seek(0)
                deck_list_string = []
                for i in range(6):
                    card = user.item_in_play_dict[str(i+1)]
                    if card != '':
                        deck_list_string.append('card_' + card.set_number + '_' + card.card_number)
                    else:
                        deck_list_string.append('')
                for line in f:
                    if 'USER_ITEM_LIST' not in line:
                        y += 1
                    else:
                        break

                x[y-1] = 'USER_ITEM_LIST = ' + str(deck_list_string) + '\n'
                break

        #write number of people in room
        for i in range(6):
            if player2.item_in_play_dict[str(i+1)] != player2.item_in_play_dict_copy[str(i+1)]:
                y = 1
                f.seek(0)
                deck_list_string = []
                for i in range(6):
                    card = player2.item_in_play_dict[str(i+1)]
                    if card != '':
                        deck_list_string.append('card_' + card.set_number + '_' + card.card_number)
                    else:
                        deck_list_string.append('')
                for line in f:
                    if 'PLAYER_ITEM_LIST' not in line:
                        y += 1
                    else:
                        break

                x[y-1] = 'PLAYER_ITEM_LIST = ' + str(deck_list_string) + '\n'
                break

        #write number of people in room
        for i in range(6):
            if user.monster_in_play_dict[str(i+1)] != '' and user.monster_in_play_dict[str(i+1)].health != user.monster_in_play_dict_copy[str(i+1)].health:
                y = 1
                f.seek(0)
                deck_list_string = []
                for i in range(6):
                    card = user.monster_in_play_dict[str(i+1)]
                    if card != '':
                        deck_list_string.append("'" + card.health +"'")
                    else:
                        deck_list_string.append('')
                for line in f:
                    if 'USER_MONSTER_HP' not in line:
                        y += 1
                    else:
                        break

                x[y-1] = 'USER_MONSTER_HP = ' + str(deck_list_string) + '\n'
                break

        #write number of people in room
        for i in range(6):
            if player2.monster_in_play_dict[str(i+1)] != '' and player2.monster_in_play_dict[str(i+1)].health != player2.monster_in_play_dict_copy[str(i+1)].health:
                y = 1
                f.seek(0)
                deck_list_string = []
                for i in range(6):
                    card = player2.monster_in_play_dict[str(i+1)]
                    if card != '':
                        deck_list_string.append("'" + card.health +"'")
                    else:
                        deck_list_string.append('')
                for line in f:
                    if 'PLAYER_MONSTER_HP' not in line:
                        y += 1
                    else:
                        break

                x[y-1] = 'PLAYER_MONSTER_HP = ' + str(deck_list_string) + '\n'
                break

        #write number of people in room
        for i in range(15):
            if user.character_under_card_by_level[str(10*(i+1))] != user.character_under_card_by_level_copy[str(10*(i+1))]:
                y = 1
                f.seek(0)
                deck_list_string = []
                for i in range(15):
                    card = user.character_under_card_by_level[str(10*(i+1))]
                    if card != '':
                        deck_list_string.append('card_' + card.set_number + '_' + card.card_number)
                    else:
                        deck_list_string.append('')
                for line in f:
                    if 'USER_CHARACTER_UNDER' not in line:
                        y += 1
                    else:
                        break

                x[y-1] = 'USER_CHARACTER_UNDER = ' + str(deck_list_string) + '\n'
                break

        #write number of people in room
        for i in range(15):
            if player2.character_under_card_by_level[str(10*(i+1))] != player2.character_under_card_by_level_copy[str(10*(i+1))]:
                y = 1
                f.seek(0)
                deck_list_string = []
                for i in range(15):
                    card = player2.character_under_card_by_level[str(10*(i+1))]
                    if card != '':
                        deck_list_string.append('card_' + card.set_number + '_' + card.card_number)
                    else:
                        deck_list_string.append('')
                for line in f:
                    if 'PLAYER_CHARACTER_UNDER' not in line:
                        y += 1
                    else:
                        break

                x[y-1] = 'PLAYER_CHARACTER_UNDER = ' + str(deck_list_string) + '\n'
                break

        #write number of people in room
        if button_status.battle_screen_pvp_turn_indicator != button_status.battle_screen_pvp_turn_indicator_copy:
            y = 1
            f.seek(0)
            for line in f:
                if 'TURN_INDICATOR' not in line:
                    y += 1
                else:
                    break

            x[y-1] = 'TURN_INDICATOR = ' + str(button_status.battle_screen_pvp_turn_indicator) + '\n'


    with open('connection.txt','w') as f:
        f.writelines(x)

def clear_text_file(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ clear text file each time restart the game"""
    player2.identity = 'AI'
    with open('connection.txt','a+') as f:
        f.seek(0)
        x = f.readlines()

        #write player_name
        y = 1
        f.seek(0)
        for line in f:
            if 'PLAYER_NAME' not in line:
                y += 1
            else:
                break
        x[y-1] = 'PLAYER_NAME = Player' + '\n'


        #write esist room
        y = 1
        f.seek(0)
        for line in f:
            if 'EXIST_ROOM' not in line:
                y += 1
            else:
                break
        x[y-1] = 'EXIST_ROOM = N/A' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'ROOM_PEOPLE_NUMBER' not in line:
                y += 1
            else:
                break
        x[y-1] = 'ROOM_PEOPLE_NUMBER = 0' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'LOBBY_PREPARE_TO_GO' not in line:
                y += 1
            else:
                break
        x[y-1] = 'LOBBY_PREPARE_TO_GO = False' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'LOBBY_MY_READY_TO_GO' not in line:
                y += 1
            else:
                break
        x[y-1] = 'LOBBY_MY_READY_TO_GO = False' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'LOBBY_OTHER_READY_TO_GO' not in line:
                y += 1
            else:
                break
        x[y-1] = 'LOBBY_OTHER_READY_TO_GO = False' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'LOBBY_GAME_START' not in line:
                y += 1
            else:
                break
        x[y-1] = 'LOBBY_GAME_START = False' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'USER_DECK_LIST' not in line:
                y += 1
            else:
                break
        x[y-1] = 'USER_DECK_LIST = []' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'PLAYER_DECK_LIST' not in line:
                y += 1
            else:
                break
        x[y-1] = 'PLAYER_DECK_LIST = []' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'USER_CHARACTER_CARD' not in line:
                y += 1
            else:
                break
        x[y-1] = 'USER_CHARACTER_CARD = []' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'PLAYER_CHARACTER_CARD' not in line:
                y += 1
            else:
                break
        x[y-1] = 'PLAYER_CHARACTER_CARD = []' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'USER_HAND_LIST' not in line:
                y += 1
            else:
                break
        x[y-1] = 'USER_HAND_LIST = []' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'PLAYER_HAND_LIST' not in line:
                y += 1
            else:
                break
        x[y-1] = 'PLAYER_HAND_LIST = []' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'USER_HP' not in line:
                y += 1
            else:
                break
        x[y-1] = 'USER_HP = 0' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'PLAYER_HP' not in line:
                y += 1
            else:
                break
        x[y-1] = 'PLAYER_HP = 0' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'USER_LV' not in line:
                y += 1
            else:
                break
        x[y-1] = 'USER_LV = 0' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'PLAYER_LV' not in line:
                y += 1
            else:
                break
        x[y-1] = 'PLAYER_LV = 0' + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'USER_MONSTER_LIST' not in line:
                y += 1
            else:
                break
        x[y-1] = "USER_MONSTER_LIST = ['','','','','','']" + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'PLAYER_MONSTER_LIST' not in line:
                y += 1
            else:
                break
        x[y-1] = "PLAYER_MONSTER_LIST = ['','','','','','']" + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'USER_ITEM_LIST' not in line:
                y += 1
            else:
                break
        x[y-1] = "USER_ITEM_LIST = ['','','','','','']" + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'PLAYER_ITEM_LIST' not in line:
                y += 1
            else:
                break
        x[y-1] = "PLAYER_ITEM_LIST = ['','','','','','']" + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'USER_MONSTER_HP' not in line:
                y += 1
            else:
                break
        x[y-1] = "USER_MONSTER_HP = ['','','','','','']" + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'PLAYER_MONSTER_HP' not in line:
                y += 1
            else:
                break
        x[y-1] = "PLAYER_MONSTER_HP = ['','','','','','']" + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'USER_CHARACTER_UNDER' not in line:
                y += 1
            else:
                break
        x[y-1] = "USER_CHARACTER_UNDER = ['','','','','','','','','','','','','','','']" + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'PLAYER_CHARACTER_UNDER' not in line:
                y += 1
            else:
                break
        x[y-1] = "PLAYER_CHARACTER_UNDER = ['','','','','','','','','','','','','','','']" + '\n'

        #write number of people in room
        y = 1
        f.seek(0)
        for line in f:
            if 'TURN_INDICATOR' not in line:
                y += 1
            else:
                break
        x[y-1] = "TURN_INDICATOR = my" + '\n'


    with open('connection.txt','w') as f:
        f.writelines(x)


#-----------------------------Check events----------------------------------------------------
def check_events(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user,action, player2):
    """Check mouse and keyboard events"""
    # text input box
    if button_status.text_input_box_display == True:
        check_events_text_input_box(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

    elif screen_status.welcome_screen_display:
        check_events_welcome_screen(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user,action, player2)

    elif screen_status.lobby_screen_display:
        check_events_lobby_screen(ai_settings, grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

    elif screen_status.prepare_screen_display:
        check_events_prepare_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

    elif screen_status.build_deck_screen_display:
        check_events_build_deck_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user)

    elif screen_status.battle_screen_display:
        check_events_battle_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

def check_events_welcome_screen(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user,action, player2):
    """ Check all events on the welcome screen"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # If settings window is on
            if button_status.welcome_screen_settings_display == True:
                # Turn sound on
                if Rect(510, 333, 40, 40).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.sound_indicator = True
                # Turn sound off
                elif Rect(560, 333, 40, 40).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.sound_indicator = False
                # Turn music on
                elif Rect(510, 403, 40, 40).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.music_indicator = True
                # Turn music off
                elif Rect(560, 403, 40, 40).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.music_indicator = False

                # Change Theme
                elif Rect(510, 470, 140, 50).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.theme_indicator = 'Lith Harbor'
                    change_bg_music('Lith Harbor')

                elif Rect(670, 470, 140, 50).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.theme_indicator = 'Leafre'
                    change_bg_music('Leafre')

                elif Rect(510, 540, 140, 50).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.theme_indicator = 'Pantheon'
                    change_bg_music('Pantheon')

                elif Rect(670, 540, 140, 50).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.theme_indicator = 'Ellinia'
                    change_bg_music('Ellinia')

                # change AI speeding
                elif Rect(550, 620, 80, 50).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.AI_speed_indicator = '1000'

                elif Rect(650, 620, 80, 50).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.AI_speed_indicator = '2000'

                elif Rect(750, 620, 80, 50).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.AI_speed_indicator = '3000'

                # Quit settings window
                elif Rect(870, 300, 30, 30).collidepoint(pygame.mouse.get_pos()):
                    button_status.welcome_screen_settings_display = False

            elif button_status.rules_display == True:
                # When we click on '>'
                if Rect(640, 37, 20, 20).collidepoint(pygame.mouse.get_pos()):
                    if int(button_status.rules_page_id) < 4:
                        button_status.rules_page_id = str(int(button_status.rules_page_id)+1)
                    else:
                        pass
                # When we click on '<'
                elif Rect(540, 37, 20, 20).collidepoint(pygame.mouse.get_pos()):
                    if int(button_status.rules_page_id) > 1:
                        button_status.rules_page_id = str(int(button_status.rules_page_id)-1)
                    else:
                        pass

                elif Rect(975, 35, 25, 25).collidepoint(pygame.mouse.get_pos()):
                    button_status.rules_display = False

            else:
                # Click on single player
                if Rect(402, 269, 396, 62).collidepoint(pygame.mouse.get_pos()):
                    screen_status.welcome_screen_display = False
                    screen_status.prepare_screen_display = True
                    if user.name == '':
                        button_status.text_input_box_display = True
                    else:
                        pass
                # Click on multiplayer
                elif Rect(434, 370, 333, 61).collidepoint(pygame.mouse.get_pos()):
                    screen_status.welcome_screen_display = False
                    screen_status.lobby_screen_display = True
                    player2.identity = 'pvp'
                    if user.name == '':
                        button_status.text_input_box_display = True
                    else:
                        pass
                    #enter_as_network_client(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user,action, player2)
                # Click on settings
                elif Rect(474, 469, 253, 62).collidepoint(pygame.mouse.get_pos()):
                    button_status.welcome_screen_settings_display = True

                # Click on rules
                elif Rect(517, 570, 167, 61).collidepoint(pygame.mouse.get_pos()):
                    button_status.rules_display = True

                # click on exit
                elif Rect(541, 670, 119, 61).collidepoint(pygame.mouse.get_pos()):
                    sys.exit()

def check_events_lobby_screen(ai_settings, grid,screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ Check input events on lobby screen"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            clear_text_file(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)
            button_status.lobby_screen_room_detail_display = 'none'
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                clear_text_file(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)
                button_status.lobby_screen_room_detail_display = 'none'
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Back button
            if Rect(0, 0, 50, 50).collidepoint(pygame.mouse.get_pos()):
                clear_text_file(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)
                button_status.lobby_screen_room_detail_display = 'none'
                screen_status.lobby_screen_display = False
                screen_status.welcome_screen_display = True
            # Change name button
            elif Rect(780, 10, 110, 30).collidepoint(pygame.mouse.get_pos()):
                button_status.text_input_box_display = True

            # Create/next/ready/start button
            elif Rect(920, 607, 100, 50).collidepoint(pygame.mouse.get_pos()):
                # create
                if button_status.lobby_screen_room_detail_display == 'none':
                    if button_status.lobby_screen_room_list_display == 'N/A':
                        button_status.lobby_screen_room_detail_display = 'my'
                        button_status.lobby_screen_room_status = '1/2'
                        button_status.lobby_screen_room_list_display = user.name

                #my next/ready/start
                elif button_status.lobby_screen_room_detail_display == 'my': #and button_status.lobby_screen_room_status == '2/2':
                    if button_status.lobby_screen_prepare_to_go_display == False:
                        button_status.lobby_screen_prepare_to_go_display = True
                    elif button_status.lobby_screen_prepare_to_go_display == True:
                        # Click on ready
                        if button_status.lobby_screen_my_ready_to_go == False:
                            lobby_screen_to_other_ready_action(ai_settings, screen,buttons, screen_status, button_status, card_database_filter, user, player2)


                        # Click on play
                        elif button_status.lobby_screen_my_ready_to_go == True and button_status.lobby_screen_other_ready_to_go == True:
                            button_status.lobby_screen_game_start = True
                            lobby_screen_game_start_action(ai_settings, grid,screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)



                # other Ready
                elif button_status.lobby_screen_room_detail_display == 'other' and button_status.lobby_screen_prepare_to_go_display == True:
                    lobby_screen_to_other_ready_action(ai_settings, screen,buttons, screen_status, button_status, card_database_filter, user, player2)


            # click on ok on end screen warning sign
            elif Rect(1100, 642, 40, 30).collidepoint(pygame.mouse.get_pos()):
                button_status.lobby_screen_end_screen_warning_button_display = ''

            # Join
            elif Rect(530, 230, 50, 30).collidepoint(pygame.mouse.get_pos()):
                if button_status.lobby_screen_room_detail_display == 'none':
                    button_status.lobby_screen_room_detail_display = 'other'
                    button_status.lobby_screen_room_status = '2/2'
            # quit
            elif Rect(920, 684, 100, 50).collidepoint(pygame.mouse.get_pos()):
                if button_status.lobby_screen_room_detail_display == 'my' or button_status.lobby_screen_room_detail_display == 'other':
                    clear_text_file(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)
                    button_status.lobby_screen_room_detail_display = 'none'

            # When in lobby_prepare to go screen
            for i in range(1,7):
                # Display edit/delete buttons
                if Rect(85 + 180* (i-1), 165, 130,110).collidepoint(pygame.mouse.get_pos()):
                    with open('user_deck_list_string.txt','r') as f:
                        f.seek(0)
                        for line in f:
                            if 'DECK_LIST_' + str(i) in line:
                                user.deck_list_index = str(i)

                # Click on Edit
                elif Rect(85 + 180* (i-1), 282, 60, 30).collidepoint(pygame.mouse.get_pos()):
                    with open('user_deck_list_string.txt','r') as f:
                        f.seek(0)
                        for line in f:
                            if 'DECK_LIST_' + str(i) in line:
                                user.deck_list = make_card_list_from_string(line.replace('DECK_LIST_' + str(i) + ' = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                            if 'CHARACTER_' + str(i) in line:
                                user.character_card = eval('card_' + line.replace('CHARACTER_' + str(i) + ' = ', '')[7:12])
                                screen_status.build_deck_screen_display = True
                                screen_status.lobby_screen_display = False

                # Click on Delete
                elif Rect(155 + 180* (i-1), 282, 60, 30).collidepoint(pygame.mouse.get_pos()):
                    with open('user_deck_list_string.txt','r') as f:
                        f.seek(0)
                        for line in f:
                            if 'DECK_LIST_' + str(i) in line:

                                with open('user_deck_list_string.txt','a+') as f:

                                    f.seek(0)
                                    x = f.readlines()
                                    y = 1

                                    f.seek(0)
                                    for line in f:
                                        if 'DECK_LIST_' + str(i) not in line:
                                            y += 1
                                        else:
                                            break

                                    del x[y-1] # Delete DECK_LIST_
                                    del x[y-1] # Delete CHARACTER_

                                with open('user_deck_list_string.txt','w') as f:
                                    f.writelines(x)

                                user.deck_list_index = 'new'

            # create new deck
            if Rect(1020, 110, 120, 35).collidepoint(pygame.mouse.get_pos()):
                with open('user_deck_list_string.txt','r') as f:
                    f.seek(0)
                    if len(f.readlines()) >= 12:
                        pass

                    else:
                        user.deck_list_index = 'new'
                        user.deck_list = []
                        user.character_card = ''
                        screen_status.build_deck_screen_display = True
                        screen_status.lobby_screen_display = False

def check_events_prepare_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ Check events in prepare screen"""

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            for i in range(1,7):
                # Display edit/delete buttons
                if Rect(85 + 180* (i-1), 165, 130,110).collidepoint(pygame.mouse.get_pos()):
                    with open('user_deck_list_string.txt','r') as f:
                        f.seek(0)
                        for line in f:
                            if 'DECK_LIST_' + str(i) in line:
                                user.deck_list_index = str(i)

                # Click on Edit
                elif Rect(85 + 180* (i-1), 282, 60, 30).collidepoint(pygame.mouse.get_pos()):
                    with open('user_deck_list_string.txt','r') as f:
                        f.seek(0)
                        for line in f:
                            if 'DECK_LIST_' + str(i) in line:
                                user.deck_list = make_card_list_from_string(line.replace('DECK_LIST_' + str(i) + ' = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                            if 'CHARACTER_' + str(i) in line:
                                user.character_card = eval('card_' + line.replace('CHARACTER_' + str(i) + ' = ', '')[7:12])
                                screen_status.build_deck_screen_display = True
                                screen_status.prepare_screen_display = False

                # Click on Delete
                elif Rect(155 + 180* (i-1), 282, 60, 30).collidepoint(pygame.mouse.get_pos()):
                    with open('user_deck_list_string.txt','r') as f:
                        f.seek(0)
                        for line in f:
                            if 'DECK_LIST_' + str(i) in line:

                                with open('user_deck_list_string.txt','a+') as f:

                                    f.seek(0)
                                    x = f.readlines()
                                    y = 1

                                    f.seek(0)
                                    for line in f:
                                        if 'DECK_LIST_' + str(i) not in line:
                                            y += 1
                                        else:
                                            break

                                    del x[y-1] # Delete DECK_LIST_
                                    del x[y-1] # Delete CHARACTER_

                                with open('user_deck_list_string.txt','w') as f:
                                    f.writelines(x)

                                user.deck_list_index = 'new'

            # Click on one of the opponent's deck
            for i in range(1,9):
                if i <= 4:
                    if Rect(70 + 160* (i-1), 395, 130,180).collidepoint(pygame.mouse.get_pos()):
                        player2.character_ai_index = str(i)
                else:
                    if Rect(70 + 160* (i-5), 585, 130,180).collidepoint(pygame.mouse.get_pos()):
                        player2.character_ai_index = str(i)

            # Click and pick a difficulty
            for i in range(1,5):
                if Rect(710, 445 + 80*(i-1),410,70).collidepoint(pygame.mouse.get_pos()):
                    player2.ai_difficulty_index = str(i)



            # back
            if Rect(0,0,50,50).collidepoint(pygame.mouse.get_pos()):
                screen_status.welcome_screen_display = True
                screen_status.prepare_screen_display = False

            # play
            elif Rect(1150,0,50,50).collidepoint(pygame.mouse.get_pos()):
                prepare_screen_to_battle_screen_action(ai_settings, screen,buttons, screen_status, button_status, card_database_filter, user, player2)
                if button_status.prepare_screen_end_screen_warning_button_display == '':
                    screen_status.battle_screen_display = True
                    screen_status.prepare_screen_display = False

                    # user.random_deck_list = random.sample(user.deck_list, len(user.deck_list))
                    # user.remain_deck_list = user.random_deck_list[6:]
                    # user.hand_list = user.random_deck_list[0:6]

            # click on ok on end screen warning sign
            elif Rect(1100, 62, 40, 30).collidepoint(pygame.mouse.get_pos()):
                button_status.prepare_screen_end_screen_warning_button_display = ''

            # Change name
            elif Rect(780, 10, 110, 30).collidepoint(pygame.mouse.get_pos()):
                button_status.text_input_box_display = True

            # create new deck
            elif Rect(1020, 110, 120, 35).collidepoint(pygame.mouse.get_pos()):
                with open('user_deck_list_string.txt','r') as f:
                    f.seek(0)
                    if len(f.readlines()) >= 12:
                        pass

                    else:
                        user.deck_list_index = 'new'
                        user.deck_list = []
                        user.character_card = ''
                        screen_status.build_deck_screen_display = True
                        screen_status.prepare_screen_display = False

        elif event.type == pygame.MOUSEMOTION: # Mostly for zoom in
            x = 0 # indicator helps remove zoom in.

            # Opponent characters
            for i in range(1,5):
                if Rect(70 + 160* (i-1), 395, 130,180).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'prepare_screen'
                    button_status.card_zoom_part_indicator = 'opponent character'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1
            for i in range(5,9):
                if Rect(70 + 160* (i-5), 585, 130,180).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'prepare_screen'
                    button_status.card_zoom_part_indicator = 'opponent character'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1


            if x == 0:
                button_status.card_zoom_active = False

def check_events_build_deck_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user):
    """ Check all events on the build deck screen"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            for i in range(1,8):
                if Rect(100 + 145*(i-1),130,130,180).collidepoint(pygame.mouse.get_pos()):
                    build_deck_screen_add_card_to_deck(str(i),screen, screen_status,card_database_filter, user)
            for i in range(8,15):
                if Rect(100 + 145*(i-8),330,130,180).collidepoint(pygame.mouse.get_pos()):
                    build_deck_screen_add_card_to_deck(str(i),screen, screen_status,card_database_filter, user)

            for i in range(1,7):
                if Rect(245 + 145*(i-1),600,130,180).collidepoint(pygame.mouse.get_pos()):
                    build_deck_screen_remove_card_from_deck(str(i),screen, screen_status,card_database_filter, user)

            # ok sign on warning
            if Rect(1100, 62, 40, 30).collidepoint(pygame.mouse.get_pos()):
                button_status.build_deck_screen_end_screen_warning_button_display = ''

            elif rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):

                        if button.text == 'Save':
                            build_deck_screen_save_deck_to_file(screen,buttons, screen_status, button_status, card_database_filter, user)
                            if button_status.build_deck_screen_end_screen_warning_button_display == '':
                                screen_status.build_deck_screen_display = False
                                screen_status.prepare_screen_display = True


                        elif button.text == 'Back':
                            screen_status.welcome_screen_display = True
                            screen_status.build_deck_screen_display = False
                            screen_status.battle_screen_display = False
                        elif button.text == '>>':
                            screen_status.build_deck_screen_card_gallery_page_id += 1
                        elif button.text == '<<':
                            screen_status.build_deck_screen_card_gallery_page_id -= 1
                        elif button.text == 'Character':
                            card_database_filter.character = not card_database_filter.character
                        elif button.text == 'Bowman':
                            card_database_filter.bowman = not card_database_filter.bowman
                        elif button.text == 'Magician':
                            card_database_filter.magician = not card_database_filter.magician
                        elif button.text == 'Thief':
                            card_database_filter.thief = not card_database_filter.thief
                        elif button.text == 'Warrior':
                            card_database_filter.warrior = not card_database_filter.warrior
                        elif button.text == 'Jobless':
                            card_database_filter.jobless = not card_database_filter.jobless
                        elif button.text == '>':
                            screen_status.build_deck_screen_my_deck_page_id += 1
                        elif button.text == '<':
                            screen_status.build_deck_screen_my_deck_page_id -= 1


        elif event.type == pygame.MOUSEMOTION: # Mostly for zoom in
            x = 0 # indicator helps remove zoom in.

            # Card gallery
            for i in range(1,8):
                if Rect(100 + 145*(i-1),130,130,180).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'build_deck_screen'
                    button_status.card_zoom_part_indicator = 'card gallery'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1
            for i in range(8,15):
                if Rect(100 + 145*(i-8),330,130,180).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'build_deck_screen'
                    button_status.card_zoom_part_indicator = 'card gallery'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1

            # Hand zoom
            for i in range(1,7):
                if Rect(245 + 145*(i-1),600,130,180).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'build_deck_screen'
                    button_status.card_zoom_part_indicator = 'hand'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1

            if Rect(65,600,130,180).collidepoint(pygame.mouse.get_pos()):
                button_status.card_zoom_active = True
                button_status.card_zoom_screen_indicator = 'build_deck_screen'
                button_status.card_zoom_part_indicator = 'character'
                button_status.card_zoom_position_indicator = str(i)
                x = 1

            if x == 0:
                button_status.card_zoom_active = False



        elif event.type == pygame.MOUSEBUTTONUP:
            pass

def check_events_battle_screen(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ Check all evetns on the battle screen"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            #check click on cards in hand
            for i in range(1,8):
                if Rect((100+145*(i-1)),610,130,180).collidepoint(pygame.mouse.get_pos()):
                    battle_screen_hand_click_action('hand',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,player2, position = str(i))
                    break

            for i in range(1,4):
                if Rect(420,(220 + 110*(i-1)),130,80).collidepoint(pygame.mouse.get_pos()):
                    battle_screen_battleground_click_action('player2-monster',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2, position = str(i))
                    break

            for i in range(4,7):
                if Rect(245, (220 + 110*(i-4)),130,80).collidepoint(pygame.mouse.get_pos()):
                    battle_screen_battleground_click_action('player2-monster',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2, position = str(i))
                    break



            if Rect(20,40,130,180).collidepoint(pygame.mouse.get_pos()):
                battle_screen_battleground_click_action('player2-character',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)

            # win/lost back to main menu button
            if Rect(500, 500, 200, 40).collidepoint(pygame.mouse.get_pos()):
                if screen_status.battle_screen_action_indicator == 'game-end':
                    screen_status.battle_screen_display = False
                    screen_status.welcome_screen_display = True

            if Rect(200, 0, 50, 30).collidepoint(pygame.mouse.get_pos()):
                button_status.rules_display = True


            # When menu window is on
            if button_status.battle_screen_menu_display == True:

                # Turn sound on
                if Rect(447+280, 323-270, 28, 28).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.sound_indicator = True
                # Turn sound off
                elif Rect(482+280, 323-270, 28, 28).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.sound_indicator = False
                # Turn music on
                elif Rect(447+280, 372-270, 28, 28).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.music_indicator = True
                # Turn music off
                elif Rect(482+280, 372-270, 28, 28).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.music_indicator = False

                # Change Theme
                elif Rect(447+280, 419-270, 98, 35).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.theme_indicator = 'Lith Harbor'
                    change_bg_music('Lith Harbor')

                elif Rect(559+280, 419-270, 98, 35).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.theme_indicator = 'Leafre'
                    change_bg_music('Leafre')

                elif Rect(447+280, 468-270, 98, 35).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.theme_indicator = 'Pantheon'
                    change_bg_music('Pantheon')

                elif Rect(559+280, 468-270, 98, 35).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.theme_indicator = 'Ellinia'
                    change_bg_music('Ellinia')

                # change AI speeding
                elif Rect(475+280, 524-270, 56, 35).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.AI_speed_indicator = '1000'

                elif Rect(545+280, 524-270, 56, 35).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.AI_speed_indicator = '2000'

                elif Rect(615+280, 524-270, 56, 35).collidepoint(pygame.mouse.get_pos()):
                    ai_settings.AI_speed_indicator = '3000'

                # Quit settings window
                elif Rect(699+280, 300-270, 21, 21).collidepoint(pygame.mouse.get_pos()):
                    button_status.battle_screen_menu_display = False

                # Concede and back to main menu
                elif Rect(700, 310, 180, 40).collidepoint(pygame.mouse.get_pos()):
                    screen_status.battle_screen_action_indicator = 'game-end'
                    button_status.battle_screen_win_lost_indicator = 'lost'

            if button_status.rules_display == True:
                # When we click on '>'
                if Rect(640, 37, 20, 20).collidepoint(pygame.mouse.get_pos()):
                    if int(button_status.rules_page_id) < 4:
                        button_status.rules_page_id = str(int(button_status.rules_page_id)+1)
                    else:
                        pass
                # When we click on '<'
                elif Rect(540, 37, 20, 20).collidepoint(pygame.mouse.get_pos()):
                    if int(button_status.rules_page_id) > 1:
                        button_status.rules_page_id = str(int(button_status.rules_page_id)-1)
                    else:
                        pass

                elif Rect(975, 35, 25, 25).collidepoint(pygame.mouse.get_pos()):
                    button_status.rules_display = False




            if rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        if button.text == 'Menu':
                            button_status.battle_screen_menu_display = True

                        elif button.text == '>':
                            screen_status.battle_screen_my_hand_page_id += 1
                            button_status.battle_screen_my_hand_indicator_display = False # Turn off display of buttons when change page

                            if (screen_status.battle_screen_action_indicator == 'stage-1-level-up'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-think-fast'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-equip'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast-and-equip'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-equip'
                            ):
                                button_status.battle_screen_instruction_bar_yes_display = False
                                button_status.battle_screen_instruction_bar_yes_backend = False

                        elif button.text == '<':
                            screen_status.battle_screen_my_hand_page_id -= 1
                            button_status.battle_screen_my_hand_indicator_display = False

                            if (screen_status.battle_screen_action_indicator == 'stage-1-level-up'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-think-fast'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-equip'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast-and-equip'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast'
                            or screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-equip'
                            ):
                                button_status.battle_screen_instruction_bar_yes_display = False
                                button_status.battle_screen_instruction_bar_yes_backend = False

                        elif button.text == 'level up':
                            battle_screen_hand_click_action('level up',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)
                        elif button.text == 'Yes':
                            battle_screen_instruction_bar_yes_skip_action('yes',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,action,player2)
                        elif button.text == 'Skip':
                            battle_screen_instruction_bar_yes_skip_action('skip',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, action, player2)


        elif event.type == pygame.MOUSEMOTION: # Mostly for zoom in
            x = 0 # indicator helps remove zoom in.
            for i in range(1,8):
                if Rect((100+145*(i-1)),610,130,180).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'battle_screen'
                    button_status.card_zoom_part_indicator = 'hand'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1

            for i in range(1,16):
                if Rect(1050,(220 + 23 * (i-1)),130,23).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'battle_screen'
                    button_status.card_zoom_part_indicator = 'character 1 under'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1

            for i in range(1,16):
                if Rect(20,(220 + 23 * (i-1)),130,23).collidepoint(pygame.mouse.get_pos()):
                    button_status.card_zoom_active = True
                    button_status.card_zoom_screen_indicator = 'battle_screen'
                    button_status.card_zoom_part_indicator = 'character 2 under'
                    button_status.card_zoom_position_indicator = str(i)
                    x = 1


            if Rect(1050,40,130,180).collidepoint(pygame.mouse.get_pos()):
                button_status.card_zoom_active = True
                button_status.card_zoom_screen_indicator = 'battle_screen'
                button_status.card_zoom_part_indicator = 'character 1'
                x = 1

            if Rect(20,40,130,180).collidepoint(pygame.mouse.get_pos()):
                button_status.card_zoom_active = True
                button_status.card_zoom_screen_indicator = 'battle_screen'
                button_status.card_zoom_part_indicator = 'character 2'
                x = 1

            if Rect(880, 5, 50, 20).collidepoint(pygame.mouse.get_pos()):
                button_status.battle_screen_history_bar_detail_display = True
                x = 1

            if x == 0:
                button_status.card_zoom_active = False
                button_status.battle_screen_history_bar_detail_display = False



        elif event.type == pygame.MOUSEBUTTONUP:
            pass

def check_events_text_input_box(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if user.name != '':
                    user.name = user.name[:-1]
                else:
                    pass
            elif event.key <= 127:
                if pygame.key.get_mods() & KMOD_SHIFT or pygame.key.get_mods() & KMOD_CAPS:
                    user.name += chr(event.key).upper()
                else:
                    user.name += chr(event.key)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #click on ok
            if Rect(567, 410, 66, 30).collidepoint(pygame.mouse.get_pos()):
                user_input_text_save('user name',ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)
                button_status.text_input_box_display = False



#-----------------------------Update screens----------------------------------------------------
def update_screen(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user,action, player2):
    """ Update images on the screen and flip to the new screen"""
    screen.fill((250,250,250))
    # Theme filter
    if ai_settings.theme_indicator == 'Lith Harbor':
        screen.blit(pygame.image.load('static/bg_images/bg_02.png'), (0,0))
    elif ai_settings.theme_indicator == 'Leafre':
        screen.blit(pygame.image.load('static/bg_images/bg_05.jpg'), (0,0))
    elif ai_settings.theme_indicator == 'Pantheon':
        screen.blit(pygame.image.load('static/bg_images/bg_06.png'), (0,0))
    elif ai_settings.theme_indicator == 'Ellinia':
        screen.blit(pygame.image.load('static/bg_images/bg_04.jpeg'), (0,0))

    if button_status.lobby_screen_game_start == True:
        if screen_status.lobby_screen_display == True and screen_status.battle_screen_display == False:
            screen_status.lobby_screen_display = False
            screen_status.battle_screen_display = True

    if screen_status.welcome_screen_display:
        welcome_screen_update(ai_settings,screen, buttons, screen_status, button_status)

    if screen_status.lobby_screen_display:
        lobby_screen_update(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user,action, player2)

    if screen_status.prepare_screen_display:
        prepare_screen_update(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2)

    if screen_status.build_deck_screen_display:
        build_deck_screen_update(ai_settings, grid, screen, buttons, screen_status, button_status, card_database_filter, user)

    if screen_status.battle_screen_display:
        battle_screen_update(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2)

    # Display zoom in affect at the end to cover previous draw when zoom in
    card_zoom_update(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    #Rules display
    rules_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    #Text input box display
    text_input_box_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    # music volume
    if ai_settings.music_indicator == True:
        pygame.mixer.music.set_volume(1.0)
    else:
        pygame.mixer.music.set_volume(0)

    pygame.display.flip()

def welcome_screen_update(ai_settings,screen, buttons, screen_status,button_status):
    """ welcome screen update"""

    welcome_screen_stable_button_display(ai_settings,screen, buttons, screen_status, button_status)

    welcome_screen_settings_menu_display(ai_settings,screen, buttons, screen_status, button_status)

def lobby_screen_update(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user,action, player2):
    """ Update display for lobby screen"""

    lobby_screen_stable_button_display(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2)

    lobby_screen_room_detail_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

    lobby_screen_room_list_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

    lobby_screen_pick_deck_warning_button_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

    if button_status.lobby_screen_prepare_to_go_display == True:
        lobby_screen_pick_deck_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

def prepare_screen_update(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2):
    """ Update prepare screen"""

    #prepare_screen_grid_display(grid, screen)

    prepare_screen_stable_button_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    prepare_screen_button_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    prepare_screen_end_screen_warning_display(screen,buttons, screen_status, button_status, card_database_filter, user)

def build_deck_screen_update(ai_settings, grid, screen, buttons, screen_status, button_status, card_database_filter, user):
    """ Build deck screen update"""

    #build_deck_screen_grid_display(grid, screen)

    build_deck_screen_stable_button_display(screen, buttons,screen_status, button_status)

    build_deck_screen_card_gallery_display(screen,buttons, screen_status, button_status, card_database_filter)

    build_deck_screen_my_deck_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    build_deck_screen_end_screen_warning_display(screen,buttons, screen_status, button_status, card_database_filter, user)

def battle_screen_update(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2):
    """ Battle screen update"""

    #battle_screen_grid_display(grid, screen)

    battle_screen_instruction_bar_display(screen,buttons, screen_status, button_status, card_database_filter, user, player2)

    battle_screen_stable_button_display(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2)

    battle_screen_my_hand_card_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    battle_screen_my_hand_button_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    battle_screen_character_1_card_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    battle_screen_character_1_button_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    battle_screen_battleground_card_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    # Display informations of player2
    battle_screen_player2_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    battle_screen_battleground_button_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    battle_screen_menu_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    # Update result in each cycle
    battle_screen_result_update(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    battle_screen_history_bar_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    battle_screen_win_lost_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

def card_zoom_update(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ display card details (zoom in) any card"""
    # Prepare screen
    if button_status.card_zoom_active:
        if button_status.card_zoom_screen_indicator == 'prepare_screen':
            if button_status.card_zoom_part_indicator == 'opponent character':
                character_list = [card_01_16, card_01_37, card_01_59, card_01_89, card_03_11, card_05_30, card_01_64, card_05_61]
                if int(button_status.card_zoom_position_indicator) <= 4:
                    located_card = character_list[int(button_status.card_zoom_position_indicator)-1]
                    rect_x = 70 + 160* (int(button_status.card_zoom_position_indicator)-1)
                    rect_y = 395

                    located_card.rect_zoom.x = rect_x - 60
                    located_card.rect_zoom.y = rect_y - 210
                    screen.blit(located_card.image_zoom, located_card.rect_zoom)

                else:
                    located_card = character_list[int(button_status.card_zoom_position_indicator)-1]
                    rect_x = 70 + 160* (int(button_status.card_zoom_position_indicator)-5)
                    rect_y = 585

                    located_card.rect_zoom.x = rect_x - 60
                    located_card.rect_zoom.y = rect_y - 210
                    screen.blit(located_card.image_zoom, located_card.rect_zoom)



    # Build deck screen
    if button_status.card_zoom_active:
        if button_status.card_zoom_screen_indicator == 'build_deck_screen':
            if button_status.card_zoom_part_indicator == 'card gallery':
                if len(cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1):14 * screen_status.build_deck_screen_card_gallery_page_id]) >= int(button_status.card_zoom_position_indicator):
                    located_card = cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1)+(int(button_status.card_zoom_position_indicator)-1)]

                    if int(button_status.card_zoom_position_indicator) <= 7:
                        rect_x = 100 + 145*(int(button_status.card_zoom_position_indicator)-1)
                        rect_y = 130
                    else:
                        rect_x = 100 + 145*(int(button_status.card_zoom_position_indicator)-8)
                        rect_y = 330

                    located_card.rect_zoom.x = rect_x - 85
                    located_card.rect_zoom.y = rect_y - 110
                    screen.blit(located_card.image_zoom, located_card.rect_zoom)

                else:
                    pass

            if button_status.card_zoom_part_indicator == 'hand':
                local_store_list = build_deck_screen_my_deck_card_list_refine(user)
                # Check to avoid errors when click on empty rect preventing removing card.
                if len(local_store_list[6*(screen_status.build_deck_screen_my_deck_page_id - 1):6 * screen_status.build_deck_screen_my_deck_page_id]) >= int(button_status.card_zoom_position_indicator):
                    located_card = local_store_list[6*(screen_status.build_deck_screen_my_deck_page_id - 1)+(int(button_status.card_zoom_position_indicator)-1)]

                    rect_x = 245 + 145*(int(button_status.card_zoom_position_indicator)-1)
                    rect_y = 600

                    located_card.rect_zoom.x = rect_x - 85
                    located_card.rect_zoom.y = rect_y - 210
                    screen.blit(located_card.image_zoom, located_card.rect_zoom)
                else:
                    pass

            if button_status.card_zoom_part_indicator == 'character':
                located_card = user.character_card

                rect_x = 100
                rect_y = 600

                located_card.rect_zoom.x = rect_x - 85
                located_card.rect_zoom.y = rect_y - 210
                screen.blit(located_card.image_zoom, located_card.rect_zoom)


    # Battle Screen
    if screen_status.battle_screen_action_indicator != 'stage-0':
        if button_status.card_zoom_active:
            if button_status.card_zoom_screen_indicator == 'battle_screen':
                if button_status.card_zoom_part_indicator == 'hand':
                    if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.card_zoom_position_indicator):
                        pass
                    else:
                        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.card_zoom_position_indicator)-1)]
                        located_card.rect_zoom.x = located_card.rect.x - 85
                        located_card.rect_zoom.y = located_card.rect.y - 210
                        screen.blit(located_card.image_zoom, located_card.rect_zoom)

                elif button_status.card_zoom_part_indicator == 'character 1':
                    located_card = user.character_card
                    located_card.rect_zoom.x = located_card.rect.x - 305
                    located_card.rect_zoom.y = located_card.rect.y
                    screen.blit(located_card.image_zoom, located_card.rect_zoom)

                elif button_status.card_zoom_part_indicator == 'character 2':
                    located_card = player2.character_card
                    located_card.rect_zoom.x = located_card.rect.x + 135
                    located_card.rect_zoom.y = located_card.rect.y
                    screen.blit(located_card.image_zoom, located_card.rect_zoom)

                elif button_status.card_zoom_part_indicator == 'character 1 under':
                    if user.character_under_card_by_level[str(int(button_status.card_zoom_position_indicator)*10)] != '':
                        located_card = user.character_under_card_by_level[str(int(button_status.card_zoom_position_indicator)*10)]
                        located_card.bottom_rect_zoom.x = 880
                        located_card.bottom_rect_zoom.y = 220 + 23 * (int(button_status.card_zoom_position_indicator)-1)
                        screen.blit(located_card.bottom_image_zoom, located_card.bottom_rect_zoom)
                    else:
                        pass

                elif button_status.card_zoom_part_indicator == 'character 2 under':
                    if player2.character_under_card_by_level[str(int(button_status.card_zoom_position_indicator)*10)] != '':
                        located_card = player2.character_under_card_by_level[str(int(button_status.card_zoom_position_indicator)*10)]
                        located_card.bottom_rect_zoom.x = 20
                        located_card.bottom_rect_zoom.y = 220 + 23 * (int(button_status.card_zoom_position_indicator)-1)
                        screen.blit(located_card.bottom_image_zoom, located_card.bottom_rect_zoom)
                    else:
                        pass

def rules_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display rules for the game"""
    if button_status.rules_display == True:
        button = Button('','', (0,0,0), 0, 0, 1200, 800, alpha = 100)
        button.update()
        button.draw(screen)
        
        button = Button('','', (255,255,255), 200, 35, 800, 730)
        button.update()
        button.draw(screen)

        if button_status.rules_page_id == '1':
            screen.blit(pygame.image.load('static/rules_images/001.png'), (200,65))

            button = Button('>','', (255,255,255), 640, 37, 20, 20, font_color = (0,0,0))
            button.update()
            button.draw(screen)

        elif button_status.rules_page_id == '2':
            screen.blit(pygame.image.load('static/rules_images/002.png'), (200,65))

            button = Button('<','', (255,255,255), 540, 37, 20, 20, font_color = (0,0,0))
            button.update()
            button.draw(screen)

            button = Button('>','', (255,255,255), 640, 37, 20, 20, font_color = (0,0,0))
            button.update()
            button.draw(screen)

        elif button_status.rules_page_id == '3':
            screen.blit(pygame.image.load('static/rules_images/003.png'), (200,65))

            button = Button('<','', (255,255,255), 540, 37, 20, 20, font_color = (0,0,0))
            button.update()
            button.draw(screen)

            button = Button('>','', (255,255,255), 640, 37, 20, 20, font_color = (0,0,0))
            button.update()
            button.draw(screen)

        elif button_status.rules_page_id == '4':
            screen.blit(pygame.image.load('static/rules_images/004.png'), (200,65))

            button = Button('<','', (255,255,255), 540, 37, 20, 20, font_color = (0,0,0))
            button.update()
            button.draw(screen)

        button = Button('Page: '+button_status.rules_page_id,'', (255,255,255), 570, 35, 60, 30, font_color = (0,0,0))
        button.update()
        button.draw(screen)

        button = Button('X','', (250,100,100), 975, 35, 25, 25, font_size = 16)
        button.update()
        button.draw(screen)

def text_input_box_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display text input box"""
    if button_status.text_input_box_display == True:
        button = Button('','', (0,0,0), 0, 0, 1200, 800, alpha = 100)
        button.update()
        button.draw(screen)

        button = Button('','', (255,255,255), 400, 275, 400, 180, alpha = 250)
        button.update()
        button.draw(screen)

        button = Button('PLEASE ENTER YOUR NAME','', (255,255,255), 400, 275, 400, 50, font_color = (0,0,0), font_size = 22, alpha = 0)
        button.update()
        button.draw(screen)

        button = Button('SAVE','', (40,120,40), 567, 410, 66, 30, font_size = 18)
        button.update()
        button.draw(screen)

        # Text box
        button = Button(user.name + '|','', (100,100,100), 450, 340, 300, 50, alpha = 250)
        button.update()
        button.draw(screen)



#-----------------------------Welcome screen display----------------------------------------------------
def welcome_screen_stable_button_display(ai_settings,screen, buttons, screen_status, button_status):
    """ Display stable buttons on welcome screen"""

    font_1 = pygame.font.Font('freesansbold.ttf', 70)
    text_image_1 = font_1.render('Welcome to Maplestory ITCG', True, (250,250,250))
    text_rect_1 = text_image_1.get_rect(center = (600,150))
    screen.blit(text_image_1, text_rect_1)

    font_6 = pygame.font.Font('freesansbold.ttf', 60)
    text_image_6 = font_6.render('Single Player', True, (255,255,255))
    text_rect_6 = text_image_6.get_rect(center = (600,300))
    screen.blit(text_image_6, text_rect_6)

    font_2 = pygame.font.Font('freesansbold.ttf', 60)
    text_image_2 = font_2.render('Multiplayer', True, (255,255,255))
    text_rect_2 = text_image_2.get_rect(center = (600,400))
    screen.blit(text_image_2, text_rect_2)

    font_3 = pygame.font.Font('freesansbold.ttf', 60)
    text_image_3 = font_3.render('Settings', True, (255,255,255))
    text_rect_3 = text_image_3.get_rect(center = (600,500))
    screen.blit(text_image_3, text_rect_3)

    font_5 = pygame.font.Font('freesansbold.ttf', 60)
    text_image_5 = font_5.render('Rules', True, (255,255,255))
    text_rect_5 = text_image_5.get_rect(center = (600,600))
    screen.blit(text_image_5, text_rect_5)

    font_4 = pygame.font.Font('freesansbold.ttf', 60)
    text_image_4 = font_4.render('Exit', True, (255,255,255))
    text_rect_4 = text_image_4.get_rect(center = (600,700))
    screen.blit(text_image_4, text_rect_4)

def welcome_screen_settings_menu_display(ai_settings,screen, buttons, screen_status, button_status):
    """ Display welcome screen settings menu"""
    if button_status.welcome_screen_settings_display == True:

        button = Button('','', (0,0,0), 300, 300, 600, 400, alpha = 200)
        button.update()
        button.draw(screen)
        # Sound settings
        button_sound = Button('Sound: ','', (0,0,0), 330, 330, 150, 50, font_size = 40, alpha = 0)
        button_sound.update()
        button_sound.draw(screen)

        if ai_settings.sound_indicator == True:
            button_1 = Button('On','', (50,150,50), 510, 333, 40, 40)
            button_1.update()
            button_1.draw(screen)

            button_2 = Button('Off','', (150,150,150), 560, 333, 40, 40)
            button_2.update()
            button_2.draw(screen)

        else:
            button_1 = Button('On','', (150,150,150), 510, 333, 40, 40)
            button_1.update()
            button_1.draw(screen)

            button_2 = Button('Off','', (150,50,50), 560, 333, 40, 40)
            button_2.update()
            button_2.draw(screen)

        # Music settings
        button_music = Button('Music: ','', (0,0,0), 330, 400, 150, 50, font_size = 40, alpha = 0)
        button_music.update()
        button_music.draw(screen)

        if ai_settings.music_indicator == True:
            button_1 = Button('On','', (50,150,50), 510, 403, 40, 40)
            button_1.update()
            button_1.draw(screen)

            button_2 = Button('Off','', (150,150,150), 560, 403, 40, 40)
            button_2.update()
            button_2.draw(screen)

        else:
            button_1 = Button('On','', (150,150,150), 510, 403, 40, 40)
            button_1.update()
            button_1.draw(screen)

            button_2 = Button('Off','', (150,50,50), 560, 403, 40, 40)
            button_2.update()
            button_2.draw(screen)

        # Theme settings
        button_theme = Button('Theme: ','', (0,0,0), 330, 470, 160, 50, font_size = 40, alpha = 0)
        button_theme.update()
        button_theme.draw(screen)

        if ai_settings.theme_indicator == 'Lith Harbor':
            button_1 = Button('Lith Harbor','', (50,150,50), 510, 470, 140, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Lith Harbor','', (150,150,150), 510, 470, 140, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)

        if ai_settings.theme_indicator == 'Leafre':
            button_1 = Button('Leafre','', (50,150,50), 670, 470, 140, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Leafre','', (150,150,150), 670, 470, 140, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)

        if ai_settings.theme_indicator == 'Pantheon':
            button_1 = Button('Pantheon','', (50,150,50), 510, 540, 140, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Pantheon','', (150,150,150), 510, 540, 140, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)

        if ai_settings.theme_indicator == 'Ellinia':
            button_1 = Button('Ellinia','', (50,150,50), 670, 540, 140, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Ellinia','', (150,150,150), 670, 540, 140, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)

        # AI speeding settings
        button_ai_speed = Button('AI Speed: ','', (0,0,0), 330, 620, 200, 50, font_size = 40, alpha = 0)
        button_ai_speed.update()
        button_ai_speed.draw(screen)

        if ai_settings.AI_speed_indicator == '1000':
            button_1 = Button('Fast','', (50,150,50), 550, 620, 80, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Fast','', (150,150,150), 550, 620, 80, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)

        if ai_settings.AI_speed_indicator == '2000':
            button_1 = Button('Normal','', (50,150,50), 650, 620, 80, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Normal','', (150,150,150), 650, 620, 80, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)

        if ai_settings.AI_speed_indicator == '3000':
            button_1 = Button('Slow','', (50,150,50), 750, 620, 80, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Slow','', (150,150,150), 750, 620, 80, 50, font_size = 18)
            button_1.update()
            button_1.draw(screen)

        # Closed settings window button
        button_1 = Button('X','', (250,100,100), 870, 300, 30, 30, font_size = 18)
        button_1.update()
        button_1.draw(screen)


#-----------------------------Lobby screen display----------------------------------------------------

def lobby_screen_stable_button_display(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2):
    """ Display stable button on lobby screen"""
    button_back = Button('Back','', (250,250,250),0, 0, 50, 50, font_size = 18, font_color = (0,0,0),alpha = 200)
    button_back.update()
    button_back.draw(screen)

    button1 = Button('Hello '+ user.name +'!','', (250,250,250),300, 0, 600, 50, font_size = 20, font_color = (0,0,0),alpha = 200)
    button1.update()
    button1.draw(screen)

    button_back = Button('Change Name','', (150,40,40),780, 10, 110, 30, font_size = 14,alpha = 200)
    button_back.update()
    button_back.draw(screen)
    # background for create game
    button2 = Button('','', (0,0,0),150, 580, 900, 181,alpha = 200)
    button2.update()
    button2.draw(screen)
    if button_status.lobby_screen_prepare_to_go_display == False:
        # Background for join existing game
        button3 = Button('','', (0,0,0),150, 70, 900, 500,alpha = 200)
        button3.update()
        button3.draw(screen)

        button4 = Button('Join an existing game:','', (0,0,0),400, 70, 400, 50, font_size = 20, alpha = 0)
        button4.update()
        button4.draw(screen)

def lobby_screen_room_list_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ Display room list"""
    if button_status.lobby_screen_prepare_to_go_display == False:
        if button_status.lobby_screen_room_list_display == 'N/A':
            pass
        else:
            if button_status.lobby_screen_room_status == '1/2':
                name = button_status.lobby_screen_room_list_display

                button3 = Button(name + "'s game:" + '   1/2','', (100,30,130),240, 150+ 70, 350, 50,alpha = 240)
                button3.update()
                button3.draw(screen)

                if button_status.lobby_screen_room_detail_display == 'none':
                    button3 = Button('Join','', (40,120,40),530, 230, 50, 30,alpha = 240)
                    button3.update()
                    button3.draw(screen)

def lobby_screen_room_detail_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ Display my room structure"""

    if button_status.lobby_screen_room_detail_display == 'none':

        if button_status.lobby_screen_room_list_display == 'N/A':
            button5 = Button('Create a game:','', (0,0,0),400, 580, 400, 50, font_size = 20, alpha = 0)
            button5.update()
            button5.draw(screen)

            button3 = Button('CREATE','', (40,40,120),920, 607, 100, 50,alpha = 240)
            button3.update()
            button3.draw(screen)

        else:
            button5 = Button('Please join the existing game!','', (0,0,0),400, 580, 400, 50, font_size = 20, alpha = 0)
            button5.update()
            button5.draw(screen)



    elif button_status.lobby_screen_room_detail_display == 'my':

        if button_status.lobby_screen_room_status == '1/2':
            button5 = Button(user.name + "'s game:" + '   1/2','', (0,0,0),400, 580, 400, 50, font_size = 20,font_color = (200,100,100), alpha = 0)
            button5.update()
            button5.draw(screen)
        elif button_status.lobby_screen_room_status == '2/2':
            button5 = Button(user.name + "'s game:" + '   2/2','', (0,0,0),400, 580, 400, 50, font_size = 20, alpha = 0)
            button5.update()
            button5.draw(screen)

        if button_status.lobby_screen_my_ready_to_go == False:
            button3 = Button(user.name,'', (200,200,110),205, 635, 650, 35,alpha = 240)
            button3.update()
            button3.draw(screen)
        elif button_status.lobby_screen_my_ready_to_go == True:
            button3 = Button(user.name,'', (110,200,110),205, 635, 650, 35,alpha = 240)
            button3.update()
            button3.draw(screen)

        if button_status.lobby_screen_room_status == '1/2':
            button3 = Button('Empty','', (250,250,250),205, 680, 650, 35,alpha = 100)
            button3.update()
            button3.draw(screen)
        elif button_status.lobby_screen_room_status == '2/2':
            if button_status.lobby_screen_other_ready_to_go == False:
                button3 = Button(player2.name,'', (200,200,110),205, 680, 650, 35,alpha = 240)
                button3.update()
                button3.draw(screen)
            elif button_status.lobby_screen_other_ready_to_go == True:
                button3 = Button(player2.name,'', (110,200,110),205, 680, 650, 35,alpha = 240)
                button3.update()
                button3.draw(screen)

        if button_status.lobby_screen_prepare_to_go_display == False:
            if button_status.lobby_screen_room_status == '1/2':
                button3 = Button('NEXT','', (120,120,120),920, 607, 100, 50,alpha = 240)
                button3.update()
                button3.draw(screen)
            elif button_status.lobby_screen_room_status == '2/2':
                button3 = Button('NEXT','', (40,120,40),920, 607, 100, 50,alpha = 240)
                button3.update()
                button3.draw(screen)
        else:
            if button_status.lobby_screen_my_ready_to_go == False:

                button3 = Button('READY!','', (40,120,40),920, 607, 100, 50,alpha = 240)
                button3.update()
                button3.draw(screen)

            elif button_status.lobby_screen_my_ready_to_go == True:
                if button_status.lobby_screen_other_ready_to_go == True:
                    button3 = Button('PLAY!','', (247, 201, 37),920, 607, 100, 50,alpha = 240)
                    button3.update()
                    button3.draw(screen)
                elif button_status.lobby_screen_other_ready_to_go == False:
                    button3 = Button('WAIT!','', (40, 40, 120),920, 607, 100, 50,alpha = 240)
                    button3.update()
                    button3.draw(screen)


        button3 = Button('QUIT','', (120,40,40),920, 684, 100, 50,alpha = 240)
        button3.update()
        button3.draw(screen)

    elif button_status.lobby_screen_room_detail_display == 'other':

        if button_status.lobby_screen_room_status == '1/2':
            button5 = Button(player2.name + "'s game:" + '   1/2','', (0,0,0),400, 580, 400, 50, font_size = 20,font_color = (200,100,100), alpha = 0)
            button5.update()
            button5.draw(screen)
        elif button_status.lobby_screen_room_status == '2/2':
            button5 = Button(player2.name + "'s game:" + '   2/2','', (0,0,0),400, 580, 400, 50, font_size = 20, alpha = 0)
            button5.update()
            button5.draw(screen)

        if button_status.lobby_screen_my_ready_to_go == False:
            button3 = Button(player2.name,'', (200,200,110),205, 635, 650, 35,alpha = 240)
            button3.update()
            button3.draw(screen)
        elif button_status.lobby_screen_my_ready_to_go == True:
            button3 = Button(player2.name,'', (110,200,110),205, 635, 650, 35,alpha = 240)
            button3.update()
            button3.draw(screen)


        if button_status.lobby_screen_room_status == '1/2':
            button3 = Button('Empty','', (250,250,250),205, 680, 650, 35,alpha = 100)
            button3.update()
            button3.draw(screen)
        elif button_status.lobby_screen_room_status == '2/2':

            if button_status.lobby_screen_other_ready_to_go == False:
                button3 = Button(user.name,'', (200,200,110),205, 680, 650, 35,alpha = 240)
                button3.update()
                button3.draw(screen)
            elif button_status.lobby_screen_other_ready_to_go == True:
                button3 = Button(user.name,'', (110,200,110),205, 680, 650, 35,alpha = 240)
                button3.update()
                button3.draw(screen)

        if button_status.lobby_screen_prepare_to_go_display == True:
            if button_status.lobby_screen_other_ready_to_go == False:
                button3 = Button('READY!','', (40,120,40),920, 607, 100, 50,alpha = 240)
                button3.update()
                button3.draw(screen)
            elif button_status.lobby_screen_other_ready_to_go == True:
                button3 = Button('WAIT...','', (40,40,120),920, 607, 100, 50,alpha = 240)
                button3.update()
                button3.draw(screen)

        button3 = Button('QUIT','', (120,40,40),920, 684, 100, 50,alpha = 240)
        button3.update()
        button3.draw(screen)

def lobby_screen_pick_deck_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ Display the screen for picking a deck"""
    # Pick deck text
    button_text_1 = Button('Pick an exist deck or create a new one: ','', (250,250,250),400, 100, 400, 35, font_color = (0,0,0), alpha = 150)
    button_text_1.update()
    button_text_1.draw(screen)

    # Deck list buttons
    with open('user_deck_list_string.txt','r') as f:
        f.seek(0)
        if len(f.readlines()) >= 12:
            pass
        else:
            button_new_deck = Button('+ New Deck','', (250,250,250),1020, 110, 120, 35, font_color = (0,0,0), alpha = 150)
            button_new_deck.update()
            button_new_deck.draw(screen)


        f.seek(0)
        x = len(f.readlines())
        y = 0
        deck_list_index = 0

        for i in range(1,7):
            f.seek(0)
            for line in f:
                if 'DECK_LIST_' + str(i) not in line:
                    y += 1
            if y < x: # DECK_LIST_i exist
                f.seek(0)
                for line in f:
                    if 'DECK_LIST_' + str(i) in line:
                        deck_length = len(make_card_list_from_string(line.replace('DECK_LIST_' + str(i) + ' = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2))
                        # deck_length = int((len(line.replace('DECK_LIST_' + str(i) + ' = ', '')) -1)/14)
                    if 'CHARACTER_' + str(i) in line:
                        character_length = 1
                        character_card = eval('card_' + line.replace('CHARACTER_' + str(i) + ' = ', '')[7:12])

                if user.deck_list_index == str(i):

                    button_top = Button(character_card.name + ': ','', (100,30,130),85 + 180* (i-1), 165, 130, 60)
                    button_top.update()
                    button_top.draw(screen)

                    if deck_length < 40:
                        button_bottom = Button(str(character_length) + '/1  |  ' + str(deck_length) +'/40','', (100,30,130),85 + 180* (i-1), 225, 130, 50, font_color = (250,0,0))
                        button_bottom.update()
                        button_bottom.draw(screen)
                    else:
                        button_bottom = Button(str(character_length) + '/1  |  ' + str(deck_length) +'/40','', (100,30,130),85 + 180* (i-1), 225, 130, 50)
                        button_bottom.update()
                        button_bottom.draw(screen)

                else:

                    button_top = Button(character_card.name + ': ','', (160,160,160),85 + 180* (i-1), 165, 130, 60, alpha = 240)
                    button_top.update()
                    button_top.draw(screen)

                    if deck_length < 40:
                        button_bottom = Button(str(character_length) + '/1  |  ' + str(deck_length) +'/40','', (160,160,160),85 + 180* (i-1), 225, 130, 50, font_color = (200,0,0), alpha = 240)
                        button_bottom.update()
                        button_bottom.draw(screen)
                    else:
                        button_bottom = Button(str(character_length) + '/1  |  ' + str(deck_length) +'/40','', (160,160,160),85 + 180* (i-1), 225, 130, 50, alpha = 240)
                        button_bottom.update()
                        button_bottom.draw(screen)

                y = 0

            else: # DECK_LIST_i not exist

                button = Button('Empty','', (200,200,200),85 + 180* (i-1), 165, 130, 110, alpha = 80)
                button.update()
                button.draw(screen)

                y = 0


    for i in range(1,7):
        if user.deck_list_index == str(i):
            button_edit = Button('Edit','', (50,50,170),85 + 180* (i-1), 282, 60, 30)
            button_edit.update()
            button_edit.draw(screen)

            button_delete = Button('Delete','', (160,30,30), 155 + 180* (i-1), 282, 60, 30)
            button_delete.update()
            button_delete.draw(screen)

def lobby_screen_pick_deck_warning_button_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ Display the waring button when deck you pick is not right"""
    if button_status.lobby_screen_end_screen_warning_button_display == 'deck less than 40 cards':
        button = Button('You need at least 40','' ,(122,33,38),1050, 580, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('cards in your deck!','' ,(122,33,38),1050, 610, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('','' ,(122,33,38),1050, 640, 150, 40,font_size = 18)
        button.update()
        button.draw(screen)

        button = Button('ok','' ,(22,143,78),1100, 642, 40, 30,font_size = 16)
        button.update()
        button.draw(screen)

    elif button_status.lobby_screen_end_screen_warning_button_display == 'no deck':
        button = Button('Please pick a deck','' ,(122,33,38),1050, 580, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('or build a new one!','' ,(122,33,38),1050, 610, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('','' ,(122,33,38),1050, 640, 150, 40,font_size = 18)
        button.update()
        button.draw(screen)

        button = Button('ok','' ,(22,143,78),1100, 642, 40, 30,font_size = 16)
        button.update()
        button.draw(screen)

def lobby_screen_to_other_ready_action(ai_settings, screen,buttons, screen_status, button_status, card_database_filter, user, player2):
    """ lobby screen other view check ready"""
    save_pass = True
    # Clear dup number each call

    with open('user_deck_list_string.txt','r') as f:
        f.seek(0)
        for line in f:
            if 'DECK_LIST_' + user.deck_list_index in line:
                list1 = make_deck_from_string(line.replace('DECK_LIST_' + user.deck_list_index + ' = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    if user.deck_list_index == '0' or user.deck_list_index == 'new':
        button_status.lobby_screen_end_screen_warning_button_display = 'no deck'
        save_pass = False

    elif len(list1) < 40:

        button_status.lobby_screen_end_screen_warning_button_display = 'deck less than 40 cards'
        save_pass = False


    if save_pass:

        player2.identity = 'pvp'
        user.deck_list = []
        user.character_card = ''

        if button_status.lobby_screen_room_detail_display == 'other':
            button_status.lobby_screen_other_ready_to_go = True
        elif button_status.lobby_screen_room_detail_display == 'my':
            button_status.lobby_screen_my_ready_to_go = True

        # Render user's deck
        with open('user_deck_list_string.txt','r') as f:
            f.seek(0)
            for line in f:
                if 'DECK_LIST_' + user.deck_list_index in line:
                    user.deck_list = make_deck_from_string(line.replace('DECK_LIST_' + user.deck_list_index + ' = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                if 'CHARACTER_' + user.deck_list_index in line:
                    user.character_card = make_deck_from_string(line.replace('CHARACTER_' + user.deck_list_index + ' = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]

        if button_status.lobby_screen_room_detail_display == 'my':
            user.random_deck_list = random.sample(user.deck_list, len(user.deck_list))
            user.remain_deck_list = user.random_deck_list[5:]
            user.hand_list = user.random_deck_list[0:5]
        elif button_status.lobby_screen_room_detail_display == 'other':
            user.random_deck_list = random.sample(user.deck_list, len(user.deck_list))
            user.remain_deck_list = user.random_deck_list[6:]
            user.hand_list = user.random_deck_list[0:6]

def lobby_screen_game_start_action(ai_settings, grid,screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ lobby screen start action"""


    # Clear up and initiate all display/progress indicator on battle screen
    # screen_status
    screen_status.battle_screen_my_hand_page_id = 1
    screen_status.battle_screen_action_indicator = 'stage-0'
    screen_status.battle_screen_player2_action_display_indicator = False
    # button_status
    button_status.battle_screen_win_lost_display = False
    button_status.battle_screen_win_lost_indicator = ''
    button_status.battle_screen_instruction_bar_yes_display = True
    button_status.battle_screen_instruction_bar_yes_backend = True
    button_status.battle_screen_instruction_bar_skip_display = False
    button_status.battle_screen_instruction_bar_skip_backend = False
    button_status.battle_screen_stable_button_backend = True
    button_status.battle_screen_my_hand_page_change_button_backend = True
    button_status.battle_screen_menu_display = False
    button_status.battle_screen_history_bar_detail_display = False
    button_status.battle_screen_history_bar_text_dict = {
        '1' : '',
        '2' : '',
        '3' : '',
        '4' : '',
        '5' : '',
        '6' : '',
        '7' : '',
        '8' : '',
        '9' : '',
        '10' : '',
        '11' : '',
        '12' : '',
        '13' : '',
        '14' : '',
        '15' : '',
    }
    button_status.battle_screen_my_hand_indicator_display = False
    button_status.battle_screen_my_hand_indicator_position = '1'
    button_status.battle_screen_player1_battleground_indicator_display = False
    button_status.battle_screen_player1_battleground_indicator_position = '1'
    button_status.battle_screen_player2_battleground_indicator_display = False
    button_status.battle_screen_player2_battleground_indicator_position = '1'
    button_status.card_zoom_active = False
    button_status.card_zoom_screen_indicator = 'build_deck_screen'
    button_status.card_zoom_part_indicator = ''
    button_status.card_zoom_position_indicator = '1'
    button_status.battle_screen_win_lost_indicator = ''

    #user
    user.monster_in_play_dict = {
        '1' : '',
        '2' : '',
        '3' : '',
        '4' : '',
        '5' : '',
        '6' : '',
    }
    user.monster_in_play_length = '0'
    user.item_in_play_dict = {
        '1' : '',
        '2' : '',
        '3' : '',
        '4' : '',
        '5' : '',
        '6' : '',
    }
    user.item_in_play_length = '0'
    user.character_under_card_by_level = {
        '10' : '',
        '20' : '',
        '30' : '',
        '40' : '',
        '50' : '',
        '60' : '',
        '70' : '',
        '80' : '',
        '90' : '',
        '100' : '',
        '110' : '',
        '120' : '',
        '130' : '',
        '140' : '',
        '150' : '',
    }
    user.stage_2_other_card_usable_list = []

    #player2
    player2.character_under_card_by_level = {
        '10' : '',
        '20' : '',
        '30' : '',
        '40' : '',
        '50' : '',
        '60' : '',
        '70' : '',
        '80' : '',
        '90' : '',
        '100' : '',
        '110' : '',
        '120' : '',
        '130' : '',
        '140' : '',
        '150' : '',
    }
    player2.monster_in_play_dict = {
        '1' : '',
        '2' : '',
        '3' : '',
        '4' : '',
        '5' : '',
        '6' : '',
    }
    player2.monster_in_play_length = '0'
    player2.item_in_play_dict = {
        '1' : '',
        '2' : '',
        '3' : '',
        '4' : '',
        '5' : '',
        '6' : '',
    }
    player2.item_in_play_length = '0'
    player2.stage_2_other_card_usable_list = []


#-----------------------------Prepare screen display----------------------------------------------------
def prepare_screen_grid_display(grid, screen):
    """ Display grid system on prepare screen"""
    screen.blit(grid.prepare_screen_menu_grid, grid.prepare_screen_menu_grid_rect)
    screen.blit(grid.prepare_screen_pick_deck_grid, grid.prepare_screen_pick_deck_grid_rect)
    screen.blit(grid.prepare_screen_ai_setup_grid, grid.prepare_screen_ai_setup_grid_rect)

def prepare_screen_stable_button_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display stable buttons"""
    # Back
    button_back = Button('Back','', (250,250,250),0, 0, 50, 50, font_size = 18, font_color = (0,0,0),alpha = 200)
    button_back.update()
    button_back.draw(screen)
    # Play
    button_play = Button('Play!','', (250,250,250),1150, 0, 50, 50, font_size = 18, font_color = (0,0,0), alpha = 150)
    button_play.update()
    button_play.draw(screen)
    # Hello
    button1 = Button('Hello '+ user.name +'!','', (250,250,250),300, 0, 600, 50, font_size = 20, font_color = (0,0,0),alpha = 200)
    button1.update()
    button1.draw(screen)
    # change name
    button_back = Button('Change Name','', (150,40,40),780, 10, 110, 30, font_size = 14,alpha = 200)
    button_back.update()
    button_back.draw(screen)
    # Pick deck text
    button_text_1 = Button('Pick an exist deck or create a new one: ','', (250,250,250),400, 100, 400, 35, font_color = (0,0,0), alpha = 150)
    button_text_1.update()
    button_text_1.draw(screen)

    # Deck list buttons
    with open('user_deck_list_string.txt','r') as f:
        f.seek(0)
        if len(f.readlines()) >= 12:
            pass
        else:
            button_new_deck = Button('+ New Deck','', (250,250,250),1020, 110, 120, 35, font_color = (0,0,0), alpha = 150)
            button_new_deck.update()
            button_new_deck.draw(screen)


        f.seek(0)
        x = len(f.readlines())
        y = 0
        deck_list_index = 0

        for i in range(1,7):
            f.seek(0)
            for line in f:
                if 'DECK_LIST_' + str(i) not in line:
                    y += 1
            if y < x: # DECK_LIST_i exist
                f.seek(0)
                for line in f:
                    if 'DECK_LIST_' + str(i) in line:
                        deck_length = len(make_card_list_from_string(line.replace('DECK_LIST_' + str(i) + ' = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2))
                        # deck_length = int((len(line.replace('DECK_LIST_' + str(i) + ' = ', '')) -1)/14)
                    if 'CHARACTER_' + str(i) in line:
                        character_length = 1
                        character_card = eval('card_' + line.replace('CHARACTER_' + str(i) + ' = ', '')[7:12])

                if user.deck_list_index == str(i):

                    button_top = Button(character_card.name + ': ','', (100,30,130),85 + 180* (i-1), 165, 130, 60)
                    button_top.update()
                    button_top.draw(screen)

                    if deck_length < 40:
                        button_bottom = Button(str(character_length) + '/1  |  ' + str(deck_length) +'/40','', (100,30,130),85 + 180* (i-1), 225, 130, 50, font_color = (250,0,0))
                        button_bottom.update()
                        button_bottom.draw(screen)
                    else:
                        button_bottom = Button(str(character_length) + '/1  |  ' + str(deck_length) +'/40','', (100,30,130),85 + 180* (i-1), 225, 130, 50)
                        button_bottom.update()
                        button_bottom.draw(screen)

                else:

                    button_top = Button(character_card.name + ': ','', (160,160,160),85 + 180* (i-1), 165, 130, 60, alpha = 240)
                    button_top.update()
                    button_top.draw(screen)

                    if deck_length < 40:
                        button_bottom = Button(str(character_length) + '/1  |  ' + str(deck_length) +'/40','', (160,160,160),85 + 180* (i-1), 225, 130, 50, font_color = (200,0,0), alpha = 240)
                        button_bottom.update()
                        button_bottom.draw(screen)
                    else:
                        button_bottom = Button(str(character_length) + '/1  |  ' + str(deck_length) +'/40','', (160,160,160),85 + 180* (i-1), 225, 130, 50, alpha = 240)
                        button_bottom.update()
                        button_bottom.draw(screen)

                y = 0

            else: # DECK_LIST_i not exist

                button = Button('Empty','', (200,200,200),85 + 180* (i-1), 165, 130, 110, alpha = 80)
                button.update()
                button.draw(screen)

                y = 0

    # Pick opponents buttons
    # Pick opponents text
    button_text_2 = Button('Pick an opponent to play against: ','', (250,250,250),400, 350, 400, 35, font_color = (0,0,0), alpha = 150) # (200,100,170)
    button_text_2.update()
    button_text_2.draw(screen)


    # 8 characters available
    character_list = [card_01_16, card_01_37, card_01_59, card_01_89, card_03_11, card_05_30, card_01_64, card_05_61]
    row_number = 1
    rect_position_x = 70
    rect_position_y = 395
    for card in character_list:
        if row_number <= 4:
            card.rect.x = rect_position_x
            card.rect.y = rect_position_y
            screen.blit(card.image, card.rect)
            rect_position_x += 160
            row_number += 1
        elif row_number <= 8:
            card.rect.x = rect_position_x - 640
            card.rect.y = rect_position_y + 190
            screen.blit(card.image, card.rect)
            rect_position_x += 160
            row_number += 1
            if row_number >= 9:
                row_number = 1


    # Pick a difficulty
    button_text_3 = Button('Pick a difficulty: ','', (250,250,250),810, 400, 200, 35, font_color = (0,0,0), alpha = 150)
    button_text_3.update()
    button_text_3.draw(screen)

    if player2.ai_difficulty_index == '1':
        button_difficulty_1 = Button('Beginner  (Opponent start with 3 cards, 50% Hp)','', (100,30,130),710, 445, 410, 70)
        button_difficulty_1.update()
        button_difficulty_1.draw(screen)
    else:
        button_difficulty_1 = Button('Beginner  (Opponent start with 3 cards, 50% Hp)','', (160,160,160),710, 445, 410, 70, alpha = 240)
        button_difficulty_1.update()
        button_difficulty_1.draw(screen)

    if player2.ai_difficulty_index == '2':
        button_difficulty_2 = Button('Normal  (Opponent start with 6 cards, 100% Hp)','', (100,30,130),710, 525, 410, 70)
        button_difficulty_2.update()
        button_difficulty_2.draw(screen)
    else:
        button_difficulty_2 = Button('Normal  (Opponent start with 6 cards, 100% Hp)','', (160,160,160),710, 525, 410, 70, alpha = 240)
        button_difficulty_2.update()
        button_difficulty_2.draw(screen)

    if player2.ai_difficulty_index == '3':
        button_difficulty_3 = Button('Hard  (Opponent start with 10 cards, 200% Hp)','', (100,30,130),710, 605, 410, 70)
        button_difficulty_3.update()
        button_difficulty_3.draw(screen)
    else:
        button_difficulty_3 = Button('Hard  (Opponent start with 10 cards, 200% Hp)','', (160,160,160),710, 605, 410, 70, alpha = 240)
        button_difficulty_3.update()
        button_difficulty_3.draw(screen)

    if player2.ai_difficulty_index == '4':
        button_difficulty_4 = Button('Impossible  (Opponent start with 30 cards, 400% Hp)','', (100,30,130),710, 685, 410, 70)
        button_difficulty_4.update()
        button_difficulty_4.draw(screen)
    else:
        button_difficulty_4 = Button('Impossible  (Opponent start with 30 cards, 400% Hp)','', (160,160,160),710, 685, 410, 70, alpha = 240)
        button_difficulty_4.update()
        button_difficulty_4.draw(screen)

def prepare_screen_button_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display unstable buttons of prepare screen"""
    for i in range(1,7):
        if user.deck_list_index == str(i):
            button_edit = Button('Edit','', (50,50,170),85 + 180* (i-1), 282, 60, 30)
            button_edit.update()
            button_edit.draw(screen)

            button_delete = Button('Delete','', (160,30,30), 155 + 180* (i-1), 282, 60, 30)
            button_delete.update()
            button_delete.draw(screen)

    # Red rectangle around opponent card
    for i in range(1,9):
        if player2.character_ai_index == str(i):
            if i <= 4:
                button_top = Button('','', (250,0,0), 65 + 160*(i-1), 390, 140, 5)
                button_top.update()
                button_top.draw(screen)

                button_bottom = Button('','', (250,0,0),65 + 160*(i-1), 575, 140, 5)
                button_bottom.update()
                button_bottom.draw(screen)

                button_left = Button('','', (250,0,0), 65 + 160*(i-1), 395, 5, 180)
                button_left.update()
                button_left.draw(screen)

                button_right = Button('','', (250,0,0), 200 + 160*(i-1), 395, 5, 180)
                button_right.update()
                button_right.draw(screen)
            else:
                button_top = Button('','', (250,0,0), 65 + 160*(i-5), 580, 140, 5)
                button_top.update()
                button_top.draw(screen)

                button_bottom = Button('','', (250,0,0),65 + 160*(i-5), 765, 140, 5)
                button_bottom.update()
                button_bottom.draw(screen)

                button_left = Button('','', (250,0,0), 65 + 160*(i-5), 585, 5, 180)
                button_left.update()
                button_left.draw(screen)

                button_right = Button('','', (250,0,0), 200 + 160*(i-5), 585, 5, 180)
                button_right.update()
                button_right.draw(screen)

def prepare_screen_end_screen_warning_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display warning when end prepare screen"""
    if button_status.prepare_screen_end_screen_warning_button_display == 'deck less than 40 cards':
        button = Button('You need at least 40','' ,(122,33,38),1050, 0, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('cards in your deck!','' ,(122,33,38),1050, 30, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('','' ,(122,33,38),1050, 60, 150, 40,font_size = 18)
        button.update()
        button.draw(screen)

        button = Button('ok','' ,(22,143,78),1100, 62, 40, 30,font_size = 16)
        button.update()
        button.draw(screen)

    elif button_status.prepare_screen_end_screen_warning_button_display == 'no deck':
        button = Button('Please pick a deck','' ,(122,33,38),1050, 0, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('or build a new one!','' ,(122,33,38),1050, 30, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('','' ,(122,33,38),1050, 60, 150, 40,font_size = 18)
        button.update()
        button.draw(screen)

        button = Button('ok','' ,(22,143,78),1100, 62, 40, 30,font_size = 16)
        button.update()
        button.draw(screen)

    elif button_status.prepare_screen_end_screen_warning_button_display == 'no character':
        button = Button('Please pick a character','' ,(122,33,38),1050, 0, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('for your opponent!','' ,(122,33,38),1050, 30, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('','' ,(122,33,38),1050, 60, 150, 40,font_size = 18)
        button.update()
        button.draw(screen)

        button = Button('ok','' ,(22,143,78),1100, 62, 40, 30,font_size = 16)
        button.update()
        button.draw(screen)

    elif button_status.prepare_screen_end_screen_warning_button_display == 'no difficulty':
        button = Button('Please pick a difficulty','' ,(122,33,38),1050, 0, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('for your opponent!','' ,(122,33,38),1050, 30, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('','' ,(122,33,38),1050, 60, 150, 40,font_size = 18)
        button.update()
        button.draw(screen)

        button = Button('ok','' ,(22,143,78),1100, 62, 40, 30,font_size = 16)
        button.update()
        button.draw(screen)

def prepare_screen_to_battle_screen_action(ai_settings, screen,buttons, screen_status, button_status, card_database_filter, user, player2):
    """ Actions when click on play!"""
    save_pass = True
    # Clear dup number each call

    with open('user_deck_list_string.txt','r') as f:
        f.seek(0)
        for line in f:
            if 'DECK_LIST_' + user.deck_list_index in line:
                list1 = make_deck_from_string(line.replace('DECK_LIST_' + user.deck_list_index + ' = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

    if user.deck_list_index == '0' or user.deck_list_index == 'new':
        button_status.prepare_screen_end_screen_warning_button_display = 'no deck'
        save_pass = False

    elif len(list1) < 40:

        button_status.prepare_screen_end_screen_warning_button_display = 'deck less than 40 cards'
        save_pass = False

    elif player2.character_ai_index == '0':
        button_status.prepare_screen_end_screen_warning_button_display = 'no character'
        save_pass = False

    elif player2.ai_difficulty_index == '0':
        button_status.prepare_screen_end_screen_warning_button_display = 'no difficulty'
        save_pass = False

    if save_pass:

        # render AI character deck
        if player2.character_ai_index == '1':
            player2.character_card = make_deck_from_string(str(['CARD_01_16']), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
            player2.deck_list = make_deck_from_string(player2.NIXIE_DECK, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

        elif player2.character_ai_index == '2':
            player2.character_card = make_deck_from_string(str(['CARD_01_37']), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
            player2.deck_list = make_deck_from_string(player2.MAYA_DECK, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

        elif player2.character_ai_index == '3':
            player2.character_card = make_deck_from_string(str(['CARD_01_59']), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
            player2.deck_list = make_deck_from_string(player2.IVAN_DECK, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

        elif player2.character_ai_index == '4':
            player2.character_card = make_deck_from_string(str(['CARD_01_89']), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
            player2.deck_list = make_deck_from_string(player2.SHERMAN_DECK, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

        elif player2.character_ai_index == '5':
            player2.character_card = make_deck_from_string(str(['CARD_03_11']), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
            player2.deck_list = make_deck_from_string(player2.MOBY_DECK, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

        elif player2.character_ai_index == '6':
            player2.character_card = make_deck_from_string(str(['CARD_05_30']), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
            player2.deck_list = make_deck_from_string(player2.MAHIBANG_DECK, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

        elif player2.character_ai_index == '7':
            player2.character_card = make_deck_from_string(str(['CARD_01_64']), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
            player2.deck_list = make_deck_from_string(player2.MISTMOON_DECK, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

        elif player2.character_ai_index == '8':
            player2.character_card = make_deck_from_string(str(['CARD_05_61']), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
            player2.deck_list = make_deck_from_string(player2.FANGBLADE_DECK, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)

        # Set up AI difficulty
        if player2.ai_difficulty_index == '1':
            player2.random_deck_list = random.sample(player2.deck_list, len(player2.deck_list))
            player2.remain_deck_list = player2.random_deck_list[3:]
            player2.hand_list = player2.random_deck_list[0:3]
            player2.character_card.health = str(int(int(player2.character_card.health)*0.5))

        elif player2.ai_difficulty_index == '2':
            player2.random_deck_list = random.sample(player2.deck_list, len(player2.deck_list))
            player2.remain_deck_list = player2.random_deck_list[6:]
            player2.hand_list = player2.random_deck_list[0:6]
            player2.character_card.health = str(int(player2.character_card.health)*1)

        elif player2.ai_difficulty_index == '3':
            player2.random_deck_list = random.sample(player2.deck_list, len(player2.deck_list))
            player2.remain_deck_list = player2.random_deck_list[10:]
            player2.hand_list = player2.random_deck_list[0:10]
            player2.character_card.health = str(int(player2.character_card.health)*2)

        elif player2.ai_difficulty_index == '4':
            player2.random_deck_list = random.sample(player2.deck_list, len(player2.deck_list))
            player2.remain_deck_list = player2.random_deck_list[6:]
            player2.hand_list = player2.random_deck_list[0:30]
            player2.character_card.health = str(int(player2.character_card.health)*4)


        # Render user's deck
        with open('user_deck_list_string.txt','r') as f:
            f.seek(0)
            for line in f:
                if 'DECK_LIST_' + user.deck_list_index in line:
                    user.deck_list = make_deck_from_string(line.replace('DECK_LIST_' + user.deck_list_index + ' = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                if 'CHARACTER_' + user.deck_list_index in line:
                    user.character_card = make_deck_from_string(line.replace('CHARACTER_' + user.deck_list_index + ' = ', ''), ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2)[0]
                    #user.character_card = eval('card_' + line.replace('CHARACTER_' + user.deck_list_index + ' = ', '')[7:12])

        user.random_deck_list = random.sample(user.deck_list, len(user.deck_list))
        user.remain_deck_list = user.random_deck_list[6:]
        user.hand_list = user.random_deck_list[0:6]


        # Clear up and initiate all display/progress indicator on battle screen
        # screen_status
        screen_status.battle_screen_my_hand_page_id = 1
        screen_status.battle_screen_action_indicator = 'stage-0'
        screen_status.battle_screen_player2_action_display_indicator = False
        # button_status
        button_status.battle_screen_win_lost_display = False
        button_status.battle_screen_win_lost_indicator = ''
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True
        button_status.battle_screen_instruction_bar_skip_display = False
        button_status.battle_screen_instruction_bar_skip_backend = False
        button_status.battle_screen_stable_button_backend = True
        button_status.battle_screen_my_hand_page_change_button_backend = True
        button_status.battle_screen_menu_display = False
        button_status.battle_screen_history_bar_detail_display = False
        button_status.battle_screen_history_bar_text_dict = {
            '1' : '',
            '2' : '',
            '3' : '',
            '4' : '',
            '5' : '',
            '6' : '',
            '7' : '',
            '8' : '',
            '9' : '',
            '10' : '',
            '11' : '',
            '12' : '',
            '13' : '',
            '14' : '',
            '15' : '',
        }
        button_status.battle_screen_my_hand_indicator_display = False
        button_status.battle_screen_my_hand_indicator_position = '1'
        button_status.battle_screen_player1_battleground_indicator_display = False
        button_status.battle_screen_player1_battleground_indicator_position = '1'
        button_status.battle_screen_player2_battleground_indicator_display = False
        button_status.battle_screen_player2_battleground_indicator_position = '1'
        button_status.card_zoom_active = False
        button_status.card_zoom_screen_indicator = 'build_deck_screen'
        button_status.card_zoom_part_indicator = ''
        button_status.card_zoom_position_indicator = '1'
        button_status.battle_screen_win_lost_indicator = ''

        #user
        user.monster_in_play_dict = {
            '1' : '',
            '2' : '',
            '3' : '',
            '4' : '',
            '5' : '',
            '6' : '',
        }
        user.monster_in_play_length = '0'
        user.item_in_play_dict = {
            '1' : '',
            '2' : '',
            '3' : '',
            '4' : '',
            '5' : '',
            '6' : '',
        }
        user.item_in_play_length = '0'
        user.character_under_card_by_level = {
            '10' : '',
            '20' : '',
            '30' : '',
            '40' : '',
            '50' : '',
            '60' : '',
            '70' : '',
            '80' : '',
            '90' : '',
            '100' : '',
            '110' : '',
            '120' : '',
            '130' : '',
            '140' : '',
            '150' : '',
        }
        user.stage_2_other_card_usable_list = []

        #player2
        player2.character_under_card_by_level = {
            '10' : '',
            '20' : '',
            '30' : '',
            '40' : '',
            '50' : '',
            '60' : '',
            '70' : '',
            '80' : '',
            '90' : '',
            '100' : '',
            '110' : '',
            '120' : '',
            '130' : '',
            '140' : '',
            '150' : '',
        }
        player2.monster_in_play_dict = {
            '1' : '',
            '2' : '',
            '3' : '',
            '4' : '',
            '5' : '',
            '6' : '',
        }
        player2.monster_in_play_length = '0'
        player2.item_in_play_dict = {
            '1' : '',
            '2' : '',
            '3' : '',
            '4' : '',
            '5' : '',
            '6' : '',
        }
        player2.item_in_play_length = '0'
        player2.stage_2_other_card_usable_list = []




#-----------------------------Build deck screen actions----------------------------------------------------
def build_deck_screen_grid_display(grid, screen):
    """ Display grid system for build deck screen"""
    screen.blit(grid.build_deck_screen_card_gallery_grid, grid.build_deck_screen_card_gallery_grid_rect)
    screen.blit(grid.build_deck_screen_deck_grid, grid.build_deck_screen_deck_grid_rect)

def build_deck_screen_stable_button_display(screen, buttons,screen_status,button_status):
    """ Display all stable buttons for build deck screen"""
    # button1 = Button('Back','build_deck_screen', (0,0,0),0, 0, 50, 50)
    # button1.update()
    # button1.draw(screen)
    button2 = Button('Save','build_deck_screen', (250,250,250),1150, 0, 50, 50, font_color = (0,0,0), alpha = 150)
    button2.update()
    button2.draw(screen)
    button3 = Button('Build your deck by picking 40 cards below: ', 'build_deck_screen', (250,250,250),300, 0, 600, 50, font_color = (0,0,0), alpha = 150)
    button3.update()
    button3.draw(screen)
    if button_status.build_deck_screen_stable_button_backend:
        buttons.extend((button2, button3))
        button_status.build_deck_screen_stable_button_backend = False


# - - - - - - - - - - - - -

def build_deck_screen_card_gallery_display(screen, buttons, screen_status, button_status, card_database_filter):
    """Display Card Gallery"""
    build_deck_screen_card_gallery_button_display(screen, buttons, screen_status, button_status, card_database_filter)
    build_deck_screen_card_gallery_card_display(screen, buttons, screen_status, button_status, card_database_filter)

def build_deck_screen_card_gallery_button_display(screen, buttons, screen_status, button_status, card_database_filter):
    """Display all buttons in the card gallery part"""
    # Page forward button
    button1 = Button('>>','build_deck_screen_card_gallery_stable', (250,250,250),1100, 300, 50, 50,font_color = (0,0,0), alpha = 150)
    # Edge cases when len() = 14,28,42 ...
    if len(cdf.request_card_list(card_database_filter)) % 14 == 0 and len(cdf.request_card_list(card_database_filter)) != 0:
        if screen_status.build_deck_screen_card_gallery_page_id != ((len(cdf.request_card_list(card_database_filter)))//14): # Make sure on the last page no foreward button shows up
            button1.update()
            button1.draw(screen)
    # Normal cases
    else:
        if screen_status.build_deck_screen_card_gallery_page_id != ((len(cdf.request_card_list(card_database_filter)))//14 + 1): # Make sure on the last page no foreward button shows up
            button1.update()
            button1.draw(screen)
    # Page backward button
    button2 = Button('<<', 'build_deck_screen_card_gallery_stable' ,(250,250,250),50, 300, 50, 50,font_color = (0,0,0), alpha = 150)
    if screen_status.build_deck_screen_card_gallery_page_id != 1: # Make sure on the first page no backward button shows up
        button2.update()
        button2.draw(screen)
    # button3: page button to display the current page number for card gallery
    button3 = Button('page: ' + str(screen_status.build_deck_screen_card_gallery_page_id), 'build_deck_screen_card_gallery_stable' ,(250,250,250),560, 510, 80, 40,font_color = (0,0,0), alpha = 150)
    button3.update()
    button3.draw(screen)
    # Class filter:
    button4 = Button('Filter: ','' ,(250,250,250),80, 70, 90, 50, font_color = (0,0,0), alpha = 150)
    button4.update()
    button4.draw(screen)
    # Character filter button
    if card_database_filter.character:
        button_character = Button('Character', '', (100,30,130),200,70,90,50)
    else:
        button_character = Button('Character', '', (250,250,250),200,70,90,50,font_color = (0,0,0), alpha = 150)
    button_character.update()
    button_character.draw(screen)
    # Bowman filter button
    if card_database_filter.bowman:
        button_bowman = Button('Bowman', '', (100,30,130),300,70,90,50)
    else:
        button_bowman = Button('Bowman', '', (250,250,250),300,70,90,50, font_color = (0,0,0), alpha = 150)
    button_bowman.update()
    button_bowman.draw(screen)
    # Magician filter button
    if card_database_filter.magician:
        button_magician = Button('Magician', '', (100,30,130),400,70,90,50)
    else:
        button_magician = Button('Magician', '', (250,250,250),400,70,90,50, font_color = (0,0,0), alpha = 150)
    button_magician.update()
    button_magician.draw(screen)
    # Thief filter button
    if card_database_filter.thief:
        button_thief = Button('Thief', '', (100,30,130),500,70,90,50)
    else:
        button_thief = Button('Thief', '', (250,250,250),500,70,90,50, font_color = (0,0,0), alpha = 150)
    button_thief.update()
    button_thief.draw(screen)
    # Warrior filter button
    if card_database_filter.warrior:
        button_warrior = Button('Warrior', '', (100,30,130),600,70,90,50)
    else:
        button_warrior = Button('Warrior', '', (250,250,250),600,70,90,50,font_color = (0,0,0), alpha = 150)
    button_warrior.update()
    button_warrior.draw(screen)
    # Jobless filter button
    if card_database_filter.jobless:
        button_jobless = Button('Jobless', '', (100,30,130),700,70,90,50)
    else:
        button_jobless = Button('Jobless', '', (250,250,250),700,70,90,50, font_color = (0,0,0), alpha = 150)
    button_jobless.update()
    button_jobless.draw(screen)
    # Add all buttons to buttons list so that check_events function can detect mouse click on those buttons.
    if button_status.build_deck_screen_card_gallery_button_backend:
        buttons.extend((button1,button2,button3,button4,button_character, button_bowman,button_magician,button_thief,button_warrior,button_jobless))
        button_status.build_deck_screen_card_gallery_button_backend = False

def build_deck_screen_card_gallery_card_display(screen, buttons, screen_status, button_status, card_database_filter):
    """Display all cards on card gallery"""
    rect_position_x = 100 #local variables for rect position for the first card in the card gallery
    rect_position_y = 130
    row_number = 1 # local variable to help keep track of position of card
    # Check the page number to make sure if will not go negative or randomly large
    if screen_status.build_deck_screen_card_gallery_page_id <= 0:
        screen_status.build_deck_screen_card_gallery_page_id = 1
    # Edge cases when len() = 14, 28, 42...
    if len(cdf.request_card_list(card_database_filter)) % 14 == 0 and len(cdf.request_card_list(card_database_filter)) != 0:
        if screen_status.build_deck_screen_card_gallery_page_id >= (len(cdf.request_card_list(card_database_filter)))//14 + 1:
            screen_status.build_deck_screen_card_gallery_page_id = (len(cdf.request_card_list(card_database_filter)))//14 + 0

    else:
        if screen_status.build_deck_screen_card_gallery_page_id >= (len(cdf.request_card_list(card_database_filter)))//14 + 2:
            screen_status.build_deck_screen_card_gallery_page_id = (len(cdf.request_card_list(card_database_filter)))//14 + 1
    # Algorithm to draw all cards in request_card_list, 14 card per page.
    for card in cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1):14 * screen_status.build_deck_screen_card_gallery_page_id]:
        if row_number <= 7:
            card.rect.x = rect_position_x
            card.rect.y = rect_position_y
            screen.blit(card.image, card.rect)
            rect_position_x += 145
            row_number += 1
        elif row_number <= 14:
            card.rect.x = rect_position_x - 1015
            card.rect.y = rect_position_y + 200
            screen.blit(card.image, card.rect)
            rect_position_x += 145
            row_number += 1
            if row_number >= 15:
                row_number = 1

# - - - - - - - - - - - - -

def build_deck_screen_my_deck_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """Display things on my deck portion"""

    build_deck_screen_my_deck_button_display(screen,buttons, screen_status, button_status, card_database_filter, user)

    build_deck_screen_my_deck_card_display(screen,buttons, screen_status, button_status, card_database_filter, user)

def build_deck_screen_my_deck_button_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """Display buttons on my deck part of the screen"""
    local_store_list = build_deck_screen_my_deck_card_list_refine(user)
    #character number display
    if user.character_card == '':
        button1 = Button('Character: 0/1','' ,(250,250,250),50, 560, 150, 30, font_color = (255,60,60), alpha = 150)
    else:
        button1 = Button('Character: 1/1','' ,(250,250,250),50, 560, 150, 30, font_color = (0,0,0), alpha = 150)
    button1.update()
    button1.draw(screen)
    #card number display
    if len(user.deck_list) >= 40:
        button2 = Button('Total: ' + str(len(user.deck_list)) + '/40','' ,(250,250,250),620, 560, 100, 30,font_color = (0,0,0), alpha = 150)
    else:
        button2 = Button('Total: ' + str(len(user.deck_list)) + '/40','' ,(250,250,250),620, 560, 100, 30, font_color = (255,60,60), alpha = 150)
    button2.update()
    button2.draw(screen)

    # Page forward button
    button3 = Button('>','', (250,250,250),1110,650, 30, 30, font_color = (0,0,0), alpha = 150)
    # Edge cases when len() = 14,28,42 ...
    if len(local_store_list) % 6 == 0 and len(local_store_list) != 0:
        if screen_status.build_deck_screen_my_deck_page_id != ((len(local_store_list))//6): # Make sure on the last page no foreward button shows up
            button3.update()
            button3.draw(screen)
    # Normal cases
    else:
        if screen_status.build_deck_screen_my_deck_page_id != ((len(local_store_list))//6 + 1): # Make sure on the last page no foreward button shows up
            button3.update()
            button3.draw(screen)
    # Page backward button
    button4 = Button('<','', (250,250,250),210,650, 30, 30, font_color = (0,0,0), alpha = 150)
    if screen_status.build_deck_screen_my_deck_page_id != 1: # Make sure on the first page no backward button shows up
        button4.update()
        button4.draw(screen)

    if button_status.build_deck_screen_my_deck_button_backend:
        buttons.extend((button3,button4))
        button_status.build_deck_screen_my_deck_button_backend = False

def build_deck_screen_my_deck_card_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """Input user.deck_list, drawing the card list propperly"""
    # Draw the character card
    if user.character_card == '':
        pass
    else:
        user.character_card.rect.x = 65
        user.character_card.rect.y = 600
        screen.blit(user.character_card.image, user.character_card.rect)
    #Clear duplicate amount each frame and render the refined list
    for card_new in user.deck_list:
        card_new.duplicate = 1
    local_store_list = build_deck_screen_my_deck_card_list_refine(user)
    #use refined list to draw
    rect_position_x = 245 #local variables for rect position for the first card in the user deck
    rect_position_y = 600
    row_number = 1
    #Display cards in local_store_list:

    if screen_status.build_deck_screen_my_deck_page_id <= 0:
        screen_status.build_deck_screen_my_deck_page_id = 1
    # Edge cases when len() = 6,12,18....
    if len(local_store_list) % 6 == 0 and len(local_store_list) != 0:
        if screen_status.build_deck_screen_my_deck_page_id >= (len(local_store_list))//6 + 1:
            screen_status.build_deck_screen_my_deck_page_id = (len(local_store_list))//6 + 0

    else:
        if screen_status.build_deck_screen_my_deck_page_id >= (len(local_store_list))//6 + 2:
            screen_status.build_deck_screen_my_deck_page_id = (len(local_store_list))//6 + 1
    # Algorithm to draw all cards in local_store_list, 6 card per page.
    for card in local_store_list[6*(screen_status.build_deck_screen_my_deck_page_id - 1):6 * screen_status.build_deck_screen_my_deck_page_id]:
        if row_number <= 6:
            card.rect.x = rect_position_x
            card.rect.y = rect_position_y
            screen.blit(card.image, card.rect)
            rect_position_x += 145
            row_number += 1
            build_deck_screen_my_deck_duplicate_number_display(card, screen)
            if row_number >= 7:
                row_number = 1

def build_deck_screen_my_deck_duplicate_number_display(card, screen):
    """Input Card instance, output how many copies of that card as a button above that card"""
    if card.duplicate <= 4:
        button_dup = Button(str(card.duplicate) + 'x','', (250,250,250),(card.rect.x + 50),(card.rect.y - 30) , 30, 30, font_color = (0,0,0), alpha = 150)
    else:
        button_dup = Button(str(card.duplicate) + 'x','', (250,250,250),(card.rect.x + 50),(card.rect.y - 30) , 30, 30, font_color = (255,60,60), alpha = 150)
    button_dup.update()
    button_dup.draw(screen)

def build_deck_screen_end_screen_warning_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display build deck screen end turn warining button"""
    if button_status.build_deck_screen_end_screen_warning_button_display == 'character card':
        button = Button('Missing A','' ,(122,33,38),1050, 0, 150, 30,font_size = 18)
        button.update()
        button.draw(screen)

        button = Button('Character Card!','' ,(122,33,38),1050, 30, 150, 30,font_size = 18)
        button.update()
        button.draw(screen)

        button = Button('','' ,(122,33,38),1050, 60, 150, 40,font_size = 18)
        button.update()
        button.draw(screen)

        button = Button('ok','' ,(22,143,78),1100, 62, 40, 30,font_size = 16)
        button.update()
        button.draw(screen)

    elif button_status.build_deck_screen_end_screen_warning_button_display == '4 copy each':
        button = Button('No More Than 4','' ,(122,33,38),1050, 0, 150, 30,font_size = 15)
        button.update()
        button.draw(screen)

        button = Button('Copies For Each Card!','' ,(122,33,38),1050, 30, 150, 30,font_size = 13)
        button.update()
        button.draw(screen)

        button = Button('','' ,(122,33,38),1050, 60, 150, 40,font_size = 18)
        button.update()
        button.draw(screen)

        button = Button('ok','' ,(22,143,78),1100, 62, 40, 30,font_size = 16)
        button.update()
        button.draw(screen)

def build_deck_screen_add_card_to_deck(card_gallery_position ,screen, screen_status,card_database_filter, user):
    """Add card from gallery to user.deck_list"""
    # Check to avoid errors when click on empty rect preventing adding card.
    if len(cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1):14 * screen_status.build_deck_screen_card_gallery_page_id]) >= int(card_gallery_position):
        if cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1)+(int(card_gallery_position)-1)].card_type == 'character':
            user.character_card = cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1)+(int(card_gallery_position)-1)]
        else:
            user.deck_list.append(cdf.request_card_list(card_database_filter)[14*(screen_status.build_deck_screen_card_gallery_page_id - 1)+(int(card_gallery_position)-1)])
    else:
        pass

def build_deck_screen_remove_card_from_deck(my_deck_position ,screen, screen_status,card_database_filter, user):
    """ Input card position and user.deck_list, remove one instance of that card from the user.deck_list"""
    local_store_list = build_deck_screen_my_deck_card_list_refine(user)
    # Check to avoid errors when click on empty rect preventing removing card.
    if len(local_store_list[6*(screen_status.build_deck_screen_my_deck_page_id - 1):6 * screen_status.build_deck_screen_my_deck_page_id]) >= int(my_deck_position):
        user.deck_list.remove(local_store_list[6*(screen_status.build_deck_screen_my_deck_page_id - 1)+(int(my_deck_position)-1)])
    else:
        pass

def build_deck_screen_my_deck_card_list_refine(user):
    """Input user.deck_list, return a refined version without duplicate and save duplicate number in class instance"""
    local_store_list = []
    for card_new in user.deck_list:

        if len(local_store_list) == 0:
            local_store_list.append(card_new)
        else:

            if build_deck_screen_my_deck_check_duplicate(card_new, local_store_list):
                card_new.duplicate += 1
            else:
                local_store_list.append(card_new)

    return sorted(local_store_list, key = lambda card: int(card.level))

def build_deck_screen_my_deck_check_duplicate(card, local_store_list):
    """ Input a card and a list, check if that card is in the list"""
    for cd in local_store_list:
        if card.set_number == cd.set_number and card.card_number == cd.card_number:
            return True
            break
    return False

def build_deck_screen_save_deck_to_file(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ save user deck list into txt file as string"""
    save_pass = True
    # Clear dup number each call
    for card_new in user.deck_list:
        card_new.duplicate = 1
    local_store_list = build_deck_screen_my_deck_card_list_refine(user)

    for card in local_store_list:

        if card.duplicate > 4:

            button_status.build_deck_screen_end_screen_warning_button_display = '4 copy each'
            save_pass = False


    if user.character_card == '':
        button_status.build_deck_screen_end_screen_warning_button_display = 'character card'
        save_pass = False


    if save_pass:

        if user.deck_list_index == 'new':

            deck_list_string = []
            character_string = ['CARD_' + user.character_card.set_number + '_' + user.character_card.card_number]
            for card in user.deck_list:
                deck_list_string.append('CARD_' + card.set_number + '_' + card.card_number)

            with open('user_deck_list_string.txt','a+') as f:
                f.seek(0)
                x = len(f.readlines())
                y = 0
                deck_list_index = 0
                for i in range(1,7):
                    f.seek(0)
                    for line in f:
                        if 'DECK_LIST_' + str(i) not in line:
                            y += 1
                    if y < x: # This means the index i has already exist, so we go for the next available i
                        y = 0
                    else: # y = x means index i is free to use
                        deck_list_index = i
                        break

                f.write('DECK_LIST_' + str(deck_list_index) + ' = ' + str(deck_list_string) + '\n')
                f.write('CHARACTER_' + str(deck_list_index) + ' = ' + str(character_string) + '\n')

        else:
            for i in range(1,7):
                if user.deck_list_index == str(i):

                    deck_list_string = []
                    character_string = ['CARD_' + user.character_card.set_number + '_' + user.character_card.card_number]
                    for card in user.deck_list:
                        deck_list_string.append('CARD_' + card.set_number + '_' + card.card_number)

                    with open('user_deck_list_string.txt','a+') as f:
                        f.seek(0)
                        x = f.readlines()
                        y = 1
                        f.seek(0)
                        for line in f:
                            if 'DECK_LIST_' + user.deck_list_index not in line:
                                y += 1
                            else:
                                break
                        x[y-1] = 'DECK_LIST_' + str(user.deck_list_index) + ' = ' + str(deck_list_string) + '\n'
                        x[y] = 'CHARACTER_' + str(user.deck_list_index) + ' = ' + str(character_string) + '\n'

                    with open('user_deck_list_string.txt','w') as f:
                        f.writelines(x)



#-----------------------------Battle Screen displays-------------------------------------------------
def battle_screen_grid_display(grid, screen):
    """ Display grid system on battle screen"""
    screen.blit(grid.battle_screen_menu_grid, grid.battle_screen_menu_grid_rect)
    screen.blit(grid.battle_screen_deck_grid, grid.battle_screen_deck_grid_rect)
    screen.blit(grid.battle_screen_character_1_grid, grid.battle_screen_character_1_grid_rect)
    screen.blit(grid.battle_screen_character_2_grid, grid.battle_screen_character_2_grid_rect)
    screen.blit(grid.battle_screen_battle_1_grid, grid.battle_screen_battle_1_grid_rect)
    screen.blit(grid.battle_screen_battle_2_grid, grid.battle_screen_battle_2_grid_rect)
    screen.blit(grid.battle_screen_item_1_grid, grid.battle_screen_item_1_grid_rect)
    screen.blit(grid.battle_screen_item_2_grid, grid.battle_screen_item_2_grid_rect)
    screen.blit(grid.battle_screen_instruction_bar_grid, grid.battle_screen_instruction_bar_grid_rect)

def battle_screen_instruction_bar_display(screen,buttons, screen_status, button_status, card_database_filter, user,player2):
    """ Display instruction bar"""
    # pvp
    if player2.identity == 'pvp':
        if button_status.battle_screen_pvp_turn_indicator == 'my' and screen_status.battle_screen_action_indicator != 'stage-0':
            screen_status.battle_screen_action_indicator = 'stage-1'
            button_status.battle_screen_pvp_turn_indicator = 'my-ing'
        elif button_status.battle_screen_pvp_turn_indicator == 'other':
            screen_status.battle_screen_action_indicator = 'stage-1'
            button_status.battle_screen_pvp_turn_indicator = 'other-ing'
    # Instruction bar control according to which stage

    if screen_status.battle_screen_action_indicator == 'stage-0':
        if player2.identity == 'pvp' and button_status.lobby_screen_room_detail_display == 'my':
            button_status.battle_screen_instruction_bar_text = "Let's play! You go first!"
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_skip_display = False
            button_status.battle_screen_instruction_bar_skip_backend = False
        elif player2.identity == 'pvp' and button_status.lobby_screen_room_detail_display == 'other':
            button_status.battle_screen_instruction_bar_text = "Let's play! Your opponent will go first!"
            button_status.battle_screen_instruction_bar_yes_display = False
            button_status.battle_screen_instruction_bar_yes_backend = False
            button_status.battle_screen_instruction_bar_skip_display = False
            button_status.battle_screen_instruction_bar_skip_backend = False
        elif player2.identity == 'AI':
            button_status.battle_screen_instruction_bar_text = "Let's play! You go first!"
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_skip_display = False
            button_status.battle_screen_instruction_bar_skip_backend = False

    elif screen_status.battle_screen_action_indicator == 'stage-1':
        button_status.battle_screen_instruction_bar_text = 'Do you want to level up this turn?'
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True

    elif screen_status.battle_screen_action_indicator == 'stage-1-level-up':
        button_status.battle_screen_instruction_bar_text = 'Pick a card to level up or skip leveling up this turn'
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True

    elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-1':
        button_status.battle_screen_instruction_bar_text = 'Character action 1: Do you want to use: ' + user.character_card.skill_1_type + ' ?'
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True

    elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-2':
        button_status.battle_screen_instruction_bar_text = 'Character action 2: Do you want to use: ' + user.character_card.skill_2_type + ' ?'
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True

    elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-3':
        button_status.battle_screen_instruction_bar_text = 'Character action 3: Do you want to use: ' + user.character_card.skill_3_type + ' ?'
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True

    elif (('stage-2-other-action-' in screen_status.battle_screen_action_indicator)
        and (screen_status.battle_screen_player2_action_display_indicator == False)
        and 'detail' not in screen_status.battle_screen_action_indicator):
        x = screen_status.battle_screen_action_indicator.replace('stage-2-other-action-','')
        button_status.battle_screen_instruction_bar_text = 'Other action: Do you want to use: ' + user.character_under_card_by_level[x].lv_type
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True

    elif (('stage-2-other-action-' in screen_status.battle_screen_action_indicator)
        and (screen_status.battle_screen_player2_action_display_indicator == False)
        ):
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True

    elif ('stage-3-monster' in screen_status.battle_screen_action_indicator
        and (screen_status.battle_screen_player2_action_display_indicator == False)):
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True

    elif screen_status.battle_screen_action_indicator == 'stage-4-end-turn':
        button_status.battle_screen_instruction_bar_text = "Your turn has end with " + user.item_in_play_length + " item. Deal " + str(int(user.item_in_play_length)*10) + ' damage. Gain ' + str(int(user.item_in_play_length)*10) + ' hp.'
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True
        button_status.battle_screen_instruction_bar_skip_display = False
        button_status.battle_screen_instruction_bar_skip_backend = False


    # instruction bar draw
    button_instruction_bar = Button(button_status.battle_screen_instruction_bar_text,'battle_screen_instruction_bar_text', (0,0,0),100, 570, 1000, 30,alpha = 100)

    if 1: # Display
        button_instruction_bar.update()
        button_instruction_bar.draw(screen)
    if 0:# Backend
        x = 0
        for button in buttons:
            if button_instruction_bar.group == button.group:
                x = 1
                break
            else:
                pass
        if x == 0:
            buttons.append(button_instruction_bar)
        else:
            pass

    # yes button
    button_yes = Button('Yes','battle_screen_instruction_bar_yes', (43,93,67),605, 540, 60, 22) #(880, 544, 60, 22)


    if button_status.battle_screen_instruction_bar_yes_display == True: # Display
        button_yes.update()
        button_yes.draw(screen)
    if button_status.battle_screen_instruction_bar_yes_backend == True: # Backend
        x = 0
        for button in buttons:
            if button_yes.group == button.group:
                x = 1
                break
            else:
                pass
        if x == 0:
            buttons.append(button_yes)
        else:
            pass
    elif button_status.battle_screen_instruction_bar_yes_backend == False:
        bt = ''
        for button in buttons:
            if button.group == button_yes.group:
                bt = button
        if bt == '':
            pass
        else:
            buttons.remove(bt)

    # Skip button
    button_skip = Button('Skip','battle_screen_instruction_bar_skip', (200,70,70),535, 540, 60, 22)

    if button_status.battle_screen_instruction_bar_skip_display == True: # Display
        button_skip.update()
        button_skip.draw(screen)
    if button_status.battle_screen_instruction_bar_skip_backend == True: # Backend
        x = 0
        for button in buttons:
            if button_skip.group == button.group:
                x = 1
                break
            else:
                pass
        if x == 0:
            buttons.append(button_skip)
        else:
            pass
    elif button_status.battle_screen_instruction_bar_skip_backend == False:
        bt = ''
        for button in buttons:
            if button.group == button_skip.group:
                bt = button
        if bt == '':
            pass
        else:
            buttons.remove(bt)

def battle_screen_stable_button_display(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user, player2):
    """ Display all stable button on battle screen"""
    button_1 = Button('Rules','', (250,250,250),200, 0, 50, 30, font_color = (0,0,0), alpha = 150)
    button_1.update()
    button_1.draw(screen)
    # menu
    button_menu = Button('Menu','', (250,250,250),950, 0, 50, 30, font_color = (0,0,0), alpha = 150)
    button_menu.update()
    button_menu.draw(screen)
    # Display user name
    button2 = Button(user.name,'', (250,250,250),1110, 570, 90, 30, font_color = (0,0,0), alpha = 150)
    button2.update()
    button2.draw(screen)
    # Display opponent's name
    if player2.character_ai_index == '1':
        player2_AI = 'NIXIE'
    elif player2.character_ai_index == '2':
        player2_AI = 'MAYA'
    elif player2.character_ai_index == '3':
        player2_AI = 'IVAN'
    elif player2.character_ai_index == '4':
        player2_AI = 'SHERMAN'
    elif player2.character_ai_index == '5':
        player2_AI = 'MOBY'
    elif player2.character_ai_index == '6':
        player2_AI = 'MAHIBANG'
    elif player2.character_ai_index == '7':
        player2_AI = 'MISTMOON'
    elif player2.character_ai_index == '8':
        player2_AI = 'FANGBLADE'
    elif player2.identity == 'pvp':
        player2_AI = player2.name
    try:
        button2 = Button(player2_AI,'', (250,250,250),0, 570, 90, 30, font_color = (0,0,0), alpha = 150)
        button2.update()
        button2.draw(screen)
    except UnboundLocalError:
        pass
    # add menu button to buttons group
    if button_status.battle_screen_stable_button_backend:
        buttons.append(button_menu)
        button_status.battle_screen_stable_button_backend = False

def battle_screen_history_bar_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display action history for both players"""


    for number,text in button_status.battle_screen_history_bar_text_dict.items():
        if int(number) == 1:
            button_text = Button(text,'', (0,0,0),250, 0, 600, 30, font_size = 13, alpha = 100)
            button_text.update()
            button_text.draw(screen)
        else:
            pass

    button_details = Button('+','', (0,0,0),850, 0, 100, 30,font_size = 25, alpha = 100)
    button_details.update()
    button_details.draw(screen)

    if button_status.battle_screen_history_bar_detail_display == True:
        i = 0
        for number,text in button_status.battle_screen_history_bar_text_dict.items():

            if int(number) % 2 == 1 and text != '':
                if text == "Game Started!":
                    button_odd = Button(text,'', (0,160,0),200, 30 + 30*(i), 800, 30, font_size = 13)
                    button_odd.update()
                    button_odd.draw(screen)
                    i += 1
                elif text == "Your turn has started":
                    button_odd = Button(text,'', (0,160,0),200, 30 + 30*(i), 800, 30, font_size = 13)
                    button_odd.update()
                    button_odd.draw(screen)
                    i += 1
                elif text == "Opponent's turn has started":
                    button_odd = Button(text,'', (160,0,0),200, 30 + 30*(i), 800, 30, font_size = 13)
                    button_odd.update()
                    button_odd.draw(screen)
                    i += 1
                else:
                    button_odd = Button(text,'', (160,160,160),200, 30 + 30*(i), 800, 30, font_size = 13)
                    button_odd.update()
                    button_odd.draw(screen)
                    i += 1
            elif int(number) % 2 == 0 and text != '':
                if text == "Game Started!":
                    button_even = Button(text,'', (0,160,0),200, 60 + 30 * (i-1), 800, 30, font_size = 13)
                    button_even.update()
                    button_even.draw(screen)
                    i += 1
                elif text == "Your turn has started":
                    button_even = Button(text,'', (0,160,0),200, 60 + 30 * (i-1), 800, 30, font_size = 13)
                    button_even.update()
                    button_even.draw(screen)
                    i += 1
                elif text == "Opponent's turn has started":
                    button_even = Button(text,'', (160,0,0),200, 60 + 30 * (i-1), 800, 30, font_size = 13)
                    button_even.update()
                    button_even.draw(screen)
                    i += 1
                else:
                    button_even = Button(text,'', (130,130,130),200, 60 + 30 * (i-1), 800, 30, font_size = 13)
                    button_even.update()
                    button_even.draw(screen)
                    i += 1

def battle_screen_my_hand_card_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display my deck on battle screen"""
    rect_position_x = 100
    rect_position_y = 610
    row_number = 1
    if screen_status.battle_screen_action_indicator == 'stage-0':
        pass
    else :

        if screen_status.battle_screen_my_hand_page_id <= 0:
            screen_status.battle_screen_my_hand_page_id = 1
        # Edge cases when len() = 6,12,18....
        if len(user.hand_list) % 7 == 0 and len(user.hand_list) != 0:
            if screen_status.battle_screen_my_hand_page_id >= (len(user.hand_list))//7 + 1:
                screen_status.battle_screen_my_hand_page_id = (len(user.hand_list))//7 + 0

        else:
            if screen_status.battle_screen_my_hand_page_id >= (len(user.hand_list))//7 + 2:
                screen_status.battle_screen_my_hand_page_id = (len(user.hand_list))//7 + 1
        # Algorithm to draw all cards in local_store_list, 6 card per page.
        for card in user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]:
            if row_number <= 7:
                card.rect.x = rect_position_x
                card.rect.y = rect_position_y
                screen.blit(card.image, card.rect)
                rect_position_x += 145
                row_number += 1
                if row_number >= 8:
                    row_number = 1

def battle_screen_my_hand_button_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display buttons in my hand on battle screen"""
    if screen_status.battle_screen_action_indicator != 'stage-0':
        # Page forward button
        button1 = Button('>','', (0,0,0),1100, 660, 50, 50)
        # Edge cases when len() = 14,28,42 ...
        if len(user.hand_list) % 7 == 0 and len(user.hand_list) != 0:
            if screen_status.battle_screen_my_hand_page_id != ((len(user.hand_list))//7): # Make sure on the last page no foreward button shows up
                button1.update()
                button1.draw(screen)
        # Normal cases
        else:
            if screen_status.battle_screen_my_hand_page_id != ((len(user.hand_list))//7 + 1): # Make sure on the last page no foreward button shows up
                button1.update()
                button1.draw(screen)
        # Page backward button
        button2 = Button('<', '' ,(0,0,0),50, 660, 50, 50)
        if screen_status.battle_screen_my_hand_page_id != 1: # Make sure on the first page no backward button shows up
            button2.update()
            button2.draw(screen)
        #
        if button_status.battle_screen_my_hand_page_change_button_backend:
            buttons.extend((button1,button2))
            button_status.battle_screen_my_hand_page_change_button_backend = False
    if ((screen_status.battle_screen_action_indicator == 'stage-1-level-up'
        or ('stage-2-character-action-' in screen_status.battle_screen_action_indicator and 'detail' in screen_status.battle_screen_action_indicator)
        or 'stage-2-other-action-detail-spawn' in screen_status.battle_screen_action_indicator
        or 'stage-2-other-action-detail-think-fast' in screen_status.battle_screen_action_indicator
        or 'stage-2-other-action-detail-equip' in screen_status.battle_screen_action_indicator
        or 'stage-2-other-action-detail-sneak' in screen_status.battle_screen_action_indicator
        or 'stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator)
        and (screen_status.battle_screen_player2_action_display_indicator == False)):
        if button_status.battle_screen_my_hand_indicator_display == True:
            located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]

            button_top = Button('','', (250,0,0),located_card.rect.x-5, located_card.rect.y - 5, 140, 5)
            button_top.update()
            button_top.draw(screen)

            button_bottom = Button('','', (250,0,0),located_card.rect.x-5, located_card.rect.y + 180, 140, 5)
            button_bottom.update()
            button_bottom.draw(screen)

            button_left = Button('','', (250,0,0),located_card.rect.x-5, located_card.rect.y, 5, 180)
            button_left.update()
            button_left.draw(screen)

            button_right = Button('','', (250,0,0),located_card.rect.x + 130, located_card.rect.y , 5, 180)
            button_right.update()
            button_right.draw(screen)
            # button_level_up = Button('***','battle_screen_handaction_****', (70,70,150),located_card.rect.x+10, located_card.rect.y - 27, 115, 27)
            # button_level_up.update()
            # button_level_up.draw(screen)

def battle_screen_character_1_card_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display character 1 card layout"""
    user.character_card.rect.x = 1050
    user.character_card.rect.y = 40
    screen.blit(user.character_card.image, user.character_card.rect)
    #
    for i in range(1,16):
        if int(user.character_card.level) >= 10 * i:
            user.character_under_card_by_level[str(10 * i)].bottom_rect.x = 1050
            user.character_under_card_by_level[str(10 * i)].bottom_rect.y = 220 + 23 * (i-1)
            screen.blit(user.character_under_card_by_level[str(10 * i)].bottom_image, user.character_under_card_by_level[str(10 * i)].bottom_rect)

    #

def battle_screen_character_1_button_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display character 1 buttons"""
    button_basic_info = Button('Lv: ' + user.character_card.level + '  HP: ' + user.character_card.health + '  Card #: ' + str(len(user.hand_list)),'', (0,0,0),1000, 0, 200, 30, alpha = 100)
    button_basic_info.update()
    button_basic_info.draw(screen)

    if ('stage-2-character-action-1' in screen_status.battle_screen_action_indicator
        and screen_status.battle_screen_player2_action_display_indicator == False):
        button_action_pointer = Button('>>','',(92,13,78),1000,132,50,23,alpha = 0)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif ('stage-2-character-action-2' in screen_status.battle_screen_action_indicator
        and screen_status.battle_screen_player2_action_display_indicator == False):
        button_action_pointer = Button('>>','',(92,13,78),1000,155,50,23, alpha = 0)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif ('stage-2-character-action-3' in screen_status.battle_screen_action_indicator
        and screen_status.battle_screen_player2_action_display_indicator == False):
        button_action_pointer = Button('>>','',(92,13,78),1000,178,50,23, alpha = 0)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif ('stage-2-other-action-' in screen_status.battle_screen_action_indicator
        and screen_status.battle_screen_player2_action_display_indicator == False
        and 'detail' not in screen_status.battle_screen_action_indicator):
        x = screen_status.battle_screen_action_indicator.replace('stage-2-other-action-','')
        button_action_pointer = Button('>>','',(92,13,78),1000,220+23*(int(x)/10-1),50,23, alpha = 0)
        button_action_pointer.update()
        button_action_pointer.draw(screen)

def battle_screen_battleground_card_display(screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Display cards on battleground """
    # Monsters
    for i in range(1,4):
        if user.monster_in_play_dict[str(i)] != '' and int(user.monster_in_play_dict[str(i)].health) > 0:
            user.monster_in_play_dict[str(i)].top_rect.x = 650
            user.monster_in_play_dict[str(i)].top_rect.y = 220 + 110*(i-1)
            screen.blit(user.monster_in_play_dict[str(i)].top_image, user.monster_in_play_dict[str(i)].top_rect)

            button_monster_info_hp = Button('HP:  ' + user.monster_in_play_dict[str(i)].health,'',(0,0,0),650,220 + 110*(i-1),40,20, font_size = 10)
            button_monster_info_hp.update()
            button_monster_info_hp.draw(screen)

            button_monster_info_attack = Button('ATT: ' + user.monster_in_play_dict[str(i)].attack,'',(0,0,0),650,240 + 110*(i-1),40,20, font_size = 10)
            button_monster_info_attack.update()
            button_monster_info_attack.draw(screen)

    for i in range(4,7):
        if user.monster_in_play_dict[str(i)] != '' and int(user.monster_in_play_dict[str(i)].health) > 0:
            user.monster_in_play_dict[str(i)].top_rect.x = 825
            user.monster_in_play_dict[str(i)].top_rect.y = 220 + 110*(i-4)
            screen.blit(user.monster_in_play_dict[str(i)].top_image, user.monster_in_play_dict[str(i)].top_rect)

            button_monster_info_hp = Button('HP:  ' + user.monster_in_play_dict[str(i)].health,'',(0,0,0),825,220 + 110*(i-4),40,20, font_size = 10)
            button_monster_info_hp.update()
            button_monster_info_hp.draw(screen)

            button_monster_info_attack = Button('ATT: ' + user.monster_in_play_dict[str(i)].attack,'',(0,0,0),825,240 + 110*(i-4),40,20, font_size = 10)
            button_monster_info_attack.update()
            button_monster_info_attack.draw(screen)
    # Items
    for i in range(1,4):
        if user.item_in_play_dict[str(i)] != '':
            user.item_in_play_dict[str(i)].top_rect.x = 620 + 130*(i-1)
            user.item_in_play_dict[str(i)].top_rect.y = 40
            screen.blit(user.item_in_play_dict[str(i)].top_image, user.item_in_play_dict[str(i)].top_rect)
    for i in range(4,7):
        if user.item_in_play_dict[str(i)] != '':
            user.item_in_play_dict[str(i)].top_rect.x = 620 + 130*(i-4)
            user.item_in_play_dict[str(i)].top_rect.y = 110
            screen.blit(user.item_in_play_dict[str(i)].top_image, user.item_in_play_dict[str(i)].top_rect)

def battle_screen_player2_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display informations of player2"""
    # Display Character card
    player2.character_card.rect.x = 20
    player2.character_card.rect.y = 40
    screen.blit(player2.character_card.image, player2.character_card.rect)

    # Info bar above character_card
    button_basic_info = Button('Lv: ' + player2.character_card.level + '  HP: ' + player2.character_card.health + '  Card #: ' + str(len(player2.hand_list)),'', (0,0,0),0, 0, 200, 30, alpha = 100)
    button_basic_info.update()
    button_basic_info.draw(screen)

    # Display cards under character card
    for i in range(1,16):
        if int(player2.character_card.level) >= 10 * i:
            player2.character_under_card_by_level[str(10 * i)].bottom_rect.x = 20
            player2.character_under_card_by_level[str(10 * i)].bottom_rect.y = 220 + 23 * (i-1)
            screen.blit(player2.character_under_card_by_level[str(10 * i)].bottom_image, player2.character_under_card_by_level[str(10 * i)].bottom_rect)

    # Display the arrow when doing actions
    if screen_status.battle_screen_action_indicator == 'player2-stage-2-character-action-1':
        button_action_pointer = Button('<<','',(92,13,78),150,132,50,23, alpha = 0)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif screen_status.battle_screen_action_indicator == 'player2-stage-2-character-action-2':
        button_action_pointer = Button('<<','',(92,13,78),150,155,50,23, alpha = 0)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif screen_status.battle_screen_action_indicator == 'player2-stage-2-character-action-3':
        button_action_pointer = Button('<<','',(92,13,78),150,178,50,23, alpha = 0)
        button_action_pointer.update()
        button_action_pointer.draw(screen)
    elif 'player2-stage-2-other-action-' in screen_status.battle_screen_action_indicator:
        if len(screen_status.battle_screen_action_indicator.replace('player2-stage-2-other-action-','')) <= 2:
            x = screen_status.battle_screen_action_indicator.replace('player2-stage-2-other-action-','')[:2]
            button_action_pointer = Button('<<','',(92,13,78),150,220+23*(int(x)/10-1),50,23, alpha = 0)
            button_action_pointer.update()
            button_action_pointer.draw(screen)
        elif len(screen_status.battle_screen_action_indicator.replace('player2-stage-2-other-action-','')) <= 3:
            x = screen_status.battle_screen_action_indicator.replace('player2-stage-2-other-action-','')[:3]
            button_action_pointer = Button('<<','',(92,13,78),150,220+23*(int(x)/10-1),50,23, alpha = 0)
            button_action_pointer.update()
            button_action_pointer.draw(screen)
        else:
            pass



    # Display Monsters
    for i in range(1,4):
        if player2.monster_in_play_dict[str(i)] != '' and int(player2.monster_in_play_dict[str(i)].health) > 0:
            player2.monster_in_play_dict[str(i)].top_rect.x = 420
            player2.monster_in_play_dict[str(i)].top_rect.y = 220 + 110*(i-1)
            screen.blit(player2.monster_in_play_dict[str(i)].top_image, player2.monster_in_play_dict[str(i)].top_rect)

            button_monster_info_hp = Button('HP:  ' + player2.monster_in_play_dict[str(i)].health,'',(0,0,0),420,220 + 110*(i-1),40,20, font_size = 10)
            button_monster_info_hp.update()
            button_monster_info_hp.draw(screen)

            button_monster_info_attack = Button('ATT: ' + player2.monster_in_play_dict[str(i)].attack,'',(0,0,0),420,240 + 110*(i-1),40,20, font_size = 10)
            button_monster_info_attack.update()
            button_monster_info_attack.draw(screen)

    for i in range(4,7):
        if player2.monster_in_play_dict[str(i)] != '' and int(player2.monster_in_play_dict[str(i)].health) > 0:
            player2.monster_in_play_dict[str(i)].top_rect.x = 245
            player2.monster_in_play_dict[str(i)].top_rect.y = 220 + 110*(i-4)
            screen.blit(player2.monster_in_play_dict[str(i)].top_image, player2.monster_in_play_dict[str(i)].top_rect)

            button_monster_info_hp = Button('HP:  ' + player2.monster_in_play_dict[str(i)].health,'',(0,0,0),245,220 + 110*(i-4),40,20, font_size = 10)
            button_monster_info_hp.update()
            button_monster_info_hp.draw(screen)

            button_monster_info_attack = Button('ATT: ' + player2.monster_in_play_dict[str(i)].attack,'',(0,0,0),245,240 + 110*(i-4),40,20, font_size = 10)
            button_monster_info_attack.update()
            button_monster_info_attack.draw(screen)

    # Display Items
    for i in range(1,4):
        if player2.item_in_play_dict[str(i)] != '':
            player2.item_in_play_dict[str(i)].top_rect.x = 476 - 130*(i-1)
            player2.item_in_play_dict[str(i)].top_rect.y = 40
            screen.blit(player2.item_in_play_dict[str(i)].top_image, player2.item_in_play_dict[str(i)].top_rect)
    for i in range(4,7):
        if player2.item_in_play_dict[str(i)] != '':
            player2.item_in_play_dict[str(i)].top_rect.x = 476 - 130*(i-4)
            player2.item_in_play_dict[str(i)].top_rect.y = 110
            screen.blit(player2.item_in_play_dict[str(i)].top_image, player2.item_in_play_dict[str(i)].top_rect)

    # Display actions cooldown
    if screen_status.battle_screen_player2_action_display_indicator:
        now = pygame.time.get_ticks()
        cooldown = int(ai_settings.AI_speed_indicator)
        if now - screen_status.time_last >= cooldown:
            screen_status.time_last = now
            battle_screen_player2_action(ai_settings,screen, buttons,screen_status, button_status, card_database_filter, user, player2)

def battle_screen_battleground_button_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display buttons on battleground"""
    if ('stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator
        or ('stage-2-character-action-' in screen_status.battle_screen_action_indicator and '-detail-tactic-1' in screen_status.battle_screen_action_indicator)
        or ('stage-2-character-action-' in screen_status.battle_screen_action_indicator and 'easy-shot' in screen_status.battle_screen_action_indicator)
        or ('stage-2-character-action-' in screen_status.battle_screen_action_indicator and 'tricky-shot' in screen_status.battle_screen_action_indicator)
        or 'stage-3-monster-' in screen_status.battle_screen_action_indicator
        or 'stage-2-other-action-detail-easy-shot' in screen_status.battle_screen_action_indicator
        or 'stage-2-other-action-detail-tricky-shot' in screen_status.battle_screen_action_indicator
        ):
        if button_status.battle_screen_player1_battleground_indicator_display == True:
            if int(button_status.battle_screen_player1_battleground_indicator_position) <= 3:
                i = int(button_status.battle_screen_player1_battleground_indicator_position)
                monster_rect_x = 650
                monster_rect_y = 220 + 110*(i-1)
                button = Button('***','', (70,70,150),monster_rect_x + 50, monster_rect_y - 27, 30, 27)
                button.update()
                button.draw(screen)
            elif int(button_status.battle_screen_player1_battleground_indicator_position) <= 6:
                i = int(button_status.battle_screen_player1_battleground_indicator_position)
                monster_rect_x = 825
                monster_rect_y = 220 + 110*(i-4)
                button = Button('***','', (70,70,150),monster_rect_x + 50, monster_rect_y - 27, 30, 27)
                button.update()
                button.draw(screen)

        if button_status.battle_screen_player2_battleground_indicator_display == True:
            if int(button_status.battle_screen_player2_battleground_indicator_position) <= 3:
                i = int(button_status.battle_screen_player2_battleground_indicator_position)
                monster_rect_x = 420
                monster_rect_y = 220 + 110*(i-1)
                button = Button('***','', (70,70,150),monster_rect_x + 50, monster_rect_y - 27, 30, 27)
                button.update()
                button.draw(screen)
            elif int(button_status.battle_screen_player2_battleground_indicator_position) <= 6:
                i = int(button_status.battle_screen_player2_battleground_indicator_position)
                monster_rect_x = 245
                monster_rect_y = 220 + 110*(i-4)
                button = Button('***','', (70,70,150),monster_rect_x + 50, monster_rect_y - 27, 30, 27)
                button.update()
                button.draw(screen)

def battle_screen_menu_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display menu on battle screen"""
    if button_status.battle_screen_menu_display == True:

        button = Button('','', (0,0,0), 580, 30, 420, 340, alpha = 200)
        button.update()
        button.draw(screen)
        # Sound settings
        button_sound = Button('Sound: ','', (0,0,0), 601, 51, 105, 35, font_size = 28, alpha = 0)
        button_sound.update()
        button_sound.draw(screen)

        if ai_settings.sound_indicator == True:
            button_1 = Button('On','', (50,150,50), 447+280, 323-270, 28, 28)
            button_1.update()
            button_1.draw(screen)

            button_2 = Button('Off','', (150,150,150), 482+280, 323-270, 28, 28)
            button_2.update()
            button_2.draw(screen)

        else:
            button_1 = Button('On','', (150,150,150), 447+280, 323-270, 28, 28)
            button_1.update()
            button_1.draw(screen)

            button_2 = Button('Off','', (150,50,50), 482+280, 323-270, 28, 28)
            button_2.update()
            button_2.draw(screen)


        # Music settings
        button_music = Button('Music: ','', (0,0,0), 321+280, 370-270, 105, 35, font_size = 28, alpha = 0)
        button_music.update()
        button_music.draw(screen)

        if ai_settings.music_indicator == True:
            button_1 = Button('On','', (50,150,50), 447+280, 372-270, 28, 28)
            button_1.update()
            button_1.draw(screen)

            button_2 = Button('Off','', (150,150,150), 482+280, 372-270, 28, 28)
            button_2.update()
            button_2.draw(screen)

        else:
            button_1 = Button('On','', (150,150,150), 447+280, 372-270, 28, 28)
            button_1.update()
            button_1.draw(screen)

            button_2 = Button('Off','', (150,50,50), 482+280, 372-270, 28, 28)
            button_2.update()
            button_2.draw(screen)

        # Theme settings
        button_theme = Button('Theme: ','', (0,0,0), 321+280, 419-270, 112, 35, font_size = 28, alpha = 0)
        button_theme.update()
        button_theme.draw(screen)

        if ai_settings.theme_indicator == 'Lith Harbor':
            button_1 = Button('Lith Harbor','', (50,150,50), 447+280, 419-270, 98, 35, font_size = 16)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Lith Harbor','', (150,150,150), 447+280, 419-270, 98, 35, font_size = 16)
            button_1.update()
            button_1.draw(screen)

        if ai_settings.theme_indicator == 'Leafre':
            button_1 = Button('Leafre','', (50,150,50), 559+280, 419-270, 98, 35, font_size = 16)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Leafre','', (150,150,150), 559+280, 419-270, 98, 35, font_size = 16)
            button_1.update()
            button_1.draw(screen)

        if ai_settings.theme_indicator == 'Pantheon':
            button_1 = Button('Pantheon','', (50,150,50), 447+280, 468-270, 98, 35, font_size = 16)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Pantheon','', (150,150,150), 447+280, 468-270, 98, 35, font_size = 16)
            button_1.update()
            button_1.draw(screen)

        if ai_settings.theme_indicator == 'Ellinia':
            button_1 = Button('Ellinia','', (50,150,50), 559+280, 468-270, 98, 35, font_size = 16)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Ellinia','', (150,150,150), 559+280, 468-270, 98, 35, font_size = 16)
            button_1.update()
            button_1.draw(screen)

        # AI speeding settings
        button_ai_speed = Button('AI Speed: ','', (0,0,0), 321+280, 524-270, 140, 35, font_size = 28, alpha = 0)
        button_ai_speed.update()
        button_ai_speed.draw(screen)

        if ai_settings.AI_speed_indicator == '1000':
            button_1 = Button('Fast','', (50,150,50), 475+280, 524-270, 56, 35, font_size = 15)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Fast','', (150,150,150), 475+280, 524-270, 56, 35, font_size = 15)
            button_1.update()
            button_1.draw(screen)

        if ai_settings.AI_speed_indicator == '2000':
            button_1 = Button('Normal','', (50,150,50), 545+280, 524-270, 56, 35, font_size = 15)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Normal','', (150,150,150), 545+280, 524-270, 56, 35, font_size = 15)
            button_1.update()
            button_1.draw(screen)

        if ai_settings.AI_speed_indicator == '3000':
            button_1 = Button('Slow','', (50,150,50), 615+280, 524-270, 56, 35, font_size = 15)
            button_1.update()
            button_1.draw(screen)
        else:
            button_1 = Button('Slow','', (150,150,150), 615+280, 524-270, 56, 35, font_size = 15)
            button_1.update()
            button_1.draw(screen)

        # Closed settings window button
        button_1 = Button('X','', (250,100,100), 699+280, 300-270, 21, 21, font_size = 16)
        button_1.update()
        button_1.draw(screen)


        button_1 = Button('Concede and Quit!','', (170,70,70), 700, 310, 180, 40)
        button_1.update()
        button_1.draw(screen)



def battle_screen_win_lost_display(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Display win/lost message"""
    if button_status.battle_screen_win_lost_indicator == 'win':
        button_win_1 = Button('VICTORY!','', (70,170,70), 300,  200, 600, 200, font_size = 70, alpha = 180)
        button_win_1.update()
        button_win_1.draw(screen)

        button_win_2 = Button('','', (70,170,70), 300,  400, 600, 200, alpha = 180)
        button_win_2.update()
        button_win_2.draw(screen)

        button_win_3 = Button('Back To Main Menu','', (70,70,170), 500,  500, 200, 40)
        button_win_3.update()
        button_win_3.draw(screen)

        screen_status.battle_screen_action_indicator = 'game-end'


    elif button_status.battle_screen_win_lost_indicator == 'lost':
        button_lost_1 = Button('DEFEAT!','', (170,70,70), 300,  200, 600, 200, font_size = 70, alpha = 180)
        button_lost_1.update()
        button_lost_1.draw(screen)

        button_lost_2 = Button('','', (170,70,70), 300,  400, 600, 200, alpha = 180)
        button_lost_2.update()
        button_lost_2.draw(screen)

        button_lost_2 = Button('Back To Main Menu','', (70,70,170), 500,  500, 200, 40)
        button_lost_2.update()
        button_lost_2.draw(screen)

        screen_status.battle_screen_action_indicator = 'game-end'

def battle_screen_result_update(ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ update result in each cycle"""
    # Monster list update
    # Remove monsters with < 0 HP and rebuild monster dict
    dict1 = {
        '1' : '',
        '2' : '',
        '3' : '',
        '4' : '',
        '5' : '',
        '6' : '',
    }
    list1 = []
    for position, card in user.monster_in_play_dict.items():
        if card != '' and int(card.health) > 0:
            list1.append(card)

    x1 = len(list1)
    while x1 > 0:
        dict1[str(x1)] = list1[x1-1]
        x1 -= 1

    user.monster_in_play_dict = dict1

    #player2
    dict2 = {
        '1' : '',
        '2' : '',
        '3' : '',
        '4' : '',
        '5' : '',
        '6' : '',
    }
    list2 = []
    for position, card in player2.monster_in_play_dict.items():
        if card != '' and int(card.health) > 0:
            list2.append(card)

    x2 = len(list2)
    while x2 > 0:
        dict2[str(x2)] = list2[x2-1]
        x2 -= 1

    player2.monster_in_play_dict = dict2






    # items list length update

    for position,card in user.item_in_play_dict.items():
        if card != '':
            user.item_in_play_length = position

    for position,card in player2.item_in_play_dict.items():
        if card != '':
            player2.item_in_play_length = position

    # monster list length update

    for position,card in user.monster_in_play_dict.items():
        if card != '':
            user.monster_in_play_length = position

    for position,card in player2.monster_in_play_dict.items():
        if card != '':
            player2.monster_in_play_length = position


    # Win/Lost situations
    if int(user.character_card.health) <= 0:
        button_status.battle_screen_win_lost_indicator = 'lost'
    if int(player2.character_card.health) <= 0:
        button_status.battle_screen_win_lost_indicator = 'win'



# -----------------------------Battle Screen Actions----------------------------------------


def battle_screen_hand_click_action(click_type,ai_settings, screen,buttons, screen_status, button_status, card_database_filter, user,player2, position = ''):
    """ Action after click on my hand part"""
    if click_type == 'hand':
        if screen_status.battle_screen_action_indicator == 'stage-1-level-up':
            if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                button_status.battle_screen_my_hand_indicator_position = position
                button_status.battle_screen_my_hand_indicator_display = True
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True

            else:
                pass

        elif 'stage-2-character-action-' in screen_status.battle_screen_action_indicator and 'detail-spawn' in screen_status.battle_screen_action_indicator:

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'monster'
                        and (int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a monster lv','').replace(' or less and click yes to play.','')))
                        and int(user.monster_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass

        elif 'stage-2-character-action-' in screen_status.battle_screen_action_indicator and 'detail-think-fast' in screen_status.battle_screen_action_indicator:

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'tactic'
                        and (int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a tactic lv','').replace(' or less and click yes to play.','')))):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass

        elif 'stage-2-character-action-' in screen_status.battle_screen_action_indicator and 'detail-equip' in screen_status.battle_screen_action_indicator:

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'item'
                        and (int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a item lv','').replace(' or less and click yes to play.','')))
                        and int(user.item_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass

        elif 'stage-2-character-action-' in screen_status.battle_screen_action_indicator and 'detail-sneak' in screen_status.battle_screen_action_indicator:

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'monster'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a card lv','').replace(' or less and click yes to play.',''))
                        and int(user.monster_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    elif (located_card.card_type == 'item'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a card lv','').replace(' or less and click yes to play.',''))
                        and int(user.item_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    elif (located_card.card_type == 'tactic'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a card lv','').replace(' or less and click yes to play.',''))
                        ):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass

        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-think-fast':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'monster'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a monster/tactic lv','').replace(' or less and click yes to play.',''))
                        and int(user.monster_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    elif (located_card.card_type == 'tactic'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a monster/tactic lv','').replace(' or less and click yes to play.',''))
                        ):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass
        elif screen_status.battle_screen_action_indicator ==  'stage-2-other-action-detail-spawn-and-equip':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'monster'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a monster/item lv','').replace(' or less and click yes to play.',''))
                        and int(user.monster_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    elif (located_card.card_type == 'item'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a monster/item lv','').replace(' or less and click yes to play.',''))
                        and int(user.item_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast-and-equip':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'item'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a tactic/item lv','').replace(' or less and click yes to play.',''))
                        and int(user.item_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    elif (located_card.card_type == 'tactic'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a tactic/item lv','').replace(' or less and click yes to play.',''))
                        ):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass
        elif screen_status.battle_screen_action_indicator ==  'stage-2-other-action-detail-spawn':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'monster'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a monster lv','').replace(' or less and click yes to play.',''))
                        and int(user.monster_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass
        elif screen_status.battle_screen_action_indicator ==  'stage-2-other-action-detail-think-fast':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'tactic'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a tactic lv','').replace(' or less and click yes to play.',''))
                        ):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass
        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-equip':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'item'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a item lv','').replace(' or less and click yes to play.',''))
                        and int(user.item_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass

        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-sneak':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True
                    located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
                    if (located_card.card_type == 'monster'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a card lv','').replace(' or less and click yes to play.',''))
                        and int(user.monster_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    elif (located_card.card_type == 'item'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a card lv','').replace(' or less and click yes to play.',''))
                        and int(user.item_in_play_length) < 6):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    elif (located_card.card_type == 'tactic'
                        and int(located_card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Pick a card lv','').replace(' or less and click yes to play.',''))
                        ):
                        button_status.battle_screen_instruction_bar_yes_display = True
                        button_status.battle_screen_instruction_bar_yes_backend = True
                    else:
                        button_status.battle_screen_instruction_bar_yes_display = False
                        button_status.battle_screen_instruction_bar_yes_backend = False
                else:
                    pass

        elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-tactic-1':

                if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) >= int(position):
                    button_status.battle_screen_my_hand_indicator_position = position
                    button_status.battle_screen_my_hand_indicator_display = True


    elif click_type == 'level up':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        for i in range(1,16):
            if user.character_under_card_by_level[str(i*10)] == '':
                user.character_under_card_by_level[str(i*10)] = located_card
                break
        user.hand_list.remove(located_card)
        user.character_card.level = str(int(user.character_card.level) + 10)
        user.character_card.health = str(int(user.character_card.health) + 20)
        button_status.battle_screen_my_hand_indicator_display = False
        add_text_to_action_history('You have leveled up with: '+located_card.name+', Lv: '+str(int(user.character_card.level)-10)+' --> '+user.character_card.level+', HP: '+str(int(user.character_card.health)-20)+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
        play_sound_effect('play card',ai_settings)

    elif click_type == 'spawn':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied spawn requirement
        for i in range(1,7):
            if user.monster_in_play_dict[str(i)] == '':
                user.monster_in_play_dict[str(i)] = located_card
                break
        user.hand_list.remove(located_card)
        button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True
        add_text_to_action_history('You have spawned the monster: '+ located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
        play_sound_effect('play card',ai_settings)

    elif click_type == 'think fast':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        x = located_card.special_effect
        if 'Quest/Quest' in x:
            user.hand_list.append(user.remain_deck_list[0])
            del user.remain_deck_list[0]

            user.hand_list.append(user.remain_deck_list[0])
            del user.remain_deck_list[0]

            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            add_text_to_action_history('You have played the tactic: '+located_card.name + ', drawn 2 cards', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('draw heal',ai_settings)

        elif 'Heal 20/Quest' in x:
            user.hand_list.append(user.remain_deck_list[0])
            del user.remain_deck_list[0]

            user.character_card.health = str(int(user.character_card.health) + 20)

            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            add_text_to_action_history('You have played the tactic: '+located_card.name+ ' ,heal yourself for 20 HP, HP: '+str(int(user.character_card.health)-20)+ ' --> '+user.character_card.health+ ', and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('draw heal',ai_settings)

        elif 'Dmg' in x:
            if 'other' in screen_status.battle_screen_action_indicator:
                screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-tactic-1'
            elif 'character' in screen_status.battle_screen_action_indicator:
                y = screen_status.battle_screen_action_indicator.replace('stage-2-character-action-','')[0]
                screen_status.battle_screen_action_indicator = 'stage-2-character-action-' + y + '-detail-tactic-1'
            button_status.battle_screen_instruction_bar_yes_display = False
            button_status.battle_screen_instruction_bar_yes_backend = False
            button_status.battle_screen_instruction_bar_text = "Pick a target to do " + x[-3:] + ' Damage'


    elif click_type == 'equip':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied item requirement

        for i in range(1,7):
            if user.item_in_play_dict[str(i)] == '':
                user.item_in_play_dict[str(i)] = located_card
                break
        user.hand_list.remove(located_card)
        button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True
        add_text_to_action_history('You have equiped the item: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
        play_sound_effect('play card',ai_settings)

    elif click_type == 'spawn/think fast':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied item requirement
        if located_card.card_type == 'monster':
            for i in range(1,7):
                if user.monster_in_play_dict[str(i)] == '':
                    user.monster_in_play_dict[str(i)] = located_card
                    break
            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            add_text_to_action_history('You have spawned the monster: '+ located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('play card',ai_settings)

        else:

            x = located_card.special_effect
            if 'Quest/Quest' in x:
                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]

                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]

                user.hand_list.remove(located_card)
                button_status.battle_screen_my_hand_indicator_display = False
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                add_text_to_action_history('You have played the tactic: '+located_card.name + ', drawn 2 cards', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                play_sound_effect('draw heal',ai_settings)


            elif 'Heal 20/Quest' in x:
                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]

                user.character_card.health = str(int(user.character_card.health) + 20)

                user.hand_list.remove(located_card)
                button_status.battle_screen_my_hand_indicator_display = False
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                add_text_to_action_history('You have played the tactic: '+located_card.name+ ' ,heal yourself for 20 HP, HP: '+str(int(user.character_card.health)-20)+ ' --> '+user.character_card.health+ ', and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                play_sound_effect('draw heal',ai_settings)


            elif 'Dmg' in x:
                screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-tactic-1'
                button_status.battle_screen_instruction_bar_yes_display = False
                button_status.battle_screen_instruction_bar_yes_backend = False
                button_status.battle_screen_instruction_bar_text = "Pick a target to do " + x[-3:] + ' Damage'


    elif click_type == 'spawn/equip':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied item requirement
        if located_card.card_type == 'monster':
            for i in range(1,7):
                if user.monster_in_play_dict[str(i)] == '':
                    user.monster_in_play_dict[str(i)] = located_card
                    break
            add_text_to_action_history('You have spawned the monster: '+ located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('play card',ai_settings)

        else:
            for i in range(1,7):
                if user.item_in_play_dict[str(i)] == '':
                    user.item_in_play_dict[str(i)] = located_card
                    break
            add_text_to_action_history('You have equiped the item: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('play card',ai_settings)

        user.hand_list.remove(located_card)
        button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True

    elif click_type == 'think fast/equip':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied item requirement
        if located_card.card_type == 'tactic':

            x = located_card.special_effect
            if 'Quest/Quest' in x:
                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]

                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]

                user.hand_list.remove(located_card)
                button_status.battle_screen_my_hand_indicator_display = False
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                add_text_to_action_history('You have played the tactic: '+located_card.name + ', drawn 2 cards', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                play_sound_effect('draw heal',ai_settings)


            elif 'Heal 20/Quest' in x:
                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]

                user.character_card.health = str(int(user.character_card.health) + 20)

                user.hand_list.remove(located_card)
                button_status.battle_screen_my_hand_indicator_display = False
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                add_text_to_action_history('You have played the tactic: '+located_card.name+ ' ,heal yourself for 20 HP, HP: '+str(int(user.character_card.health)-20)+ ' --> '+user.character_card.health+ ', and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                play_sound_effect('draw heal',ai_settings)


            elif 'Dmg' in x:
                screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-tactic-1'
                button_status.battle_screen_instruction_bar_yes_display = False
                button_status.battle_screen_instruction_bar_yes_backend = False
                button_status.battle_screen_instruction_bar_text = "Pick a target to do " + x[-3:] + ' Damage'

        else:
            for i in range(1,7):
                if user.item_in_play_dict[str(i)] == '':
                    user.item_in_play_dict[str(i)] = located_card
                    break
            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            add_text_to_action_history('You have equiped the item: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('play card',ai_settings)


    elif click_type == 'sneak':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        # Check if this card satisfied item requirement
        if located_card.card_type == 'tactic':

            x = located_card.special_effect
            if 'Quest/Quest' in x:
                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]

                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]

                user.hand_list.remove(located_card)
                button_status.battle_screen_my_hand_indicator_display = False
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                add_text_to_action_history('You have played the tactic: '+located_card.name + ', drawn 2 cards', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                play_sound_effect('draw heal',ai_settings)


            elif 'Heal 20/Quest' in x:
                user.hand_list.append(user.remain_deck_list[0])
                del user.remain_deck_list[0]

                user.character_card.health = str(int(user.character_card.health) + 20)

                user.hand_list.remove(located_card)
                button_status.battle_screen_my_hand_indicator_display = False
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                add_text_to_action_history('You have played the tactic: '+located_card.name+ ' ,heal yourself for 20 HP, HP: '+str(int(user.character_card.health)-20)+ ' --> '+user.character_card.health+ ', and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                play_sound_effect('draw heal',ai_settings)


            elif 'Dmg' in x:
                if 'other' in screen_status.battle_screen_action_indicator:
                    screen_status.battle_screen_action_indicator = 'stage-2-other-action-detail-tactic-1'
                elif 'character' in screen_status.battle_screen_action_indicator:
                    y = screen_status.battle_screen_action_indicator.replace('stage-2-character-action-','')[0]
                    screen_status.battle_screen_action_indicator = 'stage-2-character-action-' + y + '-detail-tactic-1'
                button_status.battle_screen_instruction_bar_yes_display = False
                button_status.battle_screen_instruction_bar_yes_backend = False
                button_status.battle_screen_instruction_bar_text = "Pick a target to do " + x[-3:] + ' Damage'

        elif located_card.card_type == 'item':
            for i in range(1,7):
                if user.item_in_play_dict[str(i)] == '':
                    user.item_in_play_dict[str(i)] = located_card
                    break
            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            add_text_to_action_history('You have equiped the item: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('play card',ai_settings)

        elif located_card.card_type == 'monster':
            for i in range(1,7):
                if user.monster_in_play_dict[str(i)] == '':
                    user.monster_in_play_dict[str(i)] = located_card
                    break
            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            add_text_to_action_history('You have spawned the monster: '+ located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('play card',ai_settings)


    elif click_type == 'use tactic':
        # Make sure if using auto level up by clicking yes, the global position variable is set to one.
        if len(user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1):7 * screen_status.battle_screen_my_hand_page_id]) < int(button_status.battle_screen_my_hand_indicator_position):
            button_status.battle_screen_my_hand_indicator_position = '1'
        #
        located_card = user.hand_list[7*(screen_status.battle_screen_my_hand_page_id - 1)+(int(button_status.battle_screen_my_hand_indicator_position)-1)]
        dmg = located_card.special_effect[-3:]

        if "opponent's character" in button_status.battle_screen_instruction_bar_text:
            player2.character_card.health = str(int(player2.character_card.health)-int(dmg))
            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            add_text_to_action_history('You have played the tactic: '+located_card.name+', dealt '+str(int(dmg))+ " damage to opponent's character, HP: "+str(int(player2.character_card.health)+int(dmg))+' --> '+player2.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('attack face',ai_settings)

        elif "opponent's monster" in button_status.battle_screen_instruction_bar_text:
            x = button_status.battle_screen_instruction_bar_text[-2:-1]
            player2.monster_in_play_dict[x].health = str(int(player2.monster_in_play_dict[x].health) - int(dmg))
            user.hand_list.remove(located_card)
            button_status.battle_screen_my_hand_indicator_display = False # hand buttons on card eg:****
            button_status.battle_screen_player2_battleground_indicator_display = False
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            add_text_to_action_history('You have played the tactic: '+located_card.name+', dealt '+str(int(dmg))+ " damage to opponent's monster: "+player2.monster_in_play_dict[x].name+ ", HP: "+str(int(player2.monster_in_play_dict[x].health) + int(dmg))+' --> '+player2.monster_in_play_dict[x].health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('attack face',ai_settings)

def battle_screen_battleground_click_action(click_type,ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,player2, position = ''):
    """ battleground click action """
    # If click on player2's character
    if click_type == 'player2-character':
        button_status.battle_screen_player2_battleground_indicator_display = False
        if (('stage-2-character-action-' in screen_status.battle_screen_action_indicator
            and 'detail-easy-shot' in screen_status.battle_screen_action_indicator)

            or ('stage-2-other-action-' in screen_status.battle_screen_action_indicator
                and 'detail-easy-shot' in screen_status.battle_screen_action_indicator)

                ):
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_text = "Do you want to deal 10 damage to opponent's character?"
        elif (('stage-2-character-action-' in screen_status.battle_screen_action_indicator
            and 'detail-tricky-shot' in screen_status.battle_screen_action_indicator)

            or ('stage-2-other-action-' in screen_status.battle_screen_action_indicator
                and 'detail-tricky-shot' in screen_status.battle_screen_action_indicator)

                ):
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_text = "Do you want to deal 20 damage to opponent's character?"

        elif 'stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator:
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_text = "Do you want do damage to opponent's character?"

        elif 'stage-2-character-action-' in screen_status.battle_screen_action_indicator and '-detail-tactic-1' in screen_status.battle_screen_action_indicator:
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_text = "Do you want do damage to opponent's character?"


        elif 'stage-3-monster-' in screen_status.battle_screen_action_indicator:
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            button_status.battle_screen_instruction_bar_text = "Do you want to attack opponent's character?"

    # If click on player2's monsters
    elif click_type == 'player2-monster':
        if player2.monster_in_play_dict[position] != '':
            if 'stage-3-monster-' in screen_status.battle_screen_action_indicator:
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                button_status.battle_screen_instruction_bar_text = "Do you want to attack opponent's monster: " + position + '?'
                button_status.battle_screen_player2_battleground_indicator_display = True
                button_status.battle_screen_player2_battleground_indicator_position = position

            elif (('stage-2-character-action-' in screen_status.battle_screen_action_indicator
                and 'detail-easy-shot' in screen_status.battle_screen_action_indicator)

                or ('stage-2-other-action-' in screen_status.battle_screen_action_indicator
                    and 'detail-easy-shot' in screen_status.battle_screen_action_indicator)

                    ):
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                button_status.battle_screen_instruction_bar_text = "Do you want to deal 10 damage to opponent's monster: " + position + '?'
                button_status.battle_screen_player2_battleground_indicator_display = True
                button_status.battle_screen_player2_battleground_indicator_position = position

            elif (('stage-2-character-action-' in screen_status.battle_screen_action_indicator
                and 'detail-tricky-shot' in screen_status.battle_screen_action_indicator)

                or ('stage-2-other-action-' in screen_status.battle_screen_action_indicator
                    and 'detail-tricky-shot' in screen_status.battle_screen_action_indicator)

                    ):
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                button_status.battle_screen_instruction_bar_text = "Do you want to deal 20 damage to opponent's monster: " + position + '?'
                button_status.battle_screen_player2_battleground_indicator_display = True
                button_status.battle_screen_player2_battleground_indicator_position = position


            elif 'stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator:
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                button_status.battle_screen_instruction_bar_text = "Do you want to do damage to opponent's monster: " + position + '?'
                button_status.battle_screen_player2_battleground_indicator_display = True
                button_status.battle_screen_player2_battleground_indicator_position = position

            elif 'stage-2-character-action-' in screen_status.battle_screen_action_indicator and '-detail-tactic-1' in screen_status.battle_screen_action_indicator:
                button_status.battle_screen_instruction_bar_yes_display = True
                button_status.battle_screen_instruction_bar_yes_backend = True
                button_status.battle_screen_instruction_bar_text = "Do you want to do damage to opponent's monster: " + position + '?'
                button_status.battle_screen_player2_battleground_indicator_display = True
                button_status.battle_screen_player2_battleground_indicator_position = position

    # Action be sent from yes click
    elif click_type == 'easy shot':
        if "opponent's character" in button_status.battle_screen_instruction_bar_text:
            player2.character_card.health = str(int(player2.character_card.health)-10)
            add_text_to_action_history("You have dealt 10 damage to opponent's character, HP: "+str(int(player2.character_card.health)+10)+' --> '+player2.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('attack face',ai_settings)


        elif "opponent's monster" in button_status.battle_screen_instruction_bar_text:
            x = button_status.battle_screen_instruction_bar_text.replace("Do you want to deal 10 damage to opponent's monster: ",'')[0]
            player2.monster_in_play_dict[x].health = str(int(player2.monster_in_play_dict[x].health) - 10)
            button_status.battle_screen_player2_battleground_indicator_display = False
            add_text_to_action_history("You have dealt 10 damage to opponent's monster: "+player2.monster_in_play_dict[x].name+ ", HP: "+str(int(player2.monster_in_play_dict[x].health) + 10)+' --> '+player2.monster_in_play_dict[x].health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('attack face',ai_settings)

    elif click_type == 'tricky shot':
        if "opponent's character" in button_status.battle_screen_instruction_bar_text:
            player2.character_card.health = str(int(player2.character_card.health)-20)
            add_text_to_action_history("You have dealt 20 damage to opponent's character, HP: "+str(int(player2.character_card.health)+20)+' --> '+player2.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('attack face',ai_settings)


        elif "opponent's monster" in button_status.battle_screen_instruction_bar_text:
            x = button_status.battle_screen_instruction_bar_text.replace("Do you want to deal 20 damage to opponent's monster: ",'')[0]
            player2.monster_in_play_dict[x].health = str(int(player2.monster_in_play_dict[x].health) - 20)
            button_status.battle_screen_player2_battleground_indicator_display = False
            add_text_to_action_history("You have dealt 20 damage to opponent's monster: "+player2.monster_in_play_dict[x].name+ ", HP: "+str(int(player2.monster_in_play_dict[x].health) + 20)+' --> '+player2.monster_in_play_dict[x].health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('attack face',ai_settings)

    elif click_type == 'monster_attack_character':
        x = screen_status.battle_screen_action_indicator.replace('stage-3-monster-','')[0]
        monster_attacking = user.monster_in_play_dict[x]
        player2.character_card.health = str(int(player2.character_card.health) - int(monster_attacking.attack))
        add_text_to_action_history("You monster: "+monster_attacking.name+" has dealt "+monster_attacking.attack +" damage to opponent's character, HP: "+str(int(player2.character_card.health) + int(monster_attacking.attack))+' --> '+player2.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
        play_sound_effect('attack face',ai_settings)


    elif click_type == 'monster_attack_monster':
        x = screen_status.battle_screen_action_indicator.replace('stage-3-monster-','')[0]
        monster_attacking = user.monster_in_play_dict[x]
        player2.monster_in_play_dict[position].health = str(int(player2.monster_in_play_dict[position].health) - int(monster_attacking.attack))
        button_status.battle_screen_player2_battleground_indicator_display = False
        add_text_to_action_history("You monster: "+monster_attacking.name +" have dealt "+monster_attacking.attack+" damage to opponent's monster: "+player2.monster_in_play_dict[position].name+ ", HP: "+str(int(player2.monster_in_play_dict[position].health) + int(monster_attacking.attack))+' --> '+player2.monster_in_play_dict[position].health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
        play_sound_effect('attack face',ai_settings)

def battle_screen_instruction_bar_yes_skip_action(yes_skip_indicator, ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,action,player2):
    """ change to different stages when click on yes on instruction bar"""

    # Which stage to go when user at stage-0
    if screen_status.battle_screen_action_indicator == 'stage-0':
        screen_status.battle_screen_action_indicator = 'stage-1'
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True
        add_text_to_action_history('Game Started!', screen, buttons,screen_status, button_status, card_database_filter, user, player2)


    # Which stage to go when user at stage-1
    elif screen_status.battle_screen_action_indicator == 'stage-1':
        # Prepare usable list for next stage/run once per player per turn
        if yes_skip_indicator == 'yes':

            screen_status.battle_screen_action_indicator = 'stage-1-level-up'
            button_status.battle_screen_instruction_bar_yes_display = False
            button_status.battle_screen_instruction_bar_yes_backend = False

        elif yes_skip_indicator == 'skip':
            # go to further stages
            user.stage_2_other_card_usable_list = user.get_stage_2_other_card_usable_list()
            if int(user.character_card.skill_1_lv) <= int(user.character_card.level):
                screen_status.battle_screen_action_indicator = 'stage-2-character-action-1'
            elif len(user.stage_2_other_card_usable_list) >= 1:
                for position, card in user.character_under_card_by_level.items():
                    if card == user.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
            else:
                if (user.monster_in_play_dict['1'] == ''
                and user.monster_in_play_dict['2'] == ''
                and user.monster_in_play_dict['3'] == ''
                and user.monster_in_play_dict['4'] == ''
                and user.monster_in_play_dict['5'] == ''
                and user.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'



    # Which stage to go when user at stage-1-pick-a-card-to-level-up
    elif screen_status.battle_screen_action_indicator == 'stage-1-level-up':
        if yes_skip_indicator == 'yes':
            battle_screen_hand_click_action('level up',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,player2)
        elif yes_skip_indicator == 'skip':
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True
            pass
        # Prepare usable list for next stage/run once per player per turn
        user.stage_2_other_card_usable_list = user.get_stage_2_other_card_usable_list()
        if int(user.character_card.skill_1_lv) <= int(user.character_card.level):
            screen_status.battle_screen_action_indicator = 'stage-2-character-action-1'
        elif len(user.stage_2_other_card_usable_list) >= 1:
            for position, card in user.character_under_card_by_level.items():
                if card == user.stage_2_other_card_usable_list[0]:
                    screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
        else:
            if (user.monster_in_play_dict['1'] == ''
            and user.monster_in_play_dict['2'] == ''
            and user.monster_in_play_dict['3'] == ''
            and user.monster_in_play_dict['4'] == ''
            and user.monster_in_play_dict['5'] == ''
            and user.monster_in_play_dict['6'] == ''):
                screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
            else:
                battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'



    # Which stage to go when user at stage-2-character-action-detail-
    elif ('stage-2-character-action-' in screen_status.battle_screen_action_indicator
        and '-detail-' in screen_status.battle_screen_action_indicator):
        x = screen_status.battle_screen_action_indicator.replace('stage-2-character-action-','')[0]

        if yes_skip_indicator == 'yes':

            if screen_status.battle_screen_action_indicator == 'stage-2-character-action-' + x +'-detail-easy-shot':
                battle_screen_battleground_click_action('easy shot',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)

            elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-' + x +'-detail-tricky-shot':
                battle_screen_battleground_click_action('tricky shot',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)

            elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-' + x +'-detail-spawn':
                battle_screen_hand_click_action('spawn',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)

            elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-' + x +'-detail-think-fast':
                battle_screen_hand_click_action('think fast',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)

            elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-' + x +'-detail-equip':
                battle_screen_hand_click_action('equip',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)

            elif screen_status.battle_screen_action_indicator == 'stage-2-character-action-' + x +'-detail-sneak':
                battle_screen_hand_click_action('sneak',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)


            if ('stage-2-character-action' in screen_status.battle_screen_action_indicator
                and '-detail-tactic-1' in screen_status.battle_screen_action_indicator
                and button_status.battle_screen_instruction_bar_yes_display == False):
                pass

            elif ('stage-2-character-action' in screen_status.battle_screen_action_indicator
                and '-detail-tactic-1' in screen_status.battle_screen_action_indicator
                and button_status.battle_screen_instruction_bar_yes_display == True):

                battle_screen_hand_click_action('use tactic',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)
                button_status.battle_screen_player1_battleground_indicator_display = False
                button_status.battle_screen_player2_battleground_indicator_display = False

                if int(x) <= 2:
                    attribute_name = 'skill_' + str(int(x)+1) + '_lv'
                    if int(getattr(user.character_card, attribute_name)) <= int(user.character_card.level):
                        screen_status.battle_screen_action_indicator = 'stage-2-character-action-' + str(int(x)+1)
                    elif len(user.stage_2_other_card_usable_list) >= 1:
                        for position, card in user.character_under_card_by_level.items():
                            if card == user.stage_2_other_card_usable_list[0]:
                                screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                    else:
                        if (user.monster_in_play_dict['1'] == ''
                        and user.monster_in_play_dict['2'] == ''
                        and user.monster_in_play_dict['3'] == ''
                        and user.monster_in_play_dict['4'] == ''
                        and user.monster_in_play_dict['5'] == ''
                        and user.monster_in_play_dict['6'] == ''):
                            screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                        else:
                            battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                            screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'
                else:
                    if len(user.stage_2_other_card_usable_list) >= 1:
                        for position, card in user.character_under_card_by_level.items():
                            if card == user.stage_2_other_card_usable_list[0]:
                                screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                    else:
                        if (user.monster_in_play_dict['1'] == ''
                        and user.monster_in_play_dict['2'] == ''
                        and user.monster_in_play_dict['3'] == ''
                        and user.monster_in_play_dict['4'] == ''
                        and user.monster_in_play_dict['5'] == ''
                        and user.monster_in_play_dict['6'] == ''):
                            screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                        else:
                            battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                            screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'

            else:

                if int(x) <= 2:
                    attribute_name = 'skill_' + str(int(x)+1) + '_lv'
                    if int(getattr(user.character_card, attribute_name)) <= int(user.character_card.level):
                        screen_status.battle_screen_action_indicator = 'stage-2-character-action-' + str(int(x)+1)
                    elif len(user.stage_2_other_card_usable_list) >= 1:
                        for position, card in user.character_under_card_by_level.items():
                            if card == user.stage_2_other_card_usable_list[0]:
                                screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                    else:
                        if (user.monster_in_play_dict['1'] == ''
                        and user.monster_in_play_dict['2'] == ''
                        and user.monster_in_play_dict['3'] == ''
                        and user.monster_in_play_dict['4'] == ''
                        and user.monster_in_play_dict['5'] == ''
                        and user.monster_in_play_dict['6'] == ''):
                            screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                        else:
                            battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                            screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'
                else:
                    if len(user.stage_2_other_card_usable_list) >= 1:
                        for position, card in user.character_under_card_by_level.items():
                            if card == user.stage_2_other_card_usable_list[0]:
                                screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                    else:
                        if (user.monster_in_play_dict['1'] == ''
                        and user.monster_in_play_dict['2'] == ''
                        and user.monster_in_play_dict['3'] == ''
                        and user.monster_in_play_dict['4'] == ''
                        and user.monster_in_play_dict['5'] == ''
                        and user.monster_in_play_dict['6'] == ''):
                            screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                        else:
                            battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                            screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'


        elif yes_skip_indicator == 'skip':


            if int(x) <= 2:
                attribute_name = 'skill_' + str(int(x)+1) + '_lv'
                if int(getattr(user.character_card, attribute_name)) <= int(user.character_card.level):
                    screen_status.battle_screen_action_indicator = 'stage-2-character-action-' + str(int(x)+1)
                elif len(user.stage_2_other_card_usable_list) >= 1:
                    for position, card in user.character_under_card_by_level.items():
                        if card == user.stage_2_other_card_usable_list[0]:
                            screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                else:
                    if (user.monster_in_play_dict['1'] == ''
                    and user.monster_in_play_dict['2'] == ''
                    and user.monster_in_play_dict['3'] == ''
                    and user.monster_in_play_dict['4'] == ''
                    and user.monster_in_play_dict['5'] == ''
                    and user.monster_in_play_dict['6'] == ''):
                        screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                    else:
                        battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                        screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'
            else:
                if len(user.stage_2_other_card_usable_list) >= 1:
                    for position, card in user.character_under_card_by_level.items():
                        if card == user.stage_2_other_card_usable_list[0]:
                            screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                else:
                    if (user.monster_in_play_dict['1'] == ''
                    and user.monster_in_play_dict['2'] == ''
                    and user.monster_in_play_dict['3'] == ''
                    and user.monster_in_play_dict['4'] == ''
                    and user.monster_in_play_dict['5'] == ''
                    and user.monster_in_play_dict['6'] == ''):
                        screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                    else:
                        battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                        screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'



    # Which stage to go when user at stage-2-character-action-1,2,3
    elif 'stage-2-character-action-' in screen_status.battle_screen_action_indicator:
        x = screen_status.battle_screen_action_indicator.replace('stage-2-character-action-','')

        if yes_skip_indicator == 'yes':

            battle_screen_stage_2_action(x, ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, action,player2)

        elif yes_skip_indicator == 'skip':
            pass
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True

        if screen_status.battle_screen_action_indicator == 'stage-2-character-action-' + x:
            if int(x) <= 2:
                attribute_name = 'skill_' + str(int(x)+1) + '_lv'
                if int(getattr(user.character_card, attribute_name)) <= int(user.character_card.level):
                    screen_status.battle_screen_action_indicator = 'stage-2-character-action-' + str(int(x)+1)
                elif len(user.stage_2_other_card_usable_list) >= 1:
                    for position, card in user.character_under_card_by_level.items():
                        if card == user.stage_2_other_card_usable_list[0]:
                            screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                else:
                    if (user.monster_in_play_dict['1'] == ''
                    and user.monster_in_play_dict['2'] == ''
                    and user.monster_in_play_dict['3'] == ''
                    and user.monster_in_play_dict['4'] == ''
                    and user.monster_in_play_dict['5'] == ''
                    and user.monster_in_play_dict['6'] == ''):
                        screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                    else:
                        battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                        screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'
            else:
                if len(user.stage_2_other_card_usable_list) >= 1:
                    for position, card in user.character_under_card_by_level.items():
                        if card == user.stage_2_other_card_usable_list[0]:
                            screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                else:
                    if (user.monster_in_play_dict['1'] == ''
                    and user.monster_in_play_dict['2'] == ''
                    and user.monster_in_play_dict['3'] == ''
                    and user.monster_in_play_dict['4'] == ''
                    and user.monster_in_play_dict['5'] == ''
                    and user.monster_in_play_dict['6'] == ''):
                        screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                    else:
                        battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                        screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'
        else:
            pass



    # Which stage to go when user at stage-2-other-action-detail-
    elif 'stage-2-other-action-detail-' in screen_status.battle_screen_action_indicator:

        if yes_skip_indicator == 'yes':

            if screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-think-fast':
                battle_screen_hand_click_action('spawn/think fast',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,player2)
            elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn-and-equip':
                battle_screen_hand_click_action('spawn/equip',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,player2)
            elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast-and-equip':
                battle_screen_hand_click_action('think fast/equip',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)
            elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-spawn':
                battle_screen_hand_click_action('spawn',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)
            elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-think-fast':
                battle_screen_hand_click_action('think fast',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)
            elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-equip':
                battle_screen_hand_click_action('equip',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)
            elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-easy-shot':
                battle_screen_battleground_click_action('easy shot',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)
            elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-tricky-shot':
                battle_screen_battleground_click_action('tricky shot',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)
            elif screen_status.battle_screen_action_indicator == 'stage-2-other-action-detail-sneak':
                battle_screen_hand_click_action('sneak',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)

            if ('stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator
                and button_status.battle_screen_instruction_bar_yes_display == False):
                pass

            elif ('stage-2-other-action-detail-tactic-1' in screen_status.battle_screen_action_indicator
                and button_status.battle_screen_instruction_bar_yes_display == True):
                battle_screen_hand_click_action('use tactic',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, player2)
                button_status.battle_screen_player1_battleground_indicator_display = False
                button_status.battle_screen_player2_battleground_indicator_display = False

                del user.stage_2_other_card_usable_list[0]
                if len(user.stage_2_other_card_usable_list) >= 1:
                    for position, card in user.character_under_card_by_level.items():
                        if card == user.stage_2_other_card_usable_list[0]:
                            screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                else:
                    if (user.monster_in_play_dict['1'] == ''
                    and user.monster_in_play_dict['2'] == ''
                    and user.monster_in_play_dict['3'] == ''
                    and user.monster_in_play_dict['4'] == ''
                    and user.monster_in_play_dict['5'] == ''
                    and user.monster_in_play_dict['6'] == ''):
                        screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                    else:
                        battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                        screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'

            else:

                del user.stage_2_other_card_usable_list[0]
                if len(user.stage_2_other_card_usable_list) >= 1:
                    for position, card in user.character_under_card_by_level.items():
                        if card == user.stage_2_other_card_usable_list[0]:
                            screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
                else:
                    if (user.monster_in_play_dict['1'] == ''
                    and user.monster_in_play_dict['2'] == ''
                    and user.monster_in_play_dict['3'] == ''
                    and user.monster_in_play_dict['4'] == ''
                    and user.monster_in_play_dict['5'] == ''
                    and user.monster_in_play_dict['6'] == ''):
                        screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                    else:
                        battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                        screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'

        elif yes_skip_indicator == 'skip':


            del user.stage_2_other_card_usable_list[0]
            if len(user.stage_2_other_card_usable_list) >= 1:
                for position, card in user.character_under_card_by_level.items():
                    if card == user.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
            else:
                if (user.monster_in_play_dict['1'] == ''
                and user.monster_in_play_dict['2'] == ''
                and user.monster_in_play_dict['3'] == ''
                and user.monster_in_play_dict['4'] == ''
                and user.monster_in_play_dict['5'] == ''
                and user.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'


    # Which stage to go when user at stage-2-other-action-10-150
    elif 'stage-2-other-action-' in screen_status.battle_screen_action_indicator:
        x = screen_status.battle_screen_action_indicator.replace('stage-2-other-action-','')

        if yes_skip_indicator == 'yes':

            battle_screen_stage_2_action(x, ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user, action,player2)

        elif yes_skip_indicator == 'skip':
            pass
            button_status.battle_screen_instruction_bar_yes_display = True
            button_status.battle_screen_instruction_bar_yes_backend = True

        if screen_status.battle_screen_action_indicator == 'stage-2-other-action-' + x:
            del user.stage_2_other_card_usable_list[0]
            if len(user.stage_2_other_card_usable_list) >= 1:
                for position, card in user.character_under_card_by_level.items():
                    if card == user.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'stage-2-other-action-' + position
            else:
                if (user.monster_in_play_dict['1'] == ''
                and user.monster_in_play_dict['2'] == ''
                and user.monster_in_play_dict['3'] == ''
                and user.monster_in_play_dict['4'] == ''
                and user.monster_in_play_dict['5'] == ''
                and user.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'stage-3-monster-1-action'
        else:
            pass



    elif 'stage-3-monster-' in screen_status.battle_screen_action_indicator:
        x = screen_status.battle_screen_action_indicator.replace('stage-3-monster-','')[0]

        if yes_skip_indicator == 'yes':

            if button_status.battle_screen_instruction_bar_text == "Do you want to attack opponent's character?":
                battle_screen_battleground_click_action('monster_attack_character',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,player2)

            elif "Do you want to attack opponent's monster: " in button_status.battle_screen_instruction_bar_text:
                opponent_monster_position = button_status.battle_screen_instruction_bar_text.replace("Do you want to attack opponent's monster: ",'')[0]
                battle_screen_battleground_click_action('monster_attack_monster',ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,player2,opponent_monster_position)

        elif yes_skip_indicator == 'skip':

            pass

        if int(x) < 6:

            if user.monster_in_play_dict[str(int(x)+1)] != '':
                screen_status.battle_screen_action_indicator = 'stage-3-monster-' + str(int(x)+1) + '-action'
                battle_screen_stage_3_action(str(int(x)+1), screen,buttons, screen_status, button_status, card_database_filter, user)
                button_status.battle_screen_player1_battleground_indicator_display = False
                button_status.battle_screen_player2_battleground_indicator_display = False
            else:

                screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
                button_status.battle_screen_player1_battleground_indicator_display = False
                button_status.battle_screen_player2_battleground_indicator_display = False

        else:
            screen_status.battle_screen_action_indicator = 'stage-4-end-turn'
            button_status.battle_screen_player1_battleground_indicator_display = False
            button_status.battle_screen_player2_battleground_indicator_display = False



    # Which stage to go when user at stage-4-end-turn
    elif screen_status.battle_screen_action_indicator == 'stage-4-end-turn':

        player2.character_card.health = str(int(player2.character_card.health) - 10*int(user.item_in_play_length))
        user.character_card.health = str(int(user.character_card.health) + 10*int(user.item_in_play_length))
        add_text_to_action_history('You have '+user.item_in_play_length+' items, your HP: '+str(int(user.character_card.health) - 10*int(user.item_in_play_length))+' --> '+user.character_card.health+ ", opponent's HP: "+str(int(player2.character_card.health) + 10*int(user.item_in_play_length))+' --> '+player2.character_card.health+' . Your turn has end', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
        play_sound_effect('draw heal',ai_settings)

        button_status.battle_screen_instruction_bar_yes_display = False
        button_status.battle_screen_instruction_bar_yes_backend = False
        button_status.battle_screen_instruction_bar_skip_display = False
        button_status.battle_screen_instruction_bar_skip_backend = False

        if player2.identity == 'AI':
            screen_status.battle_screen_action_indicator = 'player2-stage-0'
            screen_status.battle_screen_player2_action_display_indicator = True
        elif player2.identity == 'pvp':
            if button_status.battle_screen_pvp_turn_indicator == 'my-ing':
                button_status.battle_screen_pvp_turn_indicator = 'other'
            elif button_status.battle_screen_pvp_turn_indicator == 'other-ing':
                button_status.battle_screen_pvp_turn_indicator = 'my'


def battle_screen_stage_2_action(position, ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,action,player2):
    """ Input position of the action, output action according to the type on specific card"""

    if int(position) <= 3:
        attribute_name = 'skill_' + position + '_type'
        character_skill_name = getattr(user.character_card, attribute_name)
        if ('Easy Shot' in character_skill_name
            or 'Stab' in character_skill_name
            or 'Fire Arrow' in character_skill_name
            or 'Bash' in character_skill_name
            or 'Wand Thwack' in character_skill_name
            ):
            action.stage_2_easy_shot('character', screen,buttons, screen_status, button_status, card_database_filter, user, under_position = position)

        elif ('Tricky Shot' in character_skill_name
            or 'Crush' in character_skill_name
            or 'Slash' in character_skill_name
            ):
            action.stage_2_tricky_shot('character', screen,buttons, screen_status, button_status, card_database_filter, user, under_position = position)


        elif ('Quest' in character_skill_name

            ):
            action.stage_2_quest(ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,player2)

        elif 'Spawn' in character_skill_name:
            if character_skill_name[-1:] == 'X':
                action_level = user.character_card.level
            else:
                action_level = character_skill_name[-3:]
            action.stage_2_spawn('character',action_level, screen,buttons, screen_status, button_status, card_database_filter, user, under_position = position)

        elif 'Think Fast' in character_skill_name:
            if character_skill_name[-1:] == 'X':
                action_level = user.character_card.level
            else:
                action_level = character_skill_name[-3:]
            action.stage_2_think_fast('character',action_level, screen,buttons, screen_status, button_status, card_database_filter, user, under_position = position)

        elif 'Equip' in character_skill_name:
            if character_skill_name[-1:] == 'X':
                action_level = user.character_card.level
            else:
                action_level = character_skill_name[-3:]
            action.stage_2_equip('character',action_level, screen,buttons, screen_status, button_status, card_database_filter, user, under_position = position)

        elif 'Sneak' in character_skill_name:
            if character_skill_name[-1:] == 'X':
                action_level = user.character_card.level
            else:
                action_level = character_skill_name[-3:]
            action.stage_2_sneak('character',action_level, screen,buttons, screen_status, button_status, card_database_filter, user, under_position = position)

    else:
        if user.character_under_card_by_level[position].lv_type[-1:] == 'X':
            action_level = user.character_card.level
        else:
            action_level = user.character_under_card_by_level[position].lv_type[-3:]

        if 'Spawn' in user.character_under_card_by_level[position].lv_type:
            if 'Equip' in user.character_under_card_by_level[position].lv_type:
                action.stage_2_spawn_and_equip(position, action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
            elif 'Think Fast' in user.character_under_card_by_level[position].lv_type:
                action.stage_2_spawn_and_think_fast(position, action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
            else:
                action.stage_2_spawn('other', action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
        elif 'Think Fast' in user.character_under_card_by_level[position].lv_type:
            if 'Equip' in user.character_under_card_by_level[position].lv_type:
                action.stage_2_think_fast_and_equip(position, action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
            else:
                action.stage_2_think_fast('other', action_level, screen,buttons, screen_status, button_status, card_database_filter, user)
        elif 'Equip' in user.character_under_card_by_level[position].lv_type:
                action.stage_2_equip('other', action_level, screen,buttons, screen_status, button_status, card_database_filter, user)

        elif ('Easy Shot' in user.character_under_card_by_level[position].lv_type
            or 'Stab' in user.character_under_card_by_level[position].lv_type
            or 'Fire Arrow' in user.character_under_card_by_level[position].lv_type
            or 'Bash' in user.character_under_card_by_level[position].lv_type
            or 'Wand Thwack' in user.character_under_card_by_level[position].lv_type

            ):
            action.stage_2_easy_shot('other', screen,buttons, screen_status, button_status, card_database_filter, user)

        elif ('Tricky Shot' in user.character_under_card_by_level[position].lv_type
            or 'Slash' in user.character_under_card_by_level[position].lv_type
            or 'Crush' in user.character_under_card_by_level[position].lv_type
            ):
            action.stage_2_tricky_shot('other', screen,buttons, screen_status, button_status, card_database_filter, user)

        elif ('Quest' in user.character_under_card_by_level[position].lv_type

            ):
            action.stage_2_quest(ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,player2)

        elif ('Sneak' in user.character_under_card_by_level[position].lv_type

            ):
            action.stage_2_sneak('other',action_level, screen,buttons, screen_status, button_status, card_database_filter, user)

        elif ('Refresh' in user.character_under_card_by_level[position].lv_type

            ):
            action.stage_2_refresh(ai_settings,screen,buttons, screen_status, button_status, card_database_filter, user,player2)

        else:
            print(user.character_under_card_by_level[position].lv_type)

def battle_screen_stage_3_action(position, screen,buttons, screen_status, button_status, card_database_filter, user):
    """ Input position of the action, output action according to the type on specific card"""
    button_status.battle_screen_instruction_bar_text = "Pick a target to attack with monster: " + position
    button_status.battle_screen_instruction_bar_yes_display = False
    button_status.battle_screen_instruction_bar_yes_backend = False


# For offline AI player2 only
def battle_screen_player2_action(ai_settings,screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Actions of player2"""
    # Level up action
    if screen_status.battle_screen_action_indicator == 'player2-stage-0':
        screen_status.battle_screen_action_indicator = 'player2-stage-1'
        button_status.battle_screen_instruction_bar_text = "Now it's your opponent's turn"

    elif screen_status.battle_screen_action_indicator == 'player2-stage-1':
        screen_status.battle_screen_action_indicator = 'player2-stage-1-level-up'
        button_status.battle_screen_instruction_bar_text = 'Opponent is deciding whether to level up '
        add_text_to_action_history("Opponent's turn has started", screen, buttons,screen_status, button_status, card_database_filter, user, player2)


    elif screen_status.battle_screen_action_indicator == 'player2-stage-1-level-up':
        if player2.hand_list == []:
            button_status.battle_screen_instruction_bar_text = 'Opponent decide not to level up'
            pass
        else:
            located_card = player2.hand_list[0]
            for i in range(1,16):
                if player2.character_under_card_by_level[str(i*10)] == '':
                    player2.character_under_card_by_level[str(i*10)] = located_card
                    break
            player2.hand_list.remove(located_card)
            player2.character_card.level = str(int(player2.character_card.level) + 10)
            player2.character_card.health = str(int(player2.character_card.health) + 20)
            add_text_to_action_history('Opponent has leveled up, Lv: '+str(int(player2.character_card.level) - 10)+' --> '+player2.character_card.level+', HP: '+str(int(player2.character_card.health) - 20)+' --> '+player2.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('play card',ai_settings)

            button_status.battle_screen_instruction_bar_text = 'Opponent has leveled up to lv ' + player2.character_card.level
            player2.stage_2_other_card_usable_list = player2.get_stage_2_other_card_usable_list()

        if int(player2.character_card.skill_1_lv) <= int(player2.character_card.level):
            screen_status.battle_screen_action_indicator = 'player2-stage-2-character-action-1'
            button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_card.skill_1_type
            #pygame.time.delay(3000)
        elif len(player2.stage_2_other_card_usable_list) >= 1:
            for position, card in player2.character_under_card_by_level.items():
                if card == player2.stage_2_other_card_usable_list[0]:
                    screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                    button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                    #pygame.time.delay(3000)
        else:
            if (player2.monster_in_play_dict['1'] == ''
            and player2.monster_in_play_dict['2'] == ''
            and player2.monster_in_play_dict['3'] == ''
            and player2.monster_in_play_dict['4'] == ''
            and player2.monster_in_play_dict['5'] == ''
            and player2.monster_in_play_dict['6'] == ''):
                screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                #pygame.time.delay(3000)
            else:
                battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                button_status.battle_screen_instruction_bar_text = "Opponent deciding action for monster 1"
                    #pygame.time.delay(3000)


    elif 'player2-stage-2-character-action-detail-' in screen_status.battle_screen_action_indicator:

        if screen_status.battle_screen_action_indicator == 'player2-stage-2-character-action-detail-spawn':

            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'monster')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a monster lv','').replace(' to play','')))
                    and int(player2.monster_in_play_length) < 6):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                for i in range(1,7):
                    if player2.monster_in_play_dict[str(i)] == '':
                        player2.monster_in_play_dict[str(i)] = located_card
                        break
                player2.hand_list.remove(located_card)
                add_text_to_action_history('Opponent has spawned the monster: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                play_sound_effect('play card',ai_settings)

        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-character-action-detail-think-fast':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'tactic')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a tactic lv','').replace(' to play','')))):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:

                x = located_card.special_effect
                if 'Quest/Quest' in x:
                    player2.hand_list.append(player2.remain_deck_list[0])
                    del player2.remain_deck_list[0]

                    player2.hand_list.append(player2.remain_deck_list[0])
                    del player2.remain_deck_list[0]

                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent have played the tactic: '+located_card.name + ', drawn 2 cards', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('draw heal',ai_settings)


                elif 'Heal 20/Quest' in x:
                    player2.hand_list.append(player2.remain_deck_list[0])
                    del player2.remain_deck_list[0]

                    player2.character_card.health = str(int(player2.character_card.health) + 20)
                    player2.hand_list.remove(located_card)

                    add_text_to_action_history('Opponent have played the tactic: '+located_card.name+ ' ,heal for 20 HP, HP: '+str(int(player2.character_card.health)-20)+ ' --> '+player2.character_card.health+ ', and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('draw heal',ai_settings)

                elif 'Dmg' in x:

                    dmg = str(int(x[-3:]))
                    user.character_card.health = str(int(user.character_card.health) - int(dmg))

                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent have played the tactic: '+located_card.name+', dealt '+str(int(dmg))+ " damage to your character, HP: "+str(int(user.character_card.health)+int(dmg))+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('attack face',ai_settings)



        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-character-action-detail-equip':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'item')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a item lv','').replace(' to play','')))
                    and int(player2.item_in_play_length) < 6):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                for i in range(1,7):
                    if player2.item_in_play_dict[str(i)] == '':
                        player2.item_in_play_dict[str(i)] = located_card
                        break
                player2.hand_list.remove(located_card)
                add_text_to_action_history('Opponent has equiped the item: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                play_sound_effect('play card',ai_settings)

        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-character-action-detail-sneak':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'monster')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a card lv','').replace(' to play','')))
                    and int(player2.monster_in_play_length) < 6):
                    located_card = card
                    break
                elif ((card.card_type == 'item')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a card lv','').replace(' to play','')))
                    and int(player2.item_in_play_length) < 6):
                    located_card = card
                    break
                elif ((card.card_type == 'tactic')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a card lv','').replace(' to play','')))
                    ):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                if located_card.card_type == 'monster':
                    for i in range(1,7):
                        if player2.monster_in_play_dict[str(i)] == '':
                            player2.monster_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent has spawned the monster: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('play card',ai_settings)

                elif located_card.card_type == 'item':
                    for i in range(1,7):
                        if player2.item_in_play_dict[str(i)] == '':
                            player2.item_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent has equiped the item: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('play card',ai_settings)

                elif located_card.card_type == 'tactic':
                    x = located_card.special_effect
                    if 'Quest/Quest' in x:
                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.hand_list.remove(located_card)
                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name + ', drawn 2 cards', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('draw heal',ai_settings)


                    elif 'Heal 20/Quest' in x:
                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.character_card.health = str(int(player2.character_card.health) + 20)
                        player2.hand_list.remove(located_card)

                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name+ ' ,heal for 20 HP, HP: '+str(int(player2.character_card.health)-20)+ ' --> '+player2.character_card.health+ ', and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('draw heal',ai_settings)


                    elif 'Dmg' in x:

                        dmg = str(int(x[-3:]))
                        user.character_card.health = str(int(user.character_card.health) - int(dmg))

                        player2.hand_list.remove(located_card)
                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name+', dealt '+str(int(dmg))+ " damage to your character, HP: "+str(int(user.character_card.health)+int(dmg))+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('attack face',ai_settings)


        if len(player2.stage_2_other_card_usable_list) >= 1:
            for position, card in player2.character_under_card_by_level.items():
                if card == player2.stage_2_other_card_usable_list[0]:
                    screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                    button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                    #pygame.time.delay(3000)
        else:
            if (player2.monster_in_play_dict['1'] == ''
            and player2.monster_in_play_dict['2'] == ''
            and player2.monster_in_play_dict['3'] == ''
            and player2.monster_in_play_dict['4'] == ''
            and player2.monster_in_play_dict['5'] == ''
            and player2.monster_in_play_dict['6'] == ''):
                screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                #pygame.time.delay(3000)
            else:
                battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                button_status.battle_screen_instruction_bar_text = "Opponent deciding action for monster 1"

    #
    elif 'player2-stage-2-character-action-' in screen_status.battle_screen_action_indicator:
        x = screen_status.battle_screen_action_indicator.replace('player2-stage-2-character-action-','')
        attribute_name = 'skill_' + x + '_type'
        character_skill_name = getattr(player2.character_card, attribute_name)

        if ('Easy Shot' in character_skill_name
            or 'Stab' in character_skill_name
            or 'Fire Arrow' in character_skill_name
            or 'Bash' in character_skill_name
            or 'Wand Thwack' in character_skill_name
            ):
            user.character_card.health = str(int(user.character_card.health)-10)
            add_text_to_action_history('Opponent has used the ability: '+character_skill_name+', and dealt 10 damage to you, HP: '+str(int(user.character_card.health)+10)+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('attack face',ai_settings)

        elif ('Tricky Shot' in character_skill_name
            or 'Crush' in character_skill_name
            or 'Slash' in character_skill_name
            ):
            user.character_card.health = str(int(user.character_card.health)-20)
            add_text_to_action_history('Opponent has used the ability: '+character_skill_name+', and dealt 20 damage to you, HP: '+str(int(user.character_card.health)+20)+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('attack face',ai_settings)

        elif ('Quest' in character_skill_name

            ):
            player2.hand_list.append(player2.remain_deck_list[0])
            del player2.remain_deck_list[0]
            add_text_to_action_history('Opponent has used the ability: Quest and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('draw heal',ai_settings)


        elif 'Spawn' in character_skill_name:
            if character_skill_name[-1:] == 'X':
                action_level = user.character_card.level
            else:
                action_level = character_skill_name[-3:]
            screen_status.battle_screen_action_indicator = 'player2-stage-2-character-action-detail-spawn'
            button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a monster lv' + str(int(action_level)) + ' to play'

        elif 'Think Fast' in character_skill_name:
            if character_skill_name[-1:] == 'X':
                action_level = user.character_card.level
            else:
                action_level = character_skill_name[-3:]

            screen_status.battle_screen_action_indicator = 'player2-stage-2-character-action-detail-think-fast'
            button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a tactic lv' + str(int(action_level)) + ' to play'

        elif 'Equip' in character_skill_name:
            if character_skill_name[-1:] == 'X':
                action_level = user.character_card.level
            else:
                action_level = character_skill_name[-3:]

            screen_status.battle_screen_action_indicator = 'player2-stage-2-character-action-detail-equip'
            button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a item lv' + str(int(action_level)) + ' to play'

        elif 'Sneak' in character_skill_name:
            if character_skill_name[-1:] == 'X':
                action_level = user.character_card.level
            else:
                action_level = character_skill_name[-3:]

            screen_status.battle_screen_action_indicator = 'player2-stage-2-character-action-detail-sneak'
            button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a card lv' + str(int(action_level)) + ' to play'

        if 'player2-stage-2-character-action-' in screen_status.battle_screen_action_indicator and 'detail' not in screen_status.battle_screen_action_indicator:
            if int(x) <= 2:
                attribute_name = 'skill_' + str(int(x)+1) + '_lv'
                if int(getattr(player2.character_card, attribute_name)) <= int(player2.character_card.level):
                    screen_status.battle_screen_action_indicator = 'player2-stage-2-character-action-' + str(int(x)+1)
                    button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use : ' + getattr(player2.character_card, 'skill_' + str(int(x)+1) + '_type')

                    #pygame.time.delay(3000)
                elif len(player2.stage_2_other_card_usable_list) >= 1:
                    for position, card in player2.character_under_card_by_level.items():
                        if card == player2.stage_2_other_card_usable_list[0]:
                            screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                            button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                            #pygame.time.delay(3000)
                else:
                    if (player2.monster_in_play_dict['1'] == ''
                    and player2.monster_in_play_dict['2'] == ''
                    and player2.monster_in_play_dict['3'] == ''
                    and player2.monster_in_play_dict['4'] == ''
                    and player2.monster_in_play_dict['5'] == ''
                    and player2.monster_in_play_dict['6'] == ''):
                        screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                        button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                        #pygame.time.delay(3000)
                    else:
                        battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                        screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                        button_status.battle_screen_instruction_bar_text = "Opponent deciding action for monster 1"
                        #pygame.time.delay(3000)
            else:
                if len(player2.stage_2_other_card_usable_list) >= 1:
                    for position, card in player2.character_under_card_by_level.items():
                        if card == player2.stage_2_other_card_usable_list[0]:
                            screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                            button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                            #pygame.time.delay(3000)
                else:
                    if (player2.monster_in_play_dict['1'] == ''
                    and player2.monster_in_play_dict['2'] == ''
                    and player2.monster_in_play_dict['3'] == ''
                    and player2.monster_in_play_dict['4'] == ''
                    and player2.monster_in_play_dict['5'] == ''
                    and player2.monster_in_play_dict['6'] == ''):
                        screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                        button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                        #pygame.time.delay(3000)
                    else:
                        battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                        screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                        button_status.battle_screen_instruction_bar_text = "Opponent deciding action for monster 1"
                        #pygame.time.delay(3000)
        else:
            pass


    # Which stage to go when user at stage-2-other-action-detail-
    elif 'player2-stage-2-other-action-detail-' in screen_status.battle_screen_action_indicator:

        if screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-spawn-and-think-fast':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'monster')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a monster/tactic lv','').replace(' to play','')))
                    and int(player2.monster_in_play_length) < 6):
                    located_card = card
                    break
                elif ((card.card_type == 'tactic')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a monster/tactic lv','').replace(' to play','')))
                    ):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                if located_card.card_type == 'monster':
                    for i in range(1,7):
                        if player2.monster_in_play_dict[str(i)] == '':
                            player2.monster_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent has spawned the monster: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('play card',ai_settings)

                else:
                    x = located_card.special_effect
                    if 'Quest/Quest' in x:
                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.hand_list.remove(located_card)
                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name + ', drawn 2 cards', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('draw heal',ai_settings)

                    elif 'Heal 20/Quest' in x:
                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.character_card.health = str(int(player2.character_card.health) + 20)
                        player2.hand_list.remove(located_card)

                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name+ ' ,heal for 20 HP, HP: '+str(int(player2.character_card.health)-20)+ ' --> '+player2.character_card.health+ ', and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('draw heal',ai_settings)

                    elif 'Dmg' in x:

                        dmg = str(int(x[-3:]))
                        user.character_card.health = str(int(user.character_card.health) - int(dmg))

                        player2.hand_list.remove(located_card)
                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name+', dealt '+str(int(dmg))+ " damage to your character, HP: "+str(int(user.character_card.health)+int(dmg))+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('attack face',ai_settings)


        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-spawn-and-equip':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'monster')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a monster/item lv','').replace(' to play','')))
                    and int(player2.monster_in_play_length) < 6):
                    located_card = card
                    break
                elif ((card.card_type == 'item')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a monster/item lv','').replace(' to play','')))
                    and int(player2.item_in_play_length) < 6):
                    located_card = card
                    break

            if located_card == []:
                pass
            else:
                if located_card.card_type == 'monster':
                    for i in range(1,7):
                        if player2.monster_in_play_dict[str(i)] == '':
                            player2.monster_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent has spawned the monster: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('play card',ai_settings)

                else:
                    for i in range(1,7):
                        if player2.item_in_play_dict[str(i)] == '':
                            player2.item_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent has equiped the item: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('play card',ai_settings)

        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-think-fast-and-equip':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'item')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a tactic/item lv','').replace(' to play','')))
                    and int(player2.item_in_play_length) < 6):
                    located_card = card
                    break
                elif ((card.card_type == 'tactic')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a tactic/item lv','').replace(' to play','')))
                    ):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                if located_card.card_type == 'item':
                    for i in range(1,7):
                        if player2.item_in_play_dict[str(i)] == '':
                            player2.item_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent has equiped the item: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('play card',ai_settings)

                else:
                    x = located_card.special_effect
                    if 'Quest/Quest' in x:
                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.hand_list.remove(located_card)
                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name + ', drawn 2 cards', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('draw heal',ai_settings)

                    elif 'Heal 20/Quest' in x:
                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.character_card.health = str(int(player2.character_card.health) + 20)
                        player2.hand_list.remove(located_card)

                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name+ ' ,heal for 20 HP, HP: '+str(int(player2.character_card.health)-20)+ ' --> '+player2.character_card.health+ ', and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('draw heal',ai_settings)

                    elif 'Dmg' in x:

                        dmg = str(int(x[-3:]))
                        user.character_card.health = str(int(user.character_card.health) - int(dmg))

                        player2.hand_list.remove(located_card)
                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name+', dealt '+str(int(dmg))+ " damage to your character, HP: "+str(int(user.character_card.health)+int(dmg))+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('attack face',ai_settings)


        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-spawn':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'monster')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a monster lv','').replace(' to play','')))
                    and int(player2.monster_in_play_length) < 6):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                for i in range(1,7):
                    if player2.monster_in_play_dict[str(i)] == '':
                        player2.monster_in_play_dict[str(i)] = located_card
                        break
                player2.hand_list.remove(located_card)
                add_text_to_action_history('Opponent has spawned the monster: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                play_sound_effect('play card',ai_settings)


        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-think-fast':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'tactic')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a tactic lv','').replace(' to play','')))):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                x = located_card.special_effect
                if 'Quest/Quest' in x:
                    player2.hand_list.append(player2.remain_deck_list[0])
                    del player2.remain_deck_list[0]

                    player2.hand_list.append(player2.remain_deck_list[0])
                    del player2.remain_deck_list[0]

                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent have played the tactic: '+located_card.name + ', drawn 2 cards', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('draw heal',ai_settings)

                elif 'Heal 20/Quest' in x:
                    player2.hand_list.append(player2.remain_deck_list[0])
                    del player2.remain_deck_list[0]

                    player2.character_card.health = str(int(player2.character_card.health) + 20)
                    player2.hand_list.remove(located_card)

                    add_text_to_action_history('Opponent have played the tactic: '+located_card.name+ ' ,heal for 20 HP, HP: '+str(int(player2.character_card.health)-20)+ ' --> '+player2.character_card.health+ ', and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('draw heal',ai_settings)

                elif 'Dmg' in x:

                    dmg = str(int(x[-3:]))
                    user.character_card.health = str(int(user.character_card.health) - int(dmg))

                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent have played the tactic: '+located_card.name+', dealt '+str(int(dmg))+ " damage to your character, HP: "+str(int(user.character_card.health)+int(dmg))+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('attack face',ai_settings)


        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-equip':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'item')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a item lv','').replace(' to play','')))
                    and int(player2.item_in_play_length) < 6):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                for i in range(1,7):
                    if player2.item_in_play_dict[str(i)] == '':
                        player2.item_in_play_dict[str(i)] = located_card
                        break
                player2.hand_list.remove(located_card)
                add_text_to_action_history('Opponent has equiped the item: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                play_sound_effect('play card',ai_settings)

        elif screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-detail-sneak':
            located_card = []
            for card in player2.hand_list:
                if ((card.card_type == 'monster')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a card lv','').replace(' to play','')))
                    and int(player2.monster_in_play_length) < 6):
                    located_card = card
                    break
                elif ((card.card_type == 'item')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a card lv','').replace(' to play','')))
                    and int(player2.item_in_play_length) < 6):
                    located_card = card
                    break
                elif ((card.card_type == 'tactic')
                    and (int(card.level) <= int(button_status.battle_screen_instruction_bar_text.replace('Opponent is choosing a card lv','').replace(' to play','')))
                    ):
                    located_card = card
                    break
            if located_card == []:
                pass
            else:
                if located_card.card_type == 'monster':
                    for i in range(1,7):
                        if player2.monster_in_play_dict[str(i)] == '':
                            player2.monster_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent has spawned the monster: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('play card',ai_settings)

                elif located_card.card_type == 'item':
                    for i in range(1,7):
                        if player2.item_in_play_dict[str(i)] == '':
                            player2.item_in_play_dict[str(i)] = located_card
                            break
                    player2.hand_list.remove(located_card)
                    add_text_to_action_history('Opponent has equiped the item: '+located_card.name, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                    play_sound_effect('play card',ai_settings)

                elif located_card.card_type == 'tactic':
                    x = located_card.special_effect
                    if 'Quest/Quest' in x:
                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.hand_list.remove(located_card)
                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name + ', drawn 2 cards', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('draw heal',ai_settings)

                    elif 'Heal 20/Quest' in x:
                        player2.hand_list.append(player2.remain_deck_list[0])
                        del player2.remain_deck_list[0]

                        player2.character_card.health = str(int(player2.character_card.health) + 20)
                        player2.hand_list.remove(located_card)

                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name+ ' ,heal for 20 HP, HP: '+str(int(player2.character_card.health)-20)+ ' --> '+player2.character_card.health+ ', and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('draw heal',ai_settings)

                    elif 'Dmg' in x:

                        dmg = str(int(x[-3:]))
                        user.character_card.health = str(int(user.character_card.health) - int(dmg))

                        player2.hand_list.remove(located_card)
                        add_text_to_action_history('Opponent have played the tactic: '+located_card.name+', dealt '+str(int(dmg))+ " damage to your character, HP: "+str(int(user.character_card.health)+int(dmg))+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
                        play_sound_effect('attack face',ai_settings)



        del player2.stage_2_other_card_usable_list[0]
        if len(player2.stage_2_other_card_usable_list) >= 1:
            for position, card in player2.character_under_card_by_level.items():
                if card == player2.stage_2_other_card_usable_list[0]:
                    screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                    button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                    #pygame.time.delay(3000)
        else:
            if (player2.monster_in_play_dict['1'] == ''
            and player2.monster_in_play_dict['2'] == ''
            and player2.monster_in_play_dict['3'] == ''
            and player2.monster_in_play_dict['4'] == ''
            and player2.monster_in_play_dict['5'] == ''
            and player2.monster_in_play_dict['6'] == ''):
                screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                #pygame.time.delay(3000)
            else:
                battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                button_status.battle_screen_instruction_bar_text = "Opponent deciding action for monster 1"
                #pygame.time.delay(3000)


    #
    elif 'player2-stage-2-other-action-' in screen_status.battle_screen_action_indicator:
        x = screen_status.battle_screen_action_indicator.replace('player2-stage-2-other-action-','')

        # Check if action level is X
        if player2.character_under_card_by_level[x].lv_type[-1:] == 'X':
            action_level = player2.character_card.level
        else:
            action_level = player2.character_under_card_by_level[x].lv_type[-3:]

        if 'Spawn' in player2.character_under_card_by_level[x].lv_type:
            if 'Equip' in player2.character_under_card_by_level[x].lv_type:
                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-spawn-and-equip'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a monster/item lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
            elif 'Think Fast' in player2.character_under_card_by_level[x].lv_type:
                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-spawn-and-think-fast'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a monster/tactic lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
            else:
                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-spawn'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a monster lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
        elif 'Think Fast' in player2.character_under_card_by_level[x].lv_type:
            if 'Equip' in player2.character_under_card_by_level[x].lv_type:

                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-think-fast-and-equip'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a tactic/item lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
            else:
                screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-think-fast'
                button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a tactic lv' + str(int(action_level)) + ' to play'
                #pygame.time.delay(3000)
        elif 'Equip' in player2.character_under_card_by_level[x].lv_type:
            screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-equip'
            button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a item lv' + str(int(action_level)) + ' to play'
            #pygame.time.delay(3000)

        elif ('Sneak' in player2.character_under_card_by_level[x].lv_type

            ):
            screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-detail-sneak'
            button_status.battle_screen_instruction_bar_text = 'Opponent is choosing a card lv' + str(int(action_level)) + ' to play'
            #pygame.time.delay(3000)


        elif ('Easy Shot' in player2.character_under_card_by_level[x].lv_type
            or 'Stab' in player2.character_under_card_by_level[x].lv_type
            or 'Fire Arrow' in player2.character_under_card_by_level[x].lv_type
            or 'Bash' in player2.character_under_card_by_level[x].lv_type
            or 'Wand Thwack' in player2.character_under_card_by_level[x].lv_type

            ):
            user.character_card.health = str(int(user.character_card.health)-10)
            add_text_to_action_history('Opponent has used the ability: '+player2.character_under_card_by_level[x].lv_type+', and dealt 10 damage to you, HP: '+str(int(user.character_card.health)+10)+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('attack face',ai_settings)

        elif ('Tricky Shot' in player2.character_under_card_by_level[x].lv_type
            or 'Slash' in player2.character_under_card_by_level[x].lv_type
            or 'Crush' in player2.character_under_card_by_level[x].lv_type
            ):
            user.character_card.health = str(int(user.character_card.health)-20)
            add_text_to_action_history('Opponent has used the ability: '+player2.character_under_card_by_level[x].lv_type+', and dealt 20 damage to you, HP: '+str(int(user.character_card.health)+20)+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('attack face',ai_settings)


        elif ('Quest' in player2.character_under_card_by_level[x].lv_type

            ):
            player2.hand_list.append(player2.remain_deck_list[0])
            del player2.remain_deck_list[0]
            add_text_to_action_history('Opponent has used the ability: Quest and drawn a card', screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('draw heal',ai_settings)


        elif ('Refresh' in player2.character_under_card_by_level[x].lv_type

            ):
            player2.character_card.health = str(int(player2.character_card.health)+10)
            add_text_to_action_history('Opponent has used the ability: Refresh and heal for 10 hp, HP: '+str(int(player2.character_card.health)-10)+' --> '+player2.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
            play_sound_effect('draw heal',ai_settings)


        if screen_status.battle_screen_action_indicator == 'player2-stage-2-other-action-' + x:
            del player2.stage_2_other_card_usable_list[0]
            if len(player2.stage_2_other_card_usable_list) >= 1:
                for position, card in player2.character_under_card_by_level.items():
                    if card == player2.stage_2_other_card_usable_list[0]:
                        screen_status.battle_screen_action_indicator = 'player2-stage-2-other-action-' + position
                        button_status.battle_screen_instruction_bar_text = 'Opponent deciding whether to use: ' + player2.character_under_card_by_level[position].lv_type
                        #pygame.time.delay(3000)
            else:
                if (player2.monster_in_play_dict['1'] == ''
                and player2.monster_in_play_dict['2'] == ''
                and player2.monster_in_play_dict['3'] == ''
                and player2.monster_in_play_dict['4'] == ''
                and player2.monster_in_play_dict['5'] == ''
                and player2.monster_in_play_dict['6'] == ''):
                    screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'
                    button_status.battle_screen_instruction_bar_text = "Opponent's turn has end"
                    #pygame.time.delay(3000)
                else:
                    battle_screen_stage_3_action('1', screen,buttons, screen_status, button_status, card_database_filter, user)
                    screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-1-action'
                    button_status.battle_screen_instruction_bar_text = "Opponent deciding action for monster 1"
                    #pygame.time.delay(3000)
        else:
            pass





    elif 'player2-stage-3-monster' in screen_status.battle_screen_action_indicator:

        x = screen_status.battle_screen_action_indicator.replace('player2-stage-3-monster-','')[0]
        user.character_card.health = str(int(user.character_card.health) - int(player2.monster_in_play_dict[x].attack))
        add_text_to_action_history('Opponent has attacked with the monster: '+player2.monster_in_play_dict[x].name+', dealt '+player2.monster_in_play_dict[x].attack+' damage to your character, HP: '+str(int(user.character_card.health) + int(player2.monster_in_play_dict[x].attack))+' --> '+user.character_card.health, screen, buttons,screen_status, button_status, card_database_filter, user, player2)
        play_sound_effect('attack face',ai_settings)

        if int(x) < 6:
            if player2.monster_in_play_dict[str(int(x)+1)] != '':
                screen_status.battle_screen_action_indicator = 'player2-stage-3-monster-' + str(int(x)+1) + '-action'
                button_status.battle_screen_instruction_bar_text = "Opponent deciding action for monster " + str(int(x)+1)

            else:

                screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'

        else:
            screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn'


    # Which stage to go when user at stage-4-end-turn
    elif screen_status.battle_screen_action_indicator == 'player2-stage-4-end-turn':
        button_status.battle_screen_instruction_bar_text = "Opponent's turn has end with " + player2.item_in_play_length + " item. Deal " + str(int(player2.item_in_play_length)*10) + ' damage. Gain ' + str(int(player2.item_in_play_length)*10) + ' hp.'
        player2.character_card.health = str(int(player2.character_card.health) + 10*int(player2.item_in_play_length))
        user.character_card.health = str(int(user.character_card.health) - 10*int(player2.item_in_play_length))
        add_text_to_action_history('Opponent have '+player2.item_in_play_length+' items, your HP: '+str(int(user.character_card.health) + 10*int(player2.item_in_play_length))+' --> '+user.character_card.health+ ", opponent's HP: "+str(int(player2.character_card.health) - 10*int(player2.item_in_play_length))+' --> '+player2.character_card.health+" . Opponent's turn has end", screen, buttons,screen_status, button_status, card_database_filter, user, player2)
        play_sound_effect('draw heal',ai_settings)

        #pygame.time.delay(3000)
        screen_status.battle_screen_action_indicator = 'player2-stage-4-end-turn-transfer'


    elif screen_status.battle_screen_action_indicator == 'player2-stage-4-end-turn-transfer':


        add_text_to_action_history("Your turn has started", screen, buttons,screen_status, button_status, card_database_filter, user, player2)


        screen_status.battle_screen_action_indicator = 'stage-1'
        screen_status.battle_screen_player2_action_display_indicator = False # No longer doing player2 loops
        button_status.battle_screen_instruction_bar_yes_display = True
        button_status.battle_screen_instruction_bar_yes_backend = True
        button_status.battle_screen_instruction_bar_skip_display = True
        button_status.battle_screen_instruction_bar_skip_backend = True



#-----------------------------Tools----------------------------------------------------
def rect_union(class_list):
    """Input a list of class objects, return a union of rects of those classes"""
    if len(class_list) >= 1:
        rect_list = []
        for class_object in class_list:
            rect_list.append(class_object.rect)
        return rect_list[0].unionall(rect_list[1:])
    else:
        return Rect(0,0,0,0)

def make_card_list_from_string(string, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Input string from text file, output normal deck list with duplicate with same class instance, mainly for build deck screen use"""
    deck_list = []
    while len(string) >= 14:
        x = 'card_' + string[7:12]
        card = eval (x)
        deck_list.append(card)

        string = string[14:]


    return deck_list

def make_deck_from_string(string, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Input string from text file, output deck list with different class instance, for battle screen use """
    deck_list = []
    while len(string) >= 14:
        x = 'card_' + string[7:9] + '_' + string[10:12]
        card = eval (x)
        if card.card_type == 'monster':
            deck_list.append(Monster(name = card.name, set_number= card.set_number,card_number= card.card_number,card_type= card.card_type,job= card.job,level= card.level,
            attack= card.attack, health= card.health,lv_type= card.lv_type,lv_active_level= card.lv_active_level, special_effect= card.special_effect))
        elif card.card_type == 'tactic':
            deck_list.append(Tactic(name = card.name, set_number= card.set_number,card_number= card.card_number,card_type= card.card_type,job= card.job,level= card.level,
            lv_type= card.lv_type,lv_active_level= card.lv_active_level, special_effect= card.special_effect))
        elif card.card_type == 'item':
            deck_list.append(Item(name = card.name, set_number= card.set_number,card_number= card.card_number,card_type= card.card_type,job= card.job,level= card.level,
            lv_type= card.lv_type,lv_active_level= card.lv_active_level, special_effect= card.special_effect))
        elif card.card_type == 'character':
            deck_list.append(Character(name = card.name,set_number= card.set_number,card_number= card.card_number,card_type= card.card_type,job= card.job,level= card.level,
            health= card.health,skill_1_lv = card.skill_1_lv, skill_1_type = card.skill_1_type,skill_2_lv = card.skill_2_lv, skill_2_type = card.skill_2_type,skill_3_lv = card.skill_3_lv, skill_3_type = card.skill_3_type))

        string = string[14:]


    return deck_list

def add_text_to_action_history(string, screen, buttons,screen_status, button_status, card_database_filter, user, player2):
    """ Input string, add this string to action history"""
    new_text_dict = {
        '1' : '',
        '2' : '',
        '3' : '',
        '4' : '',
        '5' : '',
        '6' : '',
        '7' : '',
        '8' : '',
        '9' : '',
        '10' : '',
        '11' : '',
        '12' : '',
        '13' : '',
        '14' : '',
        '15' : '',
    }
    for number,text in button_status.battle_screen_history_bar_text_dict.items():
        if int(number) <= 14:
            new_text_dict[str(int(number)+1)] = text
    new_text_dict['1'] = string
    button_status.battle_screen_history_bar_text_dict = new_text_dict

def play_sound_effect(string, ai_settings):
    """ play sound effects"""
    if ai_settings.sound_indicator == True:

        SOUND_ATTACK_FACE = pygame.mixer.Sound('static/sound/attack_face.wav')
        SOUND_DRAW_HEAL = pygame.mixer.Sound('static/sound/draw_heal.wav')
        SOUND_PLAY_CARD = pygame.mixer.Sound('static/sound/play_card.wav')
        if string == 'play card':
            pygame.mixer.Sound.play(SOUND_PLAY_CARD)
        elif string == 'draw heal':
            pygame.mixer.Sound.play(SOUND_DRAW_HEAL)
        elif string == 'attack face':
            pygame.mixer.Sound.play(SOUND_ATTACK_FACE)

    else:
        pass

def change_bg_music(string):
    """ CHange bg music"""
    if string == 'Lith Harbor':
        pygame.mixer.music.stop()
        pygame.mixer.music.load('static/music/Above_The_Tree_Tops.wav')
        pygame.mixer.music.play(-1)
    elif string == 'Leafre':
        pygame.mixer.music.stop()
        pygame.mixer.music.load('static/music/Leafre.wav')
        pygame.mixer.music.play(-1)
    elif string == 'Pantheon':
        pygame.mixer.music.stop()
        pygame.mixer.music.load('static/music/Pantheon.wav')
        pygame.mixer.music.play(-1)
    elif string == 'Ellinia':
        pygame.mixer.music.stop()
        pygame.mixer.music.load('static/music/When_The_Morning_Comes.wav')
        pygame.mixer.music.play(-1)

def user_input_text_save(string_type, ai_settings, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2):
    """ save the informations user has typed in"""
    if string_type == 'user name':
        with open('connection.txt','a+') as f:
            f.seek(0)
            x = f.readlines()
            y = 1
            f.seek(0)
            for line in f:
                if 'USER_NAME' not in line:
                    y += 1
                else:
                    break
            x[y-1] = 'USER_NAME = ' + user.name + '\n'

        with open('connection.txt','w') as f:
            f.writelines(x)

def enter_as_network_client(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user,action, player2):
    """ establish connection when entering multiplayer screen"""
    host = user.ip_address
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host,port))
    while 1:
        pass

    s.close()


#--
