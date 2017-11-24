import sys
import pygame, pygame.mixer
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from button import Button
from display import Screen_status, Button_status
from grid import Grid
import card_database_functions as cdf
from user import User
from action import Action


def main():

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Maplestory ITCG')

    ai_settings = Settings()
    grid = Grid()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))


    screen_status = Screen_status()
    button_status = Button_status()
    buttons = []
    card_database_filter = cdf.Card_database_filter()
    user = User()
    action = Action()





    while True:

        gf.check_events(ai_settings,grid, screen, buttons,screen_status, button_status, card_database_filter, user, action)

        gf.update_screen(ai_settings,grid, screen, buttons, screen_status, button_status, card_database_filter, user)



        clock.tick(25)







if __name__ == "__main__":
    main()
