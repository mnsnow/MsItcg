import sys
import pygame
from pygame.locals import *
from settings import Settings
from character import Character_1, Character_2
from monster import Monster
from tactic import Tactic
from button import Button
from display import Screen_status, Button_status



def check_events(ai_settings, screen, monster, menu_buttons, buttons,screen_status, button_status):
    """Check mouse and keyboard events"""

    if screen_status.welcome_screen:
        check_events_welcome_screen(ai_settings, screen, monster, menu_buttons, buttons,screen_status, button_status)

    if screen_status.build_deck_screen:
        check_events_build_deck_screen(ai_settings, screen, monster, menu_buttons, buttons,screen_status, button_status)

    if screen_status.battle_screen:
        check_events_battle_screen(ai_settings, screen, monster, menu_buttons, buttons,screen_status, button_status)



def check_events_welcome_screen(ai_settings, screen, monster, menu_buttons, buttons,screen_status, button_status):
    """ Check all events on the welcome screen"""
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):

                        if button.text == 'In':
                            screen_status.welcome_screen = False
                            screen_status.build_deck_screen = True
                            screen_status.battle_screen = False


def check_events_build_deck_screen(ai_settings, screen, monster, menu_buttons, buttons,screen_status, button_status):
    """ Check all events on the build deck screen"""
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):

                        if button.text == 'Skip':
                            screen_status.welcome_screen = False
                            screen_status.build_deck_screen = False
                            screen_status.battle_screen = True



def check_events_battle_screen(ai_settings, screen, monster, menu_buttons, buttons,screen_status, button_status):
    """ Check all evetns on the battle screen"""
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

            elif rect_union(menu_buttons).collidepoint(pygame.mouse.get_pos()):
                for menu_button in menu_buttons:
                    if menu_button.rect.collidepoint(pygame.mouse.get_pos()):
                        if menu_button.text == 'Surrender':
                            print('surrender')
                        elif menu_button.text == 'Rules':
                            button_status.menu_rules_active()


            elif rect_union(buttons).collidepoint(pygame.mouse.get_pos()):
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




def update_screen(ai_settings, screen, character_1, character_2, monster, tactic, menu_buttons, buttons, screen_status, button_status):
    """ Update images on the screen and flip to the new screen"""

    if screen_status.welcome_screen:
        welcome_screen_update(screen, buttons)

    if screen_status.build_deck_screen:
        build_deck_screen_update(screen, buttons)

    if screen_status.battle_screen:
        battle_screen_update(ai_settings, screen, character_1, character_2, monster, tactic, menu_buttons, buttons, screen_status, button_status)


    pygame.display.flip()



def welcome_screen_update(screen, buttons):
    """ welcome screen update"""
    button1 = Button('Play', (0,0,0),50, 600, 100, 50)
    button2 = Button('In', (0,0,0),50, 650, 100, 50)
    button3 = Button('Back', (0,0,0),50, 700, 100, 50)
    button1.update()
    button2.update()
    button3.update()
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    buttons.extend((button1, button2, button3))


def build_deck_screen_update(screen, buttons):
    """ Build deck screen update"""
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


def battle_screen_update(ai_settings, screen, character_1, character_2, monster, tactic, menu_buttons, buttons, screen_status, button_status):
    """ Battle screen update"""
    # BG COLOR
    screen.fill(ai_settings.bg_color)

    # Draw Grid system
    screen.blit(ai_settings.menu_grid, ai_settings.menu_grid_rect)
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

    for menu_button in menu_buttons:
        menu_button.update()
        menu_button.draw(screen)

    if button_status.monster_handaction:
        monster_button_handaction_display(screen, buttons)
    if button_status.monster_battleaction:
        monster_button_battleaction_display(screen, buttons)
    if button_status.menu_rules:
        menu_rules_display(screen)



def monster_play(monster,button_status):
    monster.rect.x = 700
    monster.rect.y = 200
    button_status.monster_handaction_deactive()

def monster_levelup(monster,button_status):
    monster.rect.x = 1050
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


def menu_rules_display(screen):
    """What gonna happen after click on rules buttion in the menu bar"""
    button = pygame.Surface((600,400))
    button.fill((34,87,139))
    screen.blit(button,Rect(100,300,600,400))




def rect_union(class_list):
    """Input a list of class objects, return a union of rects of those classes"""
    if len(class_list) >= 1:
        rect_list = []
        for class_object in class_list:
            rect_list.append(class_object.rect)
        return rect_list[0].unionall(rect_list[1:])
    else:
        return Rect(0,0,0,0)















#--
