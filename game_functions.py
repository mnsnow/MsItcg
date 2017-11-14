import sys
import pygame
from pygame.locals import *
from settings import Settings
from character import Character_1, Character_2
from monster import Monster
from tactic import Tactic
from button import Button, Button_status

def check_events(screen,monster, button_status):
    """Check mouse and keyboard evetns"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('1')
            if monster.rect.collidepoint(pygame.mouse.get_pos()): #If click monster cards
                button_status.monster_initial_active()     #active monster initial button
                print('draw')
                #monster_action(screen)



        elif event.type == pygame.MOUSEMOTION:
            print('|')

        elif event.type == pygame.MOUSEBUTTONUP:
            print('0')


def update_screen(ai_settings, screen, character_1, character_2, monster, tactic, button_status):
    """ Update images on the screen and flip to the new screen"""
    # BG COLOR
    screen.fill(ai_settings.bg_color)

    # Draw Characters
    character_1.blitme()
    character_2.blitme()
    monster.blitme()
    tactic.blitme()
    if button_status.monster_initial:
        button1 = Button('Fight', (0,0,0),100, 500, 100, 50)
        button2 = Button('Level up', (0,0,0),200, 500, 100, 50)
        button3 = Button('Back', (0,0,0),300, 500, 100, 50)
        button1.update()
        button2.update()
        button3.update()
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)


    # Most recently draw screen visible
    pygame.display.flip()


def monster_action(screen):
    """actions once click on a monster card"""
    button1 = Button('Fight!', (0,0,0),200, 50, 100, 50)
    button2 = Button('Level up!', (0,0,0),200, 150, 100, 50)
    #button1.do_event()
    #button2.do_event()
    button1.update()
    button2.update()
    button1.draw(screen)
    button2.draw(screen)
    print('draw')
    pygame.display.update()











#--
