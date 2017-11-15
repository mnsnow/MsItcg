import sys
import pygame
from pygame.locals import *
from settings import Settings
from character import Character_1, Character_2
from monster import Monster
from tactic import Tactic
from button import Button, Button_status

def check_events(ai_settings, screen, monster, buttons, button_status):
    """Check mouse and keyboard evetns"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()


        elif event.type == pygame.MOUSEBUTTONDOWN:

            if monster.rect.collidepoint(pygame.mouse.get_pos()):
                if ai_settings.monster_grid_rect.collidepoint(pygame.mouse.get_pos()):
                    button_status.monster_handaction_active()
                elif ai_settings.character_2_grid_rect.collidepoint(pygame.mouse.get_pos()):
                    print('level up action!')
                elif ai_settings.battle_2_grid_rect.collidepoint(pygame.mouse.get_pos()):
                    button_status.monster_battleaction_active()
                    print('hit')



            elif buttons:
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):

                        if button.text == 'Play':
                            monster_play(monster,button_status)
                        elif button.text == 'Level up':
                            monster_levelup(monster,button_status)
                        elif button.text == 'Face!':
                            monster_face(monster,button_status)
                        elif button.text == 'Fight!':
                            monster_fight(monster,button_status)
                        elif button.text == 'Skip':
                            monster_skip(monster,button_status)

                        elif button.text == 'Back':     # we need to decide button back is in which menu.
                            if ai_settings.monster_grid_rect.collidepoint(pygame.mouse.get_pos()):
                                button_status.monster_handaction_deactive()
                            elif ai_settings.battle_2_grid_rect.collidepoint(pygame.mouse.get_pos()):
                                button_status.monster_battleaction_deactive()




        elif event.type == pygame.MOUSEMOTION:
            print(pygame.mouse.get_pos())

        elif event.type == pygame.MOUSEBUTTONUP:
            print('0')


def update_screen(ai_settings, screen, character_1, character_2, monster, tactic, buttons, button_status):
    """ Update images on the screen and flip to the new screen"""
    # BG COLOR
    screen.fill(ai_settings.bg_color)

    # Draw Grid system
    screen.blit(ai_settings.monster_grid, ai_settings.monster_grid_rect)
    screen.blit(ai_settings.tactic_grid, ai_settings.tactic_grid_rect)
    screen.blit(ai_settings.character_1_grid, ai_settings.character_1_grid_rect)
    screen.blit(ai_settings.character_2_grid, ai_settings.character_2_grid_rect)
    screen.blit(ai_settings.battle_1_grid, ai_settings.battle_1_grid_rect)
    screen.blit(ai_settings.battle_2_grid, ai_settings.battle_2_grid_rect)

    # Draw other stuff
    character_1.blitme()
    character_2.blitme()
    monster.blitme()
    tactic.blitme()
    if button_status.monster_handaction:
        monster_button_handaction_display(screen, buttons)
    if button_status.monster_battleaction:
        monster_button_battleaction_display(screen, buttons)



    # Most recently draw screen visible
    pygame.display.flip()


def monster_play(monster,button_status):
    monster.rect.x = 700
    monster.rect.y = 200
    button_status.monster_handaction_deactive()

def monster_levelup(monster,button_status):
    monster.rect.x = 900
    monster.rect.y = 250
    button_status.monster_handaction_deactive()

def monster_face(monster,button_status):
    print('face!!!')

def monster_fight(monster,button_status):
    print('fight!!')

def monster_skip(monster,button_status):
    print('skip turn')


def monster_button_handaction_display(screen, buttons):
    """Display monster handaction button"""
    button1 = Button('Play', (0,0,0),50, 600, 100, 50)
    button2 = Button('Level up', (0,0,0),50, 650, 100, 50)
    button3 = Button('Back', (0,0,0),50, 700, 100, 50)
    button1.update()
    button2.update()
    button3.update()
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    buttons.extend((button1, button2, button3))


def monster_button_battleaction_display(screen, buttons):
    """Display monster battle action button"""
    button1 = Button('Face!', (0,0,0),600, 200, 100, 50)
    button2 = Button('Fight!', (0,0,0),600, 250, 100, 50)
    button3 = Button('Skip', (0,0,0),600, 300, 100, 50)
    button4 = Button('Back', (0,0,0),600, 350, 100, 50)
    button1.update()
    button2.update()
    button3.update()
    button4.update()
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    buttons.extend((button1, button2, button3, button4))












#--
