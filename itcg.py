import sys
import pygame, pygame.mixer
from pygame.locals import *
from settings import Settings
from character import Character_1, Character_2
from monster import Monster
from tactic import Tactic


def run_game():

    pygame.init()
    pygame.display.set_caption('Maplestory ITCG')

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    character_1 = Character_1(screen, ai_settings)
    character_2 = Character_2(screen, ai_settings)
    monster = Monster(screen, ai_settings)
    tactic = Tactic(screen, ai_settings)

    mouse_x,mouse_y = pygame.mouse.get_pos()

    while True:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()


        # BG COLOR
        screen.fill(ai_settings.bg_color)

        # Draw Characters
        character_1.blitme()
        character_2.blitme()
        monster.blitme()
        tactic.blitme(mouse_x-50,mouse_y-50)

        # Most recently draw screen visible
        pygame.display.flip()





run_game()
