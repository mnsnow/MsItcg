import sys
import pygame, pygame.mixer
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from character import Character_1, Character_2
from monster import Monster
from tactic import Tactic
from button import Button, Button_status


def main():

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Maplestory ITCG')

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    character_1 = Character_1(screen, ai_settings)
    character_2 = Character_2(screen, ai_settings)
    monster = Monster(screen, ai_settings)
    tactic = Tactic(screen, ai_settings)


    button_status = Button_status()
    buttons = []



    while True:

        gf.check_events(screen, monster, buttons, button_status)

        gf.update_screen(ai_settings, screen, character_1, character_2, monster, tactic, buttons, button_status)



        clock.tick(25)








if __name__ == "__main__":
    main()
