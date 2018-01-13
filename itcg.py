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




def main():

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Maplestory ITCG')


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
