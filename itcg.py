import sys
import pygame, pygame.mixer
from pygame.sprite import Group
from multiprocessing import Process
import socket

import game_functions as gf
from settings import Settings
from button import Button
from display import Screen_status, Button_status
from grid import Grid
import card_database_filter as cdf
from user import User
from action import Action
from player2 import Player2


def repair_text_file():
    with open('connection.txt','a+') as f:
        f.seek(0)
        x = f.readlines()

        x = [
            'PLAYER_NAME = Player\n',
            'USER_NAME = Mapler\n',
            'EXIST_ROOM = N/A\n',
            'ROOM_PEOPLE_NUMBER = 0\n',
            'LOBBY_PREPARE_TO_GO = False\n',
            'LOBBY_MY_READY_TO_GO = False\n',
            'LOBBY_OTHER_READY_TO_GO = False\n',
            'LOBBY_GAME_START = False\n',
            'USER_DECK_LIST = []\n',
            'PLAYER_DECK_LIST = []\n',
            'USER_CHARACTER_CARD = []\n',
            'PLAYER_CHARACTER_CARD = []\n',
            'USER_HAND_LIST = []\n',
            'PLAYER_HAND_LIST = []\n',
            'USER_HP = 0\n',
            'PLAYER_HP = 0\n',
            'USER_LV = 0\n',
            'PLAYER_LV = 0\n',
            "USER_MONSTER_LIST = ['','','','','','']\n",
            "PLAYER_MONSTER_LIST = ['','','','','','']\n",
            "USER_ITEM_LIST = ['','','','','','']\n",
            "PLAYER_ITEM_LIST = ['','','','','','']\n",
            "USER_MONSTER_HP = ['','','','','','']\n",
            "PLAYER_MONSTER_HP = ['','','','','','']\n",
            "USER_CHARACTER_UNDER = ['','','','','','','','','','','','','','','']\n",
            "PLAYER_CHARACTER_UNDER = ['','','','','','','','','','','','','','','']\n",
            'TURN_INDICATOR = my'

        ]


    with open('connection.txt','w') as f:
        f.writelines(x)



def main():

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Maplestory ITCG')

    repair_text_file()

    # Global class instance controling all golbal variables
    ai_settings = Settings()
    grid = Grid()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen_status = Screen_status()
    button_status = Button_status()
    buttons = []
    card_database_filter = cdf.Card_database_filter()
    user = User()
    player2 = Player2()
    action = Action()

    # background music while the game is on
    pygame.mixer.music.load('static/music/Above_The_Tree_Tops.wav')
    pygame.mixer.music.play(-1)



    while True:

        gf.read_network_variables(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

        gf.check_events(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)

        gf.update_screen(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user,action, player2)

        gf.write_network_variables(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action, player2)


        clock.tick(25)





if __name__ == "__main__":
    main()






#---
